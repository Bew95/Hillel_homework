my_list = ['ewcew', 'qwccqw', 'cew', 'wecew', 'cvfw', 'ecewcwe', 'hpkid']
new_list = []
for id, item in enumerate(my_list):
    if id % 2 != 0:
        new_list.append(item[::-1])
    else:
        new_list.append(item)
print(new_list)

#########################################################
my_list = ['fwasfs', 'afds', 'ds', 'adda']
new_list = []
for elem in my_list:
    if elem[0] == 'a':
        new_list.append(elem)
print(new_list)

#########################################################
my_list = ['123', 'dsda', '66', 'dcsd', 'asdaa', 'ffAa']
new_list = []
for element in my_list:
    if 'a' in element:
        new_list.append(element)
print(new_list)

#########################################################
my_list = ['adada', 1341, 'dadq', 6622, 'rw', 754]
new_list = []
for element in my_list:
    if type(element) == str:
        new_list.append(element)
print(new_list)

#########################################################
my_str = 'Hello Hillel, my name is Ivan!'
new_list = []
for letter in set(my_str):
    if letter not in new_list:
        new_list.append(letter)
print(new_list)

#########################################################
my_str1 = 'saccdcnjnlclakscnlkd'
my_str2 = 'sanconlaxklsamxlkvml'
set1_ = set(my_str1)
set2_ = set(my_str2)
new_list = [set1_.intersection(set2_)]
print(new_list)

#########################################################
new_str1 = 'ak,nccfffsc'
new_str2 = 'dfdcxdamdxxscc'
result = []
for symbol in set(new_str1):
    if new_str1.count(symbol) == 1 and new_str2.count(symbol) == 1:
        result.append(symbol)
print(result)

#########################################################
new_dict = {'Фамилия': 'Ковальчук',
            'Имя': 'Иван',
            'Возраст': '25',
            'Проживание': {'Страна': 'Украина', 'Город': 'Одесса', "Улица": 'Жемчужная'},
            'Работа': {'Наличие': 'Есть', 'Должность': 'Менеджер по работе с клиентами'}
            }

#########################################################
cake_recipe = {"Коржи": {"Мука": "1 стакан", "Белки": "8 белков", "Сахар": "1.5 стакана", "Орехи": "2 стакана"},
               "Крем": {"Желтки": "8 желтков", "Сахар": "1 стакан", "Молоко": "3/4 стакана", "Сливочное масло": "300гр", "Какао": "2-3ст.л."}
               }

#########################################################
persons = [{'name': 'John', 'age': 15}, {'name': 'Jack', 'age': 15}, {'name': 'Sandra', 'age': 24}]
age = []
for person in persons:
    age.append(person['age'])
min_age = min(age)

for person in persons:
    if person['age'] == min_age:
        print(person['name'])

name = []
for person in persons:
    name.append(person['name'])
max_len_name = max(name)
print(max_len_name)

average_age = sum(age) // len(age)
print(average_age)

#########################################################
my_dict_1 = {1: 12, 2: 34, 4: 5}
my_dict_2 = {1: 21, 22: 2, 4: 5}
keys_list = []
for i in my_dict_1.keys():
    if i in my_dict_2.keys():
        keys_list.append(i)
print(keys_list)

keys_list2 = []
for i in my_dict_1.keys():
    if i not in my_dict_2.keys():
        keys_list2.append(i)
print(keys_list2)

new_dict = {}
for i in my_dict_1.items():
    if i[0] not in my_dict_2:
        new_dict[i[0]] = i[1]
print(new_dict)
new_dict2 = {}
for item in my_dict_1.items():
    if item[0] not in my_dict_2:
        new_dict2[item[0]] = item[1]
    else:
        new_dict2[item[0]] = [item[1], my_dict_2[item[0]]]
for item in my_dict_2.items():
    if item[0] not in my_dict_1:
        new_dict2[item[0]] = item[1]
print(new_dict2)





















