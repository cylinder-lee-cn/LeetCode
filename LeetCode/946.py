"""
946. 验证栈序列

给定 pushed 和 popped 两个序列，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，
返回 true；否则，返回 false 。

示例 1：
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

示例 2：
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。

提示：
0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed 是 popped 的排列。
"""


class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        queue = []
        for n in pushed:
            queue.append(n)
            while (queue and queue[-1] == popped[0]):
                queue.pop()
                popped.pop(0)
        # print(queue)
        return len(queue) == 0


s = Solution()
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
"""
此题解法：
* 建立一个空的队列
* 抽取pushed里面的元素，如果queue为空，或者queue尾部元素与popped头部元素不相等，那么就将pushed的元素弹出
  并加入queue
* 反之就是queue不为空而且queue的尾部元素与popped的头部元素相同，那么将queue的尾部元素与popped的头部元素弹出
* pushed元素都用完后，看看queue和逆序的popped是否相同，就知道queue里的能否全部弹出了。

        queue = []

        while (len(pushed) > 0):
            if (len(queue) == 0 or queue[-1] != popped[0]):
                queue.append(pushed.pop(0))
            else:
                queue.pop()
                popped.pop(0)
        return popped == queue[::-1]

* 还有一种写法，是将pushed和popped都遍历一下。
* 看看queue里是否能被全部弹出。
"""
