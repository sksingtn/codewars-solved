from collections import deque
import bisect
def dbl_linear(n):
    final = {1}
    cache = deque([1])
    while True:
        current = cache.popleft()
        child = (current*2+1,current*3+1)
        final.update(child)
        if len(final) >= n+(n//3) and bisect.bisect(sorted(final),child[0]) > n-1:
            break      
        bisect.insort(cache,child[0])
        bisect.insort(cache,child[1])
    res = sorted(final)
    return res[n]
