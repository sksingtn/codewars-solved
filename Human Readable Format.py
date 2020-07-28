def format_duration(seconds):
    
    values = [0,0,0,0,0]
    for n,unit in enumerate([3600*24*365,3600*24,3600,60,1]):
        if seconds != 0 and seconds//unit != 0:
            values[n] = int(seconds//unit)
            seconds = seconds % unit
    l = []
    dic = {}
    for i,j in zip(["year","day","hour","minute","second"],values):
        if j == 1:
            l.append(str(j)+str(" ")+str(i))
        elif j>1:
            l.append(str(j)+str(" ")+str(i)+str("s"))
    if len(l) == 1:
        return l[0]
    else:    
        return ", ".join(l[:len(l)-1])+str(" and ")+str(l[-1])       
            
        

