# Milestone 5, Practicals - Try & Except ------------------------

try:
    with open('test.txt') as test_file:
        test_data = test_file.read()
        print(test_data)
except Exception as test_error:
    print('File not found!')
    print(test_error)
    with open('test.txt', 'w') as file:
        file.write('Hello, I am a file!')

while True:
    try:
        input_1 = input('Enter a number: ')
        input_2 = input('Enter another number: ')
        int_1 = int(input_1)
        int_2 = int(input_2)
        print(int_1 / int_2)
        print('No errors were raised.')
        break
    except ValueError:
        print('You must enter a number.')
    except ZeroDivisionError:
        print('You cannot divide by zero.')
    except KeyboardInterrupt:
        print('You pressed Ctrl+C.')
