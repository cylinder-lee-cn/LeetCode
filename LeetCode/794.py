"""
794. 有效的井字游戏


用字符串数组作为井字游戏的游戏板 board。当且仅当在井字游戏过程中，
玩家有可能将字符放置成游戏板所显示的状态时，才返回 true。

该游戏板是一个 3 x 3 数组，由字符 " "，"X" 和 "O" 组成。字符 " " 代表一个空位。

以下是井字游戏的规则：
玩家轮流将字符放入空位（" "）中。
第一个玩家总是放字符 “X”，且第二个玩家总是放字符 “O”。
“X” 和 “O” 只允许放置在空位中，不允许对已放有字符的位置进行填充。
当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
当所有位置非空时，也算为游戏结束。
如果游戏结束，玩家不允许再放置字符。

示例 1:
输入: board = ["O  ", "   ", "   "]
输出: false
解释: 第一个玩家总是放置“X”。

示例 2:
输入: board = ["XOX", " X ", "   "]
输出: false
解释: 玩家应该是轮流放置的。

示例 3:
输入: board = ["XXX", "   ", "OOO"]
输出: false

示例 4:
输入: board = ["XOX", "O O", "XOX"]
输出: true

说明:
游戏板 board 是长度为 3 的字符串数组，其中每个字符串 board[i] 的长度为 3。
 board[i][j] 是集合 {" ", "X", "O"} 中的一个字符。
"""


class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        Xwin, Owin = 0, 0
        Xs, Os = 0, 0
        boardlen = len(board)

        if boardlen > 3 or boardlen < 3:
            return False

        for b in board:  # check row
            if len(b) > 3 or len(b) < 3:
                return False
            Xs = Xs + b.count('X')
            Os = Os + b.count('O')
            if b == 'XXX':
                Xwin = Xwin + 1
            elif b == 'OOO':
                Owin = Owin + 1

        for b in zip(*board):  # check col
            if b.count('X') == 3:
                Xwin = Xwin + 1
            elif b.count('O') == 3:
                Owin = Owin + 1

        t1 = [board[0][0], board[1][1], board[2][2]]
        t2 = [board[0][2], board[1][1], board[2][0]]

        # check diagonal
        if t1.count('X') == 3:
            Xwin = Xwin + 1
        elif t1.count('O') == 3:
            Owin = Owin + 1

        if t2.count('X') == 3:
            Xwin = Xwin + 1
        elif t2.count('O') == 3:
            Owin = Owin + 1

        # print(Xs, Os)
        # print(Xwin, Owin)

        if Xwin > 0 and Owin > 0:
            return False

        if Xwin > 0 and Owin == 0:
            if Xs > Os and (Xs - Os) == 1:
                return True
            else:
                return False

        if Xwin == 0 and Owin > 0:
            if Xs == Os:
                return True
            else:
                return False
        if Xwin == 0 and Owin == 0:
            if Xs == Os or (Xs - Os) == 1:
                return True
            else:
                return False


s = Solution()
print(s.validTicTacToe(["O  ", "   ", "   "]))
print(s.validTicTacToe(["XOX", " X ", "   "]))
print(s.validTicTacToe(["XXX", "   ", "OOO"]))
print(s.validTicTacToe(["XOX", "O O", "XOX"]))
"""
此题解法：
* 没有什么诀窍，就是把游戏规则整理清楚
* X先走，O后走，所以X的数量一定>=O，如果Xs>Os 还必定满足Xs-Os==1
* X和O只有一个能胜利，或者都不胜利
* 分别按照行，列，对角线对X和O是否胜利进行判断，顺便在判断一下board的长度，和每个元素的长度是否都是3
* 如果X胜利，就给X胜利的次数+1，如果O胜利就给O胜利的次数+1
* 统计整个board中X和O的个数
* 最后进行判断，如果X和O都胜利：False
* 如果X胜利，O失败，那么Xs>Os and Xs-Os==1 X一定会比O多走一步
* 如果X失败，O胜利，那么Xs==Os，X和O走的步数一样
* 如果X失败，O也失败，那么Xs==Os 或者是Xs-Os==1
"""
