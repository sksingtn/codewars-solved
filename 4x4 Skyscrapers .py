from random import choice,seed
from copy import deepcopy
def solve_puzzle(clues):
    forward = {1:[{4},{1,2,3},{1,2,3},{1,2,3}],2:[{1,2,3},{1,2,4},{1,2,3,4},{1,2,3,4}],3:[{1,2},{1,2,3},{1,2,3,4},{1,2,3,4}],4:[{1},{2},{3},{4}]}
    backward = {1:[{1,2,3},{1,2,3},{1,2,3},{4}],2:[{1,2,3,4},{1,2,3,4},{1,2,4},{1,2,3}],3:[{1,2,3,4},{1,2,3,4},{1,2,3},{1,2}],4:[{4},{3},{2},{1}]}

    matrix = [[0,0,0,0,0,0] for i in range(6)]
    for cl,(row,col) in zip(clues,[(0,1),(0,2),(0,3),(0,4),(1,5),(2,5),(3,5),(4,5),(5,4),(5,3),(5,2),(5,1),(4,0),(3,0),(2,0),(1,0)]):
        matrix[row][col] = cl


    
    for i in range(1,5):
        for j in range(1,5):
            clues_forward = [matrix[0][j],matrix[i][0]]
            clues_backward = [matrix[i][5],matrix[5][j],]
            bench = {1,2,3,4}
            for serial,c in enumerate(clues_forward,1):
                if c == 0:
                    bench = bench.intersection({1,2,3,4})
                elif c !=0 and serial == 1:
                    bench = bench.intersection(forward[c][i-1])
                elif c !=0 and serial == 2:
                    bench = bench.intersection(forward[c][j-1])
            bench2 = {1,2,3,4}
            for serial,c in enumerate(clues_backward,1):
                if c == 0:
                    bench2 = bench2.intersection({1,2,3,4})
                elif c !=0 and serial == 1:
                    bench2 = bench2.intersection(backward[c][j-1])
                elif c !=0 and serial == 2:
                    bench2 = bench2.intersection(backward[c][i-1])
            matrix[i][j] = list(bench2.intersection(bench))

    matrix.pop(0),matrix.pop(-1)
    for i in range(len(matrix)):
        matrix[i].pop(0),matrix[i].pop(-1)


    constraints = deepcopy(matrix)
    solution = [[0,0,0,0,0,0] for i in range(6)]
    for cl,(row,col) in zip(clues,[(0,1),(0,2),(0,3),(0,4),(1,5),(2,5),(3,5),(4,5),(5,4),(5,3),(5,2),(5,1),(4,0),(3,0),(2,0),(1,0)]):
        solution[row][col] = cl

    def solver(solution,constraints):
        found = False
        restart = False
        while not(found):
            count = -1
            for i in range(4):
                if restart == True:
                    restart = False
                    break
                for j in range(4):
                    count += 1
                    selection = choice(constraints[i][j])
                    for row in range(j,4):
                        if selection in constraints[i][row]:
                            constraints[i][row].remove(selection)

                    for col in range(i,4):
                        if selection in constraints[col][j]:
                            constraints[col][j].remove(selection)
                    
                    solution[i+1][j+1] = selection
                    
                    check = [l for k in constraints for l in k][count+1:]
                    if all(check) == False and check != []:
                            constraints = deepcopy(matrix)
                            solution = [[0,0,0,0,0,0] for i in range(6)]
                            for cl,(row,col) in zip(clues,[(0,1),(0,2),(0,3),(0,4),(1,5),(2,5),(3,5),(4,5),(5,4),(5,3),(5,2),(5,1),(4,0),(3,0),(2,0),(1,0)]):
                                solution[row][col] = cl
                            restart = True
                            break
                            
            else:
                found = True

        return solution        
            
    def verify(solution):
        for row,col in [(0,1),(0,2),(0,3),(0,4)]:
            if solution[row][col] != 0:
                check = []
                for i in range(1,5):
                    check.append(solution[i][col])
                count = 1
                m = check[0]
                for j in check:
                    if m<j:
                        count+=1
                        m = j
                if count != solution[row][col]:
                    return False

        for row,col in [(1,5),(2,5),(3,5),(4,5)]:
            if solution[row][col] != 0:
                check = []
                for i in range(4,0,-1):
                    check.append(solution[row][i])
                count = 1
                m = check[0]
                for j in check:
                    if m<j:
                        count+=1
                        m = j
                if count != solution[row][col]:
                    return False

        for row,col in [(5,4),(5,3),(5,2),(5,1)]:
            if solution[row][col] != 0:
                check = []
                for i in range(4,0,-1):
                    check.append(solution[i][col])
                count = 1
                m = check[0]
                for j in check:
                    if m<j:
                        count+=1
                        m = j
                if count != solution[row][col]:
                    return False

        for row,col in [(4,0),(3,0),(2,0),(1,0)]:
            if solution[row][col] != 0:
                check = []
                for i in range(1,5):
                    check.append(solution[row][i])
                count = 1
                m = check[0]
                for j in check:
                    if m<j:
                        count+=1
                        m = j
                if count != solution[row][col]:
                    return False        
                
        return True
    while verify(solution) == False:
        constraints = deepcopy(matrix)
        solution = [[0,0,0,0,0,0] for i in range(6)]
        for cl,(row,col) in zip(clues,[(0,1),(0,2),(0,3),(0,4),(1,5),(2,5),(3,5),(4,5),(5,4),(5,3),(5,2),(5,1),(4,0),(3,0),(2,0),(1,0)]):
            solution[row][col] = cl
        solution = solver(solution,constraints)
    r = []
    for _,i,j,k,l,_ in solution[1:5]:
        r.append((i,j,k,l))

    return (tuple(r))    
 
