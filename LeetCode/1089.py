"""
1089. 复写零

给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。

要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。

示例 1：
输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]

示例 2：
输入：[1,2,3]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,2,3]

提示：
1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        l_arr = len(arr)
        tmp_arr = [0] * len(arr)

        i = 0
        for a in arr:
            if i < l_arr:
                if a == 0:
                    i = i + 2
                else:
                    tmp_arr[i] = a
                    i = i + 1
            else:
                break

        for k, v in enumerate(tmp_arr):
            arr[k] = v


s = Solution()
s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
s.duplicateZeros([0, 0, 0, 0, 0, 0, 0, 0])

"""
此题解法：
* 必须在原list的基础上修改数据，不能新创建或者是利用赋值的方式获得arr，python会在内存中生成新的对象。
* 利用空间换时间
* 创建一个和arr一样大的list，默认都是0
* 遍历arr，同时有个计数器，如果 a==0 就跳过2个索引，反之将当前位置赋值为a，索引+1
* 索引小于arr长度
* 最后遍历tmparr，对应修改arr的值
"""