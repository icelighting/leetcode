'''  给定两个以字符串形式表示的非负整数 num1 和 num2，
返回 num1 和 num2 的乘积
，它们的乘积也表示为字符串形式。'''

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ##num1 = float(num1)## float  存在精度丢失,而 Int 不会,所以用int 不会把错误放大
        num1= int(num1)
        print(num1)
        num2 = int(num2)
        print(num2)
        num = num1 * num2##float 会存在精度丢失问题  对于特别大的数 因为float的范围是 2**128
        print(num)
        lit = list(str(num))
        numlist = "".join(lit)
        return numlist


if __name__ == '__main__':
    num1 = "123456789"

    num2 = "987654321"
    solute = Solution()
    print(solute.multiply(num1, num2))

