#A dictionary to map the month numbers (1-12) to the number of days in each month.

days= {1: 31,2: 28,3: 31,4: 30,5: 31, 6: 30,7: 31,8: 31,9: 30, 10: 31,11: 30,12: 31}
monthNumber = int(input("Enter the month number (1-12): "))
if 1 <= monthNumber <= 12:
        print(f"The month has {days[monthNumber]} days.")
else:
        print("Invalid month number. Please enter a valid number.")

#Advanced Requirement: Modify the program to account for leap years.

days= {1: 31,2: 28,3: 31,4: 30,5: 31, 6: 30,7: 31,8: 31,9: 30, 10: 31,11: 30,12: 31}
monthNumber = int(input("Enter the month number (1-12): "))
if 1 <= monthNumber <= 12:
        if monthNumber==2:
                leapyear=input("Checking for leap year?:")

                if leapyear=="Yes":
                        print("The month has 29 days")

                else:
                        print("The month has 28 days")

