import itertools
def next_bigger(n):
    a = n

    if "".join(sorted(str(a),reverse=True)) == str(a):
        return -1
    ab=[]
    for i in range(-2,-len(str(a))-1,-1):
        cache = int(str(a)[i:])
        if "".join(sorted(str(cache),reverse=True)) != str(cache):
            print(cache)
            for j in itertools.permutations(str(cache),len(str(cache))):
                if int("".join(j)) > cache:
                    ab.append(int("".join(j)))
            return  int(str(a)[:i]+ str(min(ab)))

import itertools
def next_biggers(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1        
        

