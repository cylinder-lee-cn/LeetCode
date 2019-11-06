"""
1185. 一周中的第几天

给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。

输入为三个整数：day、month 和 year，分别表示日、月、年。

您返回的结果必须是这几个值中的一个 
{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。

示例 1：
输入：day = 31, month = 8, year = 2019
输出："Saturday"

示例 2：
输入：day = 18, month = 7, year = 1999
输出："Sunday"

示例 3：
输入：day = 15, month = 8, year = 1993
输出："Sunday"
"""

import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        wDay = [
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
            "Sunday"
        ]
        w = datetime.datetime(year, month, day).weekday()
        return wDay[w]


s = Solution()
s.dayOfTheWeek(31, 8, 2019)
s.dayOfTheWeek(18, 7, 1999)
s.dayOfTheWeek(15, 8, 1993)
"""
此题解法：
* 可以采用蔡勒公式，未完待续
wDay = [
            "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday"
        ]

        y = year % 100
        c = int(year / 100)
        d = day
        if month in {1, 2}:
            y = y - 1
            m = month + 12
        else:
            m = month

        w = y + int(y / 4) + int(c / 4) - 2 * c + int(
            (m + 1) * 26 / 10) + d - 1

        while (w < 0):
            w = w + 7
        w = w % 7
        # print(wDay[int(w)])
        return wDay[int(w)]
"""
