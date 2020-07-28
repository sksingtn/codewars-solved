from collections import Counter
def validate_battlefield(field):
    ships = [(i,j) for i in range(10) for j in range(10) if field[i][j] == 1]
    r = range(0,10)
    store = set()
    for row,col in ships:
        for i,j in [[row-1,col-1],[row-1,col+1],[row+1,col-1],[row+1,col+1]]:
            if i in r and j in r and field[i][j] == 1:
                return False
        horizontal,vertical = False,False
        left_row,left_col = row,col
        right_row,right_col=row,col
        current = set()
        while (left_col-1 in r and field[left_row][left_col-1]==1)or(right_col+1 in r and field[right_row][right_col+1]==1):
            horizontal = True
            if left_col-1 in r and field[left_row][left_col-1]==1:
                current.add((left_row,left_col-1))
                left_col -= 1
            if right_col+1 in r and field[right_row][right_col+1]==1:
                current.add((right_row,right_col+1))
                right_col += 1
        if horizontal == True:
            current.add((row,col))

        up_row,up_col = row,col
        down_row,down_col = row,col
        while (up_row-1 in r and field[up_row-1][up_col]==1) or (down_row+1 in r and field[down_row+1][down_col]==1):
            if horizontal == True:
                return False
            vertical = True
            if (up_row-1 in r and field[up_row-1][up_col]==1):
                current.add((up_row-1,up_col))
                up_row -= 1
            if (down_row+1 in r and field[down_row+1][down_col]==1):
                current.add((down_row+1,down_col))
                down_row += 1
        if vertical == True:
            current.add((row,col))
        if horizontal == False and vertical == False:
            current.add((row,col))            
        if set(sorted(current)) not in store:
            store.add(tuple(i for i in current)) 
    return Counter(map(lambda x:len(x),store)) == {1: 4, 2: 3, 3: 2, 4: 1}
