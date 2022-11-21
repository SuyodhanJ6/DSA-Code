# Time Complexity  : O(log3N)
# Binary Search    : O(log2N)
# Most Optimized is Ternary higher base lowe value --> Constant in a danger zone
# https://www.youtube.com/watch?v=alpGaebSZFk

class Solution:
    def __init__(self):
        pass
    
    def ternarySearch(self, arr, i, j,key):
        """
        Method Name   : ternarySearch
        Description   : this function help to finding element in the array. we are dividing arry
                        in three parts.
        Output        : int
        On Failure    : None
        """
        mid1 = i + (j-i)//3
        mid2 = j - (j-i)//3
        while i <= j:
            if arr[mid1] == key:
                return mid1
            elif arr[mid2] == key:
                return mid2
            elif key < arr[mid1]:
                # Recursively call
                return self.ternarySearch(arr, i, mid1-1, key)
            elif key > arr[mid2]:
                # Recursively call
                return self.ternarySearch(arr, j, mid2+1, key)
            else:
                # Checking middle part
                # Recursively call
                return self.ternarySearch(arr, mid1, mid2, key)
            
        return -1
    
# Driver Code
arr = [20,25,47,56,59,63,65,79,82]
i = 0
j = len(arr)-1
key = int(input('Enter number to be found: '))
s = Solution()
print(s.ternarySearch(arr, i, j, key))