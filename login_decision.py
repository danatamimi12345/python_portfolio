MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

username = input("Enter a Username:")
failed =  int(input("Enter Failed attempts:"))
password = input("Enter password:")
attempts_left = MAX_FAILED - failed -1

if failed >= MAX_FAILED:
    print("Account Locked.")
elif username != KNOWN_USER:
    print("Unknown User.")
elif  password == STORED_PASSWORD:
     print("Access granted.")
else:
    print(f"Access denied. Attempts left:{attempts_left }")