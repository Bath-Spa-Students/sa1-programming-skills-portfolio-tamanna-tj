def is_it_even_or_odd(number):
    # To show if the number is even or odd
    if number % 2 == 0:
        return f"The given number {number} is even."
    else:
        return f"The given number {number} is odd."

def main():
    # Allows the user to input a number
    user_input = int(input("Please enter a number: "))
    
    # Call the function and store the result
    Answer = is_it_even_or_odd(user_input)
    
    # Prints the result
    print(Answer)

    # Ensure main runs only if the script is executed directly
if __name__ == "__main__":
    main()