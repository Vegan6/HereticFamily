from datetime import datetime
import json
import decimal

# Static Variables
WU_STATE = 'ID'
WU_CITY = 'KIDA'
WU_StationID = 'KIDA'
#Idaho_Falls, KIDA, 83404

# Heretic Key
WU_API_KEY = '892a7ac61426b970'

BATTLETAG = ''
CURRENTSERVER = ''


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        elif isinstance(o, decimal.Decimal):
            #return (str(o) for o in [o])
            return float(o)

        return json.JSONEncoder.default(self, o)

def GetUpdateTime(epochSeconds):
    # Convert SecondsFromEpoch to local datetime
    return datetime.fromtimestamp(epochSeconds)