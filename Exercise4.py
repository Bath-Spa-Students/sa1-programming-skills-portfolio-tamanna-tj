# create a simple program that asks the user a question,evaluates their answer, and provides feedback.

question = input("What is the capital of France? ")
answer = "Paris"  
if question == answer:
    print("CORRECT")
else:
    print("WRONG")

# Advanced Requirements:Ignore Capitalization

question = input("What is the capital of France? ")
answer = "Paris" 
if question.lower() == answer.lower():
    print("CORRECT")
else:
    print("WRONG")
