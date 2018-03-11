f =  open('sorted2.txt')
wordlist=[]
for l in f.readlines():
    l = l.strip()
    if l.isalpha() and len(l)>=3 and len(l)<=8:
        wordlist+=[l]
import random as random

random.seed(0)
randomchars=[]
for i in range(60):
    randomchars+=[str(unichr(random.randint(97,122)))]

#process words
#sort and hash
#wordsdict
wd={}
for w in wordlist:
    w2 = list(w)
    w2=sorted(w2)
    w3 = ''.join(w2)
    wd[w3]=w
    #print w3,w    

#process our letters
#start with 8 letters

import itertools
#for x in itertools.combinations(randomchars,8):
#    #print list(x)
#    x = sorted(list(x))
#    x = ''.join(x)
#    if x in wd:
#        print wd[x]

def nextword(char_list):    
    for i in range(8,3,-1):
        for x in itertools.combinations(char_list,i):
            x = sorted(list(x))
            x = ''.join(x)
            if x in wd:
                return wd[x]
    return None 

def bestwords(char_list):
    wordlist=[]
    while(1):
        n = nextword(char_list)
        if n == None:
            return (wordlist,char_list)
            break
        else:
            wordlist+=[n]
        r=''.join(char_list)
        for x in list(n):
            r=r.replace(x,'',1)
        char_list=list(r)
        #print char_list

#print nextword(list('star')) 

#letters=raw_input("letters:")
#x=bestwords(list(letters))
#while(1):
#    newletters = raw_input("more?:")
#    letters+=newletters
#    bestwords(list(letters))


def gameloop():
    letters=raw_input("letters:")
    #x=bestwords(list(letters))
    
def gamesetup():
    pass
def main():
    pass





import sys
if len(sys.argv) > 1:
    print bestwords(list(sys.argv[1]))[0]
    print nextword(list(sys.argv[1]))
else:
    gamesetup()
    gameloop()
    