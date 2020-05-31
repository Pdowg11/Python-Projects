valid=0
while valid == 0:
    response = eval(input('Enter Y to continue, N to stop: '))
    response = str.upper(response)
    if response != 'Y' and response != 'N':
        print('Invalid input, try again.')
    else:
        valid=1
print('Program continues')