#given a range (M,N) =(2,5) inclusive, find bitwise AND
#res= 2&3&4&5 
#Bitwise and returns 0 if bit flips happen (bits contains 1 and 0 at position)
#if a column never flipped, the value should be copied directly 

M =13
N =16
##observation: when there is a new bit add to the leftmost
##all its right bits got flipped as well 
#  0000 - 0
#  0001 -1
#  0010 -2
#  0011 -3
## thid bit got flipped from 0 to 1, all right bits also flipped to 0
#  0100 -4
#  0101 -5
#  0110 -6
#  0111 -7
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
