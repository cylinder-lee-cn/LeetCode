alist = [1, 2, 3]
result = [[]]

for a in alist:
    temp = []
    for r in result:
        temp.append(r.append(a))
        print(temp)

print(result)

# [[],[1],[2],[3],[1,2]...]