"""
1041. 困于环中的机器人

在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。机器人可以接受下列三条指令之一：

"G"：直走 1 个单位
"L"：左转 90 度
"R"：右转 90 度
机器人按顺序执行指令 instructions，并一直重复它们。

只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。

示例 1：
输入："GGLLGG"
输出：true
解释：
机器人从 (0,0) 移动到 (0,2)，转 180 度，然后回到 (0,0)。
重复这些指令，机器人将保持在以原点为中心，2 为半径的环中进行移动。

示例 2：
输入："GG"
输出：false
解释：
机器人无限向北移动。

示例 3：
输入："GL"
输出：true
解释：
机器人按 (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ... 进行移动。
 

提示：
1 <= instructions.length <= 100
instructions[i] 在 {'G', 'L', 'R'} 中
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        xmove = [0, 1, 0, -1]
        ymove = [1, 0, -1, 0]
        postion = [0, 0]
        direction = 0

        instructions4times = instructions * 4

        for go in instructions4times:
            if go == 'R':
                direction = (direction + 1) % 4
            elif go == 'L':
                direction = (direction + 3) % 4
            else:
                postion[0] = postion[0] + xmove[direction]
                postion[1] = postion[1] + ymove[direction]

        return True if postion == [0, 0] else False


s = Solution()
print(s.isRobotBounded('GGLLGG'))
print(s.isRobotBounded('GL'))
print(s.isRobotBounded('RG'))
print(s.isRobotBounded('GG'))
print(s.isRobotBounded('GR'))
"""
此题解法：
* 由于转弯都是90度，所以判断是否会回到原点，最多重复4次操作就可以获得判断。
* 也有可能是2次就知道，但是不通用
* 重复4次操作，看看是否回到原点
* 方向默认是0（北），1（东），2（南），3（南）
* 右转就是方向+1然后%4
* 左转就是方向+3然后%4
"""
