#create pin_tries
#this program  that verifies the PIN entered by the user, allowing only three attempts to input the correct number.

MAX_TRIES = 3
CORRECT_PIN = "2580"

tries = 0

while tries < MAX_TRIES :
    pin = input ("PIN:")
    tries +=1

    if pin == CORRECT_PIN :
        print ("Access granted.")
        break
    else:
        print(f"Wrong PIN.Tries Left:{MAX_TRIES - tries}")
else:
    print("Card blocked.") 