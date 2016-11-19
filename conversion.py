json_time1 = '{"day":"Monday",	"start":"08:30am", "end":"10:30am"}'

import json
parsed_time1 = json.loads(json_time1)

def convert(json_time1):
	if parsed_time1['day'] == 'Monday':
		FTime = 100
	elif parsed_time1['day'] == 'Tuesday':
		FTime = 200
	elif parsed_time1['day'] == 'Wednesday':
		FTime = 300
	elif parsed_time1['day'] == 'THursday':
		FTime = 400
	elif parsed_time1['day'] == 'Friday':
		FTime = 500
	
	if parsed_time1['start'][5:7] == "am":
		print parsed_time1['start']

		parttime2 = float(parsed_time1['start'][3:5])

		FTime = FTime + float(parsed_time1['start'][0:2]) + float(parsed_time1['start'][3:5])/60
	if parsed_time1['start'][5:7] == "pm":
		if parsed_time1[0:2] == '12':
			FTime = FTime + 12 + 0.0
		else:
			FTime = FTime + float(parsed_time1[0:2]+12) + float(parsed_time1[3:5])/60
	
	print FTime

convert(json_time1)
