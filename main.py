# -*- coding: utf-8 -*-
"""
Davina Doran
davdoran@csu.fullerton.edu
Prof: johnwoates
CPSC 223P-01
Thu Jan 28, 2021
joates@fullerton.edu
"""

class Roster:
    "class for all of the different user options"
    def ___init___(self):
        pass
                
        
    def list_students(self):
        "opens grades.txt; creates dictionary (student name = key); closes file"
        gradesFile = open("grades.txt")
        
        self.gradesDict = {}
        for line in gradesFile:
            self.student = line.strip().split(',')
            self.gradesDict[self.student[0]] = self.student[1:]
       
        gradesFile.close()
        
        "lists all of the enrolled students"
        self.studentList = list(self.gradesDict.keys())
        
        return self.studentList[1:]
    
    
    def list_grades(self):
        "opens grades.txt; creates dictionary (student name = key); closes file"
        gradesFile = open("grades.txt")
        
        self.gradesDict = {}
        for line in gradesFile:
            self.student = line.strip().split(',')
            self.gradesDict[self.student[0]] = self.student[1:]
       
        gradesFile.close()
        
        return self.gradesDict
    
    def list_attendance(self):
        attendanceFile = open("attendance.txt")
        
        self.attendanceDict = {}
        for line in attendanceFile:
            self.student = line.strip().split(',')
            self.attendanceDict[self.student[0]] = self.student[1:]
       
        attendanceFile.close()
        
        return self.attendanceDict
        
        
myClass = Roster()
print("What do you want to do? \n1 - List all students: \n2 - List all grades: \n3 - List attendance: \n")
selection = input("")

if selection == "1":
    for student in myClass.list_students():
        print(student)
elif selection == "2":
    for student in myClass.list_grades():
        print(student)
        print(myClass.list_grades()['Student'][0][1:]+":", myClass.list_grades()[student][0])
        print(myClass.list_grades()['Student'][1][1:]+":", myClass.list_grades()[student][1])
        print(myClass.list_grades()['Student'][2][1:]+":", myClass.list_grades()[student][2])
        print(myClass.list_grades()['Student'][3][1:]+":", myClass.list_grades()[student][3])
        print(myClass.list_grades()['Student'][4][1:]+":", myClass.list_grades()[student][4])
        print(myClass.list_grades()['Student'][5][1:]+":", myClass.list_grades()[student][5])
elif selection == '3':
    print("Which student?: ")
    j = 1
    for student in myClass.list_students():
        print(j, student)
        j += 1
    choice = input("\n")
    if choice == '1':
        curKey = 'Paul McCartney'
    elif choice == '2':
        curKey = 'John Lennon'
    elif choice == '3':
        curKey = 'George Harrison'
    elif choice == '4':
        curKey = 'Ringo Starr'
    elif choice == '5':
        curKey = "Robert Plant"
    elif choice == '6':
        curKey = 'Jimmy Page'
    elif choice == '7':
        curKey = 'John Bonham'
    elif choice == '8':
        curKey = 'John Paul Jones'
    elif choice == '9':
        curKey = 'Trey Anastasio'
    elif choice == '10':
        curKey = 'Jon Fishman'
    elif choice == '11':
        curKey = 'Mike Gordon'
    elif choice  == '12':
        curKey = 'Page McConnell'
    print(curKey)
    print(myClass.list_attendance()['Student'][0][1:]+":", myClass.list_attendance()[curKey][0])
    print(myClass.list_attendance()['Student'][1][1:]+":", myClass.list_attendance()[curKey][1])
    print(myClass.list_attendance()['Student'][2][1:]+":", myClass.list_attendance()[curKey][2])
    print(myClass.list_attendance()['Student'][3][1:]+":", myClass.list_attendance()[curKey][3])
    print(myClass.list_attendance()['Student'][4][1:]+":", myClass.list_attendance()[curKey][4])
    print(myClass.list_attendance()['Student'][5][1:]+":", myClass.list_attendance()[curKey][5])
    print(myClass.list_attendance()['Student'][6][1:]+":", myClass.list_attendance()[curKey][6])
    print(myClass.list_attendance()['Student'][7][1:]+":", myClass.list_attendance()[curKey][7])
    print(myClass.list_attendance()['Student'][8][1:]+":", myClass.list_attendance()[curKey][8])
    print(myClass.list_attendance()['Student'][9][1:]+":", myClass.list_attendance()[curKey][9])
    print(myClass.list_attendance()['Student'][10][1:]+":", myClass.list_attendance()[curKey][10])
    print(myClass.list_attendance()['Student'][11][1:]+":", myClass.list_attendance()[curKey][11])
    print(myClass.list_attendance()['Student'][12][1:]+":", myClass.list_attendance()[curKey][12])
    print(myClass.list_attendance()['Student'][13][1:]+":", myClass.list_attendance()[curKey][13])
    print(myClass.list_attendance()['Student'][14][1:]+":", myClass.list_attendance()[curKey][14])
    print(myClass.list_attendance()['Student'][15][1:]+":", myClass.list_attendance()[curKey][15])

elif selection == '4':
    pass