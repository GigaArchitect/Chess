pos_letters = ['a','b','c','d','e','f','g','h']
class knight :
    def __init__(self,color) :
        self.color = str(color)

    def move(self,current_pos):
        moves = []
        ch = current_pos[0]
        nm = int(current_pos[1])
        #Right
        moves.append(f"{pos_letters[pos_letters.index(ch)+2]}{nm+1}")
        moves.append(f"{pos_letters[pos_letters.index(ch)+2]}{nm-1}")
        #left
        moves.append(f"{pos_letters[pos_letters.index(ch)-2]}{nm+1}")
        moves.append(f"{pos_letters[pos_letters.index(ch)-2]}{nm-1}")
        #diag-left-forward
        moves.append(f"{pos_letters[pos_letters.index(ch)+1]}{nm+2}")
        moves.append(f"{pos_letters[pos_letters.index(ch)-1]}{nm+2}")
        #diag-right-forward
        moves.append(f"{pos_letters[pos_letters.index(ch)+1]}{nm-2}")
        moves.append(f"{pos_letters[pos_letters.index(ch)-1]}{nm-2}")

        return moves

kk = knight("black")
print(kk.move('b1'))