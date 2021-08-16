number = 4930482084027100000
nul = str(number).count('0')
print(nul)

##################################################
number = 1488008000888880000000000
if number == 0:
    print(1)
    exit()

countZero = 0
while (number % 10 == 0):
    number //= 10
    countZero += 1
print(countZero)

##################################################
my_list_1 = [1331, 44, 63, 248, "313", "jfsfkj"]
my_list_2 = ["fwfs", 331, [123], 'rqq']
my_result = my_list_1[::2] + my_list_2[::2]
print(my_result)

##################################################
my_list = [1, 3, 6, 7, 'fs']
my_list.append(my_list[0])
my_list.remove(my_list[0])
new_list = my_list
print(new_list)

##################################################
my_list = [1, 2, 3, 4, 5]
my_list.append(my_list.pop(0))
print(my_list)

##################################################
string = '16 красивее чем 22'
probel = string.split(' ')
count_number = 0
for element in probel:
    try:
        value = int(element)
        count_number += value
    except:
        pass
print(count_number)

##################################################
string = 'ajkcazc djnjk123  rvkj4 1lnjkl14 l1nlmv1 42 1 vtrv '
l_limit = 'z'
r_limit = 'm'
sub_str = string[string.index(l_limit) + 1: string.index(r_limit)]
print(sub_str)
# немного не понял задание, возможно сделал что-то не так

##################################################
my_str = 'cnlksdc'
if len(my_str) % 2 == 0:
    n = 2
    my_result = [my_str[i:i+n] for i in range(0, len(my_str), n)]
    print(my_result)
else:
    my_str = my_str + "_"
    n = 2
    my_result = [my_str[i:i + n] for i in range(0, len(my_str), n)]
    print(my_result)

##################################################
number_list = [2, 4, 1, 5, 3, 9, 0, 7]
counter = 0
for i in range(1, len(number_list) - 1):
    if number_list[i - 1] < number_list[i] > number_list[i + 1]:
        counter += 1
print(counter)














