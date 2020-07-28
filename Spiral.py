def spiralize(n):
    if n == 1:
        return [[1]]
    elif n==2:
        return [[1,1],[0,1]]
    spiral = [[0 for i in range(n)] for j in range(n)]
    for i in range(len(spiral)):
        spiral[i].insert(0,"a")
        spiral[i].append("a")
    spiral.insert(0,["a" for i in range(n+2)])
    spiral.append(["a" for i in range(n+2)])
    current_row = 1
    current_col = 1
    while True:
        b = False
        while current_col<n+1 and spiral[current_row][current_col+1] != 1 and spiral[current_row+1][current_col+1] !=1 and spiral[current_row-1][current_col+1] !=1:            
            b = True
            spiral[current_row][current_col] = 1
            current_col += 1        
        if b == True:
            current_col -= 1
            current_row += 1
            b = False
        else:
            break
        while current_row<n+1 and spiral[current_row+1][current_col] != 1 and spiral[current_row+1][current_col+1] != 1 and spiral[current_row+1][current_col-1] != 1:            
            b = True
            spiral[current_row][current_col] = 1
            current_row += 1
        if b == True:
            current_row -= 1
            current_col -= 1
            b = False
        else:
            break
        while current_col>0 and spiral[current_row][current_col-1] != 1 and spiral[current_row+1][current_col-1] != 1 and spiral[current_row-1][current_col-1] != 1:            
            b = True
            spiral[current_row][current_col] = 1
            current_col -= 1
        if b==True:    
            current_col += 1
            current_row -= 1
            b = False
        else:
            break
        while current_row>0 and spiral[current_row-1][current_col] != 1 and spiral[current_row-1][current_col+1] != 1 and spiral[current_row-1][current_col-1] != 1:
            
            b = True
            spiral[current_row][current_col] = 1
            current_row -= 1
        if b== True:    
            current_row += 1
            current_col += 1
            b = False
        else:
            break
    spiral.pop()
    spiral.pop(0)
    for i in range(len(spiral)):
        spiral[i].pop()
        spiral[i].pop(0)
    return spiral    
   

