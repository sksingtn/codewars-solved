from copy import deepcopy
def find_word(board, word):
    def find(row,col):
        visited = set()
        visited.add((row,col))
        head = [[row,col]]        
        for num,w in enumerate(word[1:]):
            update = []
            for i,j in head:               
                for x,y in [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]:
                    if x in range(0,len(board)) and y in range(0,len(board[0])) and (x,y) not in visited and board[x][y] == w:
                        if num != len(word)-2 and word[num+1]==word[num+2]:update.append([x,y])                            
                        else:update.append([x,y]);visited.add((x,y))                                                               
            if update == []:return False
            else:head = deepcopy(update)                
        return True
    
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == word[0]:
                if find(i,j) == True:return True
    return False
