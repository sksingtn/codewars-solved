def balanced_parens(n):
    hash1,hash2,hash_table = {"(":1,")":-1},{"(":1,")":0},{1:("(",1,1)}
    if n == 0: return ['']
    if n == 1: return ['()']
    treelimit = sum(map(lambda x : 2**x,range(2*n-1)))    
    find = lambda index : "(" if index % 2 else ")"
    leaf_lower = treelimit - 2**(2*n-2)
    stack = [1]
    
    def findpath(index):
        if index ==1:
            return "("                
        path,tally,lcount = hash_table[index//2]
        symbol = find(index)
        newtally = tally + hash1[symbol]
        newlcount = lcount + hash2[symbol]
        newpath = path+symbol

        if newtally < 0 or newlcount > n:
            return False
        else:
            hash_table[index] = (newpath,newtally,newlcount)
            return newpath
    
    perfect = []
    while stack:
        current = stack.pop()
        pattern = findpath(current)
        if stack == 1 or pattern:
            stack.extend([x for x in (current*2,current*2+1) if x <= treelimit])
            if current > leaf_lower:
                perfect.append(pattern+")")

    return perfect
