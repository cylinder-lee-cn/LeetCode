"""
49. 字母异位词分组

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i, s in enumerate(strs):
            s_sorted = ''.join(sorted(s))
            if s_sorted not in d:
                d[s_sorted] = [s]
            else:
                d[s_sorted].append(s)
        # print(d)
        return list(d.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

"""
此题解法：
* 字母异位词指字母相同，但排列不同的字符串。也就是排序后完全相同的词。
* 将排序后的词作为字典的key，未排序的词作为value
* 遍历strs，找到相同的key，就给value.append()一个，反之给字典增加一个新的key
* 最后输出字典.values()
"""

