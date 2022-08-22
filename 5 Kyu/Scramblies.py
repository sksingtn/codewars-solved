def scramble(s1, s2):
    for x in set(s2):
        if s1.count(x)<s2.count(x):return False
    else:return True
        
