import random
def interpret(code):  
    matrix = [list(i) for i in code.split("\n")]    
    string = False   
    op = {"+":lambda x,y:x+y,"-":lambda x,y:y-x,"*":lambda x,y:y*x,"/":lambda x,y:y//x,"%":lambda x,y:y%x}
    stack = []
    skip = False
    direction = ">"
    output = ""
    row = 0
    col = 0
    while True:
        if string == True and matrix[row][col] != '"':
            stack.append(ord(matrix[row][col]))        
        elif str(matrix[row][col]).isnumeric():
            stack.append(int(matrix[row][col]))
        elif matrix[row][col] in [">","<","^","v"]:
            direction = matrix[row][col]
        elif matrix[row][col] == "?":
            direction = random.choice([">","<","^","v"])
        elif matrix[row][col] == "_":
            direction = "<" if stack.pop() else ">"
        elif matrix[row][col] == "|":
            direction = "^" if stack.pop() else "v"
        elif matrix[row][col] == "#":
            skip = True
        elif matrix[row][col] == '"':
            if string == False:
                string = True
            else:
                string = False
        elif matrix[row][col] in op:
            a,b=stack.pop(),stack.pop()
            stack.append(int(op[matrix[row][col]](a,b)))
        elif matrix[row][col] == "!":
            stack.append(1) if stack.pop()==0 else stack.append(0)
        elif matrix[row][col] == "`":
            stack.append(1) if stack.pop()<stack.pop() else stack.append(0)
        elif matrix[row][col] == ":":
            stack.append(stack[-1]) if len(stack) else stack.append(0)
        elif matrix[row][col] == "\\":
            stack.extend([stack.pop(),stack.pop()])if len(stack)>1 else stack.extend([stack.pop(),0])
        elif matrix[row][col] == "$":
            stack.pop()
        elif matrix[row][col] == ".":
            output += str(stack.pop())
        elif matrix[row][col] == ",":            
            output += str(chr(int(stack.pop())))            
        elif matrix[row][col] == "p":
            y,x,v = stack.pop(),stack.pop(),stack.pop()
            matrix[y][x] = chr(v)
        elif matrix[row][col] == "g":
                y,x  = stack.pop(),stack.pop()
                stack.append(ord(matrix[y][x]))
        elif matrix[row][col] == " ":
            pass
        elif matrix[row][col] == "@":
            break
        if direction == ">":
            if skip == True:
                col = col + 2
                skip = False
            else:    
                col += 1
        elif direction == "<":
            if skip == True:
                col = col - 2
                skip = False
            else:    
                col -= 1
        elif  direction == "^":
            if skip == True:
                row = row - 2 
                skip = False
            else:    
                row -= 1
        elif direction == "v":
            if skip == True:
                row = row + 2
                skip = False
            else:    
                row += 1                
       
    return output
