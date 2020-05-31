#US dollar to other currency coverter
x=eval(input('Enter a positive US dollar value: '))
print('\u2BEF')

#conversion factors
eu=0.87
ye=112.50
ca=1.31
ru=73.48
#prints all conversions
print('\u20AC','%.2f' % round(x*eu,2))
print('\u00A5', '%.2f' % round(x*ye,2))
print('\u0024','%.2f' % round(x*ca,2),' Canadian Dollars')
print('\u20B9','%.2f' % round(x*ru,2))
print('%.2f')