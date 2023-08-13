def two_sum(alist, target):
    for i in range(len(alist)):
        for j in range(i+1, len(alist)):
            if alist[i] == alist[j]:
                continue
            if alist[i] + alist[j] == target:
                print(i, j)
alist = [1,2,3,2,3,4,5,6]
two_sum(alist, 9)
