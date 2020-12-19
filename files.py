
import string

def sed(ps,rs,file1,file2):
     
    fp=open(file1,'r')
    fp2=open(file2,'w')

     
    for line in fp:
          #for word in line.split():
          #line.strip(string.whitespace)
          #print(fp)
    
          line=line.replace(ps,rs)
          fp2.write(line)
          
    fp.close()
    fp2.close()
     
    
    
f1='file1.txt'
f2='file2.txt'

sed('python','java',f1,f2)

