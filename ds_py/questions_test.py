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
two_sum(alist, 7)


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
                return (str(alist[i])+","+str(alist[j]))
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


# dictionaries
def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}

def sum_product(input_tuple):
    sum_result = 0
    product_result = 1
    for i in input_tuple:
        sum_result += i
        product_result *= i    

    return sum_result, product_result

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

def char_count(string):
    # create an object to return at the end
    result = {}
    
    # loop through the string
    for i in string.lower():
        # if the char is in the result, add 1 to the result value
        if isinstance(i, str) and not (i.isspace()):
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
    # return the result
    return result
            
print(char_count('Heh ll oo'))

        
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return int(n%10) + sum_of_digits(int(n//10))
    
print(sum_of_digits(114))

def find_biggest_number(ll):
    biggest_num = ll[0]
    for i in range(1, len(ll)):
        if ll[i] > biggest_num:
            biggest_num = ll[i]
    return biggest_num
    
print('biggest_num', find_biggest_number([9,1,2,11,34,55]))

def power(b, e):
    assert int(e) == e, 'The exp must be integer'
    if e == 0:
        return 1
    elif e < 0:
        return 1/b * power(b, e+1)
    else:
        return b * power(b, e-1)
    
print(power(4.3,-4))
        
def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The gcd nums must be integer'
    if a < 0:
        a = -1 * a
    if b == 0:
        return a
    else:
        return gcd(b, a%b) 
    
print(gcd(-48, 18))

def decimal_to_binary(n):
    assert int(n) == n, 'The parameter should be integer'
    if n == 0:
        return 0
    return n%2 + 10 * decimal_to_binary(int(n/2))

print(decimal_to_binary(12))

