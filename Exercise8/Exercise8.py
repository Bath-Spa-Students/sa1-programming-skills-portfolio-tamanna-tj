# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user if they want to search for a specific name
user_choice = input("Do you want to enter a name to search for? (yes/no): ").strip().lower()

# Default search term
search= "Sam"

# Update search term if the user wants to input their own
if user_choice == "yes":
    search = input("Enter the name you want to search for: ").strip()

# Perform the search
if search in names:
    print(f"'{search}' was found in the list.")
else:
    print(f"'{search}' was not found in the list.")