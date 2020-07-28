import copy
def same_structure_as(original,other):
    global check
    check = []
    if type(original) != type(other):
        return False
    
    def recursion(array):
        for i in array:
            if type(i) == list:
                check.append(True)
                recursion(i)
            else:
                check.append(False)

    recursion(original)
    initial = copy.deepcopy(check)
    check = []
    recursion(other)
    final = copy.deepcopy(check)
    return final == initial
