# class draw :
matrix = [
        ['r','n','b','q','k','b','n','r'],
        ['p','p','p','p','p','p','p','p'],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['P','P','P','P','P','P','P','P'],
        ['R','N','B','Q','K','B','N','R']
    ]
pos_letters = ['a','b','c','d','e','f','g','h']
compelete_pos_map = {}
for i in range(8): #char
    for j in range(8): #number
        compelete_pos_map[f"{pos_letters[i]}{abs(j+1-9)}"] = matrix[j][i]
print(compelete_pos_map)