"""
80. 删除排序数组中的重复项 II

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定 nums = [1,1,1,2,2,3],
函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,1,2,3,3],
函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

你不需要考虑数组中超出新长度后面的元素。

说明:
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 1
        while j < len(nums):
            if (nums[i] == nums[j]):
                if (j - i >= 2):
                    nums.pop(j)
                else:
                    j = j + 1
            else:
                i, j = j, j + 1

        return len(nums)


s = Solution()
s.removeDuplicates([0, 1, 1, 1, 2, 2, 3])
s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3, 3])
"""
此题解法：
* 使用了双指针
* i，j=0，1 分别指向初始的第1，2个元素
* 如果nums[i]==nums[j]，那就再判断一下i和j的差距，如果>=2说明就多了，这时可以删除一个i上的元素
  反之，j增1
* 如果不相同，那么将i移动到j的位置，j增1，继续比较

附：官网解法，这个用了三指针
class Solution:
    def removeDuplicates(self, nums):

        n = len(nums)
        if (n <= 2):
            return n
        # nums[0...i]是符合要求的，
        i = 1
        k = i - 1
        j = i + 1

        while j <= n-1:
            if (nums[j] != nums[i]) or (nums[j] == nums[i] and nums[j] != nums[k]):
                k = i
                nums[i+1] = nums[j]
                i += 1
            j += 1

        return i + 1
"""
