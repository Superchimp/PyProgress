import sys
the_board = {"top-L": " ", "top-M": " ", "top-R": " ",
             "mid-L": " ", "mid-M": " ", "mid-R": " ",
             "low-L": " ", "low-M": " ", "low-R": " "}

def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])
    
def check_winner(board):
    if board["top-L"] != " ":
        if board["top-L"] == board["top-M"] == board["top-R"] or\
           board["top-L"] == board["mid-M"] == board["low-R"] or\
           board["top-L"] == board["mid-L"] == board["low-L"]:
            print("The winner is: ", board["top-L"])
            sys.exit()
    if board["mid-M"] != " ":
        if board["top-M"] == board["mid-M"] == board["low-M"] or\
           board["mid-L"] == board["mid-M"] == board["mid-R"] or\
           board["low-L"] == board["mid-M"] == board["top-R"]:
            print("The winner is: ", board["mid-M"])
            sys.exit()
    if board["low-R"] != " ":
        if board["low-L"] == board["low-M"] == board["low-R"] or\
           board["top-R"] == board["mid-R"] == board["low-R"]:
            print("The winner is: ", board["low-R"])
            sys.exit()
            
running = True
turn = "O"
move = ""
while running:  
    for i in range(9):
        print_board(the_board)
        if i > 2:
            check_winner(the_board)
        while True:
            print("Turn for "+ turn + ". Take which space?")
            move = input()
            if move not in the_board:
                print("Sorry, please entre a valid move (eg. low-M)")
                continue
            else:
                break
        the_board[move] = turn
        move = ""
        if turn == "O":
            turn = "X"
        else:
            turn = "O"
        #print_board(the_board)