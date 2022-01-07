##toggle bits given num: 25 =b(11001)
##want to toggel bits 11001 between index=2 and 4
         #             r  l
                   #->10111
def toggle_bits(n,l,r):
  #toggle bits between l and r
  #mask=1, n=25,
  mask=1
  value =0 
  power=0 
  i=1
  while i<l:
    #not in the range yet, 
    if mask&n==1: #1 bit
      value+=2^power
    mask=mask<<1
    power+=1
    i+=1
  #i ==l in the range now
  while i<=r:
    if not mask&n==1: #1 bit
      value+=2^power
    mask=mask<<1
    power+=1
    i+=1
  #i>r, not in the range now
  while i<=10:
    if mask&n==1: #1 bit
      value+=2^power
    mask=mask<<1
    power+=1
    i+=1
  return value
toggle_bits(25,2,4)
