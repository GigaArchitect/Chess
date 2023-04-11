pos_letters = ['a','b','c','d','e','f','g','h']
class pawn :
    def __init__(self,color,position) :
        self.color = str(color).lower()
        self.position = position
        self.moved = 0


    def move(self,current_pos):
        moves = []
        ch = current_pos[0]
        nm = int(current_pos[1])
        if self.moved == 0 :
            self.moved = 1
            if self.color == "w" :
                moves.append([f"{pos_letters[pos_letters.index(ch)]}{nm+1}",f"{pos_letters[pos_letters.index(ch)]}{nm+2}"])
            elif self.color == "b" : 
                moves.append([f"{pos_letters[pos_letters.index(ch)]}{nm-1}",f"{pos_letters[pos_letters.index(ch)]}{nm-2}"])
        else :
            if self.color == "w" :
                moves.append([f"{pos_letters[pos_letters.index(ch)]}{nm+1}"])
            elif self.color == "b" :
                moves.append([f"{pos_letters[pos_letters.index(ch)]}{nm-1}"])
            


        return moves

