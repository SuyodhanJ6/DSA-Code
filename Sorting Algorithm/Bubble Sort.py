# Time Complexity : O(n^2)
# In Bubble Sort we are comparing value with other and last element is always highest.skip last element.

class Solution:
    def __init__(self):
        pass
    
    def bubbleSort(self, arr):
        """
        Method Name  : bubbleSort
        Description  : this method help sort the element in the arr.
        OutPut       : array
        On Failure   : None
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
# Driver Code
arr = [20,10,30,5]
s = Solution()
print(s.bubbleSort(arr))