import re
def expand(expr):
    def pascal_d(power):#Added dynamic pascal triangle for powers above 5,not for codewars
        pascal_d = [[1],[1,1]] 
        for count,i in enumerate(range(2,power+1),start=2):
            pascal_d.append([1 if j in (0,count) else sum([pascal_d[i-1][j-1],pascal_d[i-1][j]]) for j in range(0,count+1)])
        return (pascal_d)  
    pattern = re.compile(r'\(([-]?(\d+)?[a-z])[+]?([-]?\d+)\)\^(\d+)')
    found = pattern.match(expr)
    op2,power,cache = int(found.group(3)),int(found.group(4)),found.group(1) 
    var = cache[-1]
    op1 = 1 if len(cache)==1 else (int(cache[:-1]) if cache[0]=="-" and cache[1].isnumeric() else (-1 if cache[0]=="-" else int(cache[:-1])))
    pascal = pascal_d(power)
    e = ""
    for i in range(0,power+1):
        first = power-i
        a = str(pow(op1,first)*pascal[power][i]*pow(op2,i))
        e += (str("" if a == "1" else("-" if a == "-1" and first != 0 else ("-1" if a=="-1" and first==0 else a)))+("" if first == 0 and a!= "1" else ("1" if first==0 and a == "1" else var+str("^")+str(first)))+str("+"))
    return(e[:-1].replace("+-","-").replace("^1",""))#Replace ^1 by ""

expand("(20z+81)^9")
