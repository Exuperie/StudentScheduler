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
					
					student.availability.append(conversion.convert(value))

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

				if (compare.compare(course.time1, student.availability) and course.nSpots1 > 0):
					student.addCourses(course.name, course.time1)
					course.addStudent1(student.index)

				elif (compare.compare(course.time2, student.availability) and course.nSpots2 >0):
					student.addCourses(course.name, course.time2)
					course.addStudent2(student.index)
				
			else:
				break

		    
			#student.printProperties()
			#course.printProperties()


for course in courseList:
	course.printProperties()

index = 0
for student in studentList:

	if student.coursesNumber == 5:
		index += 1
		student.printProperties

print index


