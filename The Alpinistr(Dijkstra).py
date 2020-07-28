#Dijksktra Shortest path!
def path_finder(matrix):
    matrix = [[int(i)for i in x] for x in matrix.split("\n")]
    h,w,visited,total = len(matrix),len(matrix[0]),{},0
    Pqueue = {(0,0):[matrix[0][0],(0,0)]}
    f = lambda x:Pqueue[x][0]
    while Pqueue and (h-1,h-1) not in visited:
        pop = min(Pqueue,key=f)
        (x,y),(d,prev) = pop,Pqueue.pop(pop)
        for row,col in ((x-1,y),(x,y-1),(x,y+1),(x+1,y)):
            if  ((row,col) not in visited) and ((row>=0 and row<h)) and ((col>=0 and col<w)):                
                if (row,col) not in Pqueue.keys() or ((row,col) in Pqueue.keys() and Pqueue[(row,col)][0]>d+abs(matrix[x][y]-matrix[row][col])):
                    Pqueue[(row,col)] = [d+abs(matrix[x][y]-matrix[row][col]),(x,y)]        
        visited[(x,y)] = (prev)
    journey = []
    path = visited[(h-1,h-1)]
    while path != (0,0):
        journey.append(path)
        path = visited[path]
    journey = [(h-1,h-1)]+journey+[(0,0)]
    for i in range(0,len(journey)-1):
        total+= abs(matrix[journey[i][0]][journey[i][1]]-matrix[journey[i+1][0]][journey[i+1][1]])
    return total
