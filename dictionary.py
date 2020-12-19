def histograms(s):
    mydict= dict()
    for c in s:
       mydict[c]=s.count(c)
       
    return mydict

#print(histograms('feisal mohamed')) 
#traversing through a dictionary and printing each value 

def print_hist(s):
    for i in sorted(s):
        print(i,s[i])

#print_hist(h)

#lookup in a dictionary

def reverse_lookup(w,v):
    for key in w:
        if w[key]==v:
            return key
    raise LookupError('Value not in dictionary')    


h=histograms('parrot')
#key=reverse_lookup(h,2)
#print(key)

#forward lookUp
#takes a dictionary and and a key  


def inverse(d):
    inverse={}
    for key in d:
        val=d[key]
        if val  not in inverse:
            inverse[val]=[key]
        else:
            inverse[val].append(key)
    return inverse

#values=inverse(h)
#print(values)
#Read the documentation of the dictionary method setdefault and use it to write a
#more concise version of invert_dict .

def inversse(d):
    inverse={}
    for key in d:
        val=d[key]
        inverse.setdefault(val,[]).append(key)
    
    return inverse

#values=inversse(h)
#print(values)
#Memoize the Ackermann function from Exercise 6.2 and see if memoization
#makes it possible to evaluate the function with bigger arguments

cache = {}

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)

    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]


#print(ackermann(3, 4))
#print(ackermann(3, 6))

#Write a function called has_duplicates 
#is any element that appears more than once. It should not modify the original list.

def has_duplicates(l):
  d={}
  for i in l:
      if i in d:
          return True
      d[i]=True
      
  return False


#l=['a','b','c','d']
#mylist=has_duplicates(l)
#print(mylist)
#l.append('a')
#mynewlist=has_duplicates(l)
#print(mynewlist)
















































































