"""
1154. 一年中的第几天

给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。
通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。
每个月的天数与现行公元纪年法（格里高利历）一致。

示例 1：
输入：date = "2019-01-09"
输出：9

示例 2：
输入：date = "2019-02-10"
输出：41

示例 3：
输入：date = "2003-03-01"
输出：60

示例 4：
输入：date = "2004-03-01"
输出：61

提示：
date.length == 10
date[4] == date[7] == '-'，其他的 date[i] 都是数字。
date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日。
"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = [int(x) for x in date.split('-')]
        # mDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # mDays1 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mDays = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        mDays1 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0 and y % 3200 != 0):
            days = mDays1[m - 1] + d
        else:
            days = mDays[m - 1] + d
        return days


s = Solution()
print(s.dayOfYear('2019-01-09'))
print(s.dayOfYear('2019-02-10'))
print(s.dayOfYear('2003-03-01'))
print(s.dayOfYear('2004-03-01'))
print(s.dayOfYear('2016-02-29'))
print(s.dayOfYear('1900-03-25'))

"""
此题解法：
* 构造两个List,分别存放有平年和闰年每个月结束时的天数，从1-11月（不用放12月），首位为0，共12个
* 然后判断一下是否是闰年后，查截至到前一个月累计的天数，并且将本月的天数加上
* 还可以用python自带的datetime库实现

import datetime

y, m, d = [int(x) for x in date.split('-')]
dEnd=datetime.datetime(y,m,d)
dStart=datetime.datetime(y,1,1)
#计算当前日期到当年的第一天的间隔的天数，然后加1即可
return (dEnd-dStart).days+1

效率未必有上面直接计算的高。
"""
