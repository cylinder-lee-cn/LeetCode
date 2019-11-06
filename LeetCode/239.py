"""
239. 滑动窗口最大值

给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

进阶：
你能在线性时间复杂度内解决此题吗？
"""

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        numLen = len(nums)
        if numLen == 0 or k == 1:
            return nums

        if k == numLen:
            return [max(nums)]

        result = []
        temp = nums[0:k]
        maxNum = max(temp)
        result.append(maxNum)

        for j in range(k, numLen):
            h = nums[j]
            t = temp.pop(0)
            temp.append(h)

            if h > maxNum:
                maxNum = h
            elif t == maxNum:
                maxNum = max(temp)

            result.append(maxNum)

        return result


s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 0))
"""
此题解法：
* 首先要排除掉几种特殊情况，nums长度为0，和k长度为1，都返回nums自身
* nums长度==k，返回nums中最大值
* 剩下的就需要依次遍历nums索引从k到最后的每一个
* 还要判断一下，要获取的下一个是否大于之前的最大值，如果是：就捕获；
  再判断要弹出的是否是等于最大值，如果是那就需要重新看这个段里的最大值

"""
