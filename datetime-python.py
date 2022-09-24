from datetime import datetime
import pytz

def getTodayDate(timeZone):
    '''
    Please Provide Time-Zone
    Get Today Date according to your Time-Zone 
    '''
    timezone = pytz.timezone(timeZone)
    return datetime.now(timezone).date()

def getCurrentTime(timeZone):
    '''
    Please provide Time zone
    Get the Current Time
    '''
    timezone = pytz.timezone(timeZone)
    return datetime.now(timezone).strftime("%H:%M:%S")

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



print(getCurrentTime('Asia/Kolkata'))
print(getTodayDate(('America/New_York')))
 
