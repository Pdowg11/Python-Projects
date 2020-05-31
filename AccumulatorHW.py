x=eval(input("Enter a positive integer larger than 1: "))
sum=0
fact=1
print('\nSum:')
for i in range(1,x+1):
    sum=sum+i
print(sum)
print('\nFactorial:')
for i in range(1,x+1):
    fact=fact*i
print(fact)
print('\nDONE')