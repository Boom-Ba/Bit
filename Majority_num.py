##majority element 
##approach: bit masking 

A =[2,3,4,3,3]
B =[3,3,4,2,4,4,2,4,4]
C=[2,2,3,3,4,4]
#find ele that appears more n//2 times
#above example, has n=5, so a majority number must appears >2 times 
def majority_number(B):
  max_count =len(B)//2
  index=-1
  for i in range(len(B)):
    #get counts for each element
    count=0
    
    for j in range(len(B)):
      if B[i] ==B[j]:
        count+=1
      #to be a majority number, its occurence must appear more than N//2 times
      if count>max_count:
        max_count=count
        index=i
  return B[index] if index!=-1 else -1
majority_number(C)
