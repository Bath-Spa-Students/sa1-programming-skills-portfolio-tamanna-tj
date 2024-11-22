#Loops- Pizza Toppings : 
#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 
#'quit' value. As they enter each topping, 
#Print a message saying you’ll add that topping to their pizza.

# Start a loop for pizza toppings
print("Enter your favorite pizza topping. Type 'quit' to stop")

while True:
  topping = input("Enter the toppings:").strip().lower()

  if topping == 'quit':
    print("Thank you for ordering! Your pizza is being prepared.")
    break
  else:
      print(f"Will be adding {topping} to the pizza!")