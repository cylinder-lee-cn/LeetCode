"""
777. 在LR字符串中交换相邻字符

在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。
一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。
现给定起始字符串start和结束字符串end，请编写代码，
当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。

示例 :
输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
输出: True

解释:
我们可以通过以下几步将start转换成end:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

注意:
1 <= len(start) = len(end) <= 10000。
start和end中的字符串仅限于'L', 'R'和'X'。
"""


class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if start.replace('X', '') == end.replace('X', ''):
            srp, slp = [], []
            erp, elp = [], []
            for i, s in enumerate(start):
                if s == 'R':
                    srp.append(i)
                elif s == 'L':
                    slp.append(i)
            for i, e in enumerate(end):
                if e == 'R':
                    erp.append(i)
                elif e == 'L':
                    elp.append(i)
            if all(x[1] >= x[0]
                   for x in zip(srp, erp)) and all(y[0] >= y[1]
                                                   for y in zip(slp, elp)):
                return True
            else:
                return False
        else:
            return False


"""
此题解法：
* 已知：XL->LX , XR->RX
* 根据官网的提示，可以将L、R看为左人和右人，X看为空位，左人只能往左的空位移动，
  右人只能往右的空位移动。不能跨过人移动。也就是说移动完成后左人和右人的相对位置其实不能发生变化
* 而且end里R和start里对应的索引只能更大或不变
  end里L和start里对应的索引只能更小或不变
"""
s = Solution()
print(s.canTransform("XXRXXLXXXX", "XXXXRXXLXX"))
