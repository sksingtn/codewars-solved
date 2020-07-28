def tree_by_levels(node):
    if node == None:
        return []
    total,cache  = [],[node]    
    while True:
        update = []
        for i in cache:
            total.append(i.value)
            if i.left != None:update.append(i.left)                
            if i.right != None:update.append(i.right)                
        if update != []:cache = update                        
        else:break            
    return total
