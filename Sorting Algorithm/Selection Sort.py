# Time Complexity  : O(n^2)
# In selection sort we finding min value and changing index and skipping first element in arr.
class Solution:
    def __init__(self):
        pass
    
    def selectionSort(self, arr):
        """
        Method Name   : selectionSort
        Description   : This method help to sort the element in the array.
        OutPut        : array
        On Failure    : None
        """
        
        n = len(arr)
        for i in range(n):
            minIndex = i
            for j in range(i+1, n):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            # Swapping 
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr
# Driver Code
arr = [70, 56, 23, 19, 25, 37, 48]
s = Solution()
print(s.selectionSort(arr))