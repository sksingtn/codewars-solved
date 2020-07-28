import re
from collections import defaultdict
from datetime import date
class Inspector:
    def __init__(self):
        self.allowed = []
        self.FRA,self.CAI,self.WRW = False,False,False
        self.criminal = ""
        self.vaccines = defaultdict(set)
        self.countries = ['Arstotzka','Antegria','Impor','Kolechia','Obristan','Republia','United Federation']
    def receive_bulletin(self,str):
        for line in str.split("\n"):
            line = line.strip()
            if "Allow citizens" in line:
                self.allowed.extend(map(lambda x:x.strip(),re.findall(r'(?<=.{18})([a-zA-Z ]+)',line)))
            elif "Deny citizens" in line:
                self.deny = list(map(lambda x:x.strip(),re.findall(r'(?<=.{17})([a-zA-Z ]+)',line)))
                self.allowed = [x for x in self.allowed if x not in self.deny]
            elif line == "Foreigners require access permit":self.FRA = True
            elif line == "Citizens of Arstotzka require ID card":self.CAI = True
            elif line == "Workers require work pass":self.WRW = True
            elif "Wanted" in line:self.criminal = line[21:]
            elif re.match(r'^Citizens of .*?(?<!no longer )require.*?vaccination$',line) != None:
                self.v = re.search(r'require (.*) vaccination',line).group(1)
                self.c = [x.strip() for x in re.search(r'Citizens of (.*) require',line).group(1).split(",")]
                for x in self.c:
                    self.vaccines[x].add(self.v)
            elif re.match(r'^Citizens of .*? longer require.*?vaccination$',line) != None:
                self.v = re.search(r'require (.*) vaccination',line).group(1)
                self.c = [x.strip() for x in re.search(r'Citizens of (.*) no longer require',line).group(1).split(",")]
                for  x in self.c:
                    self.vaccines[x].remove(self.v)
            elif re.match(r'Foreigners( no longer)? require(.*?)vaccination',line) != None:
                self.v = re.search(r'require(.*?)vaccination',line).group(1).strip()
                if "no longer" in line:
                    for x in self.countries:
                        if x != 'Arstotzka':
                            self.vaccines[x].remove(self.v)
                else:
                    for x in self.countries:
                        if x != 'Arstotzka':
                            self.vaccines[x].add(self.v)
            elif re.match(r'Entrants( no longer)? require(.*?)vaccination',line) != None:
                self.v = re.search(r'require(.*?)vaccination',line).group(1).strip()
                if "no longer " in line:
                    for x in self.countries:
                        self.vaccines[x].remove(self.v)
                else:
                    for x in self.countries:
                        self.vaccines[x].add(self.v)


    def inspect(self,papers):
        self.error = {"NATION":"nationality","ID#":"ID number","NAME":"name","DOB":"date of birth"}
        self.documents = defaultdict(dict)
        for paper,info in papers.items():
            self.documents[paper] = {x.split(":")[0].strip():x.split(":")[1].strip() for x in info.split("\n")}
        for x in self.documents:
            self.a,self.b = self.documents.get(x).get("NAME").split(",")
            if self.criminal == self.b.strip()+" "+self.a.strip():
                return "Detainment: Entrant is a wanted criminal."
        self.keys = {y for x in self.documents for y in self.documents[x] if y!= "EXP"}
        for x in self.keys:
            self.unique = set()
            for d in self.documents:
                if self.documents[d].get(x,None) != None:
                    self.unique.add(self.documents[d].get(x,None))
            if len(self.unique) != 1:
                return "Detainment: "+str(self.error[x])+" mismatch."
        if self.documents.get("passport",None) == None:
            return 'Entry denied: missing required passport.'
        if self.documents.get("passport").get("NATION") not in self.allowed:
            return "Entry denied: citizen of banned nation."
        self.last_date = date(1982,11,22)
        for x in self.documents:
            if self.documents.get(x).get("EXP",None) != None:
                self.expire = date(*[int(x) for x in self.documents.get(x).get("EXP").split(".")])
                if self.expire<=self.last_date:
                    return "Entry denied: "+str(x).replace("_"," ")+" expired."
        if self.CAI == True and self.documents.get('passport').get('NATION') == 'Arstotzka' and self.documents.get("ID_card",None) == None:
            return "Entry denied: missing required ID card."
        if self.WRW == True:
            if "access_permit" in self.documents.keys() and self.documents.get("access_permit").get("PURPOSE") == "WORK" and "work_pass" not in self.documents:
                return "Entry denied: missing required work pass."
        if self.FRA == True:
            if (self.documents.get("passport").get("NATION") != 'Arstotzka') and ("access_permit" not in self.documents) and ("grant_of_asylum" not in self.documents) and ("diplomatic_authorization" not in self.documents):
                return "Entry denied: missing required access permit."
            elif (self.documents.get("passport").get("NATION") != 'Arstotzka') and ("diplomatic_authorization" in self.documents) and ('Arstotzka' not in self.documents.get("diplomatic_authorization").get("ACCESS")):
                return "Entry denied: invalid diplomatic authorization."
        self.cou = self.documents.get("passport").get("NATION")
        if self.cou in self.vaccines and len(self.vaccines[self.cou]) != 0:
            if "certificate_of_vaccination" not in self.documents:
                return "Entry denied: missing required certificate of vaccination."
            else:
                for x in self.vaccines[self.cou]:
                    if x not in self.documents.get("certificate_of_vaccination").get("VACCINES"):
                        return "Entry denied: missing required vaccination."
        if self.documents.get("passport").get("NATION") == 'Arstotzka':
            return "Glory to Arstotzka."
        return "Cause no trouble."
