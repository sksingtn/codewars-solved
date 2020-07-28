def validSolution(board):
    if [j for i in board for j in i].count(0):
        return False
    for i in board:
        if len(i) != len(set(i)):
            return False
    for i in range(0,9): 
        if len(set([board[k][i] for k in range(0,9)])) != 9:
            return False  
            
    for k ,l in [[1,1],[1,4],[1,7],[4,1],[4,4],[4,7],[7,1],[7,4],[7,7]]:
        if len(set([board[k-1][l-1],board[k-1][l],board[k-1][l+1],board[k][l-1],board[k][l],board[k][l+1],board[k+1][l-1],board[k+1][l],board[k+1][l+1]])) != 9:
            return False
    return True    
