from Student import Student
import json
import conversion


studentList = []
Candelario = Student(1, "Candelario", "10:00-12:00", None)
studentList.append(Candelario)

with open('classes.json') as data_file:
	data = json.load(data_file)
	data1 = data["classes"]["101"]["name"]

print data1

conversion.foo()