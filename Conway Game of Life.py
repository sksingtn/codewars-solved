def get_generation(cells,generations):
    import copy
    if generations == 0:
        return cells
    
    def get_neighbours(m,i,j):
        neighbour = []
        for k,l in [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]:
            if k in range(0,len(m)) and l in range(len(m[1])):
                neighbour.append(m[k][l])
        return neighbour
    final = copy.deepcopy(cells)
    for times in range(generations):
        final = [i for i in final if i.insert(0,0) == None and i.append(0) == None]
        final.append([0 for i in range(len(final[1]))])
        final.insert(0,[0 for i in range(len(final[1]))])
        c = copy.deepcopy(final)
        for i in range(len(final)):
            for j in range(len(final[i])):
                if final[i][j] == 1:
                    if get_neighbours(final,i,j).count(1) not in [2,3]:
                        c[i][j] = 0
                elif final[i][j] == 0:
                    if get_neighbours(final,i,j).count(1) == 3:
                        c[i][j] = 1
        if all(z == 0 for y in c for z in y):
            return [[]]
        while any(c[0]) == False:
            c.pop(0)
        while any(c[-1]) == False:
            c.pop(-1)
        for index in [0,-1]:
            while not([i[index] for i in c].count(1) >= 1):
                for j in range(len(c)):
                    c[j].pop(index)                        
        final = c                

    return c

  
get_generation([[1, 0, 0], [0, 1, 1], [1, 1, 0]],2)                

            
