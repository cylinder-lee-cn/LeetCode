"""
401. 二进制手表

二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。



例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

案例:
输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

注意事项:

输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
"""


class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        clocks = {}

        for h in range(12):
            hh = bin(h).lstrip('0b')
            hc = hh.count('1')

            for m in range(60):
                mm = bin(m).lstrip('0b')
                mc = mm.count('1')
                cc = hc + mc
                clock = '{:d}:{:02d}'.format(h, m)

                if clocks.get(cc):
                    clocks[cc].append(clock)
                else:
                    clocks[cc] = [clock]

        if num <= 8:
            return clocks[num]
        else:
            return []


s = Solution()
s.readBinaryWatch(1)

"""
此题解法: 小时是0-11,分钟是0-59, 总共是12x60=720种可能. 采用字典法,将所有可能列举,存入字典,使用num在字典中进行查找.
如果能预先生成此字典,这个方法最好,但是此题应该采用实时计算和统计更好.

"""