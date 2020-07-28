def to_postfix (infix):
    Infix = str("(") + str(infix) + str(")")
    precedence = {"+":1,"-":1,"*":2,"/":2,"^":3}
    stack = []
    postfix = ""

    for i in Infix:
        if i == "(":
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                postfix += str(stack.pop())
            stack.pop()
        elif i in ["+","-","*","/","^"]:
            while stack[-1] != "(" and precedence[i] <= precedence[stack[-1]]:
                postfix += str(stack.pop())
            stack.append(i)
        else:
            postfix += str(i)
    return postfix        
