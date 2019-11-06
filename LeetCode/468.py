"""
468. 验证IP地址
编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。

IPv4 地址由十进制数和点来表示，每个地址包含4个十进制数，其范围为 0 - 255,
用(".")分割。比如，172.16.254.1；

同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。

IPv6 地址由8组16进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。
比如,  2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。
而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。
所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。

然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。
比如， 2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。

同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。

说明: 你可以认为给定的字符串里没有空格或者其他特殊字符。

示例 1:
输入: "172.16.254.1"
输出: "IPv4"
解释: 这是一个有效的 IPv4 地址, 所以返回 "IPv4"。

示例 2:
输入: "2001:0db8:85a3:0:0:8A2E:0370:7334"
输出: "IPv6"
解释: 这是一个有效的 IPv6 地址, 所以返回 "IPv6"。

示例 3:
输入: "256.256.256.256"
输出: "Neither"
解释: 这个地址既不是 IPv4 也不是 IPv6 地址。
"""


class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        ipParts = []
        ipType = 4

        if '.' in IP and ':' not in IP:
            ipParts = IP.split('.')
        else:
            ipParts = IP.split(':')
            ipType = 6

        if ipType == 4:
            if len(ipParts) == 4:
                if all(n.isdigit() and len(n) <= 3 for n in ipParts):
                    if all(n[0] != '0' for n in ipParts if len(n) > 1):
                        if all(0 <= int(n) <= 255 for n in ipParts):
                            return 'IPv4'

        if ipType == 6:
            if len(ipParts) == 8:
                if all(n.isalnum() for n in ipParts):
                    if all(len(n) <= 4 for n in ipParts):
                        if all(
                                n.count('0') < len(n) for n in ipParts
                                if len('n') > 1):
                            if all('0' <= n.lower() <= 'ffff'
                                   for n in ipParts):
                                return 'IPv6'
        return 'Neither'


s = Solution()
# print(s.validIPAddress("172.16.254.1"))
# print(s.validIPAddress("1e1.110.1.0"))
# print(s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
# print(s.validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334"))
print(s.validIPAddress('01.01.01.01'))

"""
此题解法：
* 此题没有难度，就是考虑是否完整
* ipv4 用'.'分隔，共有4段，每段都是0<=n<=255的数字，没有前导0
* ipv6 用':'分隔，共有8段，每段都是‘0’<=n<=‘ffff’的十六进制数，长度<=4，可以有前导0，但是不能有纯是0的重复
"""