
Welcome to Tic Tac Toe

Run using python tictactoe.py

In this game human plays against computer.
The tic tac toe game works by the minimax initially the game board contains all empty squares
[  ]     [  ]     [  ]
[  ]     [  ]     [  ]
[  ]     [  ]     [  ]
The algorithm starts with human making a move with ‘X. It asks the human to choose the index of the squares from 1 to 9. After human selects a move it prints “Computer Turn [O]” stating its computer’s move. Then the game board is printed with updated computer move. Before printing the game board computer move is printed and the number of nodes searched using regular minimax. Again the human makes its move and the computer generates again.

This continues till the game state reaches win state or lost state or draw state. If the player reaches a winning position the code stops and prints who is the winner

TEST RUN:
Welcome to Tic Tac Toe
Human will play against AI
First move is maken by human
Human turn [X]
----------------

----------------
[   ][   ][   ]
----------------
[   ][   ][   ]
----------------
[   ][   ][   ]
----------------
Enter the position to place using 1 to 9: 1
----------------

----------------
[ X ][   ][   ]
----------------
[   ][   ][   ]
----------------
[   ][   ][   ]
----------------
Computer turn [O]
1 1 Position
The AI generated 59705 nodes
Human turn [X]
----------------

----------------
[ X ][   ][   ]
----------------
[   ][ O ][   ]
----------------
[   ][   ][   ]
----------------
Enter the position to place using 1 to 9: 3
----------------

----------------
[ X ][   ][ X ]
----------------
[   ][ O ][   ]
----------------
[   ][   ][   ]
----------------
Computer turn [O]
0 1 Position
The AI generated 927 nodes
Human turn [X]
----------------

----------------
[ X ][ O ][ X ]
----------------
[   ][ O ][   ]
----------------
[   ][   ][   ]
----------------
Enter the position to place using 1 to 9: 8
----------------

----------------
[ X ][ O ][ X ]
----------------
[   ][ O ][   ]
----------------
[   ][ X ][   ]
----------------
Computer turn [O]
1 0 Position
The AI generated 61 nodes
Human turn [X]
----------------

----------------
[ X ][ O ][ X ]
----------------
[ O ][ O ][   ]
----------------
[   ][ X ][   ]
----------------
Enter the position to place using 1 to 9: 7
----------------

----------------
[ X ][ O ][ X ]
----------------
[ O ][ O ][   ]
----------------
[ X ][ X ][   ]
----------------
Computer turn [O]
1 2 Position
The AI generated 4 nodes
Computer turn [O]
----------------

----------------
[ X ][ O ][ X ]
----------------
[ O ][ O ][ O ]
----------------
[ X ][ X ][   ]
----------------
YOU LOST THE GAME

Process finished with exit code 0

In this case the AI won and Human lost as we are playing as human.

Welcome to Tic Tac Toe
Human will play against AI
First move is maken by human
Human turn [X]
----------------

----------------
[   ][   ][   ]
----------------
[   ][   ][   ]
----------------
[   ][   ][   ]
----------------
Enter the position to place using 1 to 9: 3
----------------

----------------
[   ][   ][ X ]
----------------
[   ][   ][   ]
----------------
[   ][   ][   ]
----------------
Computer turn [O]
1 1 Position
The AI generated 59705 nodes
Human turn [X]
----------------

----------------
[   ][   ][ X ]
----------------
[   ][ O ][   ]
----------------
[   ][   ][   ]
----------------
Enter the position to place using 1 to 9: 1
----------------

----------------
[ X ][   ][ X ]
----------------
[   ][ O ][   ]
----------------
[   ][   ][   ]
----------------
Computer turn [O]
0 1 Position
The AI generated 927 nodes
Human turn [X]
----------------

----------------
[ X ][ O ][ X ]
----------------
[   ][ O ][   ]
----------------
[   ][   ][   ]
----------------
Enter the position to place using 1 to 9: 8
----------------

----------------
[ X ][ O ][ X ]
----------------
[   ][ O ][   ]
----------------
[   ][ X ][   ]
----------------
Computer turn [O]
1 0 Position
The AI generated 61 nodes
Human turn [X]
----------------

----------------
[ X ][ O ][ X ]
----------------
[ O ][ O ][   ]
----------------
[   ][ X ][   ]
----------------
Enter the position to place using 1 to 9: 6
----------------

----------------
[ X ][ O ][ X ]
----------------
[ O ][ O ][ X ]
----------------
[   ][ X ][   ]
----------------
Computer turn [O]
2 2 Position
The AI generated 5 nodes
Human turn [X]
----------------

----------------
[ X ][ O ][ X ]
----------------
[ O ][ O ][ X ]
----------------
[   ][ X ][ O ]
----------------
Enter the position to place using 1 to 9: 7
----------------

----------------
[ X ][ O ][ X ]
----------------
[ O ][ O ][ X ]
----------------
[ X ][ X ][ O ]
----------------
THE GAME IS DRAW!

The game is draw as both AI and human never reached the winning state.


