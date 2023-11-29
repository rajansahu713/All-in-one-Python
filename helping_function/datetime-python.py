from datetime import datetime
import pytz

def getTodayDate(timeZone):
    '''
    Please Provide Time-Zone
    Get Today Date according to your Time-Zone 
    '''
    timezone = pytz.timezone(timeZone)
    return datetime.now(timezone).date()

def getCurrentTime24(timeZone):
    '''
    Please provide Time zone
    Get the Current Time
    '''
    timezone = pytz.timezone(timeZone)
    return datetime.now(timezone).strftime("%H:%M:%S")
    
def getCurrentTime12(timeZone):
    '''
    Please provide Time zone
    Get the Current Time
    '''
    timezone = pytz.timezone(timeZone)
    return datetime.now(timezone).strftime('%I:%M:%S %p')

def getDatetime(timeZone):
    '''
    Please provide time-zone
    Get Datetime object in return
    '''
    timezone = pytz.timezone(timeZone)
    return datetime.now(timezone)


def getAllTimeZone():
    '''
    List of World Time Zones
    '''
    return pytz.all_timezones



# print(get_month_days(datetime.date(2014, 1, 31)))
# print(getCurrentTime('Asia/Kolkata'))
# print(getTodayDate(('America/New_York')))
# print(getAllTimeZone())

print(getCurrentTime12('Asia/Kolkata'))
 
