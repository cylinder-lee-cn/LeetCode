"""
743. 网络延迟时间

有 N 个网络节点，标记为 1 到 N。

给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点，
w 是一个信号从源节点传递到目标节点的时间。

现在，我们向当前的节点 K 发送了一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。

注意:
N 的范围在 [1, 100] 之间。
K 的范围在 [1, N] 之间。
times 的长度在 [1, 6000] 之间。
所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 1 <= w <= 100。

"""


class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        import collections

        K -= 1
        nodes = collections.defaultdict(list)
        for u, v, w in times:
            nodes[u - 1].append((v - 1, w))
        dist = [float('inf')] * N
        dist[K] = 0
        done = set()
        for _ in range(N):
            smallest = min(
                (d, i) for (i, d) in enumerate(dist) if i not in done)[1]
            for v, w in nodes[smallest]:
                if v not in done and dist[smallest] + w < dist[v]:
                    dist[v] = dist[smallest] + w
            done.add(smallest)
        return -1 if float('inf') in dist else max(dist)

        # dist = [float('inf')] * (N + 1)
        # dist[0] = 0
        # dist[K] = 0
        # for i in range(1, N + 1):
        #     for t in times:
        #         u, v, w = t
        #         dist[v] = min(dist[v], dist[u] + w)

        # return -1 if float('inf') in dist else max(dist)


s = Solution()
print(s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(s.networkDelayTime([[1, 2, 1], [2, 1, 3]], 2, 2))
"""
此题解法：
* 按照官网的提示，这是一个标准的Dijkstra算法题
* 还需学习 Dijkstra算法
"""
