import math
 
# function to find the position
# of rightmost set bit
def getPosOfRightmostSetBit(n):
 
    return int(math.log2(n&-n)+1)
 
  
def setRightmostUnsetBit(n):
 
    # if n = 0, return 1
    if (n == 0):
        return 1
      
    # if all bits of 'n' are set
    if ((n & (n + 1)) == 0):   
        return n
      
    # position of rightmost unset bit in 'n'
    # passing ~n as argument
    pos = getPosOfRightmostSetBit(~n)   
      
    # set the bit at position 'pos'
    return ((1 << (pos - 1)) | n)
 
# Driver code
 
n = 21
print(setRightmostUnsetBit(n))
