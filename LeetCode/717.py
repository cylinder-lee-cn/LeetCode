"""
717. 1比特与2比特字符

有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

示例 1:
输入:
bits = [1, 0, 0]
输出: True

解释:
唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。

示例 2:
输入:
bits = [1, 1, 1, 0]
输出: False

解释:
唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。

注意:
1 <= len(bits) <= 1000.
bits[i] 总是0 或 1.
"""


class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        lb = len(bits) - 1
        i = 0
        while (i < lb):
            if (bits[i] == 1):
                i = i + 2
            else:
                i = i + 1

        return (i == lb)


s = Solution()
print(s.isOneBitCharacter([1, 0, 0]))
print(s.isOneBitCharacter([1, 0, 0, 1, 0]))
print(s.isOneBitCharacter([1, 1, 1, 0]))
print(s.isOneBitCharacter([1, 1, 1, 1, 0]))
"""
此题解法（源自网上）：由于10， 11两个编码都是以1开头的，这意味着只要是以1开头的后面一个数必定是和这个1一起的字符编码。
* 遍历这个list，如果第一个是0，只能往后走一位
* 如果第一个是1，必须往后走两位，以此类推。
* 最后看索引的位置，是不是正好取完。
"""
