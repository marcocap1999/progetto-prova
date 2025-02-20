# List of choices
def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats scissors, scissors beat paper, and paper beats rock.")

    # Ask the user for their choice
    while True:
        # Get the user's choice
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()

        # Check if the user's choice is valid
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Get the computer's choice
        computer_choice = random.choice(choices)

        # Display the choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Compare the choices
        result = determine_winner(user_choice, computer_choice)

       

