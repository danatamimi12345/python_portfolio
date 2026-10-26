<<<<<<< HEAD
MAX_FAILED = 5

role = input("Role: ")
mfa_answer = input("MFA passed (yes/no): ")
failed = int(input("Failed attempts: "))

mfa_ok = mfa_answer.lower() == "yes"
is_privileged = role == "admin" or role == "root"
can_log_in = mfa_ok and failed < MAX_FAILED

print(f"MFA OK: {mfa_ok}")
print(f"Privileged role: {is_privileged}")
print(f"Can log in: {can_log_in}")
=======
MAX_FAILED = 5

role = input("Role: ")
mfa_answer = input("MFA passed (yes/no): ")
failed = int(input("Failed attempts: "))

mfa_ok = mfa_answer.lower() == "yes"
is_privileged = role == "admin" or role == "root"
can_log_in = mfa_ok and failed < MAX_FAILED

print(f"MFA OK: {mfa_ok}")
print(f"Privileged role: {is_privileged}")
print(f"Can log in: {can_log_in}")
>>>>>>> 30b3c9f75ffd7d281c6a37555dba43d8e96fe1e9
