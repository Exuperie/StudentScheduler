from Student import Student
import json
import conversion
import compare
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

for student in studentList:

    for course in courseList:
        if student.coursesNumber < 5:

            if (compare.compare(course.time1, student.availability) and
                    course.nSpots1 > 0):
                student.addCourses(
                    course.name, course.time1)
                course.addStudent1(student)

            elif (compare.compare(course.time2, student.availability) and
                    course.nSpots2 > 0):
                student.addCourses(
                    course.name, course.time2)
                course.addStudent2(student)

        else:
            break

# student.printProperties()
        # course.printProperties()


for course in courseList:
    course.printProperties()

print " ---- "
print "End of the first iteration"
print " ---- "

# Optimization
index = 0

studentWithOneClass = []

for student in studentList:

    if student.coursesNumber == 1:
        index += 1
        studentWithOneClass.append(student)

        for course in courseList:

            if (course.nSpots1 > 0):
                if (compare.compare(course.time1, student.availability)):
                    course.printProperties()

            elif (course.nSpots2 > 0):
                if (compare.compare(course.time2, student.availability)):
                    course.printProperties()
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
                    course.printProperties()
                    student.printProperties()
                    student2.printProperties()
                    print "Can change"

                # Optimization
