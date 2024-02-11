def check_access(username, password):
    pwds = ['abc$123', 'ABC$123']
    if password.upper() in pwds:
        return "Welcome!"
    else:
        return "I don't know you."

username = input("Enter your username: ")
password = input("Enter your password: ")
print(check_access(username, password))
