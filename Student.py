class Student:
	'Student Name, Availibilities, Courses'
	def __init__(self, index, name, availibilities, coursesList):
		self.index = index
		self.name = name
		self.availibilities = availibilities
		self.coursesNumber = 5
		self.coursesList = coursesList

	def addCourses(self, coursesName):
		coursesNumber -= 1