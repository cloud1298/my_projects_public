import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

from datetime import datetime

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    symbol_result = db.execute(
        "SELECT DISTINCT symbol FROM transactions WHERE user_id = ?", user_id
    )
    total_cash = 0
    data = []

    # If there is any symbol, then extract all necessary data and append it into "data" list.
    if len(symbol_result) > 0:
        symbols = [row["symbol"] for row in symbol_result]

        for symbol in symbols:
            quote = lookup(symbol)
            name = quote["name"]
            price = quote["price"]
            shares_result = db.execute(
                "SELECT SUM(shares) AS total_shares FROM transactions WHERE symbol = (?) AND user_id = (?) ",
                symbol,
                session["user_id"],
            )
            shares = shares_result[0]["total_shares"]
            total_price = price * shares

            data.append(
                {
                    "symbol": symbol,
                    "name": name,
                    "shares": shares,
                    "price": usd(price),
                    "total_p": usd(total_price),
                }
            )

            # keep track of total cash
            total_cash += total_price

    # Prepare everything about user cash
    cash_result = db.execute(
        "SELECT cash FROM users WHERE id = (?)", session["user_id"]
    )
    cash = cash_result[0]["cash"]
    total_cash += cash

    return render_template(
        "index.html", data=data, cash=usd(cash), total_cash=usd(total_cash)
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # get necessary data for the validation
        symbol = request.form.get("symbol").upper()
        try:
            shares = (
                int(request.form.get("shares")) if request.form.get("shares") else None
            )
        except ValueError:
            shares = None
        quote = lookup(symbol)

        # Check if every data is valid
        if not symbol or not quote:
            return apology("Invalid symbol", 400)
        elif shares == None or shares < 0:
            return apology("Invalid shares", 400)
        elif shares == 0:
            return apology("Can't buy 0 shares", 400)

        # Get data for money validation
        user_id = session["user_id"]
        cash_result = db.execute("SELECT cash FROM users WHERE id = (?)", user_id)
        cash = cash_result[0]["cash"]
        price = quote["price"]
        total = shares * price

        # Check if can afford buy
        if (cash - total) < 0:
            return apology("Not enough cash", 400)

        # Get the remaining data to put everything into the database
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

        # Insert data into the "transactions" table
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)",
            user_id,
            symbol,
            shares,
            price,
            formatted_date,
        )

        # Update cash info in "users" table
        db.execute("UPDATE users SET cash = cash - (?)", total)

        flash("Bought!")

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = ? ORDER BY timestamp DESC", user_id
    )

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        get_quote = lookup(symbol)

        if not symbol or not get_quote:
            return apology("Invalid symbol", 400)

        return render_template(
            "quoted.html",
            name=get_quote["name"],
            symbol=get_quote["symbol"],
            price=usd(get_quote["price"]),
        )
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        password = request.form.get("password")
        username = request.form.get("username")

        # Check if user already exist
        user = db.execute("SELECT * FROM users WHERE username = ?", username)

        if not username:
            return apology("must provide username", 400)
        elif len(user) == 1:
            return apology("username already exists", 400)
        elif not password:
            return apology("must provide password", 400)
        elif password != request.form.get("confirmation"):
            return apology("Passwords doesn't match", 400)

        # Generate hash for the user password and save it into the database along with the username
        hash = generate_password_hash(password, method="pbkdf2", salt_length=16)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)

        return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Get the list of every existing symbol and the user id
    symbols_result = db.execute("SELECT DISTINCT symbol FROM transactions")
    symbols = [row["symbol"] for row in symbols_result]
    user_id = session["user_id"]

    if request.method == "POST":
        # Get the data from the form and the number of existing shares for the user's chosen symbol to validate input from the form
        symbol = request.form.get("symbol")
        shares_result = db.execute(
            "SELECT SUM(shares) AS total_shares FROM transactions WHERE symbol = (?) AND user_id = (?) ",
            symbol,
            user_id,
        )
        shares_num = shares_result[0]["total_shares"]

        try:
            shares = (
                int(request.form.get("shares")) if request.form.get("shares") else None
            )
        except ValueError:
            shares = None

        # Check errors
        if symbol not in symbols:
            return apology("Invalid symbol", 403)
        elif shares == None:
            return apology("Invalid value", 400)
        elif shares == 0:
            return apology("Can't sell 0 shares", 400)
        elif (shares_num - shares) < 0:
            return apology("Not enough shares to sell", 400)

        # Get the rest of data to put everything into the database
        quote = lookup(symbol)
        price = quote["price"]
        total = shares * price
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

        # Create a new transaction in the database
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)",
            user_id,
            symbol,
            -abs(shares),
            price,
            formatted_date,
        )

        # Update user's cash
        db.execute("UPDATE users SET cash = cash + (?)", total)

        # Show notification
        flash("Sold!")

        return redirect("/")

    else:
        return render_template("sell.html", symbols=symbols)
