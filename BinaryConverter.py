#inputs integer, outputs binary
x=eval(input('enter a positive integer < 256: '))

print(x//128,end="")
x=x-(x//128*128)

print(x//64,end="")
x=x-(x//64*64)

print(x//32,end="")
x=x-(x//32*32)

print(x//16,end="")
x=x-(x//16*16)

print(x//8,end="")
x=x-(x//8*8)

print(x//4,end="")
x=x-(x//4*4)

print(x//2,end="")
x=x-(x//2*2)

print(x)
print('Done')
