import time
def plants_and_zombies(l,z):
    sums = 0
    lawn = [list(x) for x in l]
    zombies = z
    active,move = [],0
    row,col = len(lawn),len(lawn[0])
    while True:
        
        for i,j,k in zombies:
            if i == move:
                active.append({"addr":(j,col-1),"hp":k,"stat":"n"})
        zombies = [x for x in zombies if x[0] != move]        

        for x in active:
            if x["stat"] == "o":
                a,b=x["addr"]
                x["addr"]=(a,b-1)
            elif x["stat"] == "n":
                x["stat"] = "o"
               
        for i in range(0,row):
            pellet = 0
            for j in range(0,col):
                if lawn[i][j].isnumeric():
                    pellet+=int(lawn[i][j])
            for _j in range(0,col):
                if pellet == 0:break
                for x in active:
                    if x["addr"]==(i,_j) and x["hp"]>0:
                        if x["hp"]>= pellet:
                            x["hp"]-=pellet
                            pellet = 0
                        else:
                            pellet -= x["hp"]
                            x["hp"] = 0
                        break
        

        S = []
        for i in range(col-1,-1,-1):
            for j in range(0,row):
                if lawn[j][i] == "S" and (j,i) not in S:
                    S.append((j,i))
        
        active = [x for x in active if x["hp"] != 0]

        record= [x.get("addr") for x in active]
        initial = time.time()
        for i,j in S:
            b1,b2,b3 = False,False,False
            for straight in range(j+1,col):
                if b1 == True:break
                if (i,straight) in record:
                    for x in active:
                        if x["addr"]==(i,straight) and x["hp"]>0:
                            x["hp"]-=1
                            b1 = True
                            break
            for r,c in zip(range(i,-1,-1),range(j,40)):
                if b2 == True:break
                if (r,c) in record:
                    for x in active:                    
                        if x["addr"]==(r,c) and x["hp"]>0:
                            x["hp"]-=1
                            b2 = True
                            break
            for x,y in zip(range(i,row),range(j,col)):
                if b3 == True:break
                if (x,y) in record:
                    for i in active:
                        if i["addr"] == (x,y) and i["hp"]>0:
                            i["hp"]-=1
                            b3 = True
                            break
        sums+= time.time()-initial 
               
         
        active = [x for x in active if x["hp"] != 0]        

        for i in range(0,row):
            for j in range(0,col):
                if lawn[i][j].isnumeric() or lawn[i][j] == "S":
                    for x in active:
                        if x["addr"] == (i,j+1):
                            lawn[i][j]=" "
                            break
        move += 1
        if zombies == [] and active == []:print("{:.3f}".format(sums));print("None");return None
        for x in active:
            if x["addr"][1] == 0:
                return move
        

import cProfile        
#cProfile.run("plants_and_zombies(['2       ', '  S     ', '21  S   ', '13      ', '2 3     '],[[0, 4, 28], [1, 1, 6], [2, 0, 10], [2, 4, 15], [3, 2, 16], [3, 3, 13]])")
cProfile.run("plants_and_zombies(  ['11SS              ', '1S12              ', '121S S            ', '3S SS             ', '31SS  S           ', 'SSS2  S           ', '5 1SS             ', '2 SS              ', '2  1  SS1         ', '11SSS             ', '5S 2   S1         ', ' 22SS             ', '4S                ', '3SS S             ', '5S                ', ' 11 SSS           ', '6 1S              ', ' 212S  S2         ', ' 141SS 11         ', '2                 ', 'S4                ', '11SS              ', '21SSS             ', 'S1S 11            ', '6SSS              '] ,[[0, 2, 79], [0, 3, 79], [0, 10, 133], [0, 11, 79], [0, 12, 66], [0, 13, 79], [0, 14, 79], [0, 15, 66], [0, 16, 106], [0, 19, 26], [0, 20, 66], [0, 22, 79], [0, 23, 66], [0, 24, 119], [1, 1, 70], [1, 4, 98], [1, 6, 112], [1, 7, 56], [1, 8, 84], [1, 9, 70], [1, 17, 126], [1, 18, 140], [1, 21, 56], [5, 5, 93], [7, 10, 71], [7, 11, 43], [7, 14, 43], [7, 16, 57], [7, 19, 14], [7, 23, 36], [7, 24, 65], [10, 1, 37], [10, 2, 48], [10, 6, 59], [10, 8, 44], [10, 9, 37], [10, 12, 39], [10, 13, 48], [10, 15, 39], [10, 20, 39], [10, 21, 29], [10, 22, 48], [11, 0, 74], [11, 4, 56], [11, 5, 42], [11, 7, 32], [11, 17, 73], [12, 18, 88], [16, 0, 28], [16, 3, 65], [20, 10, 71], [20, 14, 42], [20, 16, 56], [20, 19, 14], [20, 23, 35], [22, 1, 35], [22, 9, 35], [22, 11, 47], [22, 12, 37], [22, 13, 43], [22, 15, 37], [22, 20, 37], [22, 21, 28], [23, 2, 48], [23, 4, 51], [23, 5, 42], [23, 7, 29], [23, 17, 65], [23, 22, 48], [23, 24, 76], [25, 6, 74], [25, 8, 56], [25, 18, 82], [26, 0, 28], [29, 3, 57], [29, 10, 70], [29, 16, 56], [30, 1, 35], [30, 9, 35], [30, 12, 35], [30, 13, 42], [30, 14, 47], [30, 15, 35], [30, 19, 16], [30, 20, 35], [30, 21, 28], [30, 24, 60], [31, 2, 43], [31, 7, 28], [31, 11, 48], [31, 17, 64], [31, 23, 42], [32, 4, 55], [32, 5, 46], [32, 6, 55], [37, 8, 45], [37, 18, 74], [37, 22, 52], [38, 0, 28], [40, 16, 56], [41, 10, 77], [41, 12, 35], [41, 13, 42], [41, 14, 43], [41, 15, 35], [41, 19, 14], [41, 20, 35], [42, 1, 39], [42, 3, 55], [42, 7, 28], [42, 9, 39], [42, 11, 43], [42, 23, 37], [43, 2, 47], [43, 6, 56], [43, 17, 70], [43, 21, 34], [43, 22, 40], [43, 24, 76], [44, 4, 56], [44, 5, 48], [44, 8, 43], [45, 0, 28], [45, 18, 78], [49, 3, 41], [49, 10, 72], [49, 12, 35], [49, 13, 42], [49, 14, 42], [49, 15, 35], [49, 19, 14], [50, 1, 36], [50, 7, 28], [50, 9, 36], [50, 11, 42], [50, 16, 68], [50, 20, 39], [50, 23, 36], [52, 17, 65], [52, 21, 30], [52, 22, 42], [53, 2, 48], [53, 4, 51], [53, 5, 43], [53, 6, 62], [53, 8, 42], [53, 24, 73], [54, 0, 28], [54, 18, 72], [57, 3, 42], [57, 10, 71], [57, 12, 35], [57, 13, 42], [57, 14, 42], [57, 15, 35], [57, 19, 14]])")
