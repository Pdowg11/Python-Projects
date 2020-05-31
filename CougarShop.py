def DisplayMenu():
    print('1) Cougar Hoodie-$45.00')
    print('2) Cougar T-Shirt(green)-$20.00')
    print('3) Cougar T-Shirt(gold)-$20.00')
    print('4) Green and Gold Tervis-$15.50')
    print('5) Black and Gold Water Bottle-$18.50')
    print('6) Stuffed Cougar-$12.00')
    return

def PurchaseItems():
    global total,amt,choice,price_list
    choice=1
    choice=eval(input('Choose a number 1-6 to purchase and item: '))
    amt=eval(input('and how many do you want to purchase? '))
    purchase_list[choice-1]=price_list[choice-1]*amt
    amt_list[choice-1]+=amt
    return

def Invoice():
    global purchase_list,amt_list,total,amt,choice
    tax=1.053
    print()
    if purchase_list[0] > 0:
        print('You bought',amt_list[0],'hoodies for $',purchase_list[0])
    if purchase_list[1] > 0:
        print('You bought',amt_list[1],'green t-shirts for $',purchase_list[1])
    if purchase_list[2] > 0:
        print('You bought',amt_list[2],'gold t-shirts for $',purchase_list[2])
    if purchase_list[3] > 0:
        print('You bought',amt_list[3],'green and gold tervis for $',purchase_list[3])
    if purchase_list[4] > 0:
        print('You bought',amt_list[4],'black and gold water bottles for $',purchase_list[4])
    if purchase_list[5] > 0:
        print('You bought',amt_list[5],'stuffed cougars for $',purchase_list[5])
    sub=sum(purchase_list)
    print('\nsubtotal: $',round(sub,2))
    print('tax is 5.3%')
    print('\ntotal is: $',round(sub*tax,2))
    return


#Main Program
price_list=[45.00,20.00,20.00,15.50,18.50,12.00]
purchase_list=[0,0,0,0,0,0]
amt_list=[0,0,0,0,0,0]
print('Welcome to the Cougar Shop!\n')
response='Y'
while response == 'Y':
    DisplayMenu()
    PurchaseItems()
    response=input('\nWould you like to purchase another item? Y or N: ').upper()
Invoice()
print('\nThank you for shopping!')