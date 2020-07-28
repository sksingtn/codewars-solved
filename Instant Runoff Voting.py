from collections import Counter
def runoff(voters):
    while voters:
        votes = Counter((i[0] for i in voters))
        zero = {key:0 for key in voters[0] if key not in votes}
        votes.update(zero)
        if len(set(j for j in votes.values())) == 1 and len(votes)>1:
            return None
        else:
            if max(votes.values())>len(voters)/2:
                return max(votes,key = lambda x:votes[x])
            else:
                delete = min(votes.values())
                for i in range(len(voters)):
                    for key,value in votes.items():
                        if value == delete:
                            voters[i].remove(key)
