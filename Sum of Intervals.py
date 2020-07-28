def sum_of_intervals(intervals):
    total = list()
    for i,j in intervals:total.extend(list(range(i,j)));total = list(set(total))            
    return len(total)

        


