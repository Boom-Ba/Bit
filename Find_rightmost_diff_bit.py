#find the right most different bit
# a=10 b(1010)
# b=14 b(1110) the right most different bit is 3

#when a under mask is equal to b under mask, means a's bit =b's 
#mask left shift 1
def right_most_diff_bit(a,b):
  count=1 
  mask=1
  while a&mask ==b&mask:
    mask=mask<<1
    count+=1
  print(mask)
  return count
right_most_diff_bit(10,14)
#bit masking, mask =1 
#0001 ->1   0001
#1010 ->10  1110
#0000       0000
#left shifting mask(1*2) =2
#0010       1110(b)
#1010       0010(2)
#0010       0010 
#keep left shifting mask =4
#0100  0100
#1010  1110
#0000  0100
