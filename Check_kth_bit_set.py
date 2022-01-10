 ##check if current bit is set
 #set means the value of kth position is 1
# bin(52)=0b110100 the 3rd position is a set, because it is '1'
##method 1
def check_Kth_bit(n,k):
  i =0
  mask =1
  mask<<=k-1
  if n&mask:
    return True
  return False
check_Kth_bit(52,3)
