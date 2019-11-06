"""
841. 钥匙和房间

有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，
并且房间里可能有一些钥匙能使你进入下一个房间。

在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，
每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length
钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

最初，除 0 号房间外的其余所有房间都被锁住。
你可以自由地在房间之间来回走动。
如果能进入每个房间返回 true，否则返回 false。

示例 1：
输入: [[1],[2],[3],[]]
输出: true
解释:
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。

示例 2：
输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。

提示：
1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
所有房间中的钥匙数量总计不超过 3000。
"""


class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = [0]  # 最初的钥匙
        openrooms = set(keys)  # 最初开的房间
        rooms_len = len(rooms)

        while keys:
            key = keys.pop()  # 取出一把钥匙
            for k in rooms[key]:
                # 遍历开打房间里的钥匙
                if k not in openrooms:
                    # 如果钥匙对应的房间号不在已经open的房间集合中，
                    # 那么就是需要去开的房间
                    keys.append(k)
                    openrooms.add(k)
                    # 如果房间都打开了，那就结束了
                    if (len(openrooms) == rooms_len):
                        return True

        return (len(openrooms) == rooms_len)


s = Solution()
# print(s.canVisitAllRooms([[1], [2], [3], []]))
print(s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))


"""
 # 每个房间的钥匙列表，这个信息相等于图的一种存储形式-邻接列表（另外两种是邻接矩阵和边列表）
        ifvisited = [False] * len(rooms)
        ifvisited[0] = True
        tovisit = [0]   # 可以访问且还没访问过的房间，初始是0号房间
        while tovisit:
            num = tovisit.pop()
            for x in rooms[num]:
                if not ifvisited[x]:
                    ifvisited[x] = True
                    tovisit.append(x)  # 新拿到的钥匙
        return all(ifvisited)   # ifvisited全都是True，则返回True，否则False
        
"""