pos_letters = ['a','b','c','d','e','f','g','h']
class king :
    def __init__(self,color) :
        self.color = str(color)


    def move(self,current_pos):
        moves = []
        ch = current_pos[0]
        nm = int(current_pos[1])
        #Forward
        moves.append(f"{ch}{nm+1}")
        #Back
        moves.append(f"{ch}{nm-1}")
        #Right
        moves.append(f"{pos_letters[pos_letters.index(ch)+1]}{nm}")
        #left
        moves.append(f"{pos_letters[pos_letters.index(ch)-1]}{nm}")
        #diag-left-forward
        moves.append(f"{pos_letters[pos_letters.index(ch)-1]}{nm+1}")
        #diag-right-forward
        moves.append(f"{pos_letters[pos_letters.index(ch)+1]}{nm+1}")
        #diag-left-back
        moves.append(f"{pos_letters[pos_letters.index(ch)-1]}{nm-1}")
        #diag-right-back
        moves.append(f"{pos_letters[pos_letters.index(ch)+1]}{nm-1}")

        return moves

kk = king("black")
print(kk.move("e8"))
