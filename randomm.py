import random
import string

def read_file(s):
    hist=dict()
    fp=open(filename)
    for line in fp:
        process_line(line,hist)
    return hist





def make_hist(s):
    hist=dict()
    for line in s:
        hist[line]=hist.get(line,0)+1
    
    return hist


def process_line(line,hist):
     line=line.replace('-',' ')
     for word in line.split():
         word=word.strip(string.whitespace)
         word=word.lower()
         hist[word]=hist.get(word,0)+1
    

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)


def choose_random(hist):
        values=[]
        for v in hist.values():
            values+=[v]
        guess=random.choice(list(hist))
        key=hist[guess]
        sol=str(key)+'/'+str(len(values))
        return sol
            
def most_common(hist):
    t=[]
    for key,value in hist.items():
        t.append((value,key))
    t.sort(reverse=True)
    return t
        

#s=['a','b','c','d','a','a','b']
#hist=make_hist(s)
#guess=choose_random(hist)
#print(guess)
filename='emma.txt'
nw=read_file(filename)
print('the total words are:'+str(total_words(nw)))
print('the total unique words:'+str(different_words(nw)))

#t=most_common(nw)
#guess2=choose_random(nw)
#print(guess2)
#print('the most common words are: ')
#for freq,word in t:
 #   print(word,freq,sep='\t')
      

