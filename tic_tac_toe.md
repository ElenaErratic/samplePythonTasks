# Tic-Tac-Toe

[Solution](tic_tac_toe.py)


## Objectives
In this stage, you should write a program that:

1. Prints an empty grid at the beginning of the game.
2. Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a grid with the changes if everything is okay.
3. nds the game when someone wins or there is a draw.

You need to output the final result at the end of the game.

Good luck!

## Coordinates
Suppose the top left cell has the coordinates (1, 1) and the bottom right cell has the coordinates (3, 3) like in this table:

(1, 1) (1, 2) (1, 3)

(2, 1) (2, 2) (2, 3)

(3, 1) (3, 2) (3, 3)

## Example
The example below shows how your program should work.
Notice that after `Enter the coordinates:` comes the user input.

\--------

| _ _ _ |

| _ _ _ |

| _ _ _ |

\--------

Enter the coordinates: 2 2

\--------

| _ _ _ |

| _ X _ |

| _ _ _ |

\--------

Enter the coordinates: 2 2

This cell is occupied! Choose another one!

Enter the coordinates: two two

You should enter numbers!

Enter the coordinates: 1 4

Coordinates should be from 1 to 3!

Enter the coordinates: 1 1

\--------

| O _ _ |

| _ X _ |

| _ _ _ |

\--------

Enter the coordinates: 3 3

\--------

| O _ _ |

| _ X _ |

| _ _ X |

\--------

Enter the coordinates: 2 1

\--------

| O _ _ |

| O X _ |

| _ _ X |

\--------

Enter the coordinates: 3 1

\--------

| O _ _ |

| O X _ |

| X _ X |

\--------

Enter the coordinates: 2 3

\--------

| O _ _ |

| O X O |

| X _ X |

\--------

Enter the coordinates: 3 2

\--------

| O _ _ |

| O X O |

| X X X |

\--------

X wins
