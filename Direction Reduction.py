def dirReduc(arr):
    import re
    direction = "".join(arr)
    
    pattern = re.compile(r'(NORTHSOUTH|SOUTHNORTH|EASTWEST|WESTEAST)+')
    
    while re.search(pattern,direction) != None:
        direction = re.sub(pattern,"",direction)

    pattern = re.compile(r'(NORTH|SOUTH|EAST|WEST)')
    return [i for i in re.split(pattern,direction) if i != '']

