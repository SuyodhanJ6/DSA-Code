# Implementation of Binary search using recursion
# Time Complexity : O(LogN  )
class Solution:
    def __init__(self):
        pass
    def binarySearchRecursionSearch(self, arr, i, j, x):
        
        """
        we can use also mid = (i+j) //2 
        for Avoiding Overflow Conditions...
        """
        
        if i == j:
            if arr[i] == x:
                return i 
            else:
                return -1
        else:
            mid = i + (j-i) // 2
            print(mid)
            """
                we can use also mid = (i+j) //2 
                for Avoiding Overflow Conditions...
            """
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                # Recursively call
                return self.binarySearchRecursionSearch(arr, mid+1, j, x)
            else:
                # Recursively call
                return self.binarySearchRecursionSearch(arr, i, mid-1, x )

# Driver Code
arr = [1,2,3,4,5]
s = Solution()
n = len(arr)
i = 0
j = n-1
x = 5
result = s.binarySearchRecursionSearch(arr, i, j, x)
print(f'Position of this values is {result}')