import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats scissors, scissors beat paper, and paper beats rock.")

    # Variables to keep track of results
    wins = 0
    ties = 0
    losses = 0

    # Play 10 rounds
    for round_num in range(1, 11):
        print(f"\nRound {round_num}")
        
        # Ask the user for their choice
        while True:
            # Get the user's choice
            user_choice = input("\nChoose rock, paper, or scissors: ").lower()

            # Check if the user's choice is valid
            if user_choice not in choices:
                print("Invalid choice! Please choose rock, paper, or scissors.")
                continue
            break
        
        # Get the computer's choice
        computer_choice = random.choice(choices)

        # Display the choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Compare the choices and update the result counters
        result = determine_winner(user_choice, computer_choice)
        
        if result == "win":
            wins += 1
            print("You win this round!")
        elif result == "tie":
            ties += 1
            print("It's a tie!")
        else:
            losses += 1
            print("You lose this round!")

    # Display the final results
    print("\nGame Over!")
    print(f"Total Wins: {wins}")
    print(f"Total Ties: {ties}")
    print(f"Total Losses: {losses}")
    
    # Overall result
    if wins > losses:
        print("Congratulations, you won more rounds!")
    elif wins < losses:
        print("Sorry, you lost more rounds!")
    else:
        print("It's a tie overall!")

# Run the game
if __name__ == "__main__":
    main()
       

