gradelist=[]
cont='Y'

#will keep asking for inputs until user inputs 'N'
while cont == 'Y' or cont == 'y':
    grade=eval(input('Enter a grade: '))
    if grade==0:
        print('ERROR')
    else:
        gradelist.append(grade)
        cont=input('Do you want to add another grade to the list? ("Y" or "N"): ')

#sorts grades and prints them
gradelist.sort()
print(*gradelist)

#calculates the average value
gradetotal=0
gradetotal=sum(gradelist)
ave=gradetotal / len(gradelist)

#prints average grade rounded to 2 decimal places
print('Here is the average score: ',round(ave,2))