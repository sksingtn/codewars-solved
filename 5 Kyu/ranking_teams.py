def compute_ranks(number, games):
    score,info = dict(),dict()
    for a,b,goals,defend in games:
        score.setdefault(a,{"a":0,"d":0,"p":0})
        score.setdefault(b,{"a":0,"d":0,"p":0})
        score[a]["a"],score[b]["a"] = score[a]["a"]+goals,score[b]["a"]+defend
        score[a]["d"],score[b]["d"] = score[a]["d"]+defend,score[b]["d"]+goals
        calc = lambda x,y: 2 if x>y else (1 if x==y else 0)
        score[a]["p"] += calc(goals,defend)
        score[b]["p"] += calc(defend,goals)
    print(score)
    for x in range(number):
        if x in score.keys():
            info[x] = (score[x]["p"],score[x]["a"]-score[x]["d"],score[x]["a"])
        else:
            info[x] = (0,0,0)
    final = sorted(info.values(),reverse = True)
    ranking = []
    for x in range(number):
        ranking.append(final.index(info[x])+1)
    print(ranking)
    return ranking
        


compute_ranks(10, [])
