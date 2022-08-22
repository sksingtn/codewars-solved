
def who_is_next(names, r):
    detail = [[i,1] for i in names]
    count = 0
    while (not(r>count-1) or not(r<count+detail[0][1]+1)):
        count+= detail[0][1]
        detail[0][1]*=2
        detail.append(detail.pop(0))
    return detail[0][0]
