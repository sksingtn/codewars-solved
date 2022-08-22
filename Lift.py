from itertools import filterfalse
class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.floor,self.people,self.direction,self.stops = 0,[],1,[]
        self.capacity = capacity
        self.que = [list(y for y in x) for x in queues]

    def takePeople(self):
        self.remaining = []
        self.taken = []
        for people in self.que[self.floor]:
            if (self.capacity == len(self.people + self.taken)) or ((self.direction == 1 and people < self.floor) or (self.direction == -1 and people > self.floor)):
                self.remaining.append(people)
            else:
                self.taken.append(people)
        self.que[self.floor] = self.remaining
        return self.taken

    def dropPeople(self):
        self.initial_count = len(self.people)
        self.people = list(filter(lambda item : item != self.floor ,self.people))
        return False if self.initial_count == len(self.people) else True
        
    def theLift(self):
        while any(self.que) or self.people:
            is_dropped = self.dropPeople()
            entered = self.takePeople()
            self.people.extend(entered)
            if entered or is_dropped or (self.capacity == len(self.people) and self.que[self.floor] and ((self.direction == 1 and max(self.que[self.floor]) > self.floor) or (self.direction == -1 and min(self.que[self.floor]) < self.floor) )):
                if not self.stops or self.stops[-1] != self.floor:
                    self.stops.append(self.floor)

            lower,upper = (self.floor+1,len(self.que)) if self.direction == 1 else (0,self.floor)
            waiting = max(self.people or [0]) > self.floor if self.direction == 1 else min(self.people or [10000]) < self.floor
            not_changed = True
            if not any(self.que[lower:upper]) and (not waiting):
                not_changed = False
                self.direction *= -1

            if not self.que[self.floor] or not_changed:
                self.floor += self.direction
            
        if not self.stops: return [0]
        if self.stops[0] != 0:
            self.stops.insert(0,0)
        if self.stops[-1] != 0:
            self.stops.append(0)
        return self.stops
