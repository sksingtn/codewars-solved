from copy import deepcopy
def longest_slide_down(pyramid):
    p = deepcopy(pyramid)
    while len(p) != 1:
        for i in range(len(p[-2])):
            p[-2][i] += max([p[-1][i],p[-1][i+1]])
        del p[-1]
    return p[0][0]
