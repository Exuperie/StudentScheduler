from Student import Student
import json
import conversion
import compare
from reversetime import reversetime
from Course import Course

# Initiating Variables
courseList = []
studentList = []

# Creating the Student Instances
with open('studentsByAvailability.json') as data_file:
    data = json.load(data_file)

    for key, value in data.iteritems():
        student = Student(key)
        for items in value:

            if type(items) is unicode:
                student.name = items
            if type(items) is dict:
                for key, value in items.iteritems():

                    student.availability.append(
                        conversion.convert(value))

        studentList.append(student)


# Creating the Courses Instances
with open('classes.json') as data_file:
    data = json.load(data_file)

    for key, value in data["classes"].iteritems():
        course = Course(key)
        course.name = value['name']
        times = value['times']

        course.time1 = conversion.convert(times['time1'])
        course.time2 = conversion.convert(times['time2'])
        courseList.append(course)


# Code for assigning student to classes

def registerForCourse(student, course):
    print "properties = ", course.printProperties()
    if student.coursesNumber == 5:
        raise Exception("No more space!")

    if student.coursesNumber < 5:

        if (compare.compare(course.time1, student.availability) and
                course.nSpots1 > 0):
            student.coursesNumber += 1
            student.coursesList.append(
                [course.name, course.time1[0], course.time1[1]])

            course.addStudent1(student)

        elif (compare.compare(course.time2, student.availability) and
                course.nSpots2 > 0):
            student.coursesNumber += 1
            student.coursesList.append(
                [course.name, course.time2[0], course.time2[1]])

            course.addStudent2(student)
        else:
            print 'else'
            pass


def removeCourse(student, course):
    for key in student.coursesList:
        print "key is ", key
        if key[0] == course.name:
            student.coursesList.remove(key)
            student.coursesNumber -= 1

            for studentID in course.studentList1:
                print studentID
                print student.index
                if (studentID == student.index):
                    course.studentList1.remove(studentID)
                    course.nSpots1 += 1
                    return

            for studentID in course.studentList2:
                if (studentID == student.index):
                    course.studentList2.remove(studentID)
                    course.nSpots2 += 1
                    return

            raise Exception("Student was never registered")

    else:
        print "Course not taken"


# Courses that this student can take
def switchCourses(student, course1, course2):
    if course2.nSpots1 > 0:
        pass

    elif course2.nSpots2 > 0:
        pass

    else:
        pass


for student in studentList:

    for course in courseList:
        if student.coursesNumber < 5:

            registerForCourse(student, course)

            # if (compare.compare(course.time1, student.availability) and
            #         course.nSpots1 > 0):
            #     student.addCourses(
            #         course.name, course.time1)
            #     course.addStudent1(student)

            # elif (compare.compare(course.time2, student.availability) and
            #         course.nSpots2 > 0):
            #     student.addCourses(
            #         course.name, course.time2)
            #     course.addStudent2(student)

        else:
            break


# student.printProperties()
        # course.printProperties()


for course in courseList:
    course.printProperties()

print " ---- "
print "End of the first iteration"
print "Student Schedule in file outputStudents.json"
print " ---- "

''' Outputting JSON File

'''
studentDict = {}
for student1 in studentList:
    courseListNew = []
    for course in student.coursesList:
        time = []
        time.append(course[0])
        time.append(reversetime(course[1]))
        time.append(reversetime(course[2]))
        courseListNew.append(time)

    data = {'name': student1.name,
            'availability': student1.availability,
            'coursesNumber': student1.coursesNumber,
            'coursesList': courseListNew

            }
    studentDict[student1.index] = data

with open('outputStudents.json', 'w') as fp:
    json.dump(studentDict, fp)

# with open('outputCourses.json', 'w') as fp:
#    json.dump(coursesDict, fp)

''' Optimization
index = 0

studentWithOneClass = []

for student in studentList:

    if student.coursesNumber == 1:
        index += 1
        studentWithOneClass.append(student)

        for course in courseList:

            if (course.nSpots1 > 0):
                if (compare.compare(course.time1, student.availability)):
                    pass
                    # course.printProperties()

            elif (course.nSpots2 > 0):

                if (compare.compare(course.time2, student.availability)):
                    pass
                    # course.printProperties()
            else:
                pass
print
print "Testing"
print

for student1 in studentWithOneClass:
    student1.printProperties()

    for course in courseList:
        # Check if the student is able to register in another
        # new course
        if (not course.isStudentRegistered(student1) and
                compare.compare(course.time1, student.availability)):

            # Check a registered student (student2) is able to switch to
            # the time 2 of the same class
            for student2 in course.studentList1:
                if (compare.compare(course.time2, student2.availability)):
                    pass
                    # course.printProperties()
                    # student.printProperties()
                    # student2.printProperties()
                    # print "Can change"
'''
