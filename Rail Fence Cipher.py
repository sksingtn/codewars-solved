from itertools import cycle
from operator import add,sub
def encode_rail_fence_cipher(string,n):
    total = ""
    if string=="":return ""
    fix = ((n-2)*2+2)
    top,bottom=string[0::fix],string[n-1::fix]
    for i in range(1,n-1):
        first,last=(n-i-2)*2+2,(n-(n-i-1)-2)*2+2
        msg,count = string[i],i
        for x in cycle([first,last]):
            try:count+=x;msg+=string[count]                
            except IndexError:total+=msg;break                             
    return top+total+bottom
    
def decode_rail_fence_cipher(string, n):
    if string=="":return ""
    def alternate(start,stop):
        i,fun=start,add
        yield start
        while True:
            if i==start:fun=add
            if i==stop-1:fun=sub
            i=fun(i,1)
            yield i
    base=list()
    for i in range(1,n-1):
        first,last=(n-i-2)*2+2,(n-(n-i-1)-2)*2+2
        msg,count = string[i],i
        for x in cycle([first,last]):
            try:count+=x;msg+=string[count]
            except IndexError:base.append(len(msg));break            
    base = [len(string[0::((n-2)*2+2)])]+base+[len(string[n-1::((n-2)*2+2)])]    
    new,start,dec=list(),0,""
    for x in base:
            new.append(string[start:start+x])
            start=start+x
    for x in alternate(0,n):
            if any(new)==False:break
            dec+=new[x][0]
            new[x] = new[x][1:]
    return dec
