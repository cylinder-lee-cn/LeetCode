"""
676. 实现一个魔法字典

实现一个带有buildDict, 以及 search方法的魔法字典。

对于buildDict方法，你将被给定一串不重复的单词来构建一个字典。

对于search方法，你将被给定一个单词，并且判定能否只将这个单词中一个字母换成另一个字母，
使得所形成的新单词存在于你构建的字典中。

示例 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False

注意:
你可以假设所有输入都是小写字母 a-z。
为了便于竞赛，测试所用的数据量很小。你可以在竞赛结束后，考虑更高效的算法。
"""


class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.magicset = set()
        self.magicdict = {}

    def _candidate(self, word):
        for i in range(len(word)):
            yield word[:i] + '9' + word[i + 1:]

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.magicset = set(dict)
        for d in dict:
            for c in self._candidate(d):
                self.magicdict[c] = self.magicdict.get(c, 0) + 1

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word
        after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return any(
            self.magicdict.get(c, 0) > 1
            or self.magicdict.get(c, 0) == 1 and word not in self.magicset
            for c in self._candidate(word))


s = MagicDictionary()
s.buildDict(["hello", "hallo", "leetcode"])
print(s.search('hello'))
print(s.search('hhllo'))
print(s.search('hell'))
print(s.search('leetcoded'))
"""
此题解法：
* 利用dict和set的唯一性和易查性来解决。按照题意，被查单词如果和set中有相同的，必须由不相同的单词进行变化才能符合条件
* 将所有words放入set中
* 题意是只有小写字母，所以利用‘9’作为占位符，来依次替换单词每个位置上的字母，获取变化一位字母后的单词
  比如：hello会变成9ello，h9llo,he9lo,hel9o,hell9
* 将变化后的单词都放入字典中并统计相同单词的出现次数
* 然后将要查询的单词也进行变形，并通过dict和set进行查找
** 如果，在字典中查到的变形单词统计数量>1，那么说明有超过一个单词能变形成功，必然符合条件，返回True
** 如果，在字典中查到数量==1，那么这个单词就不能与set中的一致。
"""
