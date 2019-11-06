"""
1160. 拼写单词

给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。

示例 1：
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。

示例 2：
输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
输出：10
解释：
可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
 
提示：
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
所有字符串中都仅包含小写英文字母
"""

from typing import List
import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c_dict = collections.Counter(chars)

        result = 0

        for word in words:
            w_dict = collections.Counter(word)
            if all(c_dict.get(w, 0) >= w_dict[w] for w in w_dict.keys()):
                result = result + len(word)

        return result


s = Solution()
print(s.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
print(s.countCharacters(["hello", "world", "leetcode"], 'welldonehoneyr'))

"""
此题解法：
* 采用字典法，先将chars按字母出现的次数统计后放入字典中，此处使用collections标准库
* 遍历words，将每个word也按字母统计次数 w_dict
* 依照题意，w_dict中的每个字母都应该在c_dict中出现并且统计数字要>=c_dict中的统计数字
* 用all函数判断是否都满足即可
"""
