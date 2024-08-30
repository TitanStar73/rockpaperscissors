# rockpaperscissors

Console based Rock Paper Scissors game!

![image](https://github.com/user-attachments/assets/5606370b-6bc5-4d2f-827c-4368afaf913a)

# How to Play

Run main.py on your system, no dependencies :) OR run main.exe

# Playstyles!

To give the computer more personality you can build custom playstyles

0 - Random

1 - Probability based on history

2 - Pick players's previous move

9 - Always picks the winning move

r123 - Creates a bias based on the weights for rock, paper, scissors here 1,2,3 ; Only works on play style 0 and initial history for p1

Some basic playstyles, feel free to customise :)

1r111 - Always picks random

9r111 - Always win

2r111 - Historical probability (based on players last 40 moves)

0091111122r111 - Well rounded with slight edge but can lose

0009111122r765 - Uses some studies on the best moves (initially)
