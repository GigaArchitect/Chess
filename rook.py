pos_letters = ['a','b','c','d','e','f','g','h']
class rook :
    def __init__(self,color) :
        self.color = str(color)
        self.moved = 1


    def move(self,current_pos):
        moves = []
        ch = current_pos[0]
        nm = int(current_pos[1])
        if self.moved == 0 :
            print(f"king will be {pos_letters[pos_letters.index(ch)-1]}{nm}")
            print("rook will be kingchar+1")
            self.moved = 1
            
        else :
            #Forward
            for i in range(9):
                moves.append(f"{pos_letters[pos_letters.index(ch)]}{nm+i}")
            #Back
            for i in range(9):
                moves.append(f"{pos_letters[pos_letters.index(ch)]}{nm-i}")
            #Right
            for i in range(9):
                if pos_letters.index(ch)+i > 7 :
                    break
                moves.append(f"{pos_letters[pos_letters.index(ch)+i]}{nm}")
            #left
            for i in range(9):
                if pos_letters.index(ch)+i < 0 :
                    break
                moves.append(f"{pos_letters[pos_letters.index(ch)-i]}{nm}")

        return moves

kk = rook("black")
print(kk.move("h1"))
