"""
848. 字母移位

有一个由小写字母组成的字符串 S，和一个整数数组 shifts。

我们将字母表中的下一个字母称为原字母的移位（由于字母表是环绕的， 'z' 将会变成 'a'）。

例如·，shift('a') = 'b'， shift('t') = 'u',， 以及 shift('z') = 'a'。

对于每个 shifts[i] = x ， 我们会将 S 中的前 i+1 个字母移位 x 次。

返回将所有这些移位都应用到 S 后最终得到的字符串。

示例：
输入：S = "abc", shifts = [3,5,9]
输出："rpl"

解释：
我们以 "abc" 开始。
将 S 中的第 1 个字母移位 3 次后，我们得到 "dbc"。
再将 S 中的前 2 个字母移位 5 次后，我们得到 "igc"。
最后将 S 中的这 3 个字母移位 9 次后，我们得到答案 "rpl"。
提示：

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9
"""


class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        s_l = len(S)
        result = []
        n = 0
        for i in range(s_l - 1, -1, -1):
            s = S[i]
            n = n + shifts[i]
            result.append(chr((ord(s) - 97 + n) % 26 + 97))
        return ''.join(result[::-1])


s = Solution()
print(s.shiftingLetters('abc', [3, 5, 9]))
"""
此题解法：
* 首先，这个移动是循环的，所以如果某个字母移动了26次，那么就还是这个字母
* a-z（0-25）是97-122，也就是0+97---25+97
* 将字母对应到0-25上就是 ord(s)-97, 在这个位置上移动n次那就是 ord(s)-97+n
  在看看有多少个26的重复循环，那剩余的就是真实移动到的位置 (ord(s)-97+n)%26，看余数
* 那这个字母就是chr((ord(s)-97+n)%n+97)

* 另外这个字母总共移动的次数是sum(shifts[i:])
* 如果是顺序求解的话，每次计算sum(shifts[i:])会导致最后运行超时。
  所以，应该反向求解，从最末尾算起，然后顺势开始累加shifts[i]
"""
