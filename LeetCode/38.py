"""
报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n ，输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。

示例 1:
输入: 1
输出: "1"

示例 2:
输入: 4
输出: "1211"
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if (n == 1):
            return "1"

        start = "1"

        for i in range(n - 1):
            num = start
            temp = num[0]
            count = 0
            digits = ""

            l = len(num)
            for j in range(0, l):
                if (num[j] == temp):
                    count = count + 1
                else:
                    digits = digits + str(count)
                    digits = digits + str(temp)
                    temp = num[j]
                    count = 1

            digits = digits + str(count)
            digits = digits + str(temp)

            start = digits
        return digits


s = Solution()

print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
print(s.countAndSay(6))
print(s.countAndSay(7))
print(s.countAndSay(8))
print(s.countAndSay(9))
print(s.countAndSay(10))
print(s.countAndSay(11))

"""
解题思路,部分参考网络.
* 数列初始是1, 使用分段对数字进行计数的方式进行统计.
* 由于数列的第n项是由阅读第n-1项得到的,故此获取第n项数字只需要知道第n-1项数字,然后统计即可,所以循环n-1次
* 拿到数字,将第一位放入temp中开始依次向后判断是否与temp相同,如果相同计数器+1;
* 如果不相同将计数器count的值和temp值依次写入digits的结果内,并且将当前的num[j]放入temp,将计数器count置1
* 继续循环直至将num取完, num取完后, 用当前digits作为初始值,继续统计来获得下一个数字.
"""