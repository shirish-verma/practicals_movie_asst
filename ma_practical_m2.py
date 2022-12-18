# BMI Checker ---------------------------------------------------
print("\u0332".join("BMI Checker"))

def bmi_checker(height, weight):
    bmi_value = weight / (height ** 2)
    if bmi_value < 18.5:
        print(f'Your BMI is {round(bmi_value, 2)}. You\'re in the underweight range.')
    elif bmi_value <= 24.9:
        print(f'Your BMI is {round(bmi_value, 2)}. You\'re in the healthy weight range.')
    elif bmi_value <= 29.9:
        print(f'Your BMI is {round(bmi_value, 2)}. You\'re in the overweight range.')
    elif bmi_value <= 39.9:
        print(f'Your BMI is {round(bmi_value, 2)}. You\'re in the obese range.')   ## what happens when bmi_value is greater than 39.9?
    else:
        print(f'Your BMI of {round(bmi_value, 2)} is out of range!')

bmi_checker(1.83, 85)
bmi_checker(1.55, 61)
bmi_checker(2.09, 135)
bmi_checker(2.09, 500)
print('')

# Flight Safety Checker -----------------------------------------
print("\u0332".join("Flight Safety Checker"))

def safety_checker(alt, speed):
    if (alt < 100 or alt > 50000) or (speed < 60 or speed >500) is True:
        return 'You are NOT flying safely!'
    else:
        return 'You are flying safely!'
    
print(safety_checker(25000, 300))
print(safety_checker(50001, 250))
print(safety_checker(90, 125))
print('')

# Order of Conditions -------------------------------------------
print("\u0332".join("Order of Conditions"))
# x = int(input('Enter a number: '))
x = 5
if x > 20:
    print('x is greater than 20')
elif x > 15:
    print('x is greater than 15')
elif x > 0: 
    print('x is greater than 0')
else:
    print('x is less than 0')
print('')

# Unique Elements in a List -------------------------------------
print("\u0332".join("Unique Elements in a List"))
my_list = [1, 10, 2, 8 , 56, 23, 19, 0, 11, 1]
my_list_item = 0
unique_list = []

print(f'There are {len(my_list)} items in the list.')

while my_list_item < len(my_list):
    if my_list[my_list_item] in unique_list:
        print('There are duplicate elements.')
        break
    elif my_list_item + 1 == len(my_list):
        print('There are no duplicates!')
        break
    else:
        unique_list.append(my_list[my_list_item])
    my_list_item += 1
 
# Simple Rock Paper Scissors (+ Rounds) -------------------------
print("\u0332".join("Simple Rock-Paper-Scissors"))
# valid_inputs = ['rock', 'paper', 'scissor', 'scissors']
# srps_playr_1 = input("Player 1: Rock, Paper or Scissor? >> ").lower()
# while srps_playr_1 not in valid_inputs:
#    srps_playr_1 = input("Player 1: Invalid input. Please enter either rock, paper or scissor. Inputs are not case sensitive. >> ").lower()

# srps_playr_2 = input("Player 2: Rock, Paper or Scissor? >> ").lower()
# while srps_playr_2 not in valid_inputs:
#    srps_playr_2 = input("Player 2: Invalid input. Please enter either rock, paper or scissor. Inputs are not case sensitive. >> ").lower()

def r_p_s_game(playr_1, playr_2):
    valid_inputs = ['rock', 'paper', 'scissor', 'scissors']
    if playr_1 not in valid_inputs or playr_2 not in valid_inputs:
        return f'Player 1 entered "{playr_1}" and Player 2 entered "{playr_2}". Invalid input.'
    elif playr_1 == playr_2:
        return f'Player 1 entered "{playr_1}" and Player 2 entered "{playr_2}". Its a tie!'
    elif (playr_1 == 'rock' and playr_2 == 'scissor') or (playr_1 == 'paper' and playr_2 == 'rock') or (playr_1 == 'scissor' and playr_2 == 'paper'):
        return f'Player 1 entered "{playr_1}" and Player 2 entered "{playr_2}:. Player 1 Wins!'
    else:
        return f'Player 1 entered "{playr_1}" and Player 2 entered "{playr_2}". Player 2 Wins!'

num_playr_1_wins = 0
num_playr_2_wins = 0

# while (num_playr_1_wins or num_playr_2_wins) < 3:
#     round_playr_1 = input("Player 1: Rock, Paper or Scissor? >> ").lower()
#     round_playr_2 = input("Player 2: Rock, Paper or Scissor? >> ").lower()
#     round_result = r_p_s_game(round_playr_1, round_playr_2)
#     print(round_result)
#     if 'invalid input' in round_result.lower():
#         continue
#     elif 'player 1 wins' in round_result.lower():
#         num_playr_1_wins += 1
#     elif 'player 2 wins' in round_result.lower():
#         num_playr_2_wins += 1

# if num_playr_1_wins == 3:
#     print('Player 1 is the Champion!')
# else:
#     print('Player 2 is the Champion!')
    
    
print(r_p_s_game('scissor', 'paper'))
print(r_p_s_game('scissors', 'rock'))
print(r_p_s_game('paper', 'paper'))
print(r_p_s_game('rock', 'lizzard'))
print('')

# Counting Numbers ----------------------------------------------
print("\u0332".join("Counting Numbers"))
count_x = 0

while count_x < 50:
    count_x += 1
    print(count_x)

for cn_item in range(1, 51):
    print(cn_item)

print('')

# Counting Even Numbers -----------------------------------------
print("\u0332".join("Counting Even Numbers"))
even_count = 0

while even_count < 50:
    even_count += 1
    if even_count % 2 == 0:
        print(even_count)

for cn_even_item in range(1, 51):
    if cn_even_item % 2 == 0:
        print(cn_even_item)

print('')

# Counting Even & Odd Numbers -----------------------------------
print("\u0332".join("Counting Even & Odd Numbers"))
sum_even_num = 0
sum_odd_num = 0

for even_num in range(1,101):
    if even_num % 2 == 0:
        sum_even_num += even_num
print(sum_even_num)

for odd_num in range(1,101):
    if odd_num % 2 != 0:
        sum_odd_num += odd_num
print(sum_odd_num)      
print('')

# FizzBuzz ------------------------------------------------------
print("\u0332".join("FizzBuzz"))

for fbuzz_item in range(1, 101):
    if fbuzz_item % 3 == 0 and fbuzz_item % 5 == 0:
        print('for {} the print is FizzBuzz'.format(fbuzz_item))
        continue
    if fbuzz_item % 3 == 0:
        print('for {} the print is Fizz'.format(fbuzz_item))
    elif fbuzz_item % 5 == 0:
        print('for {} the print is Buzz'.format(fbuzz_item))

# Rock Paper Scissors with Rounds ------------------------------------------------------
print("\u0332".join("FizzBuzz"))

