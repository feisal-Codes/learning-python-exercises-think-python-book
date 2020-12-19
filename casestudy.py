
import string
#write a program that reads a file ,breaks each line into words and removes 
#whitespaces and punctutation


filename='emma.txt'


def read_file(filename):
    hist=dict()
    fp=open(filename)
    for line in fp:
        process_line(line,hist)
    return hist


def process_line(line,hist):
    line= line.replace('-',' ')
    
    for word in line.split():
        word=word.strip( string.whitespace)
        word.lower()
        hist[word]=hist.get(word,0)+1

    
    

hist=read_file(filename)
print(hist)

