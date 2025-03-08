# SimpleChess
Simple chess game developed in python. (Very first exposure to programming). 

## Context
The game rules follow tradiotional chess. Only traditional rule that was not implemented was en Passant. The 8 by 8 chest board is represented by numbers and columns. The numbers indicate the rows from (largest to smallest) and the alphabet (a-h) represents the columns in alphabetical order. Examples will be shown at the bottom of the file. 

### Gameplay
To run the file, git clone the repo and just run the a1 file :). 

- When your program runs, the initial board state should be displayed, and the user should be prompted for white’s first move.
- The standard prompt for white’s move should read **‘White’s move: '** and the standard prompt for black’s move should read **‘Black’s move: ’.**
- When a user isprompted for a move, they may do one of four things:
  - Enter ‘h’ or ‘H’: Print help text and re-prompt for move (without switching turns).
  - Enter ‘q’ or ‘Q’: Prompt the user to confirm they want to quit the game. Terminate the game on ‘y’ or ‘Y’ and re-commence play (prompt for move without switching turns) on any other input.
  - **Valid Move**: The move should be performed, the updated board should be displayed, and the player whose turn it is should switch. The user whose turn it becomes should be prompted for their move. A valid move will be of the form ‘from_square to_square’. Users must enter the positions as a letter-number (row-column) pair. Example of valid input (will depend on pieces on the board): "e2 e4" 
  - **Invalid Move**: The user should be informed that their move is invalid before being re-prompted for another move. An invalid move may be text in any form that does not conform to one of the above categories, or it may be a move in valid form that is not a valid move based
on the rules of chess.

### Data Structures and Encoding
- ‘P’, ‘K’, ‘Q’, ‘B’, ‘N’, ‘R’ represent **white’s**: pawn, king, queen, bishop, knight, and rook, respectively.
- ‘p’, ‘k’, ‘q’, ‘b’, ‘n’, ‘r’ represent **black’s**: pawn, king, queen, bishop, knight, and rook, respectively.
- ‘.’: An empty square.

## Example Gameplay
A folder of .txt files with different gameplays has been provided.
```
rnbqkbnr 8
pppppppp 7
........ 6
........ 5
........ 4
........ 3
PPPPPPPP 2
RNBQKBNR 1

abcdefgh

White's move: e2 e4
```
**Updated Board**
```
rnbqkbnr 8
pppppppp 7
........ 6
........ 5
....P... 4
........ 3
PPPP.PPP 2
RNBQKBNR 1

abcdefgh
```

