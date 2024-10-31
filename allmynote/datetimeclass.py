import datetime as dt

# tim = dt.datetime.now()
# print(tim.date())
# print(tim.time())
# print(tim.year)
# print(tim.month)
# print(tim.day)
# print(tim.hour)
# print(tim.minute)
# print(tim.second)

# tm = dt.datetime(2023, 4, 10, 12, 00)
# print(tm)
# print(tm.month)

# tm = dt.datetime(2023, 4, 10, 12, 30, 20)
# print(tm)

# check = int(dt.datetime.now().strftime("%M"))
# rang=[]
# [rang.append(rn) for rn in range(0,60)]
# while True:
#     time=dt.datetime.now()
#     nexttime= time.strftime('%M')
#     if int(nexttime) in [rn for rn in range(0,60)] and check == int(nexttime):
#         for i in range(5):
#             print("I am  going for class today")
#     check =int(nexttime ) +1
    
    
import datetime
sec = 00
while True:
    dtim = dt.datetime.now()
    day = dtim.strftime("%A")
    hour = dtim.strftime("%I")
    minute = dtim.strftime("%M")
    second = dtim.strftime("%S")
    print(hour)
    
    if day =="wednesday":
        if hour ==1 and minute ==54 and second ==50:
            for i in range(1):
                print("tou have class now")
                
                
        elif day ==" tuesday":
            print('ok')
    
    
    
    
# PYthon Math 
# import math, cmath
# l= [2, 4, 5, 7, 3]
# print(min(l))
# print(max(l))
# print(abs(-5.38))
# print(pow(5, 3), 'DONE')
# print(math.sqrt(9))
# print(math.ceil(6.3492))
# print(math.floor(5.6732))
# print(math.pi)
# print(math.pi * 1000 + 25)