import math

# Volumes and surfaces of shapes ________________________
cube_h = 25 / 7
cube_w = 25 / 2
cube_l = 35
cone_h = 10
cone_r = 3

print("\u0332".join("Volumes and Surfaces of Shapes"))
print(f'Cuboid volume = {cube_l * cube_w * cube_h:,.2f}')
print(f'Cuboid surface area = {2 * ((cube_l * cube_w) + (cube_l * cube_h) + (cube_w * cube_h)):,.2f}')
print(f'Cone volume = {(math.pi * (cone_r ** 2) * (cone_h / 3)):,.2f}')
print(f'Cone surface area = {math.pi * cone_r * (cone_r + math.sqrt((cone_h ** 2) + (cone_r ** 2))):,.2f}')
print("")

# Group's Shopping Bills_______________________________
housemates = 5
tomato = {'cost': 1, 'unit': 'pack(s)', 'per_capita_consumption': 1}
sponge = {'cost': 2, 'unit': 'unit(s)', 'per_capita_consumption': 3}
juice = {'cost': 3, 'unit': 'ltr(s)', 'per_capita_consumption': 1}
foil = {'cost': 4, 'unit': 'mtr(s)', 'per_capita_consumption': 20}
sugar = {'cost': 5, 'unit': 'gram(s)', 'per_capita_consumption': 180}

total_per_mate = (tomato['cost'] * tomato['per_capita_consumption']) + (
        sponge['cost'] * sponge['per_capita_consumption']) + (juice['cost'] * juice['per_capita_consumption']) + (
                         foil['cost'] * foil['per_capita_consumption']) + (
                         sugar['cost'] * sugar['per_capita_consumption'])

total = housemates * total_per_mate

total_incl_vat = total * 1.20
print("\u0332".join("Groups Shopping Bills"))
print(f"Total including Vat is: ${total_incl_vat:,.2f}")
print(f"Total excluding Vat is: ${total:,.2f}")
print(f"Cost per housemate excluding Vat is: ${total_per_mate:,.2f}")
print("")

# String Length _________________________________________

long_word = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
first_c = long_word[0]
last_c = long_word[-1]

print("\u0332".join("String Length"))
print(f'Length of long_word = {len(long_word)}')
print(f'First character of long_word is "{first_c}"')
print(f'The combination of the last and first character of long_word is "{last_c + first_c}"')
print("")

# Basic arithmetic _________________________________________
a = 42
b = 25

print("\u0332".join("Basic Arithmetic"))
print(f'sum of a and b = {a + b}, and the type is {type(a + b)}')
print(f'difference of a and b = {a - b}')
print(f'product of a and b = {a * b}')
print(f'division of a by b = {a / b}')
a = 4.2
print(f'sum of a and b = {a + b}, and the type is {type(a + b)}')
print("")

# Calculate shopping bills _________________________________________
tomato_base_cost = 0.87  # skipping currency and weight unit variables
tomato_base_vol = 6
sugar_base_cost = 1.09
sugar_base_vol = 0.5
sponge_base_cost = 0.29
sponge_base_vol = 10
juice_base_cost = 1.89
juice_base_vol = 1.5
foil_base_cost = 1.29
foil_base_vol = 30

print("\u0332".join("Calculate Your Shopping Bills"))
print(f'The price of 1kg of sugar is GBP {sugar_base_cost / sugar_base_vol * 1}.')
print(
    f'The price of 20 washing sponges is GBP {sponge_base_cost / sponge_base_vol * 20}, 3l of juice is GBP {round(juice_base_cost / juice_base_vol * 3, 2)}, and 2 packs of tomatoes is GBP {tomato_base_cost / tomato_base_vol * 2}.')
print("")

# Exercises on numbers _________________________________________
x = 1044.75 / 100 * 10 + 1 - 0.1

print("\u0332".join("Exercise on Numbers"))
print(f"({1044.75} + 1 - 1) / 1 * 1) = {(1044.75 + 1 - 1) / 1 * 1}")
print(f"({x} + 0.1 - 1) / 10 * 100) = {(x + 0.1 - 1) / 10 * 100}")
print("")

# Variable Assignment & Re-assignment __________________________
num_1 = 37
num_2 = 52
print("\u0332".join("Variable Assignment & Re-assignment"))
print(f'The sum of num_1 and num_2 is {num_1 + num_2}, and the product is {num_1 * num_2:,}.')
num_1 = 8
num_2 = 3
print(f'The new sum of num_1 and num_2 is {num_1 + num_2}, and the new product is {num_1 * num_2:,}.')
print("")

# Different Variable Types _____________________________________
num_x = 23
text_num_x = "57"
decimal_num_x = 98.3
sum_x = num_x + int(text_num_x) + decimal_num_x

print("\u0332".join("Different Variable Types"))
print(
    f'The variable type of num_x is {type(num_x)}, of text_num_x is {type(text_num_x)}, and decimal_num_x is {type(decimal_num_x)}.')
print(f'The sum of the variables is {sum_x}, and the type is {type(sum_x)}.')
print("")

# Printing Multiple Variables _____________________________________
print("\u0332".join("Printing Multiple Variables"))

all_values = [10, 20, 30, 40, 50, 5, 64, 8, 9, 1, 6, 7, 49, 39, 10, 56, 87, 4]
even_values = ""

for item_v in all_values:
    if item_v % 2 == 0:
        even_values += str(item_v)
        even_values += ", "

even_values = even_values[0:-2]
print('These are my even numbers: ' + even_values + '.')
print("")

# Username List _____________________________________
usernames = ['a', 'bb', 'ccc', 'dddd', 'eeeee']

print("\u0332".join("Username List"))
print('The type of usernames is', type(usernames))
print('The length of usernames is', len(usernames))
print('The type of the first item in usernames is', type(usernames[0]))
print('The length of the last item in usernames is', len(usernames[-1]))
print("")

# Letter Checker and String Reverse _____________________________________
phrase_1 = 'Clean Couch'
phrase_2 = 'Giant Table'
print("\u0332".join("Letter Checker and String Reverse"))
print('Phrase_1 is', phrase_1, 'and Phrase_2 is', phrase_2)
print('For phrase_1, the 1st letters of the two words are the same?', phrase_1.split()[0][0] is phrase_1.split()[1][0])
print('For phrase_2, the 1st letters of the two words are the same?', phrase_2.split()[0][0] is phrase_2.split()[1][0])

my_string1 = 'This is a short phrase'
my_string2 = 'This is actually a significantly longer phrase than the previous one'
list_string1 = my_string1.split(' ')
list_string2 = my_string2.split(' ')

list_string1.reverse()
list_string2.reverse()

print('The reverse of my_string1 is "', " ".join(list_string1), '".')
print('The reverse of my_string2 is "', " ".join(list_string2), '".')
print("")

# List Elements _____________________________________
list_1_child = [1, 2.89, 'random', True, ['x', 'y', 'z']]
list_2_child = [0] * 10
list_parent = [list_1_child, list_2_child]
list_new_child = [list_1_child[3], list_2_child[3]]

print("\u0332".join("List Elements"))
print('List 1 and 2 nested in a new list is', list_parent)
print('The list of the fourth element of list 1 and list 2 is', list_new_child)
print("")

# Car Number Plate Year _____________________________________
num_plates = ["G06 WTR", "WL11 WFL", "QW68 PQR"]
plate1_year = num_plates[0].split()[0][-2:]
plate2_year = num_plates[1].split()[0][-2:]
plate3_year = num_plates[2].split()[0][-2:]

print("\u0332".join("Car Number Plate Year"))
print('The last two characters of the first word in the number plates is: ', f"{plate1_year, plate2_year, plate3_year}")
print('The years converted to int in order are: ', f"{int(plate1_year)}, {int(plate2_year)}, {int(plate3_year)}")
print("")

# Name Character Insertion __________________________________
name1_nci = 'John Doe'
name2_nci = 'Jane Doe'

name1_set = set(name1_nci.lower())
name2_set = set(name2_nci.lower())

print("\u0332".join("Name Character Insertion"))
print("Names 1 and 2 are: ", name1_nci, 'and', name2_nci)
print('The common characters between name 1 and 2 are: ', name1_set.intersection(name2_set))
print("")

# Multiplying List Elements _____________________________________
list_mle = [0] * 10

print("\u0332".join("Multiplying List Elements"))
print('The length of the set made from the list of 10 zeroes is: ', len(set(list_mle)))
print("")

# Comprehensions _____________________________________
list_comp = ['Hello', 'world']
list_comp_upper = [x.upper() for x in list_comp]
num_list_comp = list(range(0, 101))
new_num_list_comp = [x_c for x_c in num_list_comp if x_c % 5 != 0]
dict_squares = {sqr: (sqr ** 2) for sqr in range(1, 16)}
dict_squares_inv = {(key_2, key_1) for key_1, key_2 in dict_squares.items()}

dict_comp_1 = {'name': 'john doe', 'age': 25, 'sex': 'male'}
dict_comp_2 = {'name': 'jane doe', 'age': 23, 'sex': 'female'}
dict_comp_3 = {'name': 'jimmy doe', 'age': 2, 'sex': 'male'}
list_of_dict = [dict_comp_1, dict_comp_2, dict_comp_3]
new_mapped_list = [map_key['name'] for map_key in list_of_dict]
print("\u0332".join("Comprehensions"))
print(new_mapped_list)
print('The new list with all characters capitalized is:', list_comp_upper)
print(num_list_comp)
print(new_num_list_comp)
print(dict_squares)
print(dict_squares_inv)
print(list_of_dict)
print(type(list_of_dict))
print(new_mapped_list)
print("")

# Simple Typed Function _____________________________________
new_list_for_function = list(['what'] * 10)


def len_of_list_function(list_for_function):
    sum_list_for_function_len = sum(len(list_item_f) for list_item_f in list_for_function)
    return sum_list_for_function_len


print("\u0332".join("Simple Typed Function"))
print(f'Sum of the length of all the words in the list is {len_of_list_function(new_list_for_function)}.')
print(f'The type of the input is {type(new_list_for_function)}, and the type of the output is {type(len_of_list_function(new_list_for_function))}.')
print("")

# Going Deep! _____________________________________
one_deep_dictionary = {'start here':1,'k1':[1,2,3,{'k2':[1,2,{'k3':['keep going',{'further':[1,2,3,4,[{'k4':'Python'}]]}]}]}]}

print("\u0332".join("Going Deep!"))
print(one_deep_dictionary['k1'][3]['k2'][2]['k3'][1]['further'][4][0]['k4'])
print("")

# Comparing Different Data Types _____________________________________

print("\u0332".join("Comparing Different Data Types"))
print(False < True)
print("")

# XOR Gate _____________________________________
def xor_function(xor_a, xor_b):
    xor_xor = (xor_a or xor_b == 1) and ((xor_a and xor_b == 1) != 1) == 1
    return xor_xor


print("\u0332".join("XOR Gate"))
print('a = 0, b = 0:',xor_function(0,0))
print('a = 1, b = 0:',xor_function(1,0))
print('a = 0, b = 1:',xor_function(0,1))
print('a = 1, b = 1:',xor_function(0,0))
print("")

# Comparing Strings & Integers _____________________________________
print("\u0332".join("Comparing Strings"))
print(f"'AAA' > 'BBB': {'AAA' > 'BBB'}")
print(f"'AAB' > 'AAA': {'AAB' > 'AAA'}")
print(f"'aaa' > 'AAA': {'a' > 'A'}")
print("")

my_x = 10
# my_n = int(input('Enter value of "my_x":'))
my_n = 20
if my_n > my_x:
    print(f'{my_n} is greater than {my_x}.')
else:
    print(f'{my_n} is not greater than {my_x}.')
print("")

# Shopping Cost Using Indexing _____________________________________
shop_dict = {'tomatoes' : 18, 'sponges' : 2, 'juice' : 4.5, 'foil' : 4, 'sugar' : 2}
shop_dict['prices'] = {'tomatoes' : 0.87, 'sponges' : 0.29, 'juice' : 1.89, 'foil' : 1.29, 'sugar' : 1.09}
shop_dict['pack_sizes'] = {'tomatoes' : 6, 'sponges' : 10, 'juice' : 1.5, 'foil' : 30, 'sugar' : 0.5}

order_cart = {'tomatoes' : 12, 'sponges' : 20, 'juice' : 1.5, 'foil' : 60, 'sugar' : 1}
order_subtotal = {}

for order_item, order_qty in order_cart.items():
    order_subtotal[order_item] = round(order_qty / shop_dict['pack_sizes'][order_item] * shop_dict['prices'][order_item], 2)

order_total = sum(order_subtotal.values())

print("\u0332".join("Shopping Cost Using Indexing"))
print('Your order total is:')
for key_x, val_y in order_subtotal.items():
    print('For ', order_cart[key_x], key_x, ' : GBP ', val_y)
print('Order total excluding VAT: GBP', order_total)
print('Order total including VAT: GBP', round(order_total * 1.2, 2))
print("\n\n")
print("END OF PRACTICE WORKBOOK.")
print("\n\n")
# python ma_practical_m1.py
