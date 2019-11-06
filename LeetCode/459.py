"""
459. 重复的子字符串

给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。

示例 2:
输入: "aba"
输出: False

示例 3:
输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

"""


class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ls = len(s)

        if (ls <= 1):
            return False

        for i in range((ls // 2 + 1), 0, -1):
            if (ls % i == 0):
                p = s[:i]
                t = ls // i
                if (t > 1 and p * t == s):
                    return True
        return False


s = Solution()
print(s.repeatedSubstringPattern('abab'))
"""
此题解法：如果是‘重复’，意味着至少出现2次，也就是切分字符串的时候能否被整除。
只需要验证能够整除ls=len（s）的分组情况。最大尝试的数字就是过ls的一半就行了
* 如果字符长度<=1就没有重复的可能
* 整除的因数 ls//2 + 1 就足够
* 按照整除的长度切分字符串，看看是否相同

来自网上的解法：
        ss = (s + s)[1:-1]
        return ss.find(s) != -1

Basic idea:

1.First char of input string is first char of repeated substring
2.Last char of input string is last char of repeated substring
3.Let S1 = S + S (where S in input string)
4.Remove 1 and last char of S1. Let this be S2
5.If S exists in S2 then return true else false
6.Let i be index in S2 where S starts then repeated
  substring length i + 1 and repeated substring S[0: i+1]
"""
