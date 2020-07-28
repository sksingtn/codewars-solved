from copy import deepcopy
addr=[[(i,j+x)for i in range(0,3) for j in range(0,3)] for x in range(0,9,3)]
s,d1,d2={1,2,3,4,5,6,7,8,9},{0:1,1:1,2:1,3:2,4:2,5:2,6:3,7:3,8:3},{1:(0,3),2:(3,6),3:(6,9)}
constant={1,2,3}
def sudoku_2(sud,row):
    check=[]
    for i in sud:
        check.extend(i)
    if len(set(check))==9 and all([i==j for i,j in zip(row,sud[0]) if i != 0]):
        for i in sud:
            print(i)
        return sud
    def rotate(matrix):
        ledge = []
        for i in matrix:
            ledge.extend(i)
        return [ledge[i::9] for i in range(8,-1,-1)]    
    for swap in range(0,3):
        for block in addr:            
            blank =[(i,j) for i,j in block if sud[i][j]==0]
            if len(blank) in range(1,4):
                for i,j in blank:                                        
                    full = {sud[i][j] for i,j in block if sud[i][j]!=0}                    
                    full = (full.union({x for x in sud[i] if x!=0})).union({sud[x][j] for x in range(0,9) if sud[x][j]!=0})
                    answer=s.difference(full)                    
                    if len(answer)==1:sud[i][j]=answer.pop()
        
        for num in range(1,10):
            count,pos,blank=0,set(),""
            for i in range(0,3):
                    if num in sud[i]:
                            count+=1
                            pos.add(d1[sud[i].index(num)])
                    else:blank=i
            if count==2:                    
                    found = False
                    pos=constant.difference(pos)
                    first,last=d2[pos.pop()]
                    backup = deepcopy(sud[blank])                   
                    for x in range(first,last):
                        if (backup[x]==0) and (found == False) and (num not in [sud[z][x] for z in range(0,9)]):
                            backup[x]=num
                            found = True
                        elif (backup[x]==0) and (found == True) and (num not in [sud[z][x] for z in range(0,9)]):
                            found = False
                            break
                    if found == True:
                        sud[blank]=backup                                                                        
        sud=sud[3:]+sud[0:3]    
    sud = rotate(sud)
    return sudoku_2(sud,row)
    
def sudoku(array):
    row = array[0]
    return sudoku_2(array,row)

puzzle = [[0,0,1,0,4,0,0,0,0],
          [6,0,3,8,0,0,7,0,5],
          [0,7,0,3,0,5,1,0,0],
          [5,4,6,0,0,0,0,0,3],
          [0,0,7,0,0,0,4,0,0],
          [2,0,0,0,0,0,5,7,6],
          [0,0,2,7,0,8,0,5,0],
          [7,0,5,0,0,6,3,0,1],
          [0,0,0,0,5,0,9,0,0]]
puzzle2 = [[0, 0, 5, 0, 0, 0, 8, 0, 0], [0, 2, 0, 8, 0, 9, 0, 7, 0], [3, 0, 0, 0, 4, 0, 0, 0, 1], [0, 3, 0, 2, 0, 6, 0, 1, 0], [0, 0, 2, 0, 0, 0, 5, 0, 0], [0, 7, 0, 5, 0, 4, 0, 6, 0], [2, 0, 0, 0, 6, 0, 0, 0, 4], [0, 8, 0, 4, 0, 2, 0, 9, 0], [0, 0, 7, 0, 0, 0, 2, 0, 0]]
sudoku(puzzle)
