"""
458. 可怜的小猪

有1000只水桶，其中有且只有一桶装的含有毒药，其余装的都是水。它们从外观看起来都一样。
如果小猪喝了毒药，它会在15分钟内死去。

问题来了，如果需要你在一小时内，弄清楚哪只水桶含有毒药，你最少需要多少只猪？
回答这个问题，并为下列的进阶问题编写一个通用算法。

进阶:
假设有 n 只水桶，猪饮水中毒后会在 m 分钟内死亡，你需要多少猪（x）就能在 p 分钟内找出“有毒”水桶？
n只水桶里有且仅有一只有毒的桶。

"""


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        times = minutesToTest / minutesToDie + 1  # 每头猪最多可测试的水桶数
        num = 0
        while pow(times, num) < buckets:
            num = num + 1
        return num


"""
此题解法：
* 就是经典的小白鼠试毒药的算法。
* 利用二进制的特性做逐一的区分
* 假定有两只鼠(n=2)，那单位时间内最多鉴别2^n瓶水是否有毒，因为
瓶1 0   0
瓶2 0   1
瓶3 1   0
瓶4 1   1
---------
鼠1     喝了此位置为1的（瓶2和瓶4）
鼠2 喝此位置为1的（瓶1和瓶4）

鼠1死，那么瓶2有毒
鼠2死，那么瓶3有毒
鼠1鼠2都死，那么瓶4有毒
都不死，瓶1有毒

* 扩展结论，单位时间内死亡的话，最多测试 2^n (n是动物数量)瓶水里是否有毒。
"""
