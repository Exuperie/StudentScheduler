#this takes two time points expressed as floats 
#check for conflict 

ctime1 = [108.5, 110.5]
stime1 = [[108.5, 112], [115, 117]]

def compare(ctime, stime):
	i = 0
	#loop through student avail1
	while i < len(stime):
		if stime[i][0]<=ctime[0] and stime[i][1]>=ctime[1]: 
			return True
		else: return False
		i+=1

		
print compare(ctime1, stime1)
