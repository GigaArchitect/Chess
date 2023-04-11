# class draw :
matrix = [
        ['BR','BK','BB','BQ','BK','BB','BK','BR'],
        ['BP','BP','BP','BP','BP','BP','BP','BP'],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['WP','WP','WP','WP','WP','WP','WP','WP'],
        ['WR','WK','WB','WQ','WK','WB','WK','WR']
    ]
pos_letters = ['a','b','c','d','e','f','g','h']
compelete_pos_map = {}
for i in range(8): #char
    for j in range(8): #number
        compelete_pos_map[f"{pos_letters[i]}{j}"] = matrix[j][i]
