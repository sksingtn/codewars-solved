
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.first = 0
        self.second = 0
        self.ranking = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]

    def inc_progress(self,arank):
        self.first = self.ranking.index(self.rank)
        self.second = self.ranking.index(arank)
        if self.first<self.second:
            self.progress += 10*((self.second-self.first)**2)
        elif self.second+1 == self.first:
            self.progress += 1
        elif self.first == self.second:
            self.progress += 3

        while self.progress>=100:            
            if self.rank in self.ranking[:15]:                
                self.rank = self.ranking[self.ranking.index(self.rank) + 1]
                self.progress -= 100
            elif self.rank == 8:
                self.progress = 0
        if self.rank == 8:
            self.progress = 0
       
