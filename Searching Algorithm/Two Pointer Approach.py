# Time Complexity  : O(n)
# Greedy Algorithm
class Solution:
    """
    This class help to find the solution.
    """
    def addTwoValue(self, arr, target):
        """
        Method Name : maximumDifference
        Description : This function help to find out the max diff between highest num and lowest num.
                        but condition is j > i
        Output      : int 
        On Failure  : None
        """
        l = 0
        r = len(arr)-1
        
        while l <= r:
            if arr[l] + arr[r] == target:
                return (arr[l], arr[r])
            elif arr[l] + arr[r] > target:
                r -= 1
            else:
                l += 1
                
# Driver Code
arr = [20, 40,60,80,90, 120,240]
target = 210
s = Solution()
print(s.addTwoValue(arr, target))