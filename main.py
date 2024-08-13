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

import random

history = [random.randint(1,3) for i in range(40)]

def get_move():
    thing = random.choice(history)
    if thing == 1:
        return 2
    elif thing == 2:
        return 3
    return 1

RESULTS_COLOR = [YELLOW, GREEN, RED]

def print_move(user,computer,result):
    print(RESULTS_COLOR[result], end='')
    for i in range(len(ASSETS[0].split('\n'))):
        print(ASSETS[user-1].split('\n')[i] + "   " + ASSETS[computer-1].split('\n')[i])
    print(DEFAULT_COLOR, end='')


scorePlayer = 0
scoreComputer = 0

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
    
    if results == 1:
        scorePlayer += 1
    elif results == 2:
        scoreComputer += 1

    print_move(choice, computer, results)
    print(f"Player: {scorePlayer} Computer: {scoreComputer}")
    history.append(choice)
    history = history[1:]

    
