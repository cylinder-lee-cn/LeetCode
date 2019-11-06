"""
88. 合并两个有序数组

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]

"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # if (n == 0):
        #     print(nums1)
        #     return
        #
        # if (m == 0):
        #     for a in range(n):
        #         nums1.pop(0)
        #         nums1.append(nums2[a])
        #     print(nums1)
        #     return
        #
        # max2 = nums2[-1]
        # min2 = nums2[0]
        #
        # l1 = len(nums1)
        # max1 = nums1[(m - 1)]
        # min1 = nums1[0]
        #
        # if (max2 <= min1):
        #     for i in range(-1, -(n + 1), -1):
        #         nums1.pop(-1)
        #         nums1.insert(0, nums2[i])
        #     print(nums1)
        #     return
        #
        # if (min2 >= max1):
        #     for i in range(-1, -(n + 1), -1):
        #         nums1.pop(-1)
        #         nums1.insert(m, nums2[i])
        #     print(nums1)
        #     return
        #
        # #
        # i = -1
        # j = -(l1 - m + 1)
        #
        # while (j >= -l1):
        #     if (max2 >= nums1[j]):
        #         nums1.pop(-1)
        #         nums1.insert(j + 2, max2)
        #         i = i - 1
        #         if (i >= -n):
        #             max2 = nums2[i]
        #         else:
        #             print(nums1)
        #             return
        #     else:
        #         if (j == -l1):
        #             while (i >= -n):
        #                 nums1.pop(-1)
        #                 nums1.insert(0, nums2[i])
        #                 i = i - 1
        #         j = j - 1
        #
        # print(nums1)
        # return

        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m = m - 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n = n - 1
        if n > 0:
            nums1[:n] = nums2[:n]

        print(nums1)


s = Solution()
# s.merge([3, 4, 5, 0, 0, 0], 3, [1, 2, 3], 3)
# s.merge([3, 4, 5, 0, 0, 0], 3, [5, 6, 7], 3)
s.merge([2, 2, 3, 4, 5, 0, 0, 0, 0], 5, [-2, -1, 3, 4], 4)

# s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

# s.merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5)

# s.merge([0, 0, 0, 0, 0], 0, [1, 2, 3, 5, 6], 5)
# s.merge([0], 0, [1], 1)
"""
此题分析, 将nums2的list插入到nums1里,而且保持有序,还要保持效率,也就是说nums1和nums2只能各遍历一次(并非嵌套循环).
O(m)+O(n) 而不是O(m)*O(n)
解法:
* 充分利用两个都是有序数组的特征,故此需要倒序读取num1和nums2
* 先解决2个特例:
    1. nums2最大值比nums1的最小值还小, 将nums2都插到nums1的前面;
    2. nums2最小值比nums1的最大值还大, 将nums2都插到nums1的后面
* 倒序读取nums2,取到最大的,然后nums1的最后一个开始比较:
    1.如果发现nums2[i]>=nums1[j],那么将nums2这个元素插入到nums1这个元素的后面;
    2.继续nums2的下一个元素,继续接着上次nums1的元素位置进行比较.直到nums1用完或者是nums2用完

最后:
    现有的代码是网友写的,非常精巧.应该仔细学习.
"""
