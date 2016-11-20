class Course:

    def __init__(self, index):
        self.index = index
        self.name = ''
        self.nSpots1 = 20
        self.nSpots2 = 20
        self.studentList1 = []
        self.studentList2 = []
        self.time1 = []
        self.time2 = []

    def printProperties(self):
        print "Name = ", self.name
        print "Index = ", self.index
        print "Time1 = ", self.time1
        print "Time2 = ", self.time2
        print "Remaining spots = ", self.nSpots1, " and ", self.nSpots2
        print "StudentList 1 = ", self.convertStudentObjectToIndexList(self.studentList1)
        print "StudentList 2 = ", self.convertStudentObjectToIndexList(self.studentList2)
        print "---"

    def addStudent1(self, student):
        self.studentList1.append(student)
        self.nSpots1 -= 1

    def convertStudentObjectToIndexList(self, genericStudentList):
        studentListIndex = []
        for student in genericStudentList:
            studentListIndex.append(student.index)
        return studentListIndex

    def isStudentRegistered(self, studentIndex):
        for student in self.studentList1:
            if studentIndex == student.index:
                return True
        for student in self.studentList2:
            if studentIndex == student.index:
                return True

        else:
            return False

    def isClassFull(self):
        if (self.nSpots1 > 0 or self.nSpots2 > 0):
            return False
        else:
            return True

    def addStudent2(self, student):
        self.studentList2.append(student)
        self.nSpots2 -= 1
