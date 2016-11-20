
class Student:

    'Student Name, Availibilities, Courses'

    def __init__(self, index):
        self.index = index
        self.name = ''
        self.availability = []
        self.coursesNumber = 0
        self.coursesList = []

    def printProperties(self):
        print "Name = ", self.name
        print "Index = ", self.index
        print "Availability = ", self.availability
        print "Courses Number = ", self.coursesNumber
        print "Courses List = ", self.coursesList
        print "---"
