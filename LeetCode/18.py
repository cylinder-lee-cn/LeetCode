"""
18. 四数之和

给定一个包含 n 个整数的数组 nums 和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, dicti = set(), {}
        numLen = len(nums)
        nums.sort()
        for i in range(numLen):
            for j in range(i + 1, numLen):
                key = nums[i] + nums[j]
                if key not in dicti.keys():
                    dicti[key] = [(i, j)]
                else:
                    dicti[key].append((i, j))
        for i in range(numLen):
            for j in range(i + 1, numLen - 2):
                exp = target - nums[i] - nums[j]
                if exp in dicti.keys():
                    for tmpIndex in dicti[exp]:
                        if tmpIndex[0] > j:
                            res.add((nums[i], nums[j], nums[tmpIndex[0]],
                                     nums[tmpIndex[1]]))
        return [list(i) for i in res]


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
"""
此题解法：
* 第一种 暴力法，拿出所有的组合情况，sum之后判断是否是target，然后利用sorted进行排重（超时了）
* 第二种

"""
