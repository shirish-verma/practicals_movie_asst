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

# Order of Conditions -------------------------------------------
print("\u0332".join("Flight Safety Checker"))

x = input('Enter a number: ')

if x > 0:
    print('x is greater than 0')
elif x > 15:
    print('x is greater than 15')
elif x > 20: 
    print('x is greater than 20')
else:
    print('x is less than 0')

