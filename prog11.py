# Copied programme from online
count = 0
total = 0
avg = 0
largest = None
smallest = None
keepgoing = True
while keepgoing:
  prompt1 = 'Enter a number \n'
  line = input(prompt1)
  try:
     line = float(line)
     count = count + 1
     total = total + line
     avg = total / count
     if smallest is None or line < smallest:
      smallest = line
     if largest is None or line > largest:
      largest = line
  except:
    if line == 'Done' or line == 'done':
      break
    else:
      print('Invalid Input')
      continue
print(count, largest, smallest)
