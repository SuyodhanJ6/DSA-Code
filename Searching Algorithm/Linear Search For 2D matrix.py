from pdb import line_prefix


class Solution:
    def __init__(self):
        pass
    
    def linearSearchFor2DMatrix(self, arr, target):
        """
        Method Name : linearSearchFor2DMatrix
        Description : this method direct search the element in the matrix 
                        Time Complexity : O(n^2)
        OutPut      : index of matrix
        On Failure  : None
        
        """
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if (arr[i][j]) == target:
                    return [i, j]
        return [-1, -1]
    
arr = [[3, 12, 9], [5, 2, 89], [90, 45, 22]]
target = 89
s = Solution()
result = s.linearSearchFor2DMatrix(arr, target)
print(result)