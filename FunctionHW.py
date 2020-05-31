def FillList(z):
    new_list=[]
    
    for i in range(0,in_num):
        y=eval(input('enter number: '))
        new_list.append(y)
    print(quest + 's','are: ',*new_list)
    return new_list

def Average():
    if quest == 'grade':
        GradeAverage=sum(GradeList)/len(GradeList)
        print(GradeAverage)
        return GradeAverage
    elif quest == 'age':
        AgeAverage=sum(AgeList)/len(AgeList)
        print(AgeAverage)
        return AgeAverage
#Main Program
valid='Y'
while valid == 'Y':
    quest=input('What data do you want to input, grade or age? ').lower()
    if quest == 'grade':
        in_num=eval(input('How many grades do you want to enter? '))
        GradeList=FillList(in_num)
        Average()
    elif quest == 'age':
        in_num=eval(input('How many ages do you want to enter? '))
        AgeList=FillList(in_num)
        Average()
    valid=input('Do you want to go again? Y or N ').upper()
print('\nDONE')