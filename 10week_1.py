def isEven( n) :
 
    # n^1 is n+1, then even, else odd
    if (n ^ 1 == n + 1) :
        return True;
    else :
        return False;
 
# Driver code
if __name__ == "__main__" :
    n = 100;
    print("Even") if isEven(n) else print( "Odd");
