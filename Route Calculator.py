def calculate(expression):
    import operator
    import re
    pattern = re.compile(r'([\+\-\*\$])')
    exp = re.split(pattern,expression)
    pattern2 = re.compile(r'^[.0123456789\+\-\*\$]+$')
    if re.findall(pattern2,expression) == []:
        return "400: Bad request"
    
    
    lookup = { "$":operator.truediv,"*":operator.mul,"-": operator.sub,"+": operator.add}
    for m in lookup:
        add = 0
        for i in range(len(exp)):
            if exp[i-add] == m:
                exp[i-add] = lookup[m](float(exp[i-1-add]),float(exp[i+1-add]))
                exp.pop(i+1-add)
                exp.pop(i-1-add)
                add += 2
            
    if str(exp[0]).endswith(".0"):
        return int(str(exp[0]).split(".")[0])
    else:
        return(float(exp[0]))
            
