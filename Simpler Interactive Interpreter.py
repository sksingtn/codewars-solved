import re
def calc(exp):#used my soluction from "Evaluate mathematical expression"
    print(exp)
    exp = exp.replace(" ","").replace("-+","-").replace("+-","-").replace("--","+")
    exp = [i for i in ["("]+re.split(r'(\+|\-|\*|\%|\/|\(|\))',exp)+[")"] if i != ""]
    def inner(string):
        op = {"/":lambda x,y:x/y,"*":lambda x,y:x*y,"+":lambda x,y:x+y,"-":lambda x,y:x-y,"%":lambda x,y:x%y}
        if len(string)>2 and string[0] == "-" and string[1] != "-" :
            string[0:2] = float(string[1])*-1,
        elif string[0] in op.keys() and len(string)==2:
            return [float(float(string[1])*-1)]
        elif len(string)==1:
            return [float(string[0])]

        for operator in [("*","/","%"),("+","-")]:
            while True:#to check -ve numbers
                for i in range(1,len(string)):
                    if string[i] == "-" and string[i-1] in ["+","-","/","*"]:
                        string[i:i+2] = float(string[i+1])*-1,
                        break
                else:break
            while len(set(operator).intersection(set(string))) != 0:
                try:op_1=string.index(operator[0])
                except ValueError:op_1=100
                try:op_2=string.index(operator[1])
                except ValueError:op_2=100
                try:op_3=string.index(operator[2])
                except (ValueError,IndexError):op_3=100
                m = min(op_1,op_2,op_3)
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
    return int(float("".join(str(i) for i in exp)))
    
def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]

class Interpreter:
    def __init__(self):
        self.var = {}
        self.functions = {}
    def input(self,expression):
        tokens = tokenize(expression)
        if tokens == []:return ""
        if len(tokens)>1 and len(set(tokens).intersection(set(["+","-","*","/","%","="])))==0:raise
        print(tokens,expression)
        if "=" in expression:
            self.loc = expression.index("=")
            self.var[expression[0]]=calc("".join([str(self.var[x]) if x in self.var else x for x in expression[self.loc+1:]]))
            return(calc("".join([str(self.var[x]) if x in self.var else x for x in expression[self.loc+1:]])))
        elif len(tokens) == 1 and tokens[0] in self.var:
            return(self.var[tokens[0]])
        elif "=" not in expression:
            return(calc("".join([str(self.var[x]) if x in self.var else x for x in expression])))
