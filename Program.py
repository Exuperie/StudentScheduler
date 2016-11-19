from Student import Student
import json

classList = []
studentList = []

with open('studentsByAvailability.json') as data_file:
	data = json.load(data_file)

	for key, value in data.iteritems():
		student = Student(key)
		for items in value:

			if type(items) is unicode:
				student.name = items

			if type(items) is dict:
				for key, value in items.iteritems():
					pass
					#print key
					
					#print value["day"]
					#print value["start"]
					#print value["end"]

		studentList.append(student)

print len(studentList)
	#print student.name

with open('classes.json') as data_file:
	data = json.load(data_file)

	for key, value in data["classes"].iteritems():
		print key
		print value




