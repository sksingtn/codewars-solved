import re
def solve_runes(runes):
    print(runes)
    pattern = r'(\-?\d+)(\+|\-|\*)(\-?\d+)\=(\-?\d+)'
    runes = re.sub(r'\-{2}',"+",runes)
    possible = {1,2,3,4,5,6,7,8,9,0}.difference(set(map(lambda x:int(x),filter(lambda x:x.isnumeric(),runes))))
    op = {"+":lambda x,y:x+y,"-":lambda x,y : x-y,"*": lambda x,y:x*y}    
    possible = list(sorted(possible))
    for i in range(1,len(runes)-1):
        if runes[i] == "?" and (runes[i-1] == "+" or runes[i-1] == "-" or runes[i-1] == "*" or runes[i-1] == "=") and runes[i+1] == "?":
            if 0 in possible:
                possible.remove(0)
                break
    if possible == []:
        return -1
    print(possible)    
    for i in possible:
        new = runes.replace("?",str(i))
        exp = re.split(pattern,new)
        exp = [i for i in exp if i != '']
        
        print(exp)
        if op[exp[1]](int(exp[0]),int(exp[2])) == int(exp[3]):
            return i
    return -1   
