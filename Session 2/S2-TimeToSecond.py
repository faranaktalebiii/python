Time = input ("Please Enter Your Time (hh:mm:ss):")
Hours = int(Time[0:2])
Minute = int(Time[3:5])
Second = int(Time[6:8])
TimeToSeconds = (Hours * 60 * 60) + (Minute * 60) + Second
print (TimeToSeconds)