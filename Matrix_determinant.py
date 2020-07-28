import cProfile
import time
import itertools
import copy
def determinant(matrix):
    det = 0    
    
    def stripper(i,j,matrix):
        new = copy.deepcopy(matrix) 
        new.pop(i)        
        for k in range(len(new)):            
            new[k].pop(j)
        return new
    if len(matrix[0]) == 1:
        return matrix[0][0]

    if len(matrix[0]) == 2:
        return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])

    if len(matrix[0]) == 3:   
        for i,j in zip(range(len(matrix[0])),itertools.cycle([1,-1])):            
            m = stripper(0,i,matrix)
            det += j * matrix[0][i] * (m[0][0]*m[1][1]-m[0][1]*m[1][0])
        return det    

    else:
        for i,j in zip(range(len(matrix[0])),itertools.cycle([1,-1])):
            m = stripper(0,i,matrix)
            det += j * matrix[0][i] * determinant(m)
            
        return det    
            
            
    
cProfile.run("determinant([[1,3,8,4,1,45,89],[6,8,4,5,1,29,48],[4,5,8,4,1,78,78],[5,8,4,3,1,78,89],[1,1,1,1,1,25,45],[45,78,96,32,45,45,45],[85,45,23,45,78,54,85]])")
    



























