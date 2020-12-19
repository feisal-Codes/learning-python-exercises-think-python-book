
import math
#method to perfom addition of all items in a list / in a nested list
def nested_sum(t):
    total=0
    for s in range (len(t)):
        if isinstance (t[s],(list,tuple)):
          cumsum(t[s])
          for r in range (len(t[s])):
              
              total+=t[s][r]
              
        else:
           total+=t[s]
    return total 
    

mylist=[1,2,3,4,]
r=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#np.cumsum(t)
#method to perfom cumlative addition of items in a list
def cumsum(t):
   total=0
   sums=[]
   for v in t:
     total = total + v
     sums.append(total)
   print(sums)
#cumsum(r[0])
#nested_sum(r)
#method to return middle items in a list
def midlle(l):
    return l[1:-1]

#print(midlle(r))
#method to sort items in a list
def is_sorted(stuff):   
    for i in range(1,len(stuff)):
        if stuff[i - 1] > stuff[i]:
           return False
    return True
#print(is_sorted([1,2,3,8]))
#method to compute anagram words 
def is_anagram(string1,string2):
    fw= list(string1)
    sc=list(string2)
    fw.sort()
    sc.sort()
    while ' ' in sc or fw:
      if ' ' in sc:
        sc.remove(' ')
        
      elif ' ' in fw:
        fw.remove(' ')
      else:
        break
    
    
    if fw==sc:

      return True
  
    return  False

#print(is_anagram('dormitory','dirty room'))


#Write a function called has_duplicates that takes a list and returns True if there
#is any element that appears more than once. It should not modify the original list.

def has_duplicates(l):
  mylist=[]
  mylist=l[:]

  for i in range(len(mylist)-1):
    if mylist.count(mylist[i])>1:
      return True
  return False


print(has_duplicates('mzrayetnqwa'))







board=['0','1','2','3','4','5','6','7','8']
turn= True


def printBoard(board):
    print(board[0]+'|'+board[1]+'|'+board[2]+'|')
    print('------')
    print(board[3]+'|'+board[4]+'|'+board[5]+'|')
    print('------')
    print(board[6]+'|'+board[7]+'|'+board[8]+'|')
    print('------')



def playerTurn(board):
  global turn
  printBoard(board)
  while True:
    if turn:
     print('Player x to select a move')
     move=int(input()) 
     #if board[move] =='x' or board[move] =='0':
         #print('Slot Already Occupied')
     #else:
     board[move]=='0'

     
     printBoard(board)
     turn=False
     
    if turn==False:
     print('Player 0 to select a move')
     move=int(input()) 
     #if board[move] =='x' or board[move] =='0':
         #print('Slot Already Occupied')
     #else:
     board[move]=='0'
     printBoard(board)
     turn=True
     


    










playerTurn(board)





























 

















































































