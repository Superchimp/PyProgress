import random

winner = ""

random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = "Rock"
elif random_choice == 1:
    computer_choice = "Paper"
else:
    computer_choice = "Scissors"
 
#We ask for user choice while also checking it is a valid answer (including starting with caps)    
user_choice = ""
while (user_choice != "Rock" and
       user_choice != "rock" and
       user_choice != "Paper" and
       user_choice != "paper" and
       user_choice != "Scissors" and
       user_choice != "scissors"):
    user_choice = input("Rock, Paper or Scissors? ")
    
#Here we make sure the spelling is converted to enable a Tie        
if user_choice == "rock":
    user_choice = "Rock"
elif user_choice == "paper":
    user_choice = "Paper"
elif user == "scissors":
    user = "Scissors"
else:
    print("Error in conversion block")

if computer_choice == user_choice:
    winner = "Tie"
elif computer_choice == "Paper" and (user_choice == "Rock" or user_choice == "rock"): #Need to confirm spelling before comparing with computer =()
    winner = "Computer"
elif computer_choice == "Rock" and (user_choice == "Scissors" or user_choice == "scissors"):
    winner = "Computer"
elif computer_choice == "Scissors" and (user_choice == "Paper" or user_choice == "paper"):
    winner = "Computer"
else:
    winner = "User"
    
if winner == "Tie":
    print("We both chose", computer_choice + ", play again.")
else:
    print(winner, "won, I chose", computer_choice +".")