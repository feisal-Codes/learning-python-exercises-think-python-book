import math
#import random



def mysqr(a):
 x=a+1
 
 while True:
    y = (x + a/x) / 2
    if y == x:

        return x
    x = y
    
def test_square_root(a):
    if mysqr(a)>math.sqrt(a):
      diff=mysqr(a)-math.sqrt(a)
    elif mysqr(a)<math.sqrt(a):
      diff=math.sqrt(a)-mysqr(a)
    else:
      diff=mysqr(a)-math.sqrt(a)
    
    print(float(a),mysqr(a),math.sqrt(a),diff)

#print( 'a '+'\tmysqr(a)'+'\tmath.sqrt(a)'+'\t''diff')
#print('---'+'\t..........\t...........\t\t..........')
#for i in range(1,10):
  # test_square_root(i)

def eval_loops():
  while True:
    userr=input("enter a number to evaluate:otherwise enter done to quit\n")
    
    if userr == 'done':
        return eval
    
    else:
      print(eval(userr))
      
#eval_loops()

def traversal(s):
   #length=len(s)
   #i=1
   #while i < length:
       
        
    #   lastletter= s[-i] 
     #  print(lastletter)
      # if i == length-1:
       #    print(s[0])

       #i+=1
   for letter in s:
     print (letter)
#traversal('feisal')

prefix='JKLMNOPQ'
suffix='ack'
sp='uack'

#for letter in prefix:
  #if letter != 'Q':
  #  print(letter + suffix)
#rint(prefix[-1]+ sp)

#search
def find(word,letter,index):
  
  while index < len(word):
    if word[index]==letter:
      print(index)
      return index
    index +=1
  return -1



#find('this is my book my book','s',0)
#count

def countt(word,myletter):
  count=0
  for letter in word:
    if letter == myletter:
      count+=1
  print(count)

#countt('feisal mohamed ibrahim ','m')


#def any_lowercase(s):
  #flag=False
  #for c in s:
    #if  c.islower():
      #return True
    #elif c.isupper():
      
    #else:
      #return False
    
  
  
#print(any_lowercase('FEISAL'))
#Caeser Cipher

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
word='cheer'
word = word.upper()
newletter=''
key=7
mode='encrypt'


for letter in word:   
  if letter in alphabet: 
    indexx=alphabet.find(letter)
    if mode =='encrypt': 
           step=indexx+key
    elif mode=='decrypt':
          step=indexx-key
    
    if step>=len(alphabet):
       step= step - len(alphabet)
    elif step < 0:
      step=step + len(alphabet)
    newletter+=alphabet[step]
print(newletter)
    





























































