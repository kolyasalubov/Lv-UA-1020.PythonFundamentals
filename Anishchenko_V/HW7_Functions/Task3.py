def chars(x):
    dic = {}
    for i in range(len(x)):
        if x[i] not in dic:
            dic[x[i]] = 1
        else:
            dic[x[i]] += 1
    return dic
