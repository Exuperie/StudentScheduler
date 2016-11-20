import compare

class Student:
    'Student Name, Availibilities, Courses'

    def __init__(self, index):
        self.index = index
        self.name = ''
        self.availability = []
        self.coursesNumber = 0
        self.coursesList = []

    def addCourses(self, courseName, courseTime):
        self.coursesNumber += 1
        self.coursesList.append([courseName, courseTime[0], courseTime[1]])

    def printProperties(self):
        print "Name = ", self.name
        print "Index = ", self.index
        print "Availability = ", self.availability
        print "Courses Number = ", self.coursesNumber
        print "Courses List = ", self.coursesList
        print

        # Courses that this student can take
        def freeCourses(self, courseList):
            freeCourseList = []

        def registerForCourse(self, course):
            if self.student.coursesNumber < 1:
                raise Exception("No more space!")

            if self.student.coursesNumber < 5:

                if (compare.compare(course.time1, self.availability) and
                        course.nSpots1 > 0):
                    self.addCourses(course.name, course.time1)
                    course.addStudent1(self)

                elif (compare.compare(course.time2, self.availability) and
                        course.nSpots2 > 0):
                    self.addCourses(course.name, course.time2)
                    course.addStudent2(self)
