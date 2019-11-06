"""
825. 适龄的朋友

人们会互相发送好友请求，现在给定一个包含有他们年龄的数组，ages[i] 表示第 i 个人的年龄。

当满足以下条件时，A 不能给 B（A、B不为同一人）发送好友请求：
age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
否则，A 可以给 B 发送好友请求。

注意如果 A 向 B 发出了请求，不等于 B 接受了 A 的请求。而且，人们不会给自己发送好友请求.
求总共会发出多少份好友请求?

示例 1:
输入: [16,16]
输出: 2
解释: 二人可以互发好友申请。

示例 2:
输入: [16,17,18]
输出: 2
解释: 好友请求可产生于 17 -> 16, 18 -> 17.

示例 3:
输入: [20,30,100,110,120]
输出: 3
解释: 好友请求可产生于 110 -> 100, 120 -> 110, 120 -> 100.

说明:
1 <= ages.length <= 20000.
1 <= ages[i] <= 120.
"""


class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        men = [0] * 121
        agesum = [0] * 121
        result = 0

        # 用映射数组来统计各年龄端总共的人数，men数组的下标是从0-120
        for a in ages:
            men[a] = men[a] + 1
        print(men)

        # 再统计自己和比自己小的总共有多少人，从0岁开始往上1年累加，这样通过一次遍历就可以完成
        for i in range(1, 121):
            agesum[i] = men[i] + agesum[i - 1]
        print(agesum)

        # 根据age[B] <= 0.5 * age[A] + 7这个调节可知，14岁及以下没有朋友
        for j in range(15, 121):
            if (men[j] == 0):
                continue
            else:
                count = agesum[j] - agesum[j // 2 + 7]
                count = count - 1
                result = result + count * men[j]
        return result


s = Solution()
# print(s.numFriendRequests([20, 30, 100, 110, 120]))
print(
    s.numFriendRequests(
        [73, 106, 39, 6, 26, 15, 30, 100, 71, 35, 46, 112, 6, 60, 110]))
"""
此题解法：
* 采用排序后向后依次比较的办法正确，但是效率不够高
        count = 0
        la = len(ages)
        ages.sort(reverse=True)
        print(ages)
        for i, a in enumerate(ages):
            for k in range(i + 1, la):
                b = ages[k]
                c = a * 0.5 + 7
                if (b > c):
                    print(a, b, c)
                    if (a == b):
                        count = count + 2
                    else:
                        count = count + 1
                else:
                    break
        return count
"""
