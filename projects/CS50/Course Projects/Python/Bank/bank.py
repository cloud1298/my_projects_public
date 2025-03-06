greeting = input("Greeting: ")
words = greeting.split()

if "hello" in words[0].lower():
    print("$0")
elif words[0][0].lower() == "h":
    print("$20")
else:
    print("$100")