"""
412. Fizz Buzz

写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：
n = 15,
返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        fb = ''
        l = []

        for i in range(1, n + 1):
            is3 = (i % 3 == 0)
            is5 = (i % 5 == 0)
            if (is3 and is5):
                fb = 'FizzBuzz'
            if (is3 and not is5):
                fb = 'Fizz'
            if (is5 and not is3):
                fb = 'Buzz'
            if (not is3 and not is5):
                fb = str(i)
            l.append(fb)
        return l


s = Solution()
print(s.fizzBuzz(15))
