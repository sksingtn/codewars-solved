from collections import Counter,OrderedDict
from itertools import chain
def mix(s1,s2):
    count = lambda x: Counter((i for i in x if i.isalpha()==True and i.islower()==True and list(str(x)).count(i)>1))
    a,b = count(s1),count(s2)
    ab = []
    for i in a | b:
        if i in a and i in b:
            ab.append(str(1 if a[i]>b[i] else(2 if b[i]>a[i] else "="))+str(":")+str(max(a[i],b[i])*i))
        elif i in a:
            ab.append(str(1)+str(":")+str(a[i]*i))
        else:
            ab.append(str(2)+str(":")+str(b[i]*i))
    l = list(sorted(ab,key = lambda x: (len(x),x),reverse = True))
    c = OrderedDict()
    for i in l:
        c.setdefault(len(i),[])
        c[len(i)].append(i)
    return "/".join([j for i in c.values() for j in i[-1::-1] ])
