import sys
import random as random
import itertools


#globals
wordlist=[]
randomchars=[]
wd={}
ranklist={}
#globals

def read_wordfile(wordfile):
    global wordlist
    global wd
    f =  open(wordfile)

    for l in f.readlines():
        l = l.strip()
        for c in l:
            if ord(c) > 122 or ord(c)<97:
                continue
        if len(l)>=3 and len(l)<=8:
            wordlist+=[l]

    for w in wordlist:
        w2 = list(w)
        w2=sorted(w2)
        w3 = ''.join(w2)
        if w3 in wd:
            rankcurrent=getrank(wd[w3])
            ranknew=getrank(w)
            if ranknew>rankcurrent:
                wd[w3]=w    
        else:
            wd[w3]=w

def getrank(w):
    if w in ranklist:
        return ranklist[w]
    return 99999

def randomchars(n):
    random.seed(0)
    for i in range(n):
        randomchars+=[str(chr(random.randint(97,122)))]

  
def nextword(char_list):    
    for i in range(8,3,-1):
        for x in itertools.combinations(char_list,i):
            x = sorted(list(x))
            x = ''.join(x)
            if x in wd:
                return wd[x]

    return None 

def allwords(char_list):
    found=[]
    for i in range(8,3,-1):
        for x in itertools.combinations(char_list,i):
            x = sorted(list(x))
            x = ''.join(x)
            if x in wd and wd[x] not in found:
                found+=[wd[x]]
    return found


def topnwords(char_list,l,n):
    found=[]
    for x in itertools.combinations(char_list,l):
        x = sorted(list(x))
        x = ''.join(x)
        if x in wd and wd[x] not in found:
            found+=[wd[x]]
    found = sorted(found,key=getrank)
    return found[:n]

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


    
def gamesetup():
    letters=input("letters:")
    return list(letters)

def recommendwords(letters):
    words=[]
    for n in range(4):
        m=topnwords(letters,8-n,2)
        words+=m
    for i in range(len(words)):
        print(i+1,words[i])
    chosenword=words[int(input("whichword? "))-1]

    r=''.join(letters)
    for x in list(chosenword):
        r=r.replace(x,'',1)
    letters=list(r)
    return letters

def readranklist():
    #return a mapping of word to rank
    global ranklist
    f = open('wiki-100k.txt',encoding='utf-8')
    rank=0
    for l in f.readlines():
        l=l.strip()
        #print(l)
        if l[0]=='#' or len(l)<3:
            continue
        for c in l:
            if ord(c) > 122 or ord(c)<97:
                continue
        if l not in ranklist:
            ranklist[l]=rank
            rank+=1 
    print(ranklist['apple'])




readranklist()
read_wordfile('words_umich.txt')
if len(sys.argv) > 1:
    #print(bestwords(list(sys.argv[1]))[0])
    #print(nextword(list(sys.argv[1])))
    #print(allwords(list(sys.argv[1])))
    print(topnwords(list(sys.argv[1]),5,5))
    x=topnwords(list(sys.argv[1]),5,5)
    print(x[2]==x[3])

else:
    letters=gamesetup()
    while(1): #gameloop
        letters = recommendwords(letters)
        letters += input("new letters? ")

    