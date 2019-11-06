"""
150. 逆波兰表达式求值

根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：
整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

示例 1：
输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9

示例 2：
输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6

示例 3：
输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        d = {'+', '-', '*', '/'}

        for t in tokens:
            if (t not in d):
                stack.append(t)
            else:
                tmpstr = '{a}{op}{b}'
                tb = stack.pop()
                ta = stack.pop()
                stack.append(str(int(eval(tmpstr.format(a=ta, op=t, b=tb)))))
        return int(stack[0])


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(
    s.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

"""
此题解法：
* 还是使用栈，将数字都入栈，如果发现是t是运算符，就取出栈中两个数字进行计算，计算完成后将结果重新入栈
* 直到遍历完tokens，就计算完成
* 这里利用了eval来计算一个字符串里的表达式的值。
----------分隔线-----------
* 网友一个更漂亮的做法
* 使用字典来存放与计算符对应的lambda表达式。通过这个来计算对应的值
        stack = [];
        countl = { 
            "+" : lambda x,y : x+y, 
            "-" : lambda x,y : x-y,
            "*" : lambda x,y : x*y,
            "/" : lambda x,y : x/y
        }
        for i in tokens:
            if i in countl:
                a = int(stack.pop());
                b = int(stack.pop());
                stack.append(countl[i](b,a));
            else:
                stack.append(i);
        return int(stack[-1]);

        也可以将"/" : lambda x,y : x/y 调整为 "/" : lambda x,y : int(x/y)
        
"""
