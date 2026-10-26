#Create risk_score.py
#calculate a long risk score and classify its level.

failed = int(input("Failed attempts in the last hour:"))
hour = int(input("Login hour (0-23):"))
new_device = input("New device(yes/no):")

score = 0

if failed >= 3:
  score += 40
if hour <= 6:
  score += 30
if new_device == "yes":
  score += 40

if score>=70:
  lavel   = "HIGH"
elif score >= 30:
  lavel ="MEDIUM"
else:
  lavel = "LOW"

print(f"Risk score:{score} ({lavel})")