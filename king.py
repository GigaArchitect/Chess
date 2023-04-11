pos_letters = ['a','b','c','d','e','f','g','h']
class king :
    def __init__(self,color,position) :
        self.color = str(color)
        self.position = position


    def move(self,current_pos):
        moves = []
        ch = current_pos[0]
        nm = int(current_pos[1])
        #Forward
        if nm + 1 > 8 :
            pass
        else :
            moves.append(f"{ch}{nm+1}")
        
        #Back
        if nm - 1 < 0 :
            pass
        else :
            moves.append(f"{ch}{nm-1}")

        #Right
        if pos_letters.index(ch)+1 > 7:
            pass
        else :
            moves.append(f"{pos_letters[pos_letters.index(ch)+1]}{nm}")
        
        #left
        if pos_letters.index(ch)-1 < 0 :
            pass
        else :
            moves. append(f"{pos_letters[pos_letters.index(ch)-1]}{nm}")
        
        #diag-left-forward
        if pos_letters.index(ch)-1 < 0 or nm +1 > 8 :
            pass
        else :
            moves.append(f"{pos_letters[pos_letters.index(ch)-1]}{nm+1}")

        #diag-right-forward
        if pos_letters.index(ch)+1 > 7 or nm + 1 > 8 :
            pass
        else :
            moves.append(f"{pos_letters[pos_letters.index(ch)+1]}{nm+1}")
        
        #diag-left-back
        if pos_letters.index(ch)-1 < 0 or nm -1 < 1 :
            pass
        else :
            moves.append(f"{pos_letters[pos_letters.index(ch)-1]}{nm-1}")
        
        #diag-right-back
        if pos_letters.index(ch)+1 > 7 or nm -1 < 1 :
            pass
        else :
            moves.append(f"{pos_letters[pos_letters.index(ch)+1]}{nm-1}")

        return moves

kk = king("black")
print(kk.move("e8"))

#valid king moves