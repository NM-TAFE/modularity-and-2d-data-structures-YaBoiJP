#functions that make the game run

from tic_tac_toe.board import Board
p1 = "X"
p2 = "O"
empty = " "

def check_win(board):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for wc in win_conditions:
        if board[wc[0] // 3][wc[0] % 3] == board[wc[1] // 3][wc[1] % 3] == board[wc[2] // 3][wc[2] % 3] != empty:
            print("Player", board[wc[0] // 3][wc[0] % 3], "wins!")
            return True
    return False

def check_tie(board):
    for row in board:
        for cell in row:
            if cell == empty:
                return False 
    return True  


def game_play():
    board = Board()
    empty = " "
    p1 = "X"
    p2 = "O"
    while True:
        player = p1 if board.count(empty) % 2 == 1 else p2
        board.display()
        next_move = input("It is your turn to choose a square " + player + " (0-8): ")
        if next_move.isdigit() and 0 <= int(next_move) <= 8 and board.cells[int(next_move) // 3][int(next_move) % 3] == empty:
            row = int(next_move) // 3   
            col = int(next_move) % 3
            board.cells[row][col] = player
            if check_win(board.cells):
                board.display()
                print("Player", player, "wins!")
                break
            elif check_tie(board.cells):
                board.display()
                print("It's a tie!")
                break
        else:
            print("Invalid move, try again.")

game_play()
