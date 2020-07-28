def simplify(poly):
    
    import re
    calc = {}
    pattern = re.compile(r'(\+|-)?(\d*)([a-z]+)')
    for i,j,k in re.findall(pattern,poly):
        if i == "":
            i = "+"
        if j == "":
            j = "1"
        calc.setdefault("".join(sorted(k)),0)
        calc["".join(sorted(k))] += int(str(i)+str(j))

    answer = ""
    for i in sorted(calc.keys(),key = lambda x : (len(x),x)):
        if calc[i] != 0:
            answer += str("+")+str(calc[i])+str(i)    
    answer = answer.replace("+-","-").replace("1","")
    if answer[0] == "+":
        return answer[1:]
    else:
        return answer
        
    
    



simplify("a+ca-ab")
