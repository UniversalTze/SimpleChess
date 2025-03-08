
"""
Chess Game
Assignment 1
Semester 2, 2021
CSSE1001/CSSE7030
"""

#from types import NoneType
from typing import Optional
from a1_support import *

# Replace these <strings> with your name, student number and email address.
__author__ = "Tze Kheng Goh, s4703754"
__email__ = "t.k.goh@uqconnect.edu.au"

def initial_state()-> None: 
    """
    Parameters:
        Takes no arguments.
        
    Return:
        Tuple: Chessboard.
    """
    return (
        ("".join(BLACK_PIECES[:-1]), BLACK_PAWN * 8)
        + (EMPTY * 8,) * 4
        + (WHITE_PAWN * 8, "".join(WHITE_PIECES[:-1]))
    )

def print_board(board) -> None:
    """
    Function will return a string version of chessboard with two spaces between
    "abcdefgh" and "87654321".
    
    Parameters:
        board: tuple.
        
    Return:
        str: the initial state of chessboard.
    """ 
    for i, line in enumerate(board):
        print(f"{line}  {8-i}")     
    print("\nabcdefgh")

def square_to_position(square: str):
    """
    Function will returns the coordinates of string given.
    
    Parameters:
        square: string to be converted into coordinates.
        
    Return:
        Tuple: coordinates on chessboard.
    """
    if len(square) == 2:
        square.split(' ')
        x = 8 -  int(square[1])
        y = ord(square[0]) - 97
        return (x,y)

def process_move(user_input: str):
    """
    Function will take a string input from user and convert it to previous
    and future coordinates the user wants to move to.
    
    Parameters:
        User_input: string.
        
    Return:
        Tuple: Previous and next position. 
    """
    if len(user_input) == 5:
        Previous, _, Next = user_input.partition(' ')
        Previous = square_to_position(Previous) 
        Next = square_to_position(Next)
        return (Previous, Next)

def change_position(board, position, character: str):
    """
    Function returns a tuple chessboard with position changed.
    
    Parameters:
        board: tuple.
        position: tuple with integers. 
        character: string.
        
    Return:
        Tuple: chessboard in its current state.   
    """
    chess_board = list(board)
    row = position[0]
    column = position[1]
    new_position =list(chess_board[row])  
    new_position[column] = character
    chess_board[row] = "".join(new_position) #updated position depending on the input 
    return tuple(chess_board)

def clear_position(board, position):
    """
    Function will clear the position given on the board.
    
    Parameters:
        board: tuple.
        position: tuple with integers.
        
    Return:
        Tuple: chessboard. 
    """
    chess_board = list(board)
    row = position[0]
    column = position[1]
    clear_position = list(chess_board[row])
    clear_position[column] = "."
    chess_board[row] = "".join(clear_position) 
    return tuple(chess_board)

def update_board(board, move):
    """
    Function will update the board with position moved, depending on input.
    
    Parameters:
        board: Tuple chessboard in its current state.
        move: Tuple with positions.
        
    Return:
        Tuple: a new version of board with position updated.
    """
    update_piece = piece_at_position(move[0], board)
    board = clear_position(board, move[0])
    board = change_position(board, move[1], update_piece)
    
    return board

def is_current_players_piece(piece: str, whites_turn: bool) -> bool:
    """
    Fucntion checks if piece belongs to player whose turn it is.
    
    Parameters:
        piece: string.
        whites_turn: boolean of True if whites turn.
        
    Return:
        A boolean value of true if piece belongs to player whose turn it is,
        else False. 
    """
    for c in piece:
        if c in "rnbqkp" and not whites_turn:
            return True
        if c in "RNBQKP" and whites_turn:
            return True
        else:
            return False

def is_move_valid(move, board, whites_turn: bool) -> bool:
    """
    Returns True if move is valid on current board for that
    player's turn and obeys the rules of chess.

    Parameters:
        move: tuple.
        board: current state of board. 
        whites_turn: whites_turn: boolean of True if whites turn. 

    Returns:
        A boolean value True if move is valid, is the person's turn and
        obeys the rules of chess. Else, False. 
    """
    piece = piece_at_position(move[0], board)
    turn = is_current_players_piece(piece, whites_turn)
    fmo = get_possible_moves(move[0], board)
    check = is_in_check(board, whites_turn)
    if move[1] in fmo and turn :
        board = update_board(board, move)
        #applies new position to current state of board. 
        if not is_in_check(board, whites_turn): 
            return True
    return False 

def can_move(board, whites_turn: bool) -> bool:
    """
    Function returns True if move does not put piece
    in check.

    Paramters:
        board: tuple chessboard
        whites_turn: whites_turn: boolean of True if whites turn. 

    Returns:
        A boolean value True if move is valid
        without putting player in check for the players turn. 
    """
    pieces = WHITE_PIECES if whites_turn else BLACK_PIECES
    for i, row in enumerate(board):
        for j, piece in enumerate(row): #checks every position on board.
            position = (i, j)
            if piece in pieces: #pieces still on the board. 
                a_moves = get_possible_moves(position, board)
                for fmo in a_moves:
                    if is_move_valid((position, fmo), board, whites_turn):
                        return True
    return False 
                       
def is_stalemate(board, whites_turn: bool) -> bool:
    """
    Function will check if the game has ended in a stalemate.

    Parameters:
        board: tuple of current state of board.
        whites_turn: whites_turn: boolean of True if whites turn.

    Returns:
        A boolean value of True if game has ended in stalemate, else
        will return False. 
    """
    check = is_in_check(board, whites_turn)
    end = can_move(board, whites_turn)
    if not end and not check:
        return True
    return False

def check_game_over(board, whites_turn: bool) -> bool:
    """
    Function will check if game is still alive or if it has ended
    in a stalemate or checkmate.

    Parameters:
        board: tuple of current state of board.
        whites_turn: boolean of True if whites turn.

    Returns:
        if checkmate:
            Fuction will print "\nCheckmate" and return True.
        if stalemate:
            Fucntion will print "\nStalemate" and return True.
        if game is still alive:
            Function will print whoever is in check on that player's turn
            and return False. 
    """
    stalemate = is_stalemate(board, whites_turn)
    check = is_in_check(board, whites_turn)
    moves = can_move(board, whites_turn)
    if stalemate:
        print("\nStalemate")
        return True
    if check and not moves:
        print("\nCheckmate")
        return True
    if check and moves:
        if whites_turn:
            print("\nWhite is in check")
        else:
            print("\nBlack is in check")
        return False 
    return False
     

def attempt_promotion(board, whites_turn: bool) -> "Board" :
    """ 
    Checks whether there is a pawn on the board that needs to be promoted.
        If there is, we prompt the user for the piece to upgrade to, replace
        the pawn with this piece, and return the updated board. Otherwise,
        just return the original board.

    Parameters:
        board (Board): The board state.
        whites_turn (bool): True iff white's turn.

    Returns:
        (Board): The updated board state, with either the promoted piece
                    in place or no changes.

    """   
    Queen = "q" 
    Rook = "r" 
    Bishop = "b"  
    Knight = "n" 
    Valid_promotions = (Queen, Rook, Bishop, Knight)
    Message = "What piece would you like (q, r, b, n)? " 
    Invaid_input = "Not a valid piece! "
    if whites_turn: 
        row = 0 
        pawn, queen, rook, bishop = WHITE_PAWN, WHITE_QUEEN, WHITE_ROOK, WHITE_BISHOP 
        knight = WHITE_KNIGHT
    else: 
        row = BOARD_SIZE - 1  
        pawn, queen, rook, bishop = BLACK_PAWN, BLACK_QUEEN, BLACK_ROOK, BLACK_BISHOP 
        knight = BLACK_KNIGHT 
    
    for col, piece in enumerate(board[row]): 
        if piece == pawn: 
            message = input(Message) 
            while message not in Valid_promotions: 
                print(Invaid_input + "\n" + Message) 
            else: 
                if message == Queen:  
                    new_piece = queen 
                elif message == Rook: 
                    new_piece = rook 
                elif message == Bishop: 
                    new_piece = bishop 
                elif message == knight: 
                    new_piece = knight
            return change_position(board, (row, col), new_piece)
    
    return board  


def is_valid_castle_attempt(move: Move, board: Board, whites_turn: bool,
    castling_info: Tuple[bool, bool, bool],
) -> bool: 
    """Determines if the given move is a valid attempt at castling for the 
    current game state.

    Parameters:
        move (Move): The move to check.
        board (Board): The current board.
        whites_turn (bool): True iff it's white's turn.
        castling_info (tuple<bool, bool, bool>): A tuple of booleans which are
                true iff the respective left rook, king and right rook have moved
                this game.

    Returns:
        (bool): True iff the supplied move is a valid castling attempt. 
    """ 
    KING_CASTLING_COL_DELTA = 2 
    KING_CASTLING_DELTAS = (
    (0, -KING_CASTLING_COL_DELTA),
    (0, KING_CASTLING_COL_DELTA),
)
    lrook_move, king_move, rrook_move = castling_info 

    if king_move: 
        return False  
    
    (start_row, start_col), (end_row, end_col) = move
    col_delta = end_col - start_col 
    row_delta = end_row - start_row  

    if (row_delta, col_delta) not in KING_CASTLING_DELTAS: 
        return False  

    long_castle = col_delta < 0  

    if (long_castle and lrook_move) or (not long_castle and rrook_move): 
        return False 

    direction = int(col_delta / KING_CASTLING_COL_DELTA) 
    squares = 3 if long_castle else 2 
    rook_position = start_row, start_col + (direction*(squares + 1)) 

    if not whites_turn:   
        rook = BLACK_ROOK 
    else: 
        rook = WHITE_ROOK

    if piece_at_position(rook_position, board) != rook: 
        return False  

    for i in range(squares): 
        position = start_row, start_col + ((i+1)*direction)
        if piece_at_position(position, board) != EMPTY: 
            return False 

    if is_in_check(board, whites_turn): 
        return False 

    for i in range(squares): 
        new_position = start_row, start_col + ((i+1)*direction) 
        move = ((start_row, start_col), new_position)
        new_board = update_board(board, move) 
        if is_in_check(new_board, whites_turn): 
            return False 
        
    return True 
        
    
def perform_castling(move: Move, board: Board) -> Board: 
    """ 
    Given a valid castling move, returns the resulting board state.

    Parameters:
        move (Move): The move to make.
        board (Board): The current board.

    Returns:
        (Board): The board representing the game state after castling.
    """
    (start_row, start_col), (_, end_col) = move
    col_delta = end_col - start_col  
    long_castle = col_delta < 0 

    if long_castle: 
        rook_p = (start_row, 0)  
    else: 
        rook_p = (start_row, BOARD_SIZE - 1)  
    
    temporary_state = update_board(board, move)
    #updades king position 
    rook_col_delta = int(-col_delta/2) 
    move = rook_p, (start_row, end_col + rook_col_delta)
    final_board = update_board(temporary_state, move) 
    return final_board 

def update_castling_info(
    move: Move, whites_turn: bool, castling_info: Tuple[bool, bool, bool]
) -> Tuple[bool, bool, bool]:
    """Returns the updated castling info for the respective player, after
    performing the given, valid move.

    Parameters:
        move (Move): The move just performed
        whites_turn (bool): True iff it's white's turn.
        castling_info (tuple<bool, bool, bool>): A tuple of booleans which are
                true iff the respective left rook, king and right rook have moved
                this game.
    Returns:
        (tuple<bool, bool, bool>): The castling info after the move has been
                performed.
    """
    original_major_piece_row = BOARD_SIZE - 1 if whites_turn else 0
    # Corresponding to the original columns for the left rook, king and right
    # rook respectively.
    original_castling_piece_cols = [0, 4, BOARD_SIZE - 1]
    move_start_position, _ = move

    # If the player is moving a rook or king that hasnt moved yet, update the
    # appropriate column in the castling info.
    for i, col in enumerate(original_castling_piece_cols):
        original_position = original_major_piece_row, col
        piece_already_moved = castling_info[i]
        if move_start_position == original_position and not piece_already_moved:
            castling_info = castling_info[:i] + (True,) + castling_info[i + 1 :]

    return castling_info
    

def h_command():
    """
    Help command. 
    """
    print(HELP_MESSAGE)
   
def main():
    """Entry point to gameplay"""
    board = initial_state()
    whites_turn = True 
    white_pieces_moved = (False, False, False)  # Left rook, king, right rook
    black_pieces_moved = (False, False, False)
    over = check_game_over(board, whites_turn)
    while not over: 
        print_board(board) 
        if whites_turn:
            Name = input("\nWhite's move: ")
        elif not whites_turn:
            Name = input("\nBlack's move: ")
        if Name in "Hh":
                h_command()
        elif Name in "Qq":
            Message = input("Are you sure you want to quit? ")
            if Message in ("Yy"):
                break
        elif not valid_move_format(Name):
            print("Invalid move\n") 
            continue 
        else:  
            castling_info = (white_pieces_moved if whites_turn else black_pieces_moved)
            moves = process_move(Name)
            if is_move_valid(moves, board, whites_turn):
                board = attempt_promotion(update_board(board, moves), whites_turn)
            elif is_valid_castle_attempt(moves, board, whites_turn, castling_info): 
                board = perform_castling(moves, board) 
            else: 
                print("Invalid move\n")  
                continue
        
            castling_info = update_castling_info(moves, whites_turn, castling_info)
            if whites_turn:
                white_pieces_moved = castling_info
            else:
                black_pieces_moved = castling_info

            whites_turn = not whites_turn
        over = check_game_over(board, whites_turn)
        if over:
            return

if __name__ == "__main__":
    main()
