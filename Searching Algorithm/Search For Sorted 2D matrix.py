class Solution:
    def __init__(self):
        pass
    
    def searchElementInSorted2DMatrix(self, matrix, target):
    
        """
        Method Name : searchElementInSorted2DMatrix
        Description : Using Row and Col we check the element is present or not 
                        we are only using one loop so 
                        Time Complexity : O(N)
        OutPut      : Boolean
        On Failure  : None
        """
        n = len(matrix)
        row = 0
        col = len(matrix[0]) - 1
        while (row < n) and (col >= 0):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
    
# Drive Code
arr = [[3, 12, 9], [5, 2, 89], [90, 45, 22]]
target = 55
s = Solution()
result = s.searchElementInSorted2DMatrix(arr, target)
print(result)
            