# Implementation of Binary search using recursion
class Solution:
    def __init__(self):
        pass
    
    
    def binarySearchIterativeSearch(self, arr, i, j, x):
        
        """
        Method Name : binarySearchIterativeSearch
        Description : using iteration we will search values in the array.
        Output      : Index of Element
        On Failure  : None 
        """
        
        while i <= j:
            mid = i + (j-i) // 2
            """
                we can use also mid = (i+j) //2 
                for Avoiding Overflow Conditions...
            """
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                # Recursively call
                i = mid + 1
            else:
                # Recursively call
                j  = mid - 1
        return -1 

# Driver Code
arr = [1,2,3,4,5]
s = Solution()
n = len(arr)
i = 0
j = n-1
x = 8
result = s.binarySearchIterativeSearch(arr, i, j, x)
print(f'Position of this values is {result}')