 # Count failed logins and the average session length.

events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]

minutes = [0, 30, 0, 15, 45]

#indentation error:faild=0 inside the for loop
failed = 0
for event in events:
 if event == "FAILED":
   failed += 1 

   #logical error:the print statemet was inside the loop
print(f"Failed logins: {failed}")

total = 0
count = 0

for value in minutes:
  if value > 0:
   total += value
   count += 1
#logical error :average was print inside the loop
print(f"Average session: {total // count} minutes")
#IndentationError: missing indentation before print
for level in range(1, 4):
 print(f"Level {level}")