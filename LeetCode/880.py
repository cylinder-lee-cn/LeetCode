"""
880. 索引处的解码字符串

给定一个编码字符串 S。为了找出解码字符串并将其写入磁带，从编码字符串中每次读取一个字符，并采取以下步骤：

如果所读的字符是字母，则将该字母写在磁带上。
如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。
现在，对于给定的编码字符串 S 和索引 K，查找并返回解码字符串中的第 K 个字母。

示例 1：
输入：S = "leet2code3", K = 10
输出："o"
解释：
解码后的字符串为 "leetleetcodeleetleetcodeleetleetcode"。
字符串中的第 10 个字母是 "o"。

示例 2：
输入：S = "ha22", K = 5
输出："h"
解释：
解码后的字符串为 "hahahaha"。第 5 个字母是 "h"。

示例 3：
输入：S = "a2345678999999999999999", K = 1
输出："a"
解释：
解码后的字符串为 "a" 重复 8301530446056247680 次。第 1 个字母是 "a"。

提示：
2 <= S.length <= 100
S 只包含小写字母与数字 2 到 9 。
S 以字母开头。
1 <= K <= 10^9
解码后的字符串保证少于 2^63 个字母。
"""


class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        l_s = 0
        idx = 0
        for j, c in enumerate(S):
            if (c.isalpha()):
                l_s = l_s + 1
                if (l_s == K):
                    return c
            else:
                l_s = l_s * int(c)

            if (l_s >= K):
                idx = j
                break

        while (idx >= 0):
            s = S[idx]
            if (s.isdigit()):
                l_s = l_s // int(s)
                K = K % l_s
            elif (K % l_s == 0):
                return S[idx]
            else:
                l_s = l_s - 1
            idx = idx - 1


s = Solution()
print(s.decodeAtIndex('leet2code3', 10))
print(s.decodeAtIndex('ha22', 5))
print(s.decodeAtIndex('a2345678999999999999999', 1))
print(s.decodeAtIndex('y959q969u3hb22odq595', 222280369))
print(s.decodeAtIndex('y959q969u3hb22odq595', 267563095))
"""
此题解法：
* 不能暴力的按照题示的要求把整个字符串都拼出来，然后找到第K位的字符，因为有可能会巨大的一个字符串
* 所以只先计算长度，找到刚好l_s>=K的时候（并且知道遍历到S的哪个位置：idx）。
  l_s长的字符串其实是由1-n个子字符串拼接而成的。
* 从idx倒着读取S，l_s//int(s)就是将长字符串看看是由那个子字符串组成的，
  K%l_s就看看去除重复的子字符串后真正落在子字符串的那里.
  如果K%l_s没有余数，说明正好落在idx对应的字母上了
* 如果s是字母就将l_s减1
y959q969u3hb22odq595
222280369
"""
