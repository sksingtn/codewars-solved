def top_3_words(text):
    import re
    words = re.findall(r'[a-z\']+',text.lower(),re.IGNORECASE)    
    a =  set([i for i in words  if i != "'" and i != "''" and i != "'''"])        
    count = {i:words.count(i) for i in a}
    top = list()
    for j,i in enumerate(sorted(count.keys(),key = lambda x : count[x],reverse = True),start = 1):
        if j == 4:
            break
        top.append(i)

    return top
