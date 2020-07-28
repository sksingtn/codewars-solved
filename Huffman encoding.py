from collections import Counter
class Tree:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
        
def frequencies(s):    
    return sorted([(i,j) for i,j in Counter(s).items()],key=lambda x:x[1])
    
def encode(freqs,s):
    global tree
    if len(freqs)<=1:return None
    new = list(map(lambda x:(Tree(x[0]),x[1]),freqs))
    tree=""
    new=sorted(new,key=lambda x:x[1])
    while len(new) != 1:
        if new[0][1]>new[1][1]:
            new=sorted(new,key=lambda x:x[1])
        tree = Tree(".",new[0][0],new[1][0])
        new = [(tree,sum([new[0][1],new[1][1]]))]+new[2:]
    tree = new[0][0]
    def code(tree,s):
        def recursion(tree,letter):
            cache = []
            if tree==[]:return False
            for x in tree:                
                if x.value==letter:return True
                if x.left != None:cache.append(x.left)
                if x.right !=None:cache.append(x.right)
            return recursion(cache,letter)
        c=""
        while True:
            if tree.value==s:break
            if recursion([tree.left],s):
                c+="0";tree=tree.left                
            else:
                c+="1";tree=tree.right                
        return c
    value = [code(tree,x) for x in s]
    return("".join(value))

def decode(freqs,bits):   
    global tree
    if len(freqs)<=1:return None 
    c = ""
    temp = tree
    for i in bits:        
        if i=="0":temp=temp.left          
        else:temp=temp.right            
        if temp.value not in (".",None):
            c+=temp.value;temp=tree                       
    return(c)  
