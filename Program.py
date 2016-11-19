from Student import Student
import json
import conversion


classList = []
studentList = []

with open('studentsByAvailability.json') as data_file:
	data = json.load(data_file)

	for key, value in data.iteritems():
		student = Student(key)
		for items in value:

			if type(items) is unicode:
				student.name = items
				print student.name
				

			if type(items) is dict:
				for key, value in items.iteritems():
					#convert(value)
					
					student.availability.append(conversion.convert(value))
				
		print student.availability
		print student.index
		print 

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
		pass



