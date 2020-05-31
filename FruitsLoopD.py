valid=0
fruits=['apple','banana','orange','peach','plum','grapes','pear','nectarine','tangerine']
print(' '.join(fruits))
x=input('Please add a fruit not in the above list: ')
while valid==0:
    if x in fruits:
        print('Thats already in the list!')
        x=input('Please add a fruit not in the above list: ')
    else:
        fruits.append(x.lower())
        valid=1
print('\n'+' '.join(fruits)+'\n')
for i in fruits:
    if i.startswith('d'):
        print('The fruits that start with "d" are: '+ i)
        y=0
    else:
       y=1
if y==1:
    print('There are no fruits that start with the letter "d".')