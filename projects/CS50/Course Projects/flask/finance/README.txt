# Stock Trading Web Application

## Overview
A web application that simulates stock trading, allowing users to register, log in, buy and sell stocks, view quotes, and track their portfolio and transaction history.

## Features
- User registration and login
- Buy and sell stocks
- View stock quotes
- Portfolio overview with current stock values
- Transaction history
- Real-time stock price lookup

## Prerequisites
- Python 3.x
- Flask (`pip install flask`)
- Flask-Session (`pip install flask-session`)
- CS50 Python library (`pip install cs50`)
- Werkzeug (`pip install werkzeug`)

## Usage
1. Run server and visit `http://127.0.0.1:5000/`
2. Register an account
3. Log in
4. Use features:
   - Buy stocks
   - Sell stocks
   - View quotes
   - Check portfolio
   - See transaction history

## Routes
- `/`: Portfolio overview
- `/buy`: Buy stocks (GET/POST)
- `/sell`: Sell stocks (GET/POST)
- `/quote`: Get stock quotes (GET/POST)
- `/history`: Transaction history
- `/login`: User login (GET/POST)
- `/logout`: User logout
- `/register`: User registration (GET/POST)

## Technical Details
- Built with Flask
- SQLite database via CS50 SQL
- Session management with filesystem
- Password hashing with Werkzeug
- Custom USD filter for currency formatting
- Cache prevention headers

## Notes
- Requires `helpers.py` with functions: `apology`, `login_required`, `lookup`, `usd`
- Initial cash set to $10,000 per user
- Stock prices from external API via `lookup()`
- No extensive error handling
