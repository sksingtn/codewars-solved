from collections import deque
from copy import deepcopy
def break_pieces(test):
    matrix = [list(x) for x in test.split("\n")]    
    blank = [(i,j) for i in range(0,len(matrix)) for j in range(0,len(matrix[i])) if matrix[i][j] == " "]
    count,outside=0,set()
    while blank:
        count+=1
        queue = deque()
        queue.append(blank.pop())
        while queue:
            i,j = queue.pop()
            for x,y in [[i,j],[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]:
                if x in range(0,len(matrix)) and y in range(0,len(matrix[1])) and matrix[x][y]== " ":
                    matrix[x][y]=count
                    queue.append((x,y))
                    if (x,y) in blank:
                        blank.remove((x,y))
                elif  x not in range(0,len(matrix)) or y not in range(0,len(matrix[1])):
                    outside.add(count)                 
    shapes = set(range(1,count+1)).difference(outside)
    if count == 1:return [test]
    final = []
    for shape in shapes:
        start,end =0,0 
        for num,row in enumerate(matrix):
            if shape in row and start == 0:start = num
            elif shape not in row and start != 0:end=num;break
        clean_shape = deepcopy(matrix[start-1:end+1])
        for x in range(0,len(clean_shape)):
            for y in range(0,len(clean_shape[x])):
                if type(clean_shape[x][y])==int and clean_shape[x][y] != shape:
                    clean_shape[x][y] = 0
                elif clean_shape[x][y] in ("-","|"):
                    if not any([clean_shape[row][col]==shape for row,col in [[x-1,y],[x,y-1],[x,y+1],[x+1,y]] if row in range(0,len(clean_shape)) and col in range(0,len(clean_shape[0]))]):
                        clean_shape[x][y] = 0
                elif clean_shape[x][y] == "+":
                    c=[clean_shape[row][col]==shape for row,col in [[x-1,y-1],[x+1,y+1],[x-1,y+1],[x+1,y-1]] if row in range(0,len(clean_shape)) and col in range(0,len(clean_shape[0]))].count(True)
                    if c>1 and c!=3:clean_shape[x][y]="-"
                    elif c==0:clean_shape[x][y]=0
                    
        final_shape = "\n".join(x.rstrip() for x in ["".join(str(i) for i in x).replace("0","").replace(str(shape)," ") for x in clean_shape])
        check = [len(x) for x in final_shape.split("\n")]
        if min(check) != max(check) and check[0]<check[-1]:
            final_shape = "\n".join(x[3:] if x[:2] == "  " else x for x in ["".join(str(i) for i in x).replace("0"," ").replace(str(shape)," ") for x in clean_shape])            
        final.append(final_shape)  
    return final
