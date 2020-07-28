import operator
from copy import deepcopy
class chess:
    def __init__(self,pieces,player):
        self.A,self.D=int(not player),player
        self.pieces = deepcopy(pieces)
        self.loc=[]
        for x in self.pieces:
            if x.get("piece")=="king" and x.get("owner")==self.D:
                self.k_loc=(x.get("y"),x.get("x"))
            else:
                self.loc.append((x["y"],x["x"]))                   
    def ro_bi_qu(self,name,function):
        self.check=[]
        for x in self.pieces:
            if x["owner"] == self.A and x["piece"]==name:
                self.x,self.y=x.get("y"),x.get("x")
                found=False
                for fun in function:
                    if found == True:
                       break                   
                    while self.x in range(0,8) and self.y in range(0,8):
                        self.x,self.y=fun(self.x,self.y)                        
                        if (self.x,self.y) in self.loc and (self.x,self.y) != (x.get("y"),x.get("x")):
                            self.x,self.y=x.get("y"),x.get("x")
                            break                          
                        elif (self.x,self.y)==self.k_loc:
                            self.check.append(x)
                            found=True
                            break
                    self.x,self.y=x.get("y"),x.get("x")    
        return self.check
                
    def rook(self):
        return chess.ro_bi_qu(self,"rook",(lambda x,y:(x,y+1),lambda x,y:(x+1,y),lambda x,y:(x-1,y),lambda x,y:(x,y-1)))
    def bishop(self):
        return chess.ro_bi_qu(self,"bishop",(lambda x,y:(x+1,y+1),lambda x,y:(x-1,y-1),lambda x,y:(x+1,y-1),lambda x,y:(x-1,y+1)))
    def queen(self):
        return chess.ro_bi_qu(self,"queen",(lambda x,y:(x,y+1),lambda x,y:(x+1,y),lambda x,y:(x-1,y),lambda x,y:(x,y-1),lambda x,y:(x+1,y+1),lambda x,y:(x-1,y-1),lambda x,y:(x+1,y-1),lambda x,y:(x-1,y+1)))
    def knight(self):
        self.check = []
        for x in self.pieces:
            if x["owner"] == self.A and x["piece"]=="knight":
                self.x,self.y=x.get("y"),x.get("x")
                for i,j in ((self.x-1,self.y+2),(self.x+1,self.y+2),(self.x-2,self.y+1),(self.x-2,self.y-1),(self.x-1,self.y-2),(self.x+1,self.y-2),(self.x+2,self.y+1),(self.x+2,self.y-1)):
                    if i in range(0,8) and j in range(0,8) and (i,j) == self.k_loc:
                        self.check.append(x)
                        break
        return self.check    
    def pawn(self):
        def dual_pawn(self,fun):
            self.check = []
            for x in self.pieces:
                if x["owner"] == self.A and x["piece"]=="pawn":
                    self.x,self.y=x.get("y"),x.get("x")
                    for f in fun:
                        i,j = f(self.x,self.y)
                        if i in range(0,8) and j in range(0,8) and (i,j)==self.k_loc:
                            self.check.append(x)
            return self.check        
        if self.A:
            return dual_pawn(self,(lambda x,y:(x+1,y-1),lambda x,y:(x+1,y+1)))
        else:
            return dual_pawn(self,(lambda x,y:(x-1,y+1),lambda x,y:(x-1,y-11)))                
    def total(self):
        return [j for i in (chess.rook(self),chess.bishop(self),chess.queen(self),chess.knight(self),chess.pawn(self)) for j in i]

def isCheck(pieces, player):
    obj = chess(pieces,player)
    return obj.total()

def isMate(pieces, player):
    base = deepcopy(pieces)
    obj = chess(pieces,player).total()
    if not obj:return False
    enemy,team = [],[]
    for x in pieces:
        if x["owner"] == player:
            team.append((x["y"],x["x"]))
        else:
            enemy.append((x["y"],x["x"]))            
    def modify(board,oldx,oldy,newx,newy):
        for i in range(len(board)):
            if board[i]["y"] == oldx and board[i]["x"] == oldy:
                board[i]["y"],board[i]["x"]=newx,newy
                break
        return board
    def delete(board,x,y):
        for i in range(len(board)):
            if board[i]["y"] == x and board[i]["x"] == y:
                del board[i]
                break       
        return board                
    #King_and_knight
    for name,move in (("king",(lambda i,j:(i-1,j-1),lambda i,j:(i-1,j),lambda i,j:(i-1,j+1),lambda i,j:(i,j+1),lambda i,j:(i,j-1),lambda i,j:(i+1,j-1),lambda i,j:(i+1,j),lambda i,j:(i+1,j+1))),("knight",((lambda i,j:(i-1,j+2)),(lambda i,j:(i+1,j+2)),(lambda i,j:(i-2,j+1)),(lambda i,j:(i-2,j-1)),(lambda i,j:(i-1,j-2)),(lambda i,j:(i+1,j-2)),(lambda i,j:(i+2,j+1)),(lambda i,j:(i+2,j-1))))):
        for x in pieces:
            if x["owner"] == player and x["piece"] == name:
                i,j=(x["y"],x["x"])
                for f in move:
                    a,b = f(i,j)
                    if a in range(0,8) and b in range(0,8) and (a,b) not in team+enemy:
                        print(a,b)
                        base = modify(base,i,j,a,b)
                        demo = chess(base,player)
                        if demo.total() == []:return False
                        else:base = deepcopy(pieces)
                    elif a in range(0,8) and b in range(0,8) and (a,b) in enemy:
                        base = delete(base,a,b)
                        base = modify(base,i,j,a,b)
                        demo = chess(base,player)
                        if demo.total() == []:return False
                        else:base = deepcopy(pieces)
    #Rook_Bishop_Queen
    for name,move in (("queen",(lambda x,y:(x,y+1),lambda x,y:(x+1,y),lambda x,y:(x-1,y),lambda x,y:(x,y-1),lambda x,y:(x+1,y+1),lambda x,y:(x-1,y-1),lambda x,y:(x+1,y-1),lambda x,y:(x-1,y+1))),("bishop",(lambda x,y:(x+1,y+1),lambda x,y:(x-1,y-1),lambda x,y:(x+1,y-1),lambda x,y:(x-1,y+1))),("rook",(lambda x,y:(x,y+1),lambda x,y:(x+1,y),lambda x,y:(x-1,y),lambda x,y:(x,y-1)))):        
        for x in pieces:
            if x["owner"] == player and x["piece"] == name:
                i,j=(x["y"],x["x"])
                for f in move:
                    a,b = f(i,j)
                    while a in range(0,8) and b in range(0,8):
                        if (a,b) not in team+enemy:
                            base = modify(base,i,j,a,b)
                            demo = chess(base,player)
                            if demo.total() == []:return False
                            else:base = deepcopy(pieces)
                        elif (a,b) in enemy:                            
                            base = delete(base,a,b)
                            base = modify(base,i,j,a,b)                            
                            demo = chess(base,player)
                            if demo.total() == []:return False
                            else:base = deepcopy(pieces);break
                        elif (a,b) in team:break
                        a,b = f(a,b)
    #pawn   
    for x in pieces:
        if x["owner"] == player and x["piece"] == "pawn":
            i,j = (x["y"],x["x"])
            if player == 0:
                ad,ba = operator.add,operator.sub                
            elif player == 1:
                ad,ba = operator.sub,operator.add                               
            if i == 6 and (ba(i,2),j) not in team+enemy and (ba(i,1),j) not in team+enemy:
                base = modify(base,i,j,ba(i,2),j)
                demo = chess(base,player)
                if demo.total() == []:return False
                else:base = deepcopy(pieces)
            if (ba(i,1),j) not in team+enemy:
                base = modify(base,i,j,ba(i,1),j)
                demo = chess(base,player)
                if demo.total() == []:return False
                else:base = deepcopy(pieces)
            #En passant
            if (i,ba(j,1)) in enemy and (ba(i,1),ba(j,1)) not in team+enemy and ba(i,1) in range(0,8) and ba(j,1) in range(0,8):
                for x in pieces:
                    if x["owner"] != player and x["piece"] == "pawn" and x["y"] == i and x["y"]==ba(j,1) and x.get("prevY",None) != None:
                        base = delete(base,i,ba(j,1))
                        base = modify(base,i,j,ba(i,1),ba(j,1))
                        demo = chess(base,player)
                        if demo.total() == []:return False
                        else:base = deepcopy(pieces);break
            if (i,ad(j,1)) in enemy and (ba(i,1),ad(j,1)) not in team+enemy and ba(i,1) in range(0,8) and ad(j,1) in range(0,8):
                for x in pieces:
                    if x["owner"] != player and x["piece"] == "pawn" and x["y"] == i and x["y"]==ad(j,1) and x.get("prevY",None) != None:
                        base = delete(base,i,ad(j,1))
                        base = modify(base,i,j,ba(i,1),ad(j,1))
                        demo = chess(base,player)
                        if demo.total() == []:return False
                        else:base = deepcopy(pieces);break                               
    return True
