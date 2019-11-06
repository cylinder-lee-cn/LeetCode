"""
937. 重新排列日志文件

你有一个日志数组 logs。每条日志都是以空格分隔的字串。

对于每条日志，其第一个字为字母数字标识符。然后，要么：

标识符后面的每个字将仅由小写字母组成，
或；
标识符后面的每个字将仅由数字组成。
我们将这两种日志分别称为字母日志和数字日志。保证每个日志在其标识符后面至少有一个字。

将日志重新排序，使得所有字母日志都排在数字日志之前。字母日志按字母顺序排序，
忽略标识符，标识符仅用于表示关系。数字日志应该按原来的顺序排列。

返回日志的最终顺序。

示例 ：
输入：["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

提示：
0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] 保证有一个标识符，并且标识符后面有一个字。
"""


class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        result = sorted(
            [ll for ll in logs if not (ll.split(' ', 2)[1].isdigit())],
            key=lambda log: log.split(' ', 1)[1])
        for log in logs:
            if (log.split(' ', 2)[1].isdigit()):
                result.append(log)
        return result


s = Solution()
print(
    s.reorderLogFiles([
        "a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"
    ]))
"""
此题解法：
* 要观察元素的第二个位置的子元素究竟是不是纯数字
* 如果不是纯数字，还要将除首位意外的子元素进行排序
* 利用split(' ',2)将字符串切成3段，看第二段是否是数字，然后利用sorted排序，定义排序的key
  排序的key是split(' ',1)，切成2段中后半部分
* 最后遍历原始logs，看看哪个是数字log，按照原始顺序添加到已经排序好的字母log数组中
"""
