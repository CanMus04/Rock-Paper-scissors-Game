
# Rock, Paper, Scissors Game
import random
import time

def computer_choice():
    """Computer randomly chooses Rock, Paper, or Scissors"""
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

def determine_winner(player, computer):
    """Determines the winner of the round"""
    if player == computer:
        return "Tie"
    
    if (player == "Rock" and computer == "Scissors") or \
       (player == "Scissors" and computer == "Paper") or \
       (player == "Paper" and computer == "Rock"):
        return "Player"
    else:
        return "Computer"

def show_score(player_score, computer_score):
    """Shows the current score"""
    print(f"\nScore: Player {player_score} - {computer_score} Computer")

print("Welcome to Rock, Paper, Scissors!")
print("You are playing against the computer. First to 3 points wins.")

player_score = 0
computer_score = 0
round_num = 1

while player_score < 3 and computer_score < 3:
    print(f"\n--- Round {round_num} ---")
   
    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    choice = input("Your choice (1-3): ")
    
    
    if choice == "1":
        player_choice = "Rock"
    elif choice == "2":
        player_choice = "Paper"
    elif choice == "3":
        player_choice = "Scissors"
    else:
        print("Invalid input. Please choose 1, 2, or 3.")
        continue
    
    print(f"\nYou chose {player_choice}.")
    
   
    print("The computer is choosing", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    
    computer_result = computer_choice()
    print(f" {computer_result}!")
    
   
    winner = determine_winner(player_choice, computer_result)
    
    if winner == "Player":
        print("You win this round!")
        player_score += 1
    elif winner == "Computer":
        print("The computer wins this round!")
        computer_score += 1
    else:
        print("This round is a tie!")
    

    show_score(player_score, computer_score)
    
    round_num += 1


print("\n=== Game Over ===")
if player_score > computer_score:
    print("Congratulations! You won the game!")
else:
    print("Too bad! The computer won the game!")

print(f"Final score: Player {player_score} - {computer_score} Computer")
print("Thanks for playing!")
