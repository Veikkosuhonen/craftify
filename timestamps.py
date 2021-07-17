import datetime
import pytz

def getIsoFormat(timeStamp):
    return pytz.utc.localize(timeStamp).isoformat()