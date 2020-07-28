
def recoverSecret(triplets):
    first,second,third = [],[],[]
    for i,j,k in triplets:
        first.append(i)
        second.append(j)
        third.append(k)
    word = []
    while len(first) != first.count(0):
        for i in range(len(first)):
            if (first[i] not in second+third) and (first[i] != 0):                
                if first[i] not in word:
                    word.append(first[i])
                first.pop(i)
                first.insert(i,second[i])
                second.pop(i)
                second.insert(i,third[i])
                third.pop(i)
                third.insert(i,0)
                
            
    return "".join(word)            

recoverSecret([["t","u","p"],["w","h","i"],["t","s","u"],["a","t","s"],["h","a","p"],["t","i","s"],["w","h","s"]])    
