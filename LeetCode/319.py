"""
319. 灯泡开关

（如果关闭则开启，如果开启则关闭）。第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。
找出 n 轮后有多少个亮着的灯泡。

示例:
输入: 3
输出: 1

解释:
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭].

你应该返回 1，因为只有一个灯泡还亮着。
"""


class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        # bulbs = [0] * n

        # for i in range(n):
        #     switch = [x for x in range(i, n, i + 1)]
        #     for j in switch:
        #         bulbs[j] = 1 - bulbs[j]
        # return bulbs.count(1)
        return int(n**0.5)


s = Solution()
print(s.bulbSwitch(3))
print(s.bulbSwitch(10))
print(s.bulbSwitch(99999))
"""
此题解法：
* 灯被开关的次数是奇数的才会亮。1-on 2-off 3-on 4-off 5-on 6-off ……
* 然后题意是n盏灯，要经过n轮的操作。
* 那么第n盏灯，经过n轮后会被开关几次？本质上就是看n的因数分解的结果
  比如n=10，那么第1，2，5，10轮都会被操作。
  比如n=100，那么1，2，4，5，10，20，25，50，100轮都会被操作
* 那就是如果1<=k<=n 在第k轮会被开关几次。如果k是完全平方数，就会被操作奇数次，反之就是偶数次
* 那么就是需要知道n中有多少个完全平方数，就有多少灯是亮的。
* 简单的办法就是从1开始计算平方值，看是否<=n，如果是就计数器+1
* 高级的办法就是将n开根号后的整数就是<=n的完全平方数的个数
"""