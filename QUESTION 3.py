def uniqueNum(n):
    res = ""
    for i in n:
        count = 0
        for x in n:
            if x == i:
                count += 1

        if count == 1:
            if res == "":
                res = str(i)
            else:
                res = res + "," + str(i)

    return res


list = [2, 3, 5, 4, 5, 3, 2, 8]
print(uniqueNum(list))