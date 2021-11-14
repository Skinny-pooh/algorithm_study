x = 32;
 
# tOGGLE cASE = swaps CAPS to lower
# case and lower case to CAPS
def toggleCase(a):
 
    for i in range(len(a)):
 
        # Bitwise EXOR with 32
        a = a[:i] + chr(ord(a[i]) ^ 32) + a[i + 1:];
    return a;
 
# Driver Code
str = "CheRrY";
print("Toggle case: ", end = "");
str = toggleCase(str);
print(str);
 
print("Original string: ", end = "");
str = toggleCase(str);
print(str);
