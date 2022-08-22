def permutations(iterable):
    total = set()
    total.add(iterable)
    items = list(range(len(iterable)))    
    while True:
        for index in range(len(items)-2,-1,-1):
            if items[index] < items[index+1]:
                target = index
                break
        else:break
            
        swap = items.index(min(x for x in items[index+1:] if x > items[target]))        
        items[target],items[swap] = items[swap],items[target]
        items[index+1:] = items[index+1:][::-1]
        total.add("".join(iterable[i] for i in items))
            
    return list(total)

permutations("shiv")
