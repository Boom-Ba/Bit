#16-10000 --1 bit shift to right -1000
#19-10011 
#common bits is 100 = 4
def find_bitwise_and_in_a_range(m,n):
  count= 0
  while m!=n:
    m =m>>1
    n =n>>1 
    count+=1
  # m==4, and right shift twice, so the res should shift back to left twice
  return m<<count
find_bitwise_and_in_a_range(16,19) 
