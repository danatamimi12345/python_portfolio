#pin_space_table.py
#calculate the munber of possible andthe time needed to guess them

GUESSES_PER_SECOND = 10

for digits in range (4,9) :
    combinations = 10 ** digits
    seconds = combinations // GUESSES_PER_SECOND
    minutes = seconds // 60
    days = minutes // (60 * 24)
    print(f"{digits} digists:{combinations} PIN, {minutes} minutes, {days} days")