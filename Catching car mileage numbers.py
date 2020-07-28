def is_interesting(number, awesome_phrases):
    def single(number,phrase):
        p="12345678909876543210"
        number = str(number)
        if (len(number)>=3) and ((number==number[::-1]) or (len(str(number).rstrip("0"))==1) or (int(number) in phrase) or (number in p)):return True    
        else:return False           
    final = [single(i,awesome_phrases) for i in range(number,number+3)]
    if final[0]:return 2
    elif any(final[1:]):return 1
    else:return 0
