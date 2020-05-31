x=eval(input('Enter a positive integer larger than 1: '))
print('The factors of',x,'are:\n')
for i in range(1, x+1):
    if x % i == 0:
        print(i)
print('\nDONE')