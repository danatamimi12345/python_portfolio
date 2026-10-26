# fix_the_policy.py
# Check a new password against an example policy and classify its length.

MIN_LENGTH = 12


username = input("Username: ")
password = input("New password: ")

# Fix 1: Syntax error - (:)add the missing colon.
if len(password) < MIN_LENGTH:
    print("- Too short.")

# Fix 2: Semantic error - use a separate if to check username equality.
if password == username:
    print("- Same as the username.")

# Fix 3: Semantic error - check the longest password first.
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

# Fix 4: Semantic error - print the length outside the else block.
print(f"Length: {len(password)} ({strength})")