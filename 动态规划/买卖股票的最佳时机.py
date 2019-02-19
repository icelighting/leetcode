'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ### 思路 ：套用两次循环肯定不行
        # 其实就是要找到最小与最大的差值
        if not prices:
            return 0
        profit = 0
        for i in range(len(prices)):
            mimum = min(prices[:i+1])
            idx = prices.index(mimum)
            mamum = max(prices[idx:i+1])
            profit = max(mamum-mimum, profit)

        return profit
if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    prices2 = [1,2]
    solute = Solution()
    print(solute.maxProfit(prices))
