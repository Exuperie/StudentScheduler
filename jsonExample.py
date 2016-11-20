with open('codejam-challenge-example.json') as data_file:
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
