def snail(array):
    import itertools
    a = []
    if len(array) == 1:
        a.append(array[0][0])
        return  a
    def stripper(matrix):
        new = []
        matrix.pop(-1)
        matrix.pop(0)
        if matrix == []:
            return []
        for j in matrix:
            new.append(j[1:-1])
        return new    
                
    while len(array) > 1:
        for i in itertools.chain((j for j in array[0]),(k[-1] for k in array[1:len(array)-1]),(l for l in array[-1][-1::-1]),(m[0] for m in array[-2:-len(array):-1])):
            a.append(i)
        array = stripper(array)
        if len(array) == 1:
            a.append(array[0][0])
            break
    return a    
            








