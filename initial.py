from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook
import stockfish as st 
import pygame as pg
from sys import exit

stc = st.Stockfish(path="/usr/bin/stockfish")
stc.update_engine_parameters({"Hash": 1024, "UCI_Chess960": "true"})
# elo_rat = int(input("Enter The ELO Rating You Find Yourself Comfortable With : "))
stc.set_elo_rating(1000)
stc.set_depth(15)

compelete_pos_map = {}

pos_letters = ['a','b','c','d','e','f','g','h']

def print_board() :
    print("\n\n")
    for i in range(8):
        print(f"{abs(i-1-7)} ",end="   ") 
        for j in range(8):
            if compelete_pos_map[f"{pos_letters[j]}"][i] == None:
                print(" ", end=" ")
            else:
                print(compelete_pos_map[f"{pos_letters[j]}"][i], end=" ")
        print("\n", end=" ")
    print("\n", end="      ")
    for i in pos_letters:
        print(f"{i.upper()}",end=" ")

def change_pos(s, d):
    ch = d[0]
    num = abs(int(d[1])-1-7)

    cur_piece = compelete_pos_map[s[0]][abs(int(s[1])-1-7)]
    if cur_piece is not None:
        cur_piece.position = f"{ch}{d[1]}"
        compelete_pos_map[s[0]][abs(int(s[1])-1-7)] = None
        compelete_pos_map[ch][num] = cur_piece
        print_board()
    else:
        print("There is no piece at the starting position")

matrix = [
    [Rook("b", "a8"), Knight("b", "b8"), Bishop("b", "c8"), Queen("b", "d8"), King("b", "e8"), Bishop("b", "f8"), Knight("b", "g8"), Rook("b", "h8")],
    [Pawn("b", "a7"), Pawn("b", "b7"), Pawn("b", "c7"), Pawn("b", "d7"), Pawn("b", "e7"), Pawn("b", "f7"), Pawn("b", "g7"), Pawn("b", "h7")],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [Pawn("w", "a2"), Pawn("w", "b2"), Pawn("w", "c2"), Pawn("w", "d2"), Pawn("w", "e2"), Pawn("w", "f2"), Pawn("w", "g2"), Pawn("w", "h2")],
    [Rook("w", "a1"), Knight("w", "b1"), Bishop("w", "c1"), Queen("w", "d1"), King("w", "e1"), Bishop("w", "f1"), Knight("w", "g1"), Rook("w", "h1")]
]

for i in range(8): #char
    compelete_pos_map[f"{pos_letters[i]}"] = []
    for j in range(8): #number
        compelete_pos_map[f"{pos_letters[i]}"].append(matrix[j][i])

print_board()

pg.init()
screen = pg.display.set_mode((700,700))
pg.display.set_caption("Chess")
board_surface = pg.image.load('./img/board.png')
clock = pg.time.Clock()
board_surface = pg.transform.scale(board_surface,(600,600))

letters = pg.transform.scale(pg.image.load('./img/text.png'),(600,60))
numbers = pg.transform.scale(pg.image.load('./img/numbers.png'),(35,600))

turn = "white"
while True :
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
    screen.blit(board_surface,(0,0))
    screen.blit(letters, (0,600))
    screen.blit(numbers, (600,0))
    x = 0
    
    for i in range(8):
            y = 0
            for j in range(8):
                ll = (y,x)
                scale  = (70,70)
                if compelete_pos_map[f"{pos_letters[j]}"][i] == None:
                    screen.blit(pg.transform.scale(pg.image.load('./img/transparent.png'),scale),ll)
                elif isinstance(compelete_pos_map[f"{pos_letters[j]}"][i],King):
                    if compelete_pos_map[f"{pos_letters[j]}"][i].color == "b":
                        screen.blit(pg.transform.scale(pg.image.load('./img/black_king.png'),scale),ll)
                    else :
                        screen.blit(pg.transform.scale(pg.image.load('./img/white_king.png'),scale),ll)
                elif isinstance(compelete_pos_map[f"{pos_letters[j]}"][i],Bishop):
                    if compelete_pos_map[f"{pos_letters[j]}"][i].color == "b":
                        screen.blit(pg.transform.scale(pg.image.load('./img/black_bishop.png'),scale),ll)
                    else :
                        screen.blit(pg.transform.scale(pg.image.load('./img/white_bishop.png'),scale),ll)
                elif isinstance(compelete_pos_map[f"{pos_letters[j]}"][i],Pawn):
                    if compelete_pos_map[f"{pos_letters[j]}"][i].color == "b":
                        screen.blit(pg.transform.scale(pg.image.load('./img/black_pawn.png'),scale),ll)
                    else :
                        screen.blit(pg.transform.scale(pg.image.load('./img/white_pawn.png'),scale),ll)
                elif isinstance(compelete_pos_map[f"{pos_letters[j]}"][i],Queen):
                    if compelete_pos_map[f"{pos_letters[j]}"][i].color == "b":
                        screen.blit(pg.transform.scale(pg.image.load('./img/black_queen.png'),scale),ll)
                    else :
                        screen.blit(pg.transform.scale(pg.image.load('./img/white_queen.png'),scale),ll)
                elif isinstance(compelete_pos_map[f"{pos_letters[j]}"][i],Knight):
                    if compelete_pos_map[f"{pos_letters[j]}"][i].color == "b":
                        screen.blit(pg.transform.scale(pg.image.load('./img/black_knight.png'),scale),ll)
                    else :
                        screen.blit(pg.transform.scale(pg.image.load('./img/white_knight.png'),scale),ll)
                elif isinstance(compelete_pos_map[f"{pos_letters[j]}"][i],Rook):
                    if compelete_pos_map[f"{pos_letters[j]}"][i].color == "b":
                        screen.blit(pg.transform.scale(pg.image.load('./img/black_rook.png'),scale),ll)
                    else :
                        screen.blit(pg.transform.scale(pg.image.load('./img/white_rook.png'),scale),ll)
                y += 75
            x += 75
    pg.display.update()
    clock.tick(60)

    if turn == "white":
        cur = input("Enter Your position Before change 2chars like -- >[d2] : ")
        sug_pei = compelete_pos_map[cur[0]][abs(int(cur[1])-1-7)]
        valid = []
        for i in sug_pei.move(sug_pei.position):
            if stc.is_move_correct(f"{cur}{i}"):
                valid.append(i)
            else :
                continue
        print(valid)
        dis = input("Enter Distenation : ")

        if not stc.is_move_correct(f"{cur}{dis}") :
            print("not a valid move")
            continue
        # Found in the middle of the Documentation :
        #In Chess960 mode of stockfish Castling is made by making king goto rook position
        #check for castle move
        if f"{cur}{dis}" == "e1h1":
            compelete_pos_map["h"][abs(int(1)-1-7)] = None
            compelete_pos_map["f"][abs(int(1)-1-7)] = Rook("w","f1")
            

        en_passant_flag = stc.will_move_be_a_capture(f"{cur}{dis}") 
        if en_passant_flag == "EN_PASSANT":
            compelete_pos_map[f"{dis[0]}"][abs(int(dis[1])-1-7)-1] = None
        
        stc.make_moves_from_current_position([f"{cur}{dis}"])

        if f"{cur}{dis}" == "e1h1":
            change_pos(cur,"g1")
            turn="black"
            continue

        change_pos(cur,dis)
        turn = "black"
        
    else :
        mv = stc.get_best_move_time(1000)
        en_passant_flag = stc.will_move_be_a_capture(f"{mv[0:2]}{mv[2:]}")
        if en_passant_flag == "EN_PASSANT":
            compelete_pos_map[f"{mv[2]}"][abs(int(mv[3])-1-7)+1] = None
        stc.make_moves_from_current_position([mv])
        change_pos(mv[0:2],mv[2:])
        turn = "white"
        
        #current porblems are (screen tearing, screan goes black when overlayed)
        