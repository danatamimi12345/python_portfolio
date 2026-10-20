# Maximum number of login attempts
MAX_LOGIN_ATTEMPTS = 5

# Get user information:
username = input("Enter your username :")
failed_attempts =int( input("Enter of failed attempts: "))

# Calculate remaining attempts
attempts_laft = MAX_LOGIN_ATTEMPTS - failed_attempts

# Print the login report
line = "*" * 30
print(line)
print(" LOGIN REPORT.")
print(line)
print(f"\n\tUSER:{username}")
print(f"\t\nFAILED:{failed_attempts}")
print(f"\n\tATTEMPTS LAFT:{attempts_laft}")