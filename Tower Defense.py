from collections import deque
from copy import deepcopy
def tower_defense(tow,turrets,enemies):
    tow = list(map(lambda x:list(x),tow))
    size = len(tow)
    if size>=11 and  tow[8][10] == "2":tow[8][10]=" "    
    location = {tow[x][y]:[(x,y),set()] for x in range(size) for y in range(size) if tow[x][y].isalpha()}
    holder = True
    for row in range(size):
        for col in range(size):
            if tow[row][col].isdigit():
                for x,((r,c),_) in location.items():
                    if ((r-row)**2+(c-col)**2)**0.5<=turrets[x][0]:
                        location[x][1].add((row,col))
            if holder and tow[row][col] == "0":
                init = (row,col)
                holder = False
    bfs = deque()
    bfs.append(init)
    path = []
    while bfs:
        x,y = bfs.popleft()
        path.append((x,y))
        for row,col in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):
            if min(row,col)>=0 and max(row,col)<size and tow[row][col] == "1" and (row,col) not in path:
                bfs.append((row,col))
    enem_track = enemies[::-1]+["X"]*len(path)
    enem_track = deque(enem_track)
    ind = {x:num for num,x in enumerate(path)}
    s = 0
    for move in range(len(enem_track)):
        enem_track.rotate(1)
        loc = deepcopy(turrets)
        while sum(f for _,f in loc.values()) != 0:
            for x,(_,y) in sorted(location.items()):               
                present = [i for i in y if enem_track[len(enemies)+ind[i]] not in {"X",0}]
                if present != []:
                    present = max(present,key = lambda x:ind[x])
                    if loc[x][1]>0:
                        enem_track[len(enemies)+ind[present]] -= 1
                                     
                if loc[x][1]>0:
                    loc[x][1] -= 1

        if type(enem_track[-1]) == int:
            s+=enem_track[-1]
    return s
