def deposit():
    global balance, deposit_list
    amt=eval(input('How much to deposit? '))
    balance = balance+amt
    deposit_list.append(amt)
    return

def withdrawl():
    global balance, withdrawl_list
    amt=eval(input('How much to withdrawl? '))
    if amt > balance:
        print('Request Declined. Insufficient Funds.')
    else:
        balance = balance-amt
        withdrawl_list.append(amt)
    return

def activity():
    global balance,deposit_list,withdrawl_list
    if len(deposit_list) > 1:
        print("\nyou've made",len(deposit_list),"deposits, and they are:")
        for item in deposit_list:
            print('$','%.2f' % round(item,2))
    else:
        print("\nyou've made",len(deposit_list),"deposit, and they are:")
        for item in deposit_list:
            print('$','%.2f' % round(item,2))
    if len(withdrawl_list) > 1:
        print("\nyou've made",len(withdrawl_list),"withdrawls, and they are:")
        for item in withdrawl_list:
            print('-$','%.2f' % round(item,2))
    else:
        print("\nyou've made",len(withdrawl_list),"withdrawl, and they are:")
        for item in withdrawl_list:
            print('-$','%.2f' % round(item,2))
    print('\nyour current balance is', balance)
    return

def interest():
    global balance
    print('Current balance:',balance)
    print('Balance with 25% interest:',balance*1.25)
    return


#Main Program
    
print('Welcome to a bank')
choice=1
deposit_list=[]
withdrawl_list=[]
balance=0
while choice != 5:
    print('\nPlease choose an option:')
    print('1) Make a Deposit')
    print('2) Make a Withdrawl')
    print('3) Display Recent Activity/Balance')
    print('4) Calculate Quarterly Interest')
    print('5) Quit')
    print('\nBalance: ',balance)
    choice=eval(input('Choose an option 1-5: '))
    
    if choice == 1:
        deposit()
    elif choice == 2:
        withdrawl()
    elif choice == 3:
        activity()
    elif choice == 4:
        interest()
    elif choice == 5:
        print('Thanks! See ya!')
    else:
        print('\nInvalid input. Try again')