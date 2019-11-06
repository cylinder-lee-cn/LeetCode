"""
721. 账户合并

给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是名称 (name)，
其余元素是 emails 表示该帐户的邮箱地址。

现在，我们想合并这些帐户。如果两个帐户都有一些共同的邮件地址，则两个帐户必定属于同一个人。
请注意，即使两个帐户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。
一个人最初可以拥有任意数量的帐户，但其所有帐户都具有相同的名称。

合并帐户后，按以下格式返回帐户：每个帐户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。
accounts 本身可以以任意顺序返回。

例子 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
["John", "johnnybravo@mail.com"],
["John", "johnsmith@mail.com", "john_newyork@mail.com"],
["Mary", "mary@mail.com"]]

Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
'johnsmith@mail.com'],
["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

Explanation:
  第一个和第三个 John 是同一个人，因为他们有共同的电子邮件 "johnsmith@mail.com"。
  第二个 John 和 Mary 是不同的人，因为他们的电子邮件地址没有被其他帐户使用。
  我们可以以任何顺序返回这些列表，例如答案[['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
  ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']]仍然会被接受。

注意：
accounts的长度将在[1，1000]的范围内。
accounts[i]的长度将在[1，10]的范围内。
accounts[i][j]的长度将在[1，30]的范围内。
"""


class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        da = {}
        al = len(accounts)
        access = [0] * al
        result = []

        for i, ac in enumerate(accounts):
            tmp = ac[1:]
            for a in tmp:
                if a in da:
                    da[a].append(i)
                else:
                    da[a] = [i]

        for j in range(al):
            if access[j] == 1:
                continue
            else:
                queue = [j]
                mailset = set()
                while len(queue) > 0:
                    idx = queue[0]
                    queue.pop(0)
                    access[idx] = 1
                    mails = accounts[idx][1:]
                    for mail in mails:
                        mailset.add(mail)
                        for t in da[mail]:
                            if access[t] == 1:
                                continue
                            else:
                                queue.append(t)
                                access[t] = 1
                tmp = [accounts[j][0]]
                tmp.extend(sorted(list(mailset)))
                result.append(tmp)
        print(result)


s = Solution()
s.accountsMerge([["John", "johnsmith@mail.com",
                  "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                 ["John", "johnsmith@mail.com",
                  "john_newyork@mail.com"], ["Mary", "mary@mail.com"],
                 ["John", "johnsmith@mail.com", "johnnybravo@mail.com"]])
"""
此题解法：
* 首先使用一个字典da来记录相同邮件以及对应索引的list
* 在定义一个与accounts等长的List来存放accounts中每个元素是否被访问。
* 计算accounts的长度 al
* 建立一个循环，range（al）
    * 如果 access[j]==1 （访问过了，就跳到下一个循环）
    * 建立一个队列queue，初始化就是queue[j]
    * 建立一个while循环，直到queue空了为止
    * 从queue的头部取出一个值，并且在access中将这个索引位标记成已访问（1）
    * 用这个idx从accounts中取出对应的邮件account[idx][1:]
      把邮件地址放入set中
    * 在字典da里遍历这个mails的每一个mail，将对应的da[mail]的索引值取出来放入queue去
    * 通过这个while就就可以将da.values()中有交集的都凑在一起。
    * 完成一个while循环后就可以将对应的账户名和邮件地址记录到result中
"""
