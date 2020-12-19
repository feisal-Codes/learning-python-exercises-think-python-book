def make_histogram(s):
    """Make a map from letters to number of times they appear in s.

    s: string

    Returns: map from letter to frequency
    """
    hist={}
    for x in s:
      hist[x] = hist.get(x, 0) + 1

              

    return hist

#print(make_histogram('feisal'))

def most_frequent(s):
 
  """Sorts the letters in s in reverse order of frequency.

    s: string

    Returns: list of letters
  """
 
  hist=make_histogram(s)
  t=[]
  for x,freq in hist.items():
    t.append((freq,x))
  t.sort(reverse=True)
  res=[]
  for freq,x in res:
       res.append(x)
  return t


def read_file(filename):

   """Returns the contents of a file as a string."""
   return open(filename).read()

if __name__ =='__main__':
    string=read_file('emma.txt')
    letters=most_frequent(string)
    for x in letters:
      print(x)
