num = 0
tot = 0.0
while True:
    try:
        sval = input('Enter a number: ')
        if sval == 'done':
            break
        fval = float(sval)
        num = num + 1
        tot = tot + fval
    except:
        print('Invalid Input')
        continue
try:
    print('Sum = ',tot,'Average = ',tot/num,'Count = ',num)
except:
    print('No numbers entered')
