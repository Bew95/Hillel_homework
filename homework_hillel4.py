import random
import string

print('#1 -------------------------------------------')

my_list_example = ['ewcew', 'qwccqw', 'cew', 'wecew', 'cvfw', 'ecewcwe', 'hpkid']
def return_list(my_list=my_list_example):
    new_list = []
    for id, item in enumerate(my_list):
        if id % 2 != 0:
            new_list.append(item[::-1])
        else:
            new_list.append(item)
    return new_list

print(return_list())

##########################################################
print('#2 -------------------------------------------')
my_list_example1 = ['fwasfs', 'afds', 'ds', 'adda']
def return_a_list(my_list=my_list_example1):
    new_list = []
    for elem in my_list:
        if elem[0] == 'a':
            new_list.append(elem)
    return new_list

print(return_a_list())

##########################################################
print('#3 -------------------------------------------')
my_list_example2 = ['123', 'dsda', '66', 'dcsd', 'asdaa', 'ffAa']
def return_a_include_list(my_list=my_list_example2):
    new_list = []
    for element in my_list:
        if 'a' in element:
            new_list.append(element)
    return new_list

print(return_a_include_list())

##########################################################
print('#4 -------------------------------------------')
my_list_example3 = ['adada', 1341, 'dadq', 6622, 'rw', 754]
def return_str_list(my_list=my_list_example3):
    new_list = []
    for element in my_list:
        if type(element) == str:
            new_list.append(element)
    return new_list

print(return_str_list())

##########################################################
print('#5 -------------------------------------------')
my_list_example4 = 'Hello Hillel, my name is Ivan!'
def list_1symbol(my_str=my_list_example4):
    new_list = []
    for letter in set(my_str):
        if my_str.count(letter) == 1:
            new_list.append(letter)
    return new_list

print(list_1symbol())

##########################################################
print('#6 -------------------------------------------')

my_str11 = 'saccdcnjnlclakscnlkd'
my_str22 = 'sanconlaxklsamxlkvml'
def create_list_2symbol(my_str1=my_str11, my_str2=my_str22):
    set1_ = set(my_str1)
    set2_ = set(my_str2)
    new_list = list(set1_.intersection(set2_))
    return new_list

print(create_list_2symbol)

##########################################################
print('#7 -------------------------------------------')

new_str111 = 'ak,nccfffsc'
new_str222 = 'dfdcxdamdxxscc'
def create_list_justonetime_symbol(new_str1=new_str111, new_str2=new_str222):
    result = []
    for symbol in set(new_str1):
        if new_str1.count(symbol) == 1 and new_str2.count(symbol) == 1:
            result.append(symbol)
    return create_list_justonetime_symbol

print(create_list_justonetime_symbol())

##########################################################
print('#8 -------------------------------------------')

names = ['pablo', 'escobar', 'narco']
domains = ['com', 'ru', 'ua', 'net']


def create_email():
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(random.randint(5, 7)))
    generating = f'{random.choice(names)}.{random.randint(100, 999)}@{rand_string}.{random.choice(domains)}'
    return generating

print(create_email())




