import re
def calc(exp):
    exp = exp.replace(" ","").replace("-+","-").replace("+-","-").replace("--","+")
    exp = [i for i in ["("]+re.split(r'(\+|\-|\*|\/|\(|\))',exp)+[")"] if i != ""]
    def inner(string):
        op = {"/":lambda x,y:x/y,"*":lambda x,y:x*y,"+":lambda x,y:x+y,"-":lambda x,y:x-y}
        if len(string)>2 and string[0] == "-" and string[1] != "-" :
            string[0:2] = float(string[1])*-1,
        elif string[0] in op.keys() and len(string)==2:
            return [float(float(string[1])*-1)]
        elif len(string)==1:
            return [float(string[0])]

        for op1,op2 in [("*","/"),("+","-")]:
            while True:#to check -ve numbers
                for i in range(1,len(string)):
                    if string[i] == "-" and string[i-1] in ["+","-","/","*"]:
                        string[i:i+2] = float(string[i+1])*-1,
                        break
                else:break
            while op1 in string or op2 in string:
                try:op_1=string.index(op1)
                except ValueError:op_1=100
                try:op_2=string.index(op2)
                except ValueError:op_2=100
                m = min(op_1,op_2)
                if  m != 100:
                    string[m-1:m+2] = op[string[m]](float(string[m-1]),float(string[m+1])),
                else:
                    break
        return string
    while exp.count("(")>0:
        cache = ""
        for i in range(len(exp)):
            if exp[i] == "(":
                cache = i
            elif exp[i] == ")":
                exp[cache:i+1] = inner(exp[cache+1:i])
                break
    return float("".join(str(i) for i in exp))
