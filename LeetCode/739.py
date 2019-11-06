"""
739. 每日温度

根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高的天数。
如果之后都不会升高，请输入 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的都是 [30, 100] 范围内的整数。
"""


class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # def days(t, i, t_l):
        #     d = 0
        #     if (t == 100):
        #         return 0

        #     if (i == temperatures_l):
        #         return 0

        #     for j in range(i + 1, t_l):
        #         if (temperatures[j] > t):
        #             return j - i
        #     return d

        # temperatures_l = len(temperatures)
        # result = []
        # for i, t in enumerate(temperatures):
        #     result.append(days(t, i, temperatures_l))

        # return result
        t_l = len(temperatures)
        stack = []
        result = [0] * t_l

        for i in range(t_l):
            while (len(stack) > 0
                   and temperatures[i] > temperatures[stack[-1]]):
                position = stack.pop()
                result[position] = i - position
            stack.append(i)
        return result


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# print(s.dailyTemperatures([73]))
"""
此题解法：
* 暴力比较法：遍历数组，取每一个温度，然后和这个元素后续的元素们进行比较，一旦找到比它大的就返回对应的索引。
  效率较低，最后超时。

* 利用栈来存放一个递减的温度序列，这样就可以找到对应增加的。
1 先初始化一个位置列表，长度与temperatures一致，默认值为0
2 在初始化一个stack来存放递减的温度元素下标
3 遍历温度列表，如果stack为空，或当前温度低于stack末尾的温度，那么将当前温度索引添加到stack中
4 重复（如果stack不为空，而且当前温度高于stack末尾的温度，取出末尾的温度索引，
  并将对应位置的值修改为i-postion（这就是升温与之前温度的索引差，就是天数）
"""
