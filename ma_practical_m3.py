# Initializing Sets ---------------------------------------------------
print("\u0332".join("Initializing Sets"))

my_set_1 = {1, 2, 4, 4, 4, 6, 8, 9}
print(my_set_1)
my_set_2 = set([12, 44, 4, 8, 10, 10, 11, 12])
print(my_set_2)
set_x = set()
set_x.add(25)
print(set_x)
set_x.add(12)
print(set_x)
set_x.add(25)
print(set_x)

for set_item in my_set_1:
    print(set_item)
print('\n')

# Find the Min and Max Value in a Set ---------------------------
print("\u0332".join("Find the Min and Max Value in a Set"))

set_int = {8, 16, 24, 1, 25, 3, 10, 65, 55} 
set_str = {'f', 'l', 'k', 'a', 'w'}
set_int_2 = {4, 12, 10, 9, 4, 13} 
set_str_2 = {'b', 'z', 't', 'm', 'y', 'c'}

print(f'{set_int} max value: {max(set_int)}')
print(f'{set_str} max value: {max(set_str)}')
print(f'{set_int_2} min value: {min(set_int_2)}')
print(f'{set_str_2} min value: {min(set_str_2)}')
print('\n')

# Adding Items to a Set -----------------------------------------
print("\u0332".join("Adding Items to a Set"))

prime_numbers = {3, 5, 7, 11, 13}
num_list = [num_item for num_item in range(10,51)]
print(num_list)
p_num_list = []

for num_check in num_list:
    for p_num_chkr in range(2, num_check):
        if num_check % p_num_chkr == 0:
            break
        elif p_num_chkr == num_check - 1:
            p_num_list.append(num_check)
print(p_num_list)
print(prime_numbers)
prime_numbers.update(p_num_list)
print(prime_numbers)
print('\n')

# Mathematical Operations ---------------------------------------
print("\u0332".join("Mathematical Operations"))

set1 = {15, 25, 35, 45, 55} 
set2 = {35, 45, 55, 65, 75}

set_intersection = set1.intersection(set2)
print(set_intersection)

set_union = set1.union(set2)
print(set_union)

set_sy_difference = set1.symmetric_difference(set2)
print(set_sy_difference)
print('\n')

# Finding missing & additional items ---------------------------------------
print("\u0332".join("Finding Missing & Additional Items"))
# Print the missing & additional items in list1 (hint: convert list to a set)
# Print the missing & additional items in list2

list1 = [1, 2, 3, 4, 5, 6, 7, 8] 
list2 = [5, 6, 7, 8, 9, 10, 11, 12]

conv_to_set1 = set(list1)
conv_to_set2 = set(list2)

missing_in_list1 = conv_to_set2.difference(conv_to_set1)
additional_in_list1 = conv_to_set1.difference(conv_to_set2)
print(missing_in_list1)
print(additional_in_list1)

missing_in_list2 = conv_to_set1.difference(conv_to_set2)
additional_in_list2 = conv_to_set2.difference(conv_to_set1)
print(missing_in_list2)
print(additional_in_list2)
print('\n')

# Lists and Sets ------------------------------------------------
print("\u0332".join("Lists and Sets"))

new_list1 = [1, 5, 10, 20, 40, 80] 
new_list2 = [6, 7, 20, 80, 100] 
new_list3 = [3, 4, 15, 20, 30, 70, 80, 120]

new_set1 = set(new_list1)
new_set2 = set(new_list2)
new_set3 = set(new_list3)

overall_inter = new_set1.intersection(new_set2, new_set3)
print(overall_inter)

print("\n\n")
print("END OF PRACTICE WORKBOOK.")
print("\n\n")

# python ma_practical_m3.py