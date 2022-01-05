#find longly integer with freq=1
a= [1,2,3,4,3,2,1] 
#XOR 
def longly_integer(a):
  res=0
  for i in a:
    res =res^i
  return res
longly_integer(a)

#find right most bit of num
#4%2=0 4/2=2 2%2=0 2/2=1 1%2=1 
#divid /base , number right shift by 1 120/10 =12 
#4 =100(2) 4//2 =2 = 10(b) 2//2=1 = 1(b)
#time logn
### if Mask & n ==True
### 0 0 1  ->  0 0 1  -> 0 0 1
### 1 0 0      0 1 0     0 0 1
### 0 0 0      0 0 0     0 0 1
def find_position_of_rightmost_bit(n): #mask =1  || 001
  if n<0:
    return -1
  count =0 
  while (n):
    if n& 1: 
      return count
    n=n>>1
    count+=1
print(find_position_of_rightmost_bit(4))
