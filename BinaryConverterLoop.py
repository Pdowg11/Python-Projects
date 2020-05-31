#inputs integer, outputs binary - using a FOR loop
x=eval(input('enter a positive integer < 256: '))
divisor=128

for y in range(0,8):
    print(x//divisor,end='')
    x=x-(x//divisor)*divisor
    divisor=divisor//2
print('\nDONE')