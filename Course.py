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
		print "StudentList 1 = ", self.studentList1
		print "StudentList 2 = ", self.studentList2
		print

	def addStudent1(self, studentIndex):
		self.studentList1.append(studentIndex)
		self.nSpots1 -= 1


	def addStudent2(self, studentIndex):
		self.studentList2.append(studentIndex)
		self.nSpots2 -= 1