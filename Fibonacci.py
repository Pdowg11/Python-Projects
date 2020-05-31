def fibonacci(num):
    a, b=0,1
    print('Sequence: ', a, b, end=' ')
    for x in range(0, num-2):
        c=a+b
        print(a+b,end=' ')
        a=b
        b=c
    return

#Main Program

print('I will display the Fibonacci Sequence.')
y='Y'
while y == 'Y':
    n=eval(input('How many terms? Enter an integer greater than 2: '))
    fibonacci(n)
    y= input('\nTry again? Y or N: ').upper()
print('\nDONE')