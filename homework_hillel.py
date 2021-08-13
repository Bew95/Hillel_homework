value = 12
new_value = value / 2 if value < 100 else value * -1
print(new_value)

#####################################################
value = 103
new_value = value = 1 if value < 100 else 0
print(new_value)

#####################################################
value = 30
new_value = value = True if value < 100 else False
print(new_value)

#####################################################
my_str = "jdsjksjqdkqnd"
my_str = my_str[::2]
print(my_str)

#####################################################
my_str = "sdvdfv"
my_str = my_str * 2 if len(my_str) < 5 else my_str
print(my_str)

#####################################################
my_str = "dsc"
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_str)