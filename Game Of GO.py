from itertools import islice,dropwhile
from collections import namedtuple

class Go:

    """ Implementation of Game of Go with a Group based Incremental Approach """
    def __init__(self,height,width=None):
        self.height,self.width = height, width or height
        if self.height not in range(26) or self.width not in range(26):
            raise Exception
        self.alphabet = filter(lambda x : x != "i",map(lambda x : chr(97 + x),range(26)))
        self.marker = list(islice(self.alphabet,0,self.width))
        self.group = namedtuple("group",["pieces","liberty"])
        self.size = {"height": self.height, "width": self.width}
        self.info = {"x":[],"o":[]}
        self.history = []
        self.handicap = False
                
    @property
    def turn(self):
        return "black" if len(self.history) % 2 == 0 else "white"

    def reset(self):
        self.info = {"x":[],"o":[]}
        self.history = []
        self.handicap = False
        
    @staticmethod
    def create_pieces(pieces):
        new = set()
        for g in pieces:
            new |= g.pieces
        return new
    
    def create_liberty(self,i,j,check=False):
        liberty = set()
        for x,y in ((-1,0),(0,-1),(0,1),(1,0)):
            x,y = x+i,y+j
            if check or (x in range(self.height) and y in range(self.width)):
                liberty.add((x,y))
        return liberty

    def merge(self,current,groups,i,j,liberty):
        """ Detects if the current move should become a lone group or a composite one """
        self.info[current] = [x for x in self.info[current] if x is not None]

        new_groups,new_liberties = set(),set()
        for g in groups:
            new_groups |= g.pieces
            new_liberties |= g.liberty

        new_groups.add((i,j))
        new_liberties.remove((i,j))
        new_liberties |= liberty
        
        self.info[current].append(self.group(new_groups,new_liberties))
        return False if new_liberties else True

    def str_to_int(self,i,j):
        if int(i) not in range(1,self.height+1) or j.lower() not in self.marker:
            raise Exception
        return self.height - int(i), self.marker.index(j.lower())

    def rollback(self,n):        
        if n > len(self.history):            
            raise            
        self.history = self.history[:-n]
        if not self.history:
            self.info = {"x":[],"o":[]}
        else:
            if self.history[-1] is None:
                self.info = self.deepalt(next(dropwhile(lambda x : x is None,self.history[::-1]),{"x":[],"o":[]}))
            else:
                self.info = self.deepalt(self.history[-1])


    def pass_turn(self):
        self.history.append(None)

    def handicap_stones(self,n):
        #Supported Boards
        if (self.height,self.width) not in {(9,9),(13,13),(19,19)}:
            raise Exception
        
        #Correct No of stones
        if (self.height == 9 and n not in range(1,6)) or (self.height in (13,19) and n not in range(1,10)):
            raise Exception

        #Handicap Placing Criteria
        if self.handicap or len(self.history) != 0:
            raise Exception

        #Main Functionality
        c = 2 if self.height == 9 else 3
        main = self.height
        
        stones = lambda itr1,itr2,order : list(zip(order,list(zip(itr1,itr2))[c:-c][::int(((main-2*c)+1)/2 - 1)]))

        total = []
        middle = int(((main+1) / 2)-1)
        
        total.extend(stones(range(0,main),range(main-1,-1,-1),(1,5,2))+stones(range(0,main),range(0,main),(4,5,3))
                     +stones([middle]*main,range(0,main),(6,5,7))+stones(range(0,main),[middle]*main,(8,5,9)))
        
        turn = "x" if len(self.history) % 2 == 0 else "o"
        total = sorted(list(set(total)),key=lambda x : x[0])[:n]
        for _,(i,j) in total:
            liberty = self.create_liberty(i,j)
            self.info[turn].append(self.group({(i,j)},liberty))

        self.handicap = True


    def move(self,*args):
        for move in args:
            self.single_move(move)
    
    def single_move(self,location):
        suicide = False
        i,j = self.str_to_int(location[:-1],location[-1])
        
        #Checks for overlap and liberties
        all_pieces = Go.create_pieces(self.info["x"]+self.info["o"])

        if (i,j) in all_pieces:
            raise

        liberty = self.create_liberty(i,j) - (all_pieces)

        current,opponent = ("x","o") if len(self.history) % 2 == 0 else ("o","x")

        #Merging Into Existing or Creating new groups
        new_group = []
        for num,group in enumerate(self.info[current]):
            if (i,j) in group.liberty:
                new_group.append(group)
                self.info[current][num] = None
        if not new_group:
            new = self.group({(i,j)},liberty)
            self.info[current].append(new)
            #If its a lone group and has no liberties then possibly suicide
            if not liberty:
                suicide = True
        else:
            #If the current placement has no room but the overall group has liberties then its not a suicide
            suicide = self.merge(current,new_group,i,j,liberty)


        #Cleaning Groups with no liberties
        for num,group in enumerate(self.info[opponent]):
            if (i,j) in group.liberty:
                if len(group.liberty) == 1:
                    if suicide:
                        suicide = False
                    #Assigning Freed liberties
                    removed = self.info[opponent][num].pieces
                    self.info[opponent][num] = None
                    for new_i,new_j in removed:
                        for group in self.info[current]:
                            if self.create_liberty(new_i,new_j,check=True) & group.pieces:
                                group.liberty.add((new_i,new_j)) 
                else:
                    group.liberty.remove((i,j))
                
        self.info[opponent] = [x for x in self.info[opponent] if x is not None]        
        self.history.append(self.deepalt(self.info))

        #Suicide or KO Move then Internal Rollback
        if suicide or len(self.history) >= 3 and self.history[-1] == self.history[-3]:
            self.rollback(1)            
            raise
        
    def deepalt(self,info):
        #Faster Alternative of Deepcopy
        return {"x":list(self.group(set(x.pieces),set(x.liberty)) for x in info["x"]),"o":list(self.group(set(x.pieces),set(x.liberty)) for x in info["o"])}

        
    @property
    def board(self):
        board = [["."]*self.width for rows in range(self.height)]
        for symbol,groups in (("x",self.info["x"]),("o",self.info["o"])):
            for group in groups:
                for i,j in group.pieces:
                    board[i][j] = symbol

        return board


    def get_position(self,location):
        i,j = self.str_to_int(location[:-1],location[-1])
        
        #Checks for overlap and liberties
        black_pieces,white_pieces = Go.create_pieces(self.info["x"]),Go.create_pieces(self.info["o"])

        return "x" if (i,j) in black_pieces else ( "o" if (i,j) in white_pieces else ".")




