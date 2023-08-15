import random
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
   
# dictionaries .py 
def dict_search(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return ('the value do not exist in the dictionary')

mydict = {'name':'leo', 'age':26}
print(dict_search(mydict, 26))

city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']

new_temps = {city: random.randint(20, 30) for city in city_names}
print(new_temps)

new_dict = {city: temp for (city, temp) in new_temps.items() if temp > 25}
print('new_dict', new_dict)

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

def count_words_frequency(words):
    count_words = {}
    for i in words:
        count_words[i] = count_words.get(i, 0) + 1
    return count_words  
print(count_words_frequency(words))

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result
                
print(merge_dicts(dict1, dict2))
