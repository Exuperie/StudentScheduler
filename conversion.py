import json
#json_time1 = '{"day":"Tuesday", "start":"08:30am", "end":"10:30am"}'


#time = json.loads(json_time1)

# this converts date/hr/min to one integer for comparison
# 
def convert(time):
        duration = list()

        #check day first
        if time['day'] == 'Monday':
            FTime = 100
        elif time['day'] == 'Tuesday':
            FTime = 200
        elif time['day'] == 'Wednesday':
            FTime = 300
        elif time['day'] == 'Thursday':
            FTime = 400
        elif time['day']  == 'Friday':
            FTime = 500


    #convert starting time
        if time['start'][5:7] == "am":
            STime = FTime + float(time['start'][0:2]) + float(time['start'][3:5])/60
        if time['start'][5:7] == "pm":
            if time[0:2] == '12':
                STime = FTime + 12 + 0.0
            else:
                STime = FTime + float(time[0:2]+12) + float(time[3:5])/60
        duration.append(STime)
    #convert ending time
        if time['end'][5:7] == "am":
            ETime = FTime + float(time['end'][0:2]) + float(time['end'][3:5])/60
        if time['end'][5:7] == "pm":
            if time['end'][0:2] == '12':
                ETime = FTime + 12 + 0.0
            else:
                ETime = FTime + float(time['end'][0:2]) + 12 + float(time['end'][3:5])/60
        duration.append(ETime)
        print duration


with open('avail.json') as data_file:
    data = json.load(data_file)
    convert(data)
