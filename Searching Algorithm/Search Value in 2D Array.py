# Time Complexity O(log(m*n))
class Solution:
    """
    This class help to find the solution.
    """
    def search2DArray(self,arr,target):
        """
        Method Name : search2DArray
        Description : This function help to find out the value in 2D array.
        Output      : boolean
        On Failure  : None
        """
        # Row
        m = len(arr) 
        # Edge Case
        if m == 0:
            return False
        # Columns
        n = len(arr[0])
        left, right = 0, m*n - 1
        while left <= right:
            mid = left + (right  - left) // 2   
            # Row number mid // n
            # Column number mid%n
            mid_element = arr[mid//n][mid%n]
            if mid_element == target:
                return True
            elif target < mid_element:
                right  =mid- 1
            else:
                left = mid+1 
        return False
# Driver Code
arr = [[1,3,5,7],[10,11,16,20], [23,30,34,60]]
target = 300
s = Solution()
print(s.search2DArray(arr, target))
