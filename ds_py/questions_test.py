def two_sum(alist, target):
    pairs_list = []
    for i in range(len(alist)):
        for j in range(i+1, len(alist)):
            if alist[i] == alist[j]:
                continue
            if alist[i] + alist[j] == target:
                pairs_list.append(f"{alist[i]}+{alist[j]}")
                print(f"{alist[i]} + {alist[j]}")
    print('pairs_list', pairs_list)
alist = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
# two_sum(alist, 7)


def contains_duplicate(nums):
    # TODO
    duplicates_list = []
    for i in range(len(nums)):
        duplicates_list.append(i)
        if i in duplicates_list:
            print(i)
        
nums = [1,2,3,1]
contains_duplicate(nums)

def print_unordered_list(alist):
    for i in range(len(alist)):
        for j in range(len(alist)):
            if alist[i] < alist[j]:
                print(str(alist[i])+","+str(alist[j]))
alist = [3,4,5,7,1,2]
print_unordered_list(alist)

def reverse(alist):
    for i in range(0, int(len(alist)/2)):
        prev = len(alist)-i-1
        tmp = alist[i]
        alist[i] = alist[prev]
        alist[prev] = tmp
    print(alist)
alist2 = [1,2,3,4,5]
reverse(alist2) 
    
        
        