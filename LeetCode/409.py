"""
409. 最长回文串

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:
输入:
"abccccdd"
输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        cs = set(s)
        evensum = 0
        maxodd = 0

        for c in cs:
            n = s.count(c)
            if (n % 2 == 0):
                evensum = evensum + n
            else:
                evensum = evensum + n - 1
                maxodd = 1

        evensum = evensum + maxodd

        return evensum


s = Solution()
# print(s.longestPalindrome(''))
print(s.longestPalindrome(
    'civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'))

"""
解题思路: 统计字符串中各个字母的个数(区分大小写), 可以利用set来获取唯一的字符.
字符个数是偶数的,全要. 字符个数是奇数的需要n-1个. 如果字符个数有奇数,最后合计的数字要+1,
因为回文字符串的最中间可以是奇数(就是左右对称).
"""