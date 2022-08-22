import re
def who_is_winner(pieces_position_list):
    board = [["0"]*7 for _ in range(6)]
    red_pat = r'R{4}'
    yel_pat = r'Y{4}'
    
    def create_pattern(board):
        pattern = []
        straight = [item for row in board for item in row]
        pattern.extend(["".join(x) for x in board]+["".join([board[col][row] for col in range(6)]) for row in range(7)])    
        for initial,step,size in ((0,8,6),(1,8,6),(2,8,5),(3,8,4),(-3,-8,5),(-4,-8,4),(3,6,4),(4,6,5),(5,6,6),(6,6,6),(-4,-6,4),(-5,-6,5)):
            pattern.append("".join(straight[initial::step][:size]))
        return "|".join(pattern)

    info = {"A":(0,5),"B":(1,5),"C":(2,5),"D":(3,5),"E":(4,5),"F":(5,5),"G":(6,5)}
    for num,pieces in enumerate(pieces_position_list,1):
        col,team = pieces[:3].split("_")
        x,y = info[col]
        info[col] = (x,y-1)
        board[y][x] = team
        if num>7:
            current = create_pattern(board)
            if re.search(red_pat,current):
                return 'Red'
            elif re.search(yel_pat,current):
                return 'Yellow'
        
        
    return 'Draw'
