#create a program that stores and prints your name, home town, and age to the console using a Python dictionary.
# Store the information (name, hometown, and age) as key-value pairs in a dictionary.
info = {
    "name": "Thamanna Jannath",       
    "hometown": "Ajman",  
    "age": 19                 
}
# Print the values on separate lines using a single print() statement.
print(info["name"])
print(info["hometown"])
print(info["age"])

#advanced requirement: giving both your first and second name when asked for your name.
name=input("Enter your name:")
hometown=input("Enter your hometown:")
age=input("Enter your age:")
info ={"name": name,"hometown":hometown,"age": age}
print(info["name"])
print(info["hometown"])
print(info["age"])
