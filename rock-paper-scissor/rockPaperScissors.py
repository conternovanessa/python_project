import random
# Rock beats Scissors
# Scissor beats Paper
# Paper beats Rock

print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
player = int (input("Pick a number: "))
player_play = "Not choice"
if player == 1 :
  player_play = "✊ Rock"
elif player == 2:
  player_play = "✋ Paper"
elif player == 3:
  player_play = "✌ Scissors"
else:
  print("Wrong choice you can only decide between 1 and 3")
print(f"Player chose : {player_play}")

computer = random.randint(1,3)
computer_play = " Not choice"
if computer == 1 :
  computer_play = "✊ Rock"
elif computer == 2:
  computer_play = "✋ Paper"
elif computer == 3:
  computer_play = "✌ Scissors"
else:
  print("Wrong choice you can only decide between 1 and 3")
print(f"Computer chose: {computer_play}")

if computer == player:
  print("It's a tie")
elif computer == 1 and player == 2 or computer == 2 and player == 3 or computer == 3 and player == 1:
  print("The player won!")
else:
  print("The computer won!")




print("===================")
print("Rock Paper Scissors Lizard Spock")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")
player = int (input("Pick a number: "))
player_play = "Not choice"
if player == 1 :
  player_play = "✊ Rock"
elif player == 2:
  player_play = "✋ Paper"
elif player == 3:
  player_play = "✌ Scissors"
elif player == 4:
  player_play = "🦎 Lizard"
elif player == 5:
  player_play = "🖖 Spock"
else:
  print("Wrong choice you can only decide between 1 and 5")
print(f"Player chose : {player_play}")

computer = random.randint(1,5)
computer_play = " Not choice"
if computer == 1 :
  computer_play = "✊ Rock"
elif computer == 2:
  computer_play = "✋ Paper"
elif computer == 3:
  computer_play = "✌ Scissors"
elif computer == 4:
  computer_play = "🦎 Lizard"
elif computer == 5:
  computer_play = "🖖 Spock"
else:
  print("Wrong choice you can only decide between 1 and 3")
print(f"Computer chose: {computer_play}")

if computer == player:
  print("It's a tie")
elif player == 1 and (computer== 4 or computer == 3) or player == 2 and (computer == 1 or computer == 5) or player == 3 and (computer == 2 or computer == 4) or player == 4 and (computer == 2 or computer == 5) or player == 5 and (computer == 1 or computer == 3):
  print("The player won")
else:
  print("The computer won")