def path_finder(matrix):   
    matrix = [list(x) for x in matrix.split("\n")]
    h,w,visited = len(matrix),len(matrix[0]),{}
    Pqueue = {(0,0):[0,(0,0)]} 
    f = lambda x:Pqueue[x][0]
    while Pqueue and (h-1,h-1) not in visited:
        pop = min(Pqueue,key=f)
        (x,y),(d,prev) = pop,Pqueue.pop(pop)
        for row,col in ((x-1,y),(x,y-1),(x,y+1),(x+1,y)):
            if  ((row,col) not in visited) and ((row>=0 and row<h)) and ((col>=0 and col<w)) and (matrix[row][col] != "W") and ((row,col) not in Pqueue.keys()):
                Pqueue[(row,col)] = [d+1,(x,y)]       
        visited[(x,y)] = (prev)
    count = 0
    if (h-1,h-1) in visited:
        path = visited[(h-1,h-1)]
        while path != (0,0):
            count +=1
            path = visited[path]
        return count+1
    return False
