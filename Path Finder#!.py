from itertools import chain
def path_finder(maze):    
    maze = [list(i) for i in maze.split("\n")]    
    if "W" not in [i for i in chain((k[0] for k in maze[1:]),(j for j in maze[-1][-2::-1]))]:
        return True
    if "W" not in [i for i in chain((k[-1] for k in maze[-2::-1]),(j for j in maze[0][1:]))]:
        return True        
    def main(i,j,matrix):
        address = [[i,j]]

        def surround(row,col,board,exception):
            total = []
            for k,l in [[row-1,col-1],[row-1,col],[row-1,col+1],[row,col-1],[row,col+1],[row+1,col-1],[row+1,col],[row+1,col+1]]:
                if k in range(0,len(board)) and l in range(0,len(board[0])) and board[k][l] == "W" and [k,l] not in exception:
                    total.append([k,l])
            return total        
                    
        for k,l in address:
            address.extend(surround(k,l,matrix,address))
        return address

    for i in range(1,len(maze)):
        if maze[i][0] == "W":
            for k,l in main(i,0,maze):
                if [k,l] in [m for m in chain(([0,i] for i in range(1,len(maze[0]))),([j,len(maze[0])-1]for j in range(1,len(maze)-1)))]:
                    return False

    for i in range(1,len(maze[0])-1):
        if maze[len(maze)-1][i] == "W":
            for k,l in main(len(maze)-1,i,maze):
                if [k,l] in [m for m in chain(([0,i] for i in range(1,len(maze[0]))),([j,len(maze[0])-1]for j in range(1,len(maze)-1)))]:
                    return False
    return True
