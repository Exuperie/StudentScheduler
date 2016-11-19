import json
json_time1 = '{"day":"Tuesday", "start":"08:30am", "end":"10:30am"}'


parsed_time1 = json.loads(json_time1)

# this converts date/hr/min to one integer for comparison
# 
def convert(json_time1):
        duration = list()

        #check day first
        if parsed_time1.get('day') == 'Monday':
            FTime = 100
        elif parsed_time1.get('day')  == 'Tuesday':
            FTime = 200
        elif parsed_time1.get('day') == 'Wednesday':
            FTime = 300
        elif parsed_time1.get('day') == 'Thursday':
            FTime = 400
        elif parsed_time1.get('day')  == 'Friday':
            FTime = 500


    #convert starting time
        if parsed_time1.get('start')[5:7] == "am":
            STime = FTime + float(parsed_time1['start'][0:2]) + float(parsed_time1['start'][3:5])/60
        if parsed_time1.get('start')[5:7] == "pm":
            if parsed_time1[0:2] == '12':
                STime = FTime + 12 + 0.0
            else:
                STime = FTime + float(parsed_time1[0:2]+12) + float(parsed_time1[3:5])/60
        duration.append(STime)
    #convert ending time
        if parsed_time1.get('end')[5:7] == "am":
            ETime = FTime + float(parsed_time1['end'][0:2]) + float(parsed_time1['end'][3:5])/60
        if parsed_time1.get('end')[5:7] == "pm":
            if parsed_time1[0:2] == '12':
                ETime = FTime + 12 + 0.0
            else:
                ETime = FTime + float(parsed_time1[0:2]+12) + float(parsed_time1[3:5])/60
        duration.append(ETime)
        print duration


convert(json_time1)
