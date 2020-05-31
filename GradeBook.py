def FillLists():
    global namelist,gradelist,numstudents,numgrades
    
    for r in range(numstudents):
        name=input("Enter a student's name: ")
        namelist.append(name)
        for c in range(numgrades):
            gradelist[r][c]=eval(input('Enter grade: '))
    return

def Averages():
    global numstudents,numgrades,avelist,gradelist
    
    for r in range(numstudents):
        grades=gradelist[r] #assign row r of 2-d list to variable grades
        avg=sum(grades)/len(grades)
        avelist.append(avg)
    return

def Display():
    global numstudents,numgrades,gradelist,namelist,avelist
    
    print()
    print('Gradebook:')
    for thing in range(len(namelist)):
        print(namelist[thing],'\t',*gradelist[thing],'\tGrade average is:',avelist[thing])
    return
#main
namelist=[]
numstudents=eval(input('How many students are there? '))
numgrades=eval(input('How many grades per student? '))
gradelist=[[0 for y in range(numgrades)] for x in range(numstudents)]
avelist=[]

FillLists()
Averages()
Display()