num = 319.5
#desired output: Wednesday 7:30pm

def reversetime(num): 
	#first get day
	if str(num)[0] == '1':
		day = 'Monday'
	if str(num)[0] == '2':
		day = 'Tuesday'
	if str(num)[0] == '3':
		day = 'Wednesday'
	if str(num)[0] == '4':
		day = 'Thursday' 
	if str(num)[0] == '5':
		day = 'Friday'
	#then get hour & minute
	hr = str(int(num)%100)
	minute = str(int((num - int(num))*60))

	time = [day, hr, minute]
	return time

print reversetime(num)
