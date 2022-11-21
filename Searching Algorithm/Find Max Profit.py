# Time Complexity  : O(n)
class Solution:
    def __init__(self):
        pass
    
    
    def findMaxProfit(self, price):
        
        """
        Method Name : findMaxProfit
        Description : This method help to find the max sell of and find out the profit
        Output      : int
        On Failure  : None 
        """
        minPrice = float('inf')
        maxProfit = 0
        for i in range(len(price)):
            if price[i] < minPrice:
                minPrice = price[i]
            elif price[i] - minPrice > maxProfit:
                maxProfit = price[i] - minPrice
                
        return maxProfit
# Driver Code
price = [7,1,5,3,6,4]
s = Solution()
print(s.findMaxProfit(price))