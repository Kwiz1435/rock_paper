import random

# Define a list of actions the computer can take
actions = ["Rock", "Paper", "Scissors"]

# Continue the game until the player types "I quit"
while True:
    # Ask the player for their decision
    player_action = input("Enter your decision (Rock/Paper/Scissors), or 'I quit' to end the game: ")
    
    # Check if the player wants to quit
    if player_action.lower() == "i quit":
        print("Thank you for playing!")
        break
        
    # Check if the player entered a valid action
    elif player_action not in actions:
        print("Invalid decision. Please enter Rock, Paper, or Scissors.")
        
    # Otherwise, play the game
    else:
        # Choose a random action for the computer
        computer_action = random.choice(actions)
        print(f"Computer decision: {computer_action}")
        
        # Determine the winner
        if player_action == computer_action:
            print("Game tied!")
        elif (player_action == "Rock" and computer_action == "Paper") or (player_action == "Scissors" and computer_action == "Rock") or (player_action == "Paper" and computer_action == "Scissors"):
            print("You lose!")
        else:
            print("You win!")
