ROCK = r"""
 .----------------. 
| .--------------. |
| |     ____     | |
| |   .'    `.   | |
| |  /        \  | |
| |  |  ROCK  |  | |
| |  \        /  | |
| |   `.____.'   | |
| |              | |
| '--------------' |
 '----------------' 
"""

PAPER = r"""
 .----------------. 
| .--------------. |
| |   ________   | |
| |  |        |  | |
| |  | PAPER  |  | |
| |  |        |  | |
| |  |        |  | |
| |  |________|  | |
| |              | |
| '--------------' |
 '----------------' 
"""

SCISSORS = r"""
 .----------------. 
| .--------------. |
| |          _   | |
| |  \      / /  | |
| |   \    / /   | |
| |     [][]     | |
| |   /    \ \   | |
| |  /      \_\  | |
| |   SCISSORS   | |
| '--------------' |
 '----------------' 
"""
ASSETS = [ROCK, PAPER, SCISSORS]

DEFAULT_COLOR = "\033[0m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"
WHITE = "\033[37m"

def get_move():
    return 1

def print_move(user,computer,result):
    for i in range(len(ASSETS[0].split('\n'))):
        print(ASSETS[user-1].split('\n')[i] + "   " + ASSETS[computer-1].split('\n')[i])

while True:
    while True:
        choice = input("Enter your choice: Rock (1), Paper(2) or Scissors(3): ").lower()
        if choice in {"rock", "paper", "scissors", "1", "2", "3", "r", "p", "s"}:
            break
    
    if choice in {"rock", "1", "r"}:
        choice = 1
    elif choice in {"paper", "2", "p"}:
        choice = 2
    elif choice in {"scissors", "3", "s"}:
        choice = 3
    
    computer = get_move()

    results = None # 0 = draw, 1 = win, 2 = lose
    if choice == 1:
        if computer == 1:
            results = 0
        elif computer == 2:
            results = 2
        else:
            results = 1
    elif choice == 2:
        if computer == 1:
            results = 1
        elif computer == 2:
            results = 0
        else:
            results = 2
    elif choice == 3:
        if computer == 1:
            results = 2
        elif computer == 2:
            results = 1
        else:
            results = 0
    
    print_move(choice, computer, results)

    
