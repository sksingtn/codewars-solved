def valid(a):
    groups,number = len(a[0]),len(a[0][0])
    if all(len("".join(i)) == len(set("".join(i))) and len(i) == groups and all(len(j) == number for j in i) for i in a) == False:
        return False
    info = dict()
    for days in a:
        for groups in days:
            for players in groups:
                info.setdefault(players,[])
                info[players].extend([i for i in groups if i != players])
    unique = set()            
    for days in a:        
        unique.add("".join(sorted("".join(days))))
        
    if len(unique) != 1:
        return False

    
    return all(len(set(i)) == len(i) for i in info.values())    
            


    
