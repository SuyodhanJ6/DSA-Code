# Time Complexity  : O(n^2)
class Solution:
    def __init__(self):
        pass
    
    def insertionSort(self, arr):
        """
        Method Name   : insertionSort
        Description   : This method help to sort the element in the array.
        OutPut        : array
        On Failure    : None
        """
        for i in range(1, len(arr)):
            j = i - 1 # Starting index j = 0 and i = 1
            key  = arr[i] 
            
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
            
        return arr
                
# Driver Code4

arr = [12,21,2]
s = Solution()
print(s.insertionSort(arr))        