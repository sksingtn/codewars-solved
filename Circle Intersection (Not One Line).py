from math import *;
def circleIntersection(a,b,r):
    print(a,b,r)
    if a==b:return floor(pi*r**2)
    try:
        v=lambda a,b,r :(acos(1/(r/(hypot(a[0]-b[0],a[1]-b[1])/2)))*2)
        return floor(0.5*r**2*(v(a,b,r)-sin(v(a,b,r)))*2)
    except:return 0     
