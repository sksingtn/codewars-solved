class Piece:
    def __init__(self,pieces):
        self.pieces = pieces[:2]
        self.id = pieces[-1]
        self.left = (pieces[0][0],pieces[1][0])
        self.right = (pieces[0][1],pieces[1][1])
        self.top = (pieces[0][0],pieces[0][1])
        self.down = (pieces[1][0],pieces[1][1])
        
def puzzle_solver(pieces, width, height):
    search = True
    boundaries = {"left":{},"up":{}}
    for (topleft,topright),(downleft,downright),ID in pieces:
        if search and set((downleft,topleft,topright)) == {None}:
            corner = Piece(((topleft,topright),(downleft,downright),ID))
            search = False
        boundaries['left'][(topleft,downleft)] = boundaries['up'][(topleft,topright)] =  Piece(((topleft,topright),(downleft,downright),ID))
            
    mapping = [[None]*width for x in range(height)]
    mapping[0][0] = corner
    
    for x in range(height):
        for y in range(width):
            if mapping[x][y] is not None:
                continue
            if y-1 >= 0:
                base = mapping[x][y-1]                
                mapping[x][y] = boundaries["left"][base.right]
            else:
                base = mapping[x-1][y]
                mapping[x][y] = boundaries["up"][base.down]
    return([tuple( mapping[x][y].id for y in range(width)) for x in range(height) ])
            
