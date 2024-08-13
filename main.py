# main.py

def greet_user():
    """
    This function prompts the user for their first and last name,
    then prints a greeting message including their full name.
    """
    first_name = input("Enter your first name: ")  # Prompt for first name
    last_name = input("Enter your last name: ")    # Prompt for last name
    full_name = f"{first_name} {last_name}"        # Combine first and last name
    print(f"Hello, {full_name}!")                  # Print greeting with full name

if __name__ == "__main__":
    # This block ensures that the greet_user function is only executed
    # if the script is run directly, not when imported as a module.
    greet_user()
