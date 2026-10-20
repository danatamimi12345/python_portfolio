
seconds = int(input("Enter session length in seconds: "))

# Calculate minutes and remaining seconds
minutes = seconds // 60
remaining_seconds = seconds % 60

# Display the result
print(f"The session is {minutes} minutes and {remaining_seconds} seconds.")

# Test outputs:
# Input: 905 -> The session is 15 minutes and 5 seconds.
# Input: 60  -> The session is 1 minutes and 0 seconds.
# Input: 59  -> The session is 0 minutes and 59 seconds.