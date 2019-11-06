"""
1189. “气球” 的最大数量

给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

示例 1：
输入：text = "nlaebolko"
输出：1

示例 2：
输入：text = "loonbalxballpoon"
输出：2

示例 3：
输入：text = "leetcode"
输出：0

提示：
1 <= text.length <= 10^4
text 全部由小写英文字母组成
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bDict = {}
        bset = {'b', 'a', 'l', 'o', 'n'}

        for t in text:
            if t in bset:
                bDict[t] = bDict.get(t, 0) + 1

        if bDict is None or len(bDict) < 5:
            return 0

        bDict['l'] = bDict['l'] // 2
        bDict['o'] = bDict['o'] // 2

        # print(bDict, len(bDict))
        return min(bDict.values())


s = Solution()
print(s.maxNumberOfBalloons('nlaebolko'))
print(s.maxNumberOfBalloons('loonbalxballpoon'))
print(s.maxNumberOfBalloons('leetcode'))
"""
此题解法：
* 先将单个字母放入set中，同时建立空dict
* 然后遍历text，将符合set的字母放入dict中进行计数
* 如果dict为空或者长度小于5，那么就是缺字母，返回0
* 将l和o的计数量整除2，那么 b a l o n 这些必备字母的最小数就是可以组成balloon的数量
"""
