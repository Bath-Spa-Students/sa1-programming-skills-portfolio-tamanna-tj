# create a simple program that asks the user a question,evaluates their answer, and provides feedback.
# Write a program that asks the user “What is the capital of France?” and waits for their response.
question = input("What is the capital of France? ")
answer = "Paris"  
# If the user’s answer is correct (i.e., “Paris”), the program should print a message saying the answer is correct.
if question == answer:
    print("CORRECT")
# If the answer is incorrect, the program should print a message saying the answer is wrong.
else:
    print("WRONG")

# Advanced Requirements:Ignore Capitalization

question = input("What is the capital of France? ")
answer = "Paris" 
if question.lower() == answer.lower():
    print("CORRECT")
else:
    print("WRONG")
