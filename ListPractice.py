grades=[]

for c in range(1,6):
    x = eval(input('enter grade: '))
    grades.append(x)

grades.sort()
print(*grades)