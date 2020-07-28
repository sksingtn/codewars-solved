from re import sub
def parse_int(string):
    if string == "one million":
        return 1000000
    info = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,\
            "fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,"thirty":30,"forty":40,"fifty":50,\
            "sixty":60,"seventy":70,"eighty":80,"ninety":90}
            
    string = sub(r'\band',"",string)
    string = string.replace("-"," ")
    total,cache = 0,0   
    for i in string.split():
        if i in info.keys():
            cache += info[i]
        elif i == "thousand":
            if cache == 0:
                total += 1000
            else:
                total += cache*1000
            cache = 0
        elif i == "hundred":
            if cache == 0:
                cache += 100
            else:
                cache = cache*100
    return (total+cache)

parse_int("one thousand and forty")
