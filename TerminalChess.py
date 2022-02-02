#          CCCC         HHHH     HHHH    EEEEEEEEEEEEE       SSSSSS          SSSSSS   
#         CCCCCCC       HHHH     HHHH    EEEEEEEEEEEEE      SSSSSSSS        SSSSSSSS  
#       CCCC   CCCC     HHHH     HHHH    EEEE             SSSSS    SSS    SSSSS    SSS
#      CCCC     CCCC    HHHHHHHHHHHHH    EEEE               SSSSS           SSSSS     
#      CCCC             HHHHHHHHHHHHH    EEEEEEEE             SSSS            SSSS    
#      CCCC             HHHHHHHHHHHHH    EEEEEEEE               SSSS            SSSS  
#       CCCC   CCCC     HHHH     HHHH    EEEE             SSS    SSSS     SSS    SSSS 
#        CCCCCCCC       HHHH     HHHH    EEEEEEEEEEEEE     SSSSSSSS        SSSSSSSS   
#          CCCC         HHHH     HHHH    EEEEEEEEEEEEE       SSSSS           SSSSS    




#A CHESS GAME Created by Dave Angelo D. Jimenez


#Edited using Python 3.8.5 on the Python IDLE editor  
#This is the second attempt at developing a terminal based chess game. 
#Here's to hoping I can manage to keep the code clean and readable on this second attempt

#About the game
#The game makes use of a two-dimensional List to simulate a chessboard with pieces on it. Movement and interactions are done solely based on the positions of the pieces on the two-dimensional List.
#The pieces are represented by the combination of the color of the piece, the initials of the piece (except for the knight, knight is N), and an assigned number for distinguishing between the duplicate pieces.

#Feaures:
#   Basic Legal Moves for all pieces
#   En Passant
#   Castling
#   Pawn Promotion
#   Checkmates
#   Manual Draw
#   Saving Current Game
#   Loading Last game
#   High Score Wins
#   ASCII GUI
#   Two Players

#Lacks checking for stalemates. Manual Draw required. No enemy AI

import copy

#Initialize Pieces
wr1 = "wR1"
wr2 = "wR2"
wn1 = "wN1"
wn2 = "wN2"
wb1= "wB1"
wb2= "wB2"
wk = "wK1"
wq = "wQ1"
wp1 = "wP1"
wp2 = "wP2"
wp3 = "wP3"
wp4 = "wP4"
wp5 = "wP5"
wp6 = "wP6"
wp7 = "wP7"
wp8 = "wP8"

br1 = "bR1"
br2 = "bR2"
bn1 = "bN1"
bn2 = "bN2"
bb1 = "bB1"
bb2 = "bB2"
bk = "bK1"
bq = "bQ1"
bp1 = "bP1"
bp2 = "bP2"
bp3 = "bP3"
bp4 = "bP4"
bp5 = "bP5"
bp6 = "bP6"
bp7 = "bP7"
bp8 = "bP8"
fs = "   "

#Game System
piece = []                      #Initializes Board
state = 0                       #Initialize Game State
white_turn = True               #Initialize Turn

#Checking
checking_piece = ""
check_square_list = []          #Initialize List that records the squares that block the opposing king

#Double Checked
double_checked = False

#En Passant
ep_square = []
can_ep = False
ep_capture = False

#Castling
has_bR1_moved = False
has_bR2_moved = False
has_wR1_moved = False
has_wR2_moved = False
has_bK1_moved = False
has_wK1_moved = False
can_castle_white_short = False
can_castle_white_long = False
can_castle_black_short = False
can_castle_black_long = False

#Pawn Promotion
pawn_to_promote = ""
white_promotion_number = 3
black_promotion_number = 3

#Score
score_list = []

def initialize():
    global piece
    global white_turn
    global has_bR1_moved
    global has_bR2_moved
    global has_wR1_moved
    global has_wR2_moved
    global has_bK1_moved
    global has_wK1_moved
    global can_castle_white_short
    global can_castle_white_long
    global can_castle_black_short
    global can_castle_black_long
    global pawn_to_promote
    global white_promotion_number
    global black_promotion_number
    global double_checked
    
    #Initializes standard chess piece layout
    piece = [[wr1,wn1,wb1,wq,wk,wb2,wn2,wr2], [wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8], [fs,fs,fs,fs,fs,fs,fs,fs], [fs,fs,fs,fs,fs,fs,fs,fs],      
             [fs,fs,fs,fs,fs,fs,fs,fs], [fs,fs,fs,fs,fs,fs,fs,fs], [bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8], [br1,bn1,bb1,bq,bk,bb2,bn2,br2]]

    #Initializes starting turn as white
    white_turn = True

    #Initializes Castling Components
    has_bR1_moved = False
    has_bR2_moved = False
    has_wR1_moved = False
    has_wR2_moved = False
    has_bK1_moved = False
    has_wK1_moved = False
    can_castle_white_short = False
    can_castle_white_long = False
    can_castle_black_short = False
    can_castle_black_long = False

    #Initializes Pawn Promotion Components
    pawn_to_promote = ""
    white_promotion_number = 3
    black_promoton_number = 3

    double_checked = False
    

def mainMenu():             #The main menu for the Game
    print("                                                                                     ")
    print("A seemingly functional chess game by Dave Angelo D. Jimenez                          ")
    print("______________________________________________________________________________________________")
    print("                                                                                     ")
    print("          CCCC         HHHH     HHHH    EEEEEEEEEEEEE       SSSSSS          SSSSSS   ")
    print("         CCCCCCC       HHHH     HHHH    EEEEEEEEEEEEE      SSSSSSSS        SSSSSSSS  ")
    print("       CCCC   CCCC     HHHH     HHHH    EEEE             SSSSS    SSS    SSSSS    SSS")
    print("      CCCC     CCCC    HHHHHHHHHHHHH    EEEE               SSSSS           SSSSS     ")
    print("      CCCC             HHHHHHHHHHHHH    EEEEEEEE             SSSS            SSSS    ")
    print("      CCCC             HHHHHHHHHHHHH    EEEEEEEE               SSSS            SSSS  ")
    print("       CCCC   CCCC     HHHH     HHHH    EEEE             SSS    SSSS     SSS    SSSS ")
    print("        CCCCCCCC       HHHH     HHHH    EEEEEEEEEEEEE     SSSSSSSS        SSSSSSSS   ")
    print("          CCCC         HHHH     HHHH    EEEEEEEEEEEEE       SSSSS           SSSSS    ")
    print()
    print("                                       Chess Piece Designs taken from www.asciiart.eu")
    print("______________________________________________________________________________________________")
    print("How to Play: -   To move a piece type in this format [(piece initial) + (number) + (file) + (rank)]")
    print("                     Example: 'Move: p5e4' to move a p5 pawn to the e4 square")
    print("             -   To capture an opposing piece, move your piece to the square that the enemy piece is occupying")
    print("             -   Type commands in game to go back to the main menu or save the game\n")
    print("Enter '1' to Start a New Game")
    print("Enter '2' to Load last Game")
    print("Enter '3' to view Most Wins")
    print("Enter '4' to clear scores")
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("Choice: "))
            valid_choice = True
            if choice > 4:
                print("Invalid choice. Please try again.")
                valid_choice = False
            
        except:
            print("Invalid choice. Please try again.")
            
    if choice == 1:         #If starting a new game, initialize the board and pieces. This block of code is placed here to limit flag usage and prevent reinitialization of pieces
        initialize()
    return choice

def printBoard():           #Prints the ASCII graphics for the Board and the Pieces
    global piece
                                                                                                                                                    #Prototype Layout
    #print("   A     B     C     D     E     F     G     H   ")
    #print(" _____ _____ _____ _____ _____ _____ _____ _____ ")
    #print("#■■■■■#     #■■■■■#     #■■■■■#     #■■■■■#     #")
    #print("# "+piece[7][0]+" # "+piece[7][1]+" # "+piece[7][2]+" # "+piece[7][3]+" # "+piece[7][4]+" # "+piece[7][5]+" # "+piece[7][6]+" # "+piece[7][7]+" #  8")
    #print("#■■■■■#_____#■■■■■#_____#■■■■■#_____#■■■■■#_____#")
    #print("#     #■■■■■#     #■■■■■#     #■■■■■#     #■■■■■#")
    #print("# "+piece[6][0]+" # "+piece[6][1]+" # "+piece[6][2]+" # "+piece[6][3]+" # "+piece[6][4]+" # "+piece[6][5]+" # "+piece[6][6]+" # "+piece[6][7]+" #  7")
    #print("#_____#■■■■■#_____#■■■■■#_____#■■■■■#_____#■■■■■#")
    #print("#■■■■■#     #■■■■■#     #■■■■■#     #■■■■■#     #")
    #print("# "+piece[5][0]+" # "+piece[5][1]+" # "+piece[5][2]+" # "+piece[5][3]+" # "+piece[5][4]+" # "+piece[5][5]+" # "+piece[5][6]+" # "+piece[5][7]+" #  6")
    #print("#■■■■■#_____#■■■■■#_____#■■■■■#_____#■■■■■#_____#")
    #print("#     #■■■■■#     #■■■■■#     #■■■■■#     #■■■■■#")
    #print("# "+piece[4][0]+" # "+piece[4][1]+" # "+piece[4][2]+" # "+piece[4][3]+" # "+piece[4][4]+" # "+piece[4][5]+" # "+piece[4][6]+" # "+piece[4][7]+" #  5")
    #print("#_____#■■■■■#_____#■■■■■#_____#■■■■■#_____#■■■■■#")
    #print("#■■■■■#     #■■■■■#     #■■■■■#     #■■■■■#     #")
    #print("# "+piece[3][0]+" # "+piece[3][1]+" # "+piece[3][2]+" # "+piece[3][3]+" # "+piece[3][4]+" # "+piece[3][5]+" # "+piece[3][6]+" # "+piece[3][7]+" #  4")
    #print("#■■■■■#_____#■■■■■#_____#■■■■■#_____#■■■■■#_____#")
    #print("#     #■■■■■#     #■■■■■#     #■■■■■#     #■■■■■#")
    #print("# "+piece[2][0]+" # "+piece[2][1]+" # "+piece[2][2]+" # "+piece[2][3]+" # "+piece[2][4]+" # "+piece[2][5]+" # "+piece[2][6]+" # "+piece[2][7]+" #  3")
    #print("#_____#■■■■■#_____#■■■■■#_____#■■■■■#_____#■■■■■#")
    #print("#■■■■■#     #■■■■■#     #■■■■■#     #■■■■■#     #")
    #print("# "+piece[1][0]+" # "+piece[1][1]+" # "+piece[1][2]+" # "+piece[1][3]+" # "+piece[1][4]+" # "+piece[1][5]+" # "+piece[1][6]+" # "+piece[1][7]+" #  2")
    #print("#■■■■■#_____#■■■■■#_____#■■■■■#_____#■■■■■#_____#")
    #print("#     #■■■■■#     #■■■■■#     #■■■■■#     #■■■■■#")
    #print("# "+piece[0][0]+" # "+piece[0][1]+" # "+piece[0][2]+" # "+piece[0][3]+" # "+piece[0][4]+" # "+piece[0][5]+" # "+piece[0][6]+" # "+piece[0][7]+" #  1")
    #print("#_____#■■■■■#_____#■■■■■#_____#■■■■■#_____#■■■■■#")

    print("              _        _        _        __       __       _")                           #Prints the letters for each file
    print("    /\       |_)      /        | \      |_       |_       /        |_|")
    print("   /--\      |_)      \_       |_/      |__      |        \_?      | |")
    print()
    
    is_starting_square_white = True
    for i in range(8):                                                                              #Prints the entire bord
        printRank(is_starting_square_white, i)
        is_starting_square_white = False if is_starting_square_white else True

    print()
    
def printRank(is_starting_square_white, position_y):                                                #Prints the squares 
    is_current_square_white = True if is_starting_square_white else False

    for i in range(5):
        if not is_starting_square_white:
            if i == 0:
                print("#########         #########         #########         #########         ", end = "")
            else:
                for j in range(8):
                    printPieceLine(j, i, piece[7-position_y][j], is_current_square_white)
                    is_current_square_white = False if is_current_square_white else True

                    if j == 7:
                        printNumber(i, position_y)
                
        elif is_starting_square_white:
            if i == 0:
                print("         #########         #########         #########         #########", end="")
            else:
                for j in range(8):
                    printPieceLine(j, i, piece[7-position_y][j], is_current_square_white)
                    is_current_square_white = False if is_current_square_white else True
                    if j == 7:
                        printNumber(i, position_y)
        print()
        
def printPieceLine(position_x, position_y, target_piece, is_current_square_white):                      #Prints pieces by line
    if  position_x == 0:
        printSquare(position_y, is_current_square_white, target_piece)
    if  position_x == 1:
        printSquare(position_y, is_current_square_white, target_piece)
    if  position_x == 2:
        printSquare(position_y, is_current_square_white, target_piece)
    if  position_x == 3:
        printSquare(position_y, is_current_square_white, target_piece)
    if  position_x == 4:
        printSquare(position_y, is_current_square_white, target_piece)
    if  position_x == 5:
        printSquare(position_y, is_current_square_white, target_piece)
    if  position_x == 6:
        printSquare(position_y, is_current_square_white, target_piece)
    if  position_x == 7:
        printSquare(position_y, is_current_square_white, target_piece)

def printSquare(position_y, is_current_square_white, target_piece):                                     #Checks for each square in the current line and prints the segments of the pieces corresponding to that square and line
    if target_piece[1] == "R":
        printRook(position_y, is_current_square_white, target_piece)
    elif target_piece[1] == "N":
        printKnight(position_y, is_current_square_white, target_piece)
    elif target_piece[1] == "B":
        printBishop(position_y, is_current_square_white, target_piece)
    elif target_piece[1] == "Q":
        printQueen(position_y, is_current_square_white, target_piece)
    elif target_piece[1] == "K":
        printKing(position_y, is_current_square_white, target_piece)
    elif target_piece[1] == "P":
        printPawn(position_y, is_current_square_white, target_piece)
    else:
        printFreeSpace(position_y, is_current_square_white)

def printNumber(position_y, rank):                                                                      #Prints the numbers for the ranks                                                                                      
    if rank == 0: #Number 8
        if position_y == 1:
            print("  _  ", end = "")
        elif position_y == 2:
            print(" (_) ", end = "")
        elif position_y == 3:
            print(" (_) ", end = "")
    elif rank == 1: #Number 7
        if position_y == 1:
            print("  __ ", end = "")
        elif position_y == 2:
            print("   / ", end = "")
        elif position_y == 3:
            print("  /  ", end = "")
    elif rank == 2: #Number 6
        if position_y == 1:
            print("     ", end = "")
        elif position_y == 2:
            print("  /  ", end = "")
        elif position_y == 3:
            print(" (_) ", end = "")
    elif rank == 3: #Number 5
        if position_y == 1:
            print("  _  ", end = "")
        elif position_y == 2:
            print(" |_  ", end = "")
        elif position_y == 3:
            print("  _) ", end = "")
    elif rank == 4: #Number 4
        if position_y == 1:
            print("   . ", end = "")
        elif position_y == 2:
            print("  /| ", end = "")
        elif position_y == 3:
            print(" '-| ", end = "")
    elif rank == 5: #Number 3
        if position_y == 1:
            print("  _  ", end = "")
        elif position_y == 2:
            print("  _) ", end = "")
        elif position_y == 3:
            print("  _) ", end = "")
    elif rank == 6: #Number 2
        if position_y == 1:
            print("  _  ", end = "")
        elif position_y == 2:
            print("   ) ", end = "")
        elif position_y == 3:
            print("  /_ ", end = "")
    elif rank == 7: #Number 1
        if position_y == 1:
            print("     ", end = "")
        elif position_y == 2:
            print("  /| ", end = "")
        elif position_y == 3:
            print("   | ", end = "")

def printRook(position_y, is_current_square_white, target_piece):                               #Prints segments of the rook by line
    if position_y == 1:
        if is_current_square_white:
            print("  [`'`'] ", end = "")
        else:
            print("##[`'`']#", end = "")
    elif position_y == 2:
        if is_current_square_white:
            print("   |  |  ", end = "")
        else:
            print("###|  |##", end = "")
    elif position_y == 3:
        if is_current_square_white:
            print("   |  |  ", end = "")
        else:
            print("###|  |##", end = "")
    elif position_y == 4:
        if is_current_square_white:
            print("   " + target_piece + "   ", end = "")
        else:
            print("## " + target_piece + " ##", end = "")

def printKnight(position_y, is_current_square_white, target_piece):                             #Prints segments of the knight by line
    if position_y == 1:
        if is_current_square_white:
            print("  \`~'/  ", end = "")
        else:
            print("##\`~'/##", end = "")
    elif position_y == 2:
        if is_current_square_white:
            print("  (o o)  ", end = "")
        else:
            print("##(o o)##", end = "")
    elif position_y == 3:
        if is_current_square_white:
            print("   \ / \ ", end = "")
        else:
            print("###\ / \#", end = "")
    elif position_y == 4:
        if is_current_square_white:
            print("   " + target_piece + "   ", end = "")
        else:
            print("## " + target_piece + " ##", end = "")

def printBishop(position_y, is_current_square_white, target_piece):                             #Prints segments of the bishop by line
    if position_y == 1:
        if is_current_square_white:
            print("  '//\`  ", end = "")
        else:
            print("##'//\`##", end = "")
    elif position_y == 2:
        if is_current_square_white:
            print("  (o:0)  ", end = "")
        else:
            print("##(o:0)##", end = "")
    elif position_y == 3:
        if is_current_square_white:
            print("   (:)   ", end = "")
        else:
            print("###(:)###", end = "")
    elif position_y == 4:
        if is_current_square_white:
            print("   " + target_piece + "   ", end = "")
        else:
            print("## " + target_piece + " ##", end = "")

def printQueen(position_y, is_current_square_white, target_piece):                              #Prints segments of the queen by line
    if position_y == 1:
        if is_current_square_white:
            print("  /\*/\  ", end = "")
        else:
            print("##/\:/\##", end = "")
    elif position_y == 2:
        if is_current_square_white:
            print(" /(o o)\ ", end = "")
        else:
            print("#/(o:o)\#", end = "")
    elif position_y == 3:
        if is_current_square_white:
            print("   (_)   ", end = "")
        else:
            print("###(:)###", end = "")
    elif position_y == 4:
        if is_current_square_white:
            print("   " + target_piece + "   ", end = "")
        else:
            print("## " + target_piece + " ##", end = "")

def printKing(position_y, is_current_square_white, target_piece):                               #Prints segments of the king by line
    if position_y == 1:
        if is_current_square_white:
            print("  |:+:|  ", end = "")
        else:
            print("##|`+'|##", end = "")
    elif position_y == 2:
        if is_current_square_white:
            print("  (o:o)  ", end = "")
        else:
            print("##(o o)##", end = "")
    elif position_y == 3:
        if is_current_square_white:
            print("   (:)   ", end = "")
        else:
            print("###(_)###", end = "")
    elif position_y == 4:
        if is_current_square_white:
            print("   " + target_piece + "   ", end = "")
        else:
            print("## " + target_piece + " ##", end = "")

def printPawn(position_y, is_current_square_white, target_piece):                               #Prints segments of the pawn by line
    if position_y == 1:
        if is_current_square_white:
            print("   (_)   ", end = "")
        else:
            print("###(_)###", end = "")
    elif position_y == 2:
        if is_current_square_white:
            print("   | |   ", end = "")
        else:
            print("###| |###", end = "")
    elif position_y == 3:
        if is_current_square_white:
            print("   |_|   ", end = "")
        else:
            print("###|_|###", end = "")
    elif position_y == 4:
        if is_current_square_white:
            print("   " + target_piece + "   ", end = "")
        else:
            print("## " + target_piece + " ##", end = "")

def printFreeSpace(position_y, is_current_square_white):
    if position_y == 1:
        if is_current_square_white:
            print("         ", end = "")
        else:
            print("#########", end = "")
    elif position_y == 2:
        if is_current_square_white:
            print("         ", end = "")
        else:
            print("#########", end = "")
    elif position_y == 3:
        if is_current_square_white:
            print("         ", end = "")
        else:
            print("#########", end = "")
    elif position_y == 4:
        if is_current_square_white:
            print("         ", end = "")
        else:
            print("#########", end = "")

def gameUpdate():               #Runs the logic for the game
    global state
    global check_square_list
    global checking_piece
    global piece

    checking_piece = ""
    valid_move = False
    check_square_list = []
    checked = isChecked()
    last_position = copy.deepcopy(piece)
    
    if checked:
        if checkForCheckmate(isBlockable(), isEscapable(), canCaptureChecker()):           
            state = 0
            printBoard()
            
            name = input("Enter your name: ")
            saveScore(name)

    if state != 0:
        printBoard()

        while not valid_move or checked:        #Keep Asking for moves until the move is valid
            player_input = playerInput()
            if player_input == "DRAW":          #Draw immediately exits to main menu
                state == 0
            
            if state == 0:                      #Exit to main menu
                break
            
            if player_input == "SAVE":          #Saving current game
                saveGame()
                print("Game Saved")
                continue

            target_piece = player_input[0]      #Checks if the move is valid
            target_square = player_input[1]
            valid_move = moveCheck(target_piece, target_square)

            if valid_move:                      #Checks if the attempted move doesn't lead into checks with the ally king
                updatePieces(target_piece, target_square)
                checked = isChecked()
                piece = copy.deepcopy(last_position)
                if checked:
                    print("Either your king is checked or your piece is pinned")
        
        if state != 0:                          #Update game if not going to Main Menu
            updatePieces(target_piece, target_square)
            if canPromotePawn():
                promotePawn()
            changeTurn()

def update():                   #Where all the code is organized
    global state
    
    #State Machine
    if state == 0:              #Main Menu
        state = mainMenu()     
    elif state == 1:            #Start New Game
        gameUpdate()
    elif state == 2:            #Load Last Game
        loadGame()
        state = 1
    elif state == 3:            #Load and Show players with most wins
        showScore()
        input("Press enter to continue")
        state = 0
    elif state == 4:
        clearScore()
        print("Scores successfully cleared")
        state = 0

def playerInput():
    global state                #Declare global for going back to the main menu
    
    piece_exists = False        
    square_exists = False

    while not piece_exists or not square_exists:        #Keep asking for inputs until both the target piece and the target square exist on the board
        if white_turn:
            print("White's Turn                                                                 Commands: MENU, DRAW, SAVE     (Move input example: 'Move: p4e4')")
        else:
            print("Black's Turn                                                                 Commands: MENU, DRAW, SAVE     (Move input example: 'Move: p4e4'")
        player_input = input("Move: ")          
        player_input = player_input.upper()

        if player_input == "MENU":                      #Return to Main Menu
            state = 0
            return

        if player_input == "SAVE":
            return "SAVE"

        if player_input == "DRAW":
            state = 0
            return "DRAW"
        if white_turn:                                  #Attaches a "w" or "b" character at the beginning of the string depending on whose turn
            player_input = "w" + player_input
        else:
            player_input = "b" + player_input

        #Identify if the piece to move exists
        target_piece = player_input[:3]                             #Identifies the piece to move using the first 3 letters of the string input as the name of the piece (ex. "wP5")
        piece_exists = pieceCheck(target_piece)                     #Identifies if the piece exists within the board

        #Identify if the target square exists within the board
        target_square = (player_input[3:5])                             #Identifies the target square using the last 2 characters of the string input (e. "e4")
        square_exists = squareCheck(target_square)                      #Identifies if the target square exists within the board using the letter-number coordinate pair

        if not piece_exists:
            print("The piece does not exist or is no longer in play")
        if not square_exists:
            print("The target square is out of bounds")

    target_square = squareCoordinateTranslate(target_square)    #Identifies target square to move using the last 2 letters of the string input as a letter-number coordinate pair of the square (ex. "e4")            
    return target_piece, target_square                 #Return the piece and target square
    
def getPieceCoordinate(target_piece):                  #Returns the coordinate of the piece on the board
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == target_piece:
                return j, i

def pieceCheck(target_piece):                          #Check if piece exists on the board
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == target_piece:
                return True
    return False

def squareCheck(square):                    #Check if square is within the board
    try:                                    #Prevents errors if user inputs random strings
        if square[0] != "A" and square[0] != "B" and square[0] != "C" and square[0] != "D" and square[0] != "E" and square[0] != "F" and square[0] != "G" and square[0] != "H":
            return False                                        
        if int(square[1]) < 1 or int(square[1]) > 8:
            return False
    except:
        return False
    return True

def squareCoordinateTranslate(square):      #Translates letter to number and returns a coordinate pair in string format
    if square[0] == "A":
        return "0" + square[1]
    elif square[0] == "B":
        return "1" + square[1]
    elif square[0] == "C":
        return "2" + square[1]
    elif square[0] == "D":
        return "3" + square[1]
    elif square[0] == "E":
        return "4" + square[1]
    elif square[0] == "F":
        return "5" + square[1]
    elif square[0] == "G":
        return "6" + square[1]
    elif square[0] == "H":
        return "7" + square[1]

def recordSquare(x, y, record):             #Records square in a list for king check purposes
    global check_square_list
    if record:
        check_square_list.append([x, y])

def moveCheck(target_piece, target_square):     #Checks if a move is valid
    global has_bR1_moved                        #Variables for Castling
    global has_bR2_moved
    global has_wR1_moved
    global has_wR2_moved
    global has_bK1_moved
    global has_wK1_moved
    global has_wK1_moved
    global has_bK1_moved
    
    if white_turn:
        turn_initial = "w"
    else:
        turn_initial = "b"
    
    #Get the coordinates of the target piece
    target_piece_coordinate = getPieceCoordinate(target_piece)
    target_piece_x = target_piece_coordinate[0]
    target_piece_y = target_piece_coordinate[1]

    #Get the coordinates of the target square
    target_square_x = int(target_square[0])
    target_square_y = int(target_square[1]) - 1
        
    #ROOK
    if target_piece[:2] == turn_initial + "R":      #Checks move for Rook
        valid_move = rookMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, turn_initial, False, False)
        if not valid_move:
            print("Invalid Move for Rook")
            return False
        else:                                       #Check flags for castling
            if target_piece == "wR1":
                has_wR1_moved = True
            if target_piece == "wR2":
                has_wR2_moved = True
            if target_piece == "bR1":
                has_bR1_moved = True
            if target_piece == "bR2":
                has_bR2_moved = True
            return True
        
    #KNIGHT            
    if target_piece[:2] == turn_initial + "N":      #Check move for Knight
        valid = knightMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, turn_initial, False)
        if not valid:
            print("Invalid Move for Knight")
            return False
        else:
            return True

    #BISHOP
    if target_piece[:2] == turn_initial + "B":      #Check move for Bishop
        valid = bishopMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, turn_initial, False, False)
        if not valid:
            print("Invalid Move for Bishop")
            return False
        else:
            return True

    #QUEEN                
    if target_piece[:2] == turn_initial + "Q":      #Check move for Queen
        valid = queenMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, turn_initial, False, False)
        if not valid:
            print("Invalid Move for Queen")
            return False
        else:
            return True    

    #KING
    if target_piece[:2] == turn_initial + "K":      #Check Move for King
        valid = kingMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, turn_initial, False)
        if not valid:
            print("Invalid Move for King")
            return False
        else:
            if white_turn:
                has_wK1_moved = True
            else:
                has_bK1_moved = True
            return True
    #Pawn                                           #Check Move for Pawn
    if target_piece[:2] == turn_initial + "P": 
        valid = pawnMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, turn_initial, False)
        if not valid:
            print("Invalid Move for Pawn")
            return False
        else:
            return True

def rookMoveCheck(position_x, position_y, target_x, target_y, turn_initial, checking_for_blocks, record):                               #ROOK ROOK 
    counter = 0                         #Counter for checking each square before reaching target square

    if piece[target_y][target_x][0] == turn_initial and piece[target_y][target_x][1:] != "K1":  #Checks for an ally piece obstructing at the target square. Useful for checks
        if not checking_for_blocks:                                                             #The target square is obstructed only if we are not checking for squares that can block the enemy king
            return False

    if abs(position_x - target_x) > 0 and abs(position_y - target_y) == 0:
        if position_x > target_x:
            while counter < abs(position_x-target_x)-1:                   #Check squares to the left   <------
                counter += 1
                recordSquare(position_x-counter, position_y, record)
                if piece[position_y][position_x-counter] != "   " and piece[position_y][position_x-counter][1:] != "K1": #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                    return False
        elif position_x < target_x:
            while counter < abs(target_x-position_x)-1:                   #Check squares to the right  ------->
                counter += 1
                recordSquare(position_x+counter, position_y, record)
                if piece[position_y][position_x+counter] != "   " and piece[position_y][position_x+counter][1:] != "K1": #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                    return False
    elif abs(position_x - target_x) == 0 and abs(position_y - target_y) > 0:
        if position_y > target_y:                                                                    
            while counter < abs(position_y-target_y)-1:                   #Check squares below       |||||
                counter += 1                                                                        #VVVVV
                recordSquare(position_x, position_y-counter, record)
                if piece[position_y-counter][position_x] != "   " and piece[position_y-counter][position_x][1:] != "K1": #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                    return False
        elif position_y < target_y:                                                                #^^^^^
            while counter < abs(target_y-position_y)-1:                   #Check squares above      |||||
                counter += 1
                recordSquare(position_x, position_y+counter, record)
                if piece[position_y+counter][position_x] != "   " and piece[position_y+counter][position_x][1:] != "K1": #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                    return False
    if abs(position_x - target_x) > 0 and abs(position_y - target_y) > 0:         #If moving diagonally
        return False

    return True

def knightMoveCheck(position_x, position_y, target_x, target_y, turn_initial, checking_for_blocks):                               #KNIGHT KNIGHT                                 
    y_move = abs(position_y - target_y)                  
    x_move = abs(position_x - target_x)

    if piece[target_y][target_x][0] == turn_initial and piece[target_y][target_x][1:] != "K1":  #Checks for an ally piece obstructing at the target square. Useful for checks
        if not checking_for_blocks:                                                             #The target square is obstructed only if we are not checking for squares that can block the enemy king
            return False

    if y_move < 1 or y_move > 2:                #Check if the target square is within 2 squares along the file
        return False
    if x_move < 1 or x_move > 2:                #Check if the target square is within 2 squares along the rank
        return False
    if y_move == x_move:                        #Check if the target square allows an L movement
        return False
        
    return True

def bishopMoveCheck(position_x, position_y, target_x, target_y, turn_initial, checking_for_blocks, record):                     #BISHOP BISHOP
    counter = 0                         #Counter for checking each square before reaching target square
    
    if piece[target_y][target_x][0] == turn_initial and piece[target_y][target_x][1:] != "K1" : #Checks for an ally piece obstructing at the target square. Useful for checks
        if not checking_for_blocks:                                                             #The target square is obstructed only if we are not checking for squares that can block the enemy king
            return False
    
    if abs(position_x-target_x) - abs(position_y-target_y) == 0:                #Check if the target square is found on the diagonal
        if position_x < target_x:     
            if position_y < target_y:
                while counter < abs(position_x-target_x)-1:                     #Check squares on upper right diagonal
                    counter += 1
                    recordSquare(position_x+counter, position_y+counter, record)
                    if piece[position_y+counter][position_x+counter] != "   " and piece[position_y+counter][position_x+counter][1:] != "K1":    #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
            if position_y > target_y:
                while counter < abs(position_x-target_x)-1:                     #Check squares on lower right diagonal
                    counter += 1
                    recordSquare(position_x+counter, position_y-counter, record)
                    if piece[position_y-counter][position_x+counter] != "   " and piece[position_y-counter][position_x+counter][1:] != "K1":    #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
        if position_x > target_x:
            if position_y < target_y:
                while counter < abs(position_x-target_x)-1:                     #Check squares on upper left diagonal
                    counter += 1
                    recordSquare(position_x-counter, position_y+counter, record)
                    if piece[position_y+counter][position_x-counter] != "   " and piece[position_y+counter][position_x-counter][1:] != "K1":    #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
            if position_y > target_y:
                while counter < abs(position_x-target_x)-1:                     #Check squares on lower left diagonal
                    counter += 1
                    recordSquare(position_x-counter, position_y-counter, record)
                    if piece[position_y-counter][position_x-counter] != "   " and piece[position_y-counter][position_x-counter][1:] != "K1":    #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
    else:
        return False
    
    return True
    
def queenMoveCheck(position_x, position_y, target_x, target_y, turn_initial, checking_for_blocks, record):                      #QUEEN QUEEN
    counter = 0
    
    if piece[target_y][target_x][0] == turn_initial and piece[target_y][target_x][1:] != "K1" : #Checks for an ally piece obstructing at the target square. Useful for checks
        if not checking_for_blocks:                                                             #The target square is obstructed only if we are not checking for squares that can block the enemy king
            return False    
    
    if abs(position_x-target_x) - abs(position_y-target_y) == 0:                #Check if the target square is found on the diagonal
        if position_x < target_x:     
            if position_y < target_y:
                while counter < abs(position_x-target_x)-1:                     #Check squares on upper right diagonal
                    counter += 1
                    recordSquare(position_x+counter, position_y+counter, record)
                    if piece[position_y+counter][position_x+counter] != "   " and piece[position_y+counter][position_x+counter][1:] != "K1":    #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
            if position_y > target_y:
                while counter < abs(position_x-target_x)-1:                     #Check squares on lower right diagonal
                    counter += 1
                    recordSquare(position_x+counter, position_y-counter, record)
                    if piece[position_y-counter][position_x+counter] != "   " and piece[position_y-counter][position_x+counter][1:] != "K1":    #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
        if position_x > target_x:
            if position_y < target_y:
                while counter < abs(position_x-target_x)-1:                     #Check squares on upper left diagonal
                    counter += 1
                    recordSquare(position_x-counter, position_y+counter, record)
                    if piece[position_y+counter][position_x-counter] != "   " and piece[position_y+counter][position_x-counter][1:] != "K1":    #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
            if position_y > target_y:
                while counter < abs(position_x-target_x)-1:                     #Check squares on lower left diagonal
                    counter += 1
                    recordSquare(position_x-counter, position_y-counter, record)
                    if piece[position_y-counter][position_x-counter] != "   " and piece[position_y-counter][position_x-counter][1:] != "K1":    #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
    else:
        if abs(position_x - target_x) > 0 and abs(position_y - target_y) == 0:
            if position_x > target_x:
                while counter < abs(position_x-target_x)-1:                   #Check squares to the left   <------
                    counter += 1
                    recordSquare(position_x-counter, position_y, record)
                    if piece[position_y][position_x-counter] != "   " and piece[position_y][position_x-counter][1:] != "K1": #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
            elif position_x < target_x:
                while counter < abs(target_x-position_x)-1:                   #Check squares to the right  ------->
                    counter += 1
                    recordSquare(position_x+counter, position_y, record)
                    if piece[position_y][position_x+counter] != "   " and piece[position_y][position_x+counter][1:] != "K1": #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
        elif abs(position_x - target_x) == 0 and abs(position_y - target_y) > 0:
            if position_y > target_y:                                                                    
                while counter < abs(position_y-target_y)-1:                   #Check squares below       |||||
                    counter += 1                                                                        #VVVVV
                    recordSquare(position_x, position_y-counter, record)
                    if piece[position_y-counter][position_x] != "   " and piece[position_y-counter][position_x][1:] != "K1": #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
            elif position_y < target_y:                                                                #^^^^^
                while counter < abs(target_y-position_y)-1:                   #Check squares above      |||||
                    counter += 1
                    recordSquare(position_x, position_y+counter, record)
                    if piece[position_y+counter][position_x] != "   " and piece[position_y+counter][position_x][1:] != "K1": #Checks for piece obstructions from ally and enemy pieces before reaching target square. Prevents movement if obstructed
                        return False
        elif abs(position_x - target_x) > 0 and abs(position_y - target_y) > 0:
            return False
        
    return True

def kingMoveCheck(position_x, position_y, target_x, target_y, turn_initial, checking_for_blocks):                       #KING KING
    global can_castle_white_short
    global can_castle_white_long
    global can_castle_black_short
    global can_castle_black_long
    
    if abs(position_x - target_x) > 1 or abs(position_y-target_y) > 1:      #If moving more than one square
        if abs(position_x - target_x) == 2:
            if white_turn:
                if position_x - target_x > 0:                   #Castle to the left White
                    if not has_wR1_moved and rookMoveCheck(0, 0, 3, 0, turn_intial, False, False):
                        can_castle_white_long = True
                        return True
                else:                                           #Castle to the right White
                    if not has_wR2_moved and rookMoveCheck(7, 0, 5, 0, turn_initial, False, False):                 
                        can_castle_white_short = True
                        return True
            else:
                if position_x - target_x > 0:                   #Castle to the left Black
                    if not has_bR1_moved and rookMoveCheck(0, 7, 3, 7, turn_initial, False, False):
                        can_castle_black_long = True
                        return True
                else:                                           #Castle to the right Black
                    if not has_bR2_moved and rookMoveCheck(7, 7, 5, 7, turn_initial, False, False):                 
                        canC_cstle_blackShort = True
                        return True
        return False
    if piece[target_y][target_x][0] == turn_initial:                                  #If encounter ally piece, invalid move
        if not checking_for_blocks:
            return False
    return True

def pawnMoveCheck(position_x, position_y, target_x, target_y, turn_initial, checking_for_blocks):                       #PAWN PAWN
    global ep_square
    global can_ep
    global ep_capture
    
    if abs(position_y-target_y) == 1 and abs(position_x-target_x) == 1:                         #Allows diagonal movement to capture opposing piece
        if piece[target_y][target_x][0] == turn_initial:                                        #Checks for an ally piece obstructing at the target square. Useful for checks
            if not checking_for_blocks:                                                         #The target square is obstructed only if we are not checking for squares that can block the enemy king
                return False
        if piece[target_y][target_x][0] != turn_initial:
            if piece[target_y][target_x][0] == " ":
                if target_x == ep_square[0] and target_y == ep_square[1] and can_ep:     #Enables capture if En Pasant
                    ep_capture = True
                    return True
            else:
                return True
        
    if piece[target_y][target_x] != "   ":                                      #Checks for any piece obstructing at the target square.
        return False    
    
    if turn_initial == "w":                                                     #Allows 2 squares on first move
        if position_y == 1 and target_y == 3 and position_x == target_x:
            if piece[target_y-1][target_x] != "   ":                            #Checks for any piece obstructing before target square.                                                        
                return False             
            ep_square = [position_x, 2]                                         #Prepare En Passant
            can_ep = True
            return True
    else:
        if position_y == 6 and target_y == 4 and position_x == target_x:
            if piece[target_y+1][target_x] != "   ":                            #Checks for any piece obstructing before the target square.                                                        
                return False 
            ep_square = [position_x, 5]
            can_ep = True
            return True
    
    if abs(position_y - target_y) > 1:                                          #Prevent pawn from moving more than one square
        return False

    if turn_initial == "w" and position_y > target_y:                           #Prevent pawn from moving in reverse
        return False
    elif turn_initial == "b" and position_y < target_y:
        return False
    
    if position_x-target_x != 0:                                                #Prevent pawn from moving horizontally
        return False
    
    return True

def updatePieces(target_piece, target_square):          #Updates pieces in the list
    global has_bR1_moved
    global has_bR2_moved
    global has_wR1_moved
    global has_wR2_moved
    global has_bK1_moved
    global has_wK1_moved

    global ep_square
    global en_capture
    global can_ep
    
    #Get Coordinates for the piece to move and target square
    coordinate = getPieceCoordinate(target_piece)
    position_x = coordinate[0]
    position_y = coordinate[1]
    target_x = int(target_square[0])
    target_y = int(target_square[1])-1
    
    piece[target_y][target_x] = target_piece    #Place piece on the target square
    piece[position_y][position_x] = fs          #Free space on previous square

    #Perform Castle
    if can_castle_white_short and not has_wR2_moved:    #White Castle Short
        piece[0][5] = "wR2"
        piece[0][7] = fs
        has_wR2_moved = True
        has_wK1_moved = True
    if can_castle_white_long and not has_wR1_moved:     #White Castle Long
        piece[0][3] = "wR1"
        piece[0][0] = fs
        haswR1Moved = True
        has_wK1_move = True
    if can_castle_black_short and not has_bR2_moved:    #Black Castle Short
        piece[7][5] = "bR2"
        piece[7][7] = fs
        has_bR2_moved = True
        has_bK1_moved = True
    if can_castle_black_long and not has_bR1_moved:     #Black Castle Long
        piece[7][3] = "bR1"
        piece[7][0] = fs
        has_bR1_moved = True
        has_bK1_moved = True

    if ep_capture:                              #If En Passant Capture
        if white_turn:
            piece[target_y - 1][target_x] = fs  #Remove capture pawn from the board
        else:
            piece[target_y + 1][target_x] = fs
                                                #Reset En Passant Components
        ep_square = []
        en_capture = False
        can_ep = False

def changeTurn():                               #Switches Turns
    global white_turn
    if white_turn:
        white_turn = False
    else:
        white_turn = True

def checkForCheckmate(blockable, escapable, can_capture):           #Checks for checkmate. Checks if the check is blockable, if the king can escape, or the checking piece can be capturesd
    global double_checked
    #print("Can Block: " + str(blockable))
    #print("Can Escape: " + str(escapable))
    #print("Can Capture: " + str(can_capture))
    
    if not blockable:
        if not double_checked:                      #If double Checked, only valid move is to move the king
            if can_capture:                         #If the piece can be captured but the king is still left checked
                if not escapable:
                    if white_turn:
                        print("Checkmate. Black Wins!")
                        return True
                    else:
                        print("Checkmate. White Wins!")
                        return True
            elif not escapable:                     
                if white_turn:
                    print("Checkmate. Black Wins!")
                    return True
                else:
                    print("Checkmate. White Wins!")
                    return True
        else:
            if not escapable:
                if white_turn:
                    print("Checkmate. Black Wins!")
                    return True
                else:
                    print("Checkmate. White Wins!")
                    return True
            double_checked = False
                
    return False

def isChecked():                                    #Checks for king checks
    global double_checked
    
    checking_pieces = 0
    
    if white_turn:
        coordinate = getPieceCoordinate("wK1")
        target_x = coordinate[0]
        target_y = coordinate[1]

        checking_pieces = eachPieceCheck(target_x, target_y, "b", False, True, False)
    else:
        coordinate = getPieceCoordinate("bK1")
        target_x = coordinate[0]
        target_y = coordinate[1]
        
        checking_pieces = eachPieceCheck(target_x, target_y, "w", False, True, False)

    if checking_pieces > 1:
        print("King is Checked!")
        double_checked = True
        return True
    elif checking_pieces == 1:
        print("King is Checked!")
        return True

    return False

def isBlockable():                                  #Checks if a check is blockable by ally piece
    checking_pieces = 0

    for coordinate in check_square_list:
        target_x = coordinate[0]
        target_y = coordinate[1]
        if white_turn:
            checking_pieces = eachPieceCheck(target_x, target_y, "w", False, False, False)
        else:
            checking_pieces = eachPieceCheck(target_x, target_y, "b", False, False, False)

    #print(checking_pieces)
    if checking_pieces >= 1:
        #print("Can be defended")
        return True

    return False

def isEscapable():                                  #Checks if a king can still escape
    checking_pieces = 0
    king_square_list = []
    available_squares = 0
    
    if white_turn:
        coordinate = getPieceCoordinate("wK1")
        target_x = coordinate[0]
        target_y = coordinate[1]
        turn_initial = "w"
    else:
        coordinate = getPieceCoordinate("bK1")
        target_x = coordinate[0]
        target_y = coordinate[1]
        turn_initial = "b"

    #Get available adjacent squares around the king 
    if target_x + 1 >= 0 and target_x + 1 <= 7 and target_y >= 0 and target_y <= 7:
        if kingMoveCheck(target_x, target_y, target_x + 1, target_y, turn_initial, False):
            king_square_list.append([target_x + 1, target_y])
            available_squares += 1
            
    if target_x + 1 >= 0 and target_x + 1 <= 7 and target_y + 1 >= 0 and target_y + 1 <= 7:
        if kingMoveCheck(target_x, target_y, target_x + 1, target_y + 1, turn_initial, False):
            king_square_list.append([target_x + 1, target_y + 1])
            available_squares += 1
            
    if target_x >= 0 and target_x <= 7 and target_y  + 1 >= 0 and target_y + 1 <= 7:
        if kingMoveCheck(target_x, target_y, target_x, target_y + 1, turn_initial, False):
            king_square_list.append([target_x, target_y + 1])
            available_squares += 1
            
    if target_x - 1 >= 0 and target_x - 1 <= 7 and target_y + 1 >= 0 and target_y + 1 <= 7:
        if kingMoveCheck(target_x, target_y, target_x - 1, target_y + 1, turn_initial, False):
            king_square_list.append([target_x - 1, target_y + 1])
            available_squares += 1
            
    if target_x - 1 >= 0 and target_x - 1 <= 7 and target_y >= 0 and target_y <= 7:
        if kingMoveCheck(target_x, target_y, target_x - 1, target_y, turn_initial, False):
            king_square_list.append([target_x - 1, target_y])
            available_squares += 1
            
    if target_x - 1 >= 0 and target_x - 1 <= 7 and target_y - 1 >= 0 and target_y - 1 <= 7:
        if kingMoveCheck(target_x, target_y, target_x - 1, target_y - 1, turn_initial, False):
            king_square_list.append([target_x - 1, target_y -1])
            available_squares += 1
            
    if target_x >= 0 and target_x <= 7 and target_y - 1 >= 0 and target_y - 1 <= 7:
        if kingMoveCheck(target_x, target_y, target_x, target_y - 1, turn_initial, False):
            king_square_list.append([target_x, target_y - 1])
            available_squares += 1
            
    if target_x + 1 >= 0 and target_x + 1 <= 7 and target_y - 1 >= 0 and target_y - 1 <= 7:
        if kingMoveCheck(target_x, target_y, target_x + 1, target_y - 1, turn_initial, False):
            king_square_list.append([target_x + 1, target_y - 1])
            available_squares += 1

    #Evaluate each square
    for coordinate in king_square_list:
        target_x = coordinate[0]
        target_y = coordinate[1]
        if white_turn:
            if eachPieceCheck(target_x, target_y, "b", True, False, False) > 0:
                available_squares -= 1
        else:
            if eachPieceCheck(target_x, target_y, "w", True, False, False) > 0:
                available_squares -= 1
    if available_squares < 1:               #If there are available squares that lead to checks
        return False
    elif king_square_list == []:            #If there exists no available square to move the king
        return False
    return True

def canCaptureChecker():                        #Checks if the checking piece can be captured
    checking_pieces = 0                         #Initialize the number of checking pieces

    coordinate = getPieceCoordinate(checking_piece) #Gets the coordinate of the checking piece
    target_x = coordinate[0]
    target_y = coordinate[1]

    if white_turn:                                  #Checks if ally piece can capture checking piece
        checking_pieces = eachPieceCheck(target_x, target_y, "w", False, False, True)
    else:
        checking_pieces = eachPieceCheck(target_x, target_y, "b", False, False, True)

    if checking_pieces >= 1:
        #print("Can capture piece!")
        return True

    return False    

def eachPieceCheck(target_x, target_y, target_initial, checking_for_blocks, record, allow_king):                         #Used for checking if a square is available to an enemy piece
    checking_pieces = 0
    if pieceCheck(target_initial + "R1"):
        if checkForChecks(target_initial + "R1", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "R2"):
        if checkForChecks(target_initial + "R2", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "R3"):
        if checkForChecks(target_initial + "R3", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "R4"):
        if checkForChecks(target_initial + "R4", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "N1"):
        if checkForChecks(target_initial + "N1", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "N2"):
        if checkForChecks(target_initial + "N2", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "N3"):
        if checkForChecks(target_initial + "N3", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "N4"):
        if checkForChecks(target_initial + "N4", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "B1"):
        if checkForChecks(target_initial + "B1", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "B2"):
        if checkForChecks(target_initial + "B2", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "B3"):
        if checkForChecks(target_initial + "B3", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "B4"):
        if checkForChecks(target_initial + "B4", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "Q1"):
        if checkForChecks(target_initial + "Q1", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "Q2"):
        if checkForChecks(target_initial + "Q2", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "Q3"):
        if checkForChecks(target_initial + "Q3", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "Q4"):
        if checkForChecks(target_initial + "Q4", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "K1"):
        if checkForChecks(target_initial + "K1", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "P1"):
        if checkForChecks(target_initial + "P1", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "P2"):
        if checkForChecks(target_initial + "P2", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "P3"):
        if checkForChecks(target_initial + "P3", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "P4"):
        if checkForChecks(target_initial + "P4", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "P5"):
        if checkForChecks(target_initial + "P5", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "P6"):
        if checkForChecks(target_initial + "P6", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "P7"):
        if checkForChecks(target_initial + "P7", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    if pieceCheck(target_initial + "P8"):
        if checkForChecks(target_initial + "P8", target_x, target_y, target_initial, checking_for_blocks, record, allow_king):
            checking_pieces += 1
    return checking_pieces

def checkForChecks(target_piece, target_square_x, target_square_y, target_initial, checking_for_blocks, record, allow_king):       #Checks if a square is available to the specified piece
    global checking_piece
    coordinate = getPieceCoordinate(target_piece)
    target_piece_x = coordinate[0]
    target_piece_y = coordinate[1]

    #print(target_piece_x, target_piece_y)
    
    if not (target_piece_x == target_square_x and target_piece_y == target_square_y):
        #ROOK
        if target_piece[:2] == target_initial + "R":        #Checks move for Rook
            if rookMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, target_initial, checking_for_blocks, record):
                checking_piece = target_piece
                return True
        #KNIGHT            
        if target_piece[:2] == target_initial + "N":        #Check move for Knight
            if knightMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, target_initial, checking_for_blocks):
                checking_piece = target_piece
                return True
        #BISHOP
        if target_piece[:2] == target_initial + "B":        #Check move for Bishop
            if bishopMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, target_initial, checking_for_blocks, record):
                checking_piece = target_piece
                return True
        #QUEEN                
        if target_piece[:2] == target_initial + "Q":        #Check move for Queen
            if queenMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, target_initial, checking_for_blocks, record):
                checking_piece = target_piece
                return True
        #KING
        if target_piece[:2] == target_initial + "K" and allow_king:        #Check Move for King
            if kingMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, target_initial, checking_for_blocks):
                checking_piece = target_piece
                return True        
        #Pawn                                               #Check Move for Pawn
        if target_piece[:2] == target_initial + "P": 
            if pawnMoveCheck(target_piece_x, target_piece_y, target_square_x, target_square_y, target_initial, checking_for_blocks):   
                checking_piece = target_piece
                return True
    return False
        
def canPromotePawn():                           #Checks for pawns to promote if a pawn is at the other end of the board
    global pawn_to_promote
    if white_turn:
        for i in range(8):
            if piece[7][i][1] == "P":
                pawn_to_promote = piece[7][i]
                return True
    else:
        for i in range(8):
            if piece[0][i][1] == "P":
                pawn_to_promote = piece[0][i]
                return True
    return False

def promotePawn():                              #Promotes the pawn
    global white_promotion_number
    global black_promotion_number
    
    coordinate = getPieceCoordinate(pawn_to_promote)
    target_x = coordinate[0]
    target_y = coordinate[1]
    promote_to_piece = input("(R = Rook, N = Knight, B = Bishop, Q = Queen)\nPromote Pawn to: ")
    if promote_to_piece.upper() == "R":         #Promote to Rook
        if white_turn:
            piece[target_y][target_x] = "wR" + str(white_promotion_number)
            white_promotion_number += 1
        else:
            piece[target_y][target_x] = "bR" + str(black_promotion_number)
            black_promotion_number += 1
    if promote_to_piece.upper() == "N":         #Promote to Knight
        if white_turn:
            piece[target_y][target_x] = "wN" + str(white_promotion_number)
            white_promotion_number += 1
        else:
            piece[target_y][target_x] = "bN" + str(black_promotion_number)
            black_promotion_number += 1
    if promote_to_piece.upper() == "B":         #Promote to Bishop
        if white_turn:
            piece[target_y][target_x] = "wB" + str(white_promotion_number)
            white_promotion_number += 1
        else:
            piece[target_y][target_x] = "bB" + str(black_promotion_number)
            black_promotion_number += 1
    if promote_to_piece.upper() == "Q":         #Promote to Queen
        if white_turn:
            piece[target_y][target_x] = "wQ" + str(white_promotion_number)
            white_promotion_number += 1
        else:
            piece[target_y][target_x] = "bQ" + str(black_promotion_number)
            black_promotion_number += 1    

def saveGame():                                 #Saves the current state of the game into a text file
    global piece
    global white_turn
    
    with open('last_game.txt', 'w+') as save_data:  #Saves piece positions, en passant square, if can en passant, and turn for that game.
        for list_item_y in piece:
            for list_item_x in list_item_y:
                if list_item_x == "   ":
                    save_data.write('%s\n' % "fs")
                else:
                    save_data.write('%s\n' % list_item_x)
        save_data.write('%s\n' % white_turn)
        if ep_square != []:
            save_data.write('%s\n' % str(ep_square[0]))
            save_data.write('%s\n' % str(ep_square[1]))
            save_data.write('%s\n' % can_ep)

def loadGame():                                 #Loads the last game saved
    global piece
    global white_turn
    global ep_square
    global can_ep
    piece = [[],[],[],[],[],[],[],[]]
    position_y = 0
    counter = 0
    with open('last_game.txt', 'r') as save_data:   
        for line in save_data:
            if counter > 7:
                counter = 0
                position_y += 1
                
            current_place = line[:-1]
            if position_y > 7:
                if counter == 0:
                    if current_place == "True":             #Updates whose turn
                        white_turn =  True
                    else:
                        white_turn = False
                if counter == 1:                            #Updates En Passant square
                    ep_square.append(int(current_place))
                if counter == 2:
                    ep_square.append(int(current_place))
                if counter == 3:                            #Checks if can en passant
                    if current_place == "True":
                        can_ep =  True
                    else:
                        can_ep = False
            elif current_place == "fs":                     #Updates Board
                piece[position_y].append("   ")
            else:
                piece[position_y].append(current_place)
            counter += 1

def saveScore(name):                            #Saves scores after every completed game
    loadScore()
    name_exists = False
    index = 0
    if score_list != [[]]:
        for score in score_list:
            print(score[0])
            if score[0] == name:
                name_exists = True
                break
            index += 1

    if name_exists:                             #Tallies score to name if the same name is inputed
        score_list[index][1] += 1
    else:
        score_list.append([name, 1])
    
    with open('scores.txt', 'w+') as save_data:
        for list_item_y in score_list:
            for list_item_x in list_item_y:
                save_data.write('%s\n' % list_item_x)

def loadScore():                                #Loads scores from saved text file
    global score_list
    score_list = [[]]
    counter = 0
    position_y = 0
    try:
        with open('scores.txt', 'r') as save_data:
            for line in save_data:
                if counter > 1:
                    counter = 0
                    position_y += 1
                    score_list.append([])

                if counter == 1:
                    current_place = line[:-1]
                    score_list[position_y].append(int(current_place))
                else:
                    current_place = line[:-1]
                    score_list[position_y].append(current_place)
                counter += 1
    except:                                     #Creates text file if no file exists
        with open('scores.txt', "w+"):
            print(end="")
        loadScore()
    
def showScore():                                #Shows the score on the terminal
    global score_list
    loadScore()

    if score_list != [[]]:                      #If there are saved scores
        for i in range(len(score_list)-1):
            flag = 0

            for j in range(len(score_list)-1):
                if score_list[j][1] < score_list[j + 1][1]:
                    temp = score_list[j]
                    score_list[j] = score_list[j + 1]
                    score_list[j + 1] = temp
                    flag = 1
                    
            if flag == 0:
                break

        counter = 1
        print("-----------------------------------")
        print("\n\nPlayers with the most Wins\n")
        for score in score_list:
            print("     " + str(counter), ". "+ score[0], "- " + str(score[1]) + " Wins" )
            counter += 1
        print("\n\n-----------------------------------")
    else:                                       #If no scores exist
        print("-----------------------------------")
        print("\n\nPlayers with the most Wins\n")
        print("No Scores Recorded" )
        print("\n\n-----------------------------------")

def clearScore():                               #Clears the scores
    with open('scores.txt', "w"):
        print(end="")
            
while True:
    update()                    #Runs the Game 
    
