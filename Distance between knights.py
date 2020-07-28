
def knight(p1,p2):
    change = lambda a:str(8-int(a[1])) + str(ord(a[0].lower())-97)
    o,p = int(change(p1)[0]),int(change(p1)[1])
    q,r = int(change(p2)[0]),int(change(p2)[1])
    
    a = [[0 for i in range(0,8)] for j in range(0,8)]
    def moves(adress,matrix):        
        possible = []
        for i,j in adress:
            for k,l in [[i-2,j-1],[i-2,j+1],[i-1,j+2],[i+1,j+2],[i+2,j-1],[i+2,j+1],[i-1,j-2],[i+1,j-2]]:
                if k in range(0,8) and l in range(0,8):
                    possible.append([k,l])
        return possible
        
        
    init = [[o,p]]
    count = 1
    while True:    
        m = moves(init,a)
        if [q,r] in m:
            return count
        init = m
        count +=1
    


