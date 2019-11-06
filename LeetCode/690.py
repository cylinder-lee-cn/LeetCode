"""
690. 员工的重要性

给定一个保存员工信息的数据结构，它包含了员工唯一的id，重要度 和 直系下属的id。
比如，员工1是员工2的领导，员工2是员工3的领导。他们相应的重要度为15, 10, 5。
那么员工1的数据结构是[1, 15, [2]]，员工2的数据结构是[2, 10, [3]]，
员工3的数据结构是[3, 5, []]。
注意虽然员工3也是员工1的一个下属，但是由于并不是直系下属，因此没有体现在员工1的数据结构中。

现在输入一个公司的所有员工信息，以及单个员工id，返回这个员工和他所有下属的重要度之和。

示例 1:
输入: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
输出: 11

解释:
员工1自身的重要度是5，他有两个直系下属2和3，而且2和3的重要度均为3。因此员工1的总重要度是 5 + 3 + 3 = 11。

注意:
一个员工最多有一个直系领导，但是可以有多个直系下属
员工数量不超过2000。
"""


# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def __init__(self):
        self.allimport = 0

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {}

        def getsubimport(myid, eid):
            self.allimport = self.allimport + d[myid][0]
            if (len(eid) >= 1):
                for sid in eid:
                    getsubimport(sid, d[sid][1])
            else:
                return self.allimport

        for e in employees:
            if (d.get(e.id) is None):
                d[e.id] = [e.importance, e.subordinates]

        getsubimport(id, d[id][1])
        return self.allimport


# e1 = Employee(1, 5, [2, 3])
# e2 = Employee(2, 3, [])
# e3 = Employee(3, 3, [])
# es = [e1, e2, e3]
e1 = Employee(1, 2, [2])
e2 = Employee(2, 3, [])
es = [e1, e2]
s = Solution()
print(s.getImportance(es, 2))
"""
此题解法：
* 使用递归，为了提高速度，先初始化一个字典，将所有的员工信息放入字典中，便于检索
* 定义一个getsubimport(当前id，直属员工id)的函数，来查找直属员工的重要度，
    每次将员工的重要度都累加到self.allimport上
* 如果一个人的直属员工数为0，说明找到头了，将self.allimport返回。
"""
