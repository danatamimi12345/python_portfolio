<<<<<<< HEAD
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
print(f"\n\tFAILED:{failed_attempts}")
=======
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
print(f"\n\tFAILED:{failed_attempts}")
>>>>>>> 30b3c9f75ffd7d281c6a37555dba43d8e96fe1e9
print(f"\n\tATTEMPTS LAFT:{attempts_laft}")