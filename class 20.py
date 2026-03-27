# from datetime import time, date, datetime
# today = date.today()
# now = datetime.now()
# print("Today's date is",today)
# print("Today's time and date",now)
# print(today.year,today.month,today.day)
# import random
# import time
# def GetRandomDate(startdate, enddate):
#     print("Random date",startdate, "and", enddate)
#     randomgenerator = random.random()
#     dateformat = "%m/%d/%y"
#     a = time.mktime(time.strptime(startdate,dateformat))
#     b = time.mktime(time.strptime(enddate,dateformat))
#     rt = a + randomgenerator * (b-a)
#     rd = time.strftime(dateformat,time.localtime(rt))
#     return rd
# print("random date = ",GetRandomDate("1/1/2014","12/8/2023"))
# import random 
# import time
# def getRandomDate(startDate, endDate ): 
#     print("Printing random date between", startDate, " and ", endDate)
#     randomGenerator = random.random()
#     dateFormat = '%m/%d/%Y'
#     startTime = time.mktime(time.strptime(startDate, dateFormat))
#     endTime = time.mktime(time.strptime(endDate, dateFormat))
#     randomTime = startTime + randomGenerator * (endTime - startTime)
#     randomDate = time.strftime(dateFormat, time.localtime(randomTime))
#     return randomDate

# print ("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))
def hotelcost(nights):
    return 140*nights
def planecost(city):
    if "London"==city:return 180
    elif "Los Angeles"==city:return 165
    elif "Dubai"==city:return 150
    elif "Texas"==city:return 195
def carrental(days):
    if days>=7:
        return 35*days-20
    if days>=3:
        return 35*days-10
    else:
        return 35*days
print("Cost in city London:",planecost("London"))
print("Cost of hotel for 5 nights",hotelcost(5))
print("Cost of car rental for 8 days",carrental(8))