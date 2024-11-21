#a program that simulates a password entry system.
# Define the correct password.
crrct_pass="12345"
maximum_try=5
tries=0
# Use a while loop to repeatedly ask the user for the password until the correct one is entered.
while tries < maximum_try:
    user_input=input("Enter the password:")

    if user_input==crrct_pass:
        print("Access Granded!") # Output an appropriate message when the correct password is entered.
        break
    else:  
        tries+=1
        tries_left=maximum_try-tries
        if tries_left>0:
            print(f"Incorrect Password.  Try again. You only have {tries_left} tries left")
        else:
            print("Incorrect Password.Maximum number of tries have been finished.The authorities have been alerted!")