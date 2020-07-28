from itertools import product
def get_pins(observed):
  info = {"1":["1","2","4"],"2":["2","1","3","5"],"3":["3","2","6"],"4":["4","1","5","7"],"5":["5","2","4","6","8"]\
          ,"6":["6","5","3","9"],"7":["7","4","8"],"8":["8","7","5","9","0"],"9":["9","8","6"],"0":["0","8"]}
  if len(observed)==1:return info[observed]
  return ["".join(i) for i in list(product(*[info[x] for x in observed]))]
