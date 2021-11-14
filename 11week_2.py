 
def findElement(arr, n):
 
    # leftMax[i] stores maximum of arr[0..i-1]
    leftMax = [None] * n
    leftMax[0] = arr[0]
 
    # Fill leftMax[]1..n-1]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], arr[i-1])
 
    # Initialize minimum from right
    rightMin = [None]*n
    rightMin[n-1] = arr[n-1]
 
    # Fill rightMin
    for i in range(n-2, -1, -1):
        rightMin[i] = min(rightMin[i+1], arr[i])
    # Traverse array from right
    for i in range(1, n-1):
 
        # Check if we found a required element
        # for ith element, it should be more than maximum of of array
        # elements [0....i-1] and should be less than the minimum of
        # [i+1.....n-1] array elements
        if leftMax[i-1] <= arr[i] and arr[i] <= rightMin[i+1]:
            return i
 
    # If there was no element matching criteria
    return -1
 
 
# Driver program
if __name__ == "__main__":
 
    arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    n = len(arr)
    print("Index of the element is", findElement(arr, n))
