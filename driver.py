#import pygame as pg
import stockfish as st 
from sys import exit
stc = st.Stockfish(path="/usr/bin/stockfish")
stc.update_engine_parameters({"Hash": 1024, "UCI_Chess960": "true"})
# elo_rat = int(input("Enter The ELO Rating You Find Yourself Comfortable With : "))
stc.set_elo_rating(1000)
stc.set_depth(15)

print(stc.get_board_visual())

# pg.init()
# screen = pg.display.set_mode((600,600))

# pg.display.set_caption("Chess")

# board_surface = pg.transform.scale(pg.image.load('./img/board.png'), (600,600))

# while True :
#     for event in pg.event.get():
#         if event.type == pg.QUIT :
#             pg.quit()
#             exit()
#     screen.blit(board_surface,(0,0))
#     pg.display.update()
#     pg.time.Clock().tick(60)

