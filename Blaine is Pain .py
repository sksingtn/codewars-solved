from collections import namedtuple,deque

def train_crash(track, a_train, a_train_pos, b_train, b_train_pos, limit):
    mapping = {'-': {(0, -1): ['-', '\\', '/','+','S'], (0, 1): ['-', '\\', '/','+','S']}, '|': {(-1, 0): ['|', '\\', '/','+','S'], (1, 0): ['|', '\\', '/','+','S']},
            '/': {(0, 1): ['-'],(-1, 0): ['|','+','S'], (-1, 1): ['/','X'], (0, -1): ['-'], (1, -1): ['/','X','S'], (1, 0): ['|','+','S']},
           '\\': {(-1, -1): ['\\','X'], (-1, 0): ['|','+','S'], (0, -1): ['-'], (0, 1): ['-'], (1, 0): ['|','+','S'], (1, 1): ['\\','X','S']}}
    
    crossing = {'+': {'|': '|', '-': '-', '/': '|', '\\': '|'}, 'X': {'\\': '\\', '/': '/'}, 'S': {'|': '|', '-': '-','\\': '\\', '/': '/'}}
    pieces,start = namedtuple("piece",["type","position"]),track.find("/")
    grid = [list(pieces(type=piece,position=(x,y)) if piece != ' ' else piece for y,piece in enumerate(row)) for x,row in enumerate(track.split("\n"))]

    def getNext(current,tra,lo):
        x,y = current.position
        symbol = current.type
        #Converting Stations into fundamental pieces
        if symbol in crossing:
            symbol = crossing[symbol][lo[-2].type]

        for (newx,newy),possible in mapping[symbol].items():
            try:
                if min([x+newx,y+newy]) < 0:
                    raise IndexError
                nextItem = grid[x+newx][y+newy]
            except IndexError:
                continue
            
            if isinstance(nextItem,pieces) and nextItem.type in possible and (x+newx,y+newy) not in tra:
                return nextItem
                
    loop = [grid[0][start]]
    traversed = deque(maxlen=2)
    
    #Untangling the track and making it a continous loop
    while True:
        current = loop[-1]        
        traversed.append(current.position)
        res = getNext(current,traversed,loop)
        if res.position == (0,start):
            break        
        loop.append(res)

    t1name,t1len,t1pos,t1stop = a_train[0],len(a_train)-1,a_train_pos,None
    t2name,t2len,t2pos,t2stop = b_train[0],len(b_train)-1,b_train_pos,None    
    def cross_station(name,pos,stop,length,time,clock_wise = False):
        if loop[pos].type == 'S' and stop is None and name.lower() != 'x' and time != 0:
            stop = length
        if stop == 0:
            stop = None
        if stop is None:
            if clock_wise:
                pos += 1
            else:
                pos += -1
        else:
            stop -= 1
        return (pos,stop)
        
    def locate(pos,trainlength,left=True):
        if not left:
            pos = (pos - trainlength) % len(loop)
        train = loop[pos:pos+trainlength+1]
        extra = pos + trainlength - len(loop) + 1    
        return loop[pos:pos+trainlength+1] + ((extra > 0 and loop[:extra]) or [])

    conv = lambda items :{item.position for item in items}
    makeCyclic = lambda index : index % len(loop)
    #Running the simulation
    for time in range(limit+1):
        t1pos,t2pos = makeCyclic(t1pos),makeCyclic(t2pos)
        t1area = locate(t1pos,t1len,left=t1name.isupper())
        t2area = locate(t2pos,t2len,left=t2name.isupper())
        if len(t1area) + len(t2area) != len(conv(t1area) | conv(t2area)):
            return time
        t1pos,t1stop = cross_station(t1name,t1pos,t1stop,t1len,time,clock_wise = t1name.islower())
        t2pos,t2stop = cross_station(t2name,t2pos,t2stop,t2len,time,clock_wise= t2name.islower())

    return -1
