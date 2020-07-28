from collections import OrderedDict
def score_card(balls,batsmen):
    score = OrderedDict()
    batsmen = list(batsmen)
    score,pitch,out = score.fromkeys(batsmen,0),[batsmen.pop(0),batsmen.pop(0)],[]
    for num,x in enumerate(balls,start=1):
        if x == "1" or x == "3":
            score[pitch[0]]+=int(x)
            pitch = pitch[::-1]
        elif x == "2" or x=="4" or x=="6":score[pitch[0]]+=int(x)                       
        elif x == "w":
            out.append(pitch[0])
            if batsmen == []:break
            pitch[0]=batsmen.pop(0)
        if num%6==0:
            pitch = pitch[::-1]
    return("\n".join(["{0} {1:>3}{2}".format(bat,"-" if bat in batsmen else score," not out"if (bat not in out and bat not in batsmen) else "") for bat,score in score.items()]+["TOTAL "+str(sum(score.values()))]))
