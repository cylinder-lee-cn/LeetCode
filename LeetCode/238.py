"""
238. 除自身以外数组的乘积


给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n_l = len(nums)
        # goright = []
        # goleft = []
        # output = [None] * n_l
        # mulright, mulleft = 1, 1
        # for i in range(n_l):
        #     mulright = mulright * nums[i]
        #     goright.append(mulright)
        #     mulleft = mulleft * nums[n_l - 1 - i]
        #     goleft.insert(0, mulleft)

        # output[0] = goleft[1]
        # for j in range(1, n_l - 1):
        #     output[j] = goright[j - 1] * goleft[j + 1]
        #     # print(goright[j - 1], goleft[j + 1])

        # output[-1] = goright[-2]
        # return output

        p = 1
        outputs = []
        for num in nums:
            outputs.append(p)
            p = p * num

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            outputs[i] = outputs[i] * p
            p = p * nums[i]

        return outputs


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
"""
此题解法：
* 将数组所有元素累计相乘，然后依次遍历元素，积÷元素=nums中除nums[i]之外元素的乘积
* 但是题目不允许这个做法。。。。

* 使用两个同样长度的数组分别存放顺序相乘和逆序相乘的结果
goright=[1,1x2,1x2x3,1x2x3x4]
goleft= [1x2x3x4,2x3x4,3x4,4]
将这两个数组错开两位就会发现
                    1       1x2     1x2x3   1x2x3x4
1x2x3x4     2x3x4   3x4     4
去掉一头一尾，上下组合后就是所需要的

* 更简便的方法
        p = 1
        outputs = []
        for num in nums:
            outputs.append(p)
            p *= num

        p = 1
        for i in range(len(nums)-1, -1, -1):
            outputs[i] *= p
            p *= nums[i]

        return outputs
* 首先遍历nums，累计积初始1，放入outputs中，后续依次乘前n-1个元素
outputs=[1,1x1,1x1x2,1x1x2x3]
nums=[1,2,3,4]
            1       1x1     1x1x2  1x1x2x3
          2x3x4x1   3x4x1   4x1    1
          2x3x4     1x3x4   1x2x4  1x2x3

* 重新初始化累计积=1
* 然后逆序读取outputs，outputs[i]=outputs*p
* 下一个p就是 p*nums[i]
"""
