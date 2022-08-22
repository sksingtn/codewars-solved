from math import factorial as fac
from itertools import groupby
from functools import reduce
from collections import Counter
from decimal import Decimal

class Words:
    def __init__(self,word):
        self.word = list(word.upper())
        
    def __iter__(self):
        for x,_ in groupby(sorted(self.word),lambda x : x):
            yield x

    def permute(self,exclude):        
        current = list(self.word)
        current.remove(exclude)
        dividend = list(map(lambda x : fac(x),filter(lambda x : x != 1,Counter(current).values())))
        
        if dividend:
            dividend = reduce(lambda x,y: x*y,dividend)
        else:
            dividend = 1            
        return Decimal(fac(len(current)))/Decimal(dividend)
            
    def delete(self,item):
        self.word.remove(item)

def listPosition(word):
    obj = Words(word)
    pos = 0

    for i in range(len(word)):
        for letter in obj:
            if letter == word[i]:
                obj.delete(word[i])
                break
            else:
                pos += obj.permute(letter)
                
    return pos + 1     
        

print(listPosition("SAUMYA"))





