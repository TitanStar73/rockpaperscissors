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

PLAY_STYLE = "1r111" # Randomly picks a play style from here, that way computers can have a specific "playstyle"
"""
Play styles:
0 - Random
1 - Probability based on history
2 - Pick players's previous move
9 - Always picks the winning move
r123 - Creates a bias based on the weights for rock, paper, scissors here 1,2,3 ; Only works on play style 0 and initial history for p1

Some basic playstyles, feel free to customise :)
1r111 - Always picks random
9r111 - Always win
2r111 - Historical probability
0091111122r111 - Well rounded with slight edge but can lose
0009111122r765 - Uses some studies on the best moves (initially)
"""

PLAYBOOK = []
for i in range(int(PLAY_STYLE[-3])):
    PLAYBOOK.append(1)
for i in range(int(PLAY_STYLE[-2])):
    PLAYBOOK.append(2)
for i in range(int(PLAY_STYLE[-1])):
    PLAYBOOK.append(3)

PLAY_STYLE = PLAY_STYLE.split('r')[0]
PLAY_STYLE = [int(char) for char in PLAY_STYLE]

history = [random.choice(PLAYBOOK) for i in range(40)]

def get_move():
    my_play = random.choice(PLAY_STYLE)
    if my_play == 0:
        return random.choice(PLAYBOOK)
    elif my_play == 1:
        thing = random.choice(history)
        if thing == 1:
            return 2
        elif thing == 2:
            return 3
        return 1
    elif my_play == 2:
        return history[-1]
    elif my_play == 9:
        return 9
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
    if computer == 9:
        if choice == 1:
            computer = 2
        elif choice == 2:
            computer = 3
        else:
            computer = 1

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

    
