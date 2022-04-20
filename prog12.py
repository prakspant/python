#program to find smallest and largest number among a set of number
smallest = None
largest = None
while True:
    x = input('Enter a number: ')
    if x == 'done' or x == 'Done':
        break
    try:
        num = float(x)
        if smallest is None:
            smallest = num
        elif smallest > num:
            smallest = num
        if largest is None:
            largest = num
        elif largest < num:
            largest = num
        print('Enter Done to find out the smallest and largest number. ')
    except:
        print('Please enter a valid input: ')
print('Smallest = ',smallest,'Largest = ',largest)
