"""
165. 比较版本号

比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

你可以假设版本字符串非空，并且只包含数字和 . 字符。
 . 字符不代表小数点，而是用于分隔数字序列。

例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。

示例 1:
输入: version1 = "0.1", version2 = "1.1"
输出: -1

示例 2:
输入: version1 = "1.0.1", version2 = "1"
输出: 1

示例 3:
输入: version1 = "7.5.2.4", version2 = "7.5.3"
输出: -1
"""


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = version1.split('.')
        ver2 = version2.split('.')

        vl1 = len(ver1)
        vl2 = len(ver2)

        result = 0

        if vl1 > vl2:
            for i in range(vl1 - vl2):
                ver2.append('0')
        elif vl1 < vl2:
            for i in range(vl2 - vl1):
                ver1.append('0')
        # print(ver1, ver2)

        for j in range(max(vl1, vl2)):
            if int(ver1[j]) == int(ver2[j]):
                continue
            elif int(ver1[j]) > int(ver2[j]):
                result = 1
                break
            elif int(ver1[j]) < int(ver2[j]):
                result = -1
                break
        return result


s = Solution()
print(s.compareVersion('0.1', '1.1'))
print(s.compareVersion('1.0.1', '1'))
print(s.compareVersion('7.5.2.4', '7.5.3'))
print(s.compareVersion('7.5.03.0', '7.5.3'))
"""
此题解法：
* 首先利用 “.” 将两个版本号分割成数组，然后将短的用‘0’补齐
* 依次遍历ver1和ver2两个数组，相同索引的元素进行比较，如果相同就跳到下一个循环
  如果v1[j]>v2[j] 就中断，并且返回1
  如果v1[j]<v2[j] 就中断，并且返回-1
  如果一直相同，最后返回0
*
"""
