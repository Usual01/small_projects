import random

user_score = 0
computer_score = 0
games = 0
draw = 0
options = ["rock", "paper", "scissors"]

while True:
    user = input("Choose between Rock/Paper/scisssors\npress q to quit at anytime\n").lower()
    if user == "q":
        break
    if user not in options:
        continue 
    index = random.randint(0, 2)
    computer = options[index]
    print(f"computer chose: {computer}")
    if (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" or computer == "paper"):
        print("you won", "you chose",user.upper(),"computer chose", computer.upper())
        user_score += 1
        games += 1
    elif computer == user:
        draw += 1
        print("its a tie", "you chose",user.upper(),"computer chose", computer.upper())
        games += 1
    else:
        print("you lost", "you chose",user.upper(),"computer chose", computer.upper())
        computer_score += 1
        games += 1
if user_score != computer_score:
    print("you won", user_score, "computer won", computer_score, "and tied in", draw,"out of",games,"games")
elif user_score == computer_score:
    print("It was a draw!","you won", user_score, "computer won", computer_score, "and tied in", draw,"out of",games,"games")