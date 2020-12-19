def countdown(n):
    if n <= 0:
        print("blastOff")
    else:
        print(n)
        countdown(n-1)
#countdown(3)

def print_n(s,n):
    if n<=0:
        return
    name()
    print_n(name,n-1) 

def name():
    print('my name is feisal')

#print_n(name,5)

def fermat(a,b,c,n):
    if n>2:
        if (a**n + b**n)== c**n:
           print('fermat wa wrong')
        else:
            print('no ,that doesnt work')
       
    
    else:
      print("enter value of n greater than 2")

def is_triangle(a,b,c):
     if a + b >= c :
         print("yes ,they do")
     else:
         print("no")
    






def myf():
    a=int(input("enter value for a\n"))
    b=int(input("enter value for b\n"))
    c=int(input("enter value for c\n"))
    #n=int(input("enter value for n\n"))
    #fermat(a,b,c,n)
    is_triangle(a,b,c)

#myf()

#recursion
def recurse(n,s):
    print(n,s)
    if n==0:
        print(s)
    else:
        recurse(n-1,n+s)
recurse(3,0)






































    