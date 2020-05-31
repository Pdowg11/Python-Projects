valid=0

#prints fruit list w/out commas and brackets
fruits=['apple','banana','orange','peach','plum','grapes','pear','nectarine','tangerine']
print(' '.join(fruits))
x=input('Please add a fruit not in the above list: ')

#dummy code to not allow fruit already in list
while valid==0:
    if x in fruits:
        print('Thats already in the list!')
        x=input('Please add a fruit not in the above list: ')
    else:
        fruits.append(x.lower())
        fruits.sort()
        valid=1
print('\n'+' '.join(fruits)+'\n')
for i in fruits:
    if i.startswith('p'):
        print(i)
print('\nDONE')