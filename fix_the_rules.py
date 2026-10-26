<<<<<<< HEAD

# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")

# runtime: Convert the port input from a string to an integer.
port = int(input("Port: "))

# semantic: Use == to compare instead of assigning a value.
is_admin = role == "admin"

# syntax: Use the correct <= operator.
is_system_port = port <= 1023

# semantic: Compare port with both 80 and 443.
is_web_port = port == 80 or port == 443

print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")
=======

# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")

# runtime: Convert the port input from a string to an integer.
port = int(input("Port: "))

# semantic: Use == to compare instead of assigning a value.
is_admin = role == "admin"

# syntax: Use the correct <= operator.
is_system_port = port <= 1023

# semantic: Compare port with both 80 and 443.
is_web_port = port == 80 or port == 443

print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")
>>>>>>> 30b3c9f75ffd7d281c6a37555dba43d8e96fe1e9
