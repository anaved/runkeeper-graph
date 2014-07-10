

import re
from datetime import date, datetime
import settings
import exceptions



    
def parse_bool(val):
    if val is None:
        return None
    elif isinstance(val, bool):
        return val
    elif val.lower() == 'true':
        return True
    elif val.lower() == 'false':
        return False
    else:
        raise exceptions.ParseValueError("Error parsing bool value.")

def parse_date(val):
    if val is None:
        return None
    else:
        mobj = re.match('\w+,\s*(\d+)\s+(\w+)\s+(\d+)', val)
        if mobj is not None:
            return date(int(mobj.group(3)), 
                        settings.MONTH2NUM[mobj.group(2)],
                        int(mobj.group(1)))
        else:
            exceptions.ParseValueError("Error parsing date value.")
            
def parse_datetime(val):
    if val is None:
        return None
    else:
        mobj = re.match('\w+,\s*(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+):(\d+)', val)
        if mobj is not None:
            return datetime(int(mobj.group(3)), 
                            settings.MONTH2NUM[mobj.group(2)],
                            int(mobj.group(1)),
                            int(mobj.group(4)),
                            int(mobj.group(5)),
                            int(mobj.group(6)),)
        else:
            exceptions.ParseValueError("Error parsing date-time value.")
        
def parse_distance(val):
    if val is None:
        return None
    try:
        return float(val)
    except:
        raise exceptions.ParseValueError("Error parsing distance value.")
    
def parse_distance_km(val):
    if val is None:
        return None
    try:
        return float(val) * 1000
    except:
        raise exceptions.ParseValueError("Error parsing distance value.")
    
def parse_resource_dict(prop_defs, data):
    prop_dict = dict([(k, None) for k in prop_defs])
    for k,v in data.items():
        if prop_defs.has_key(k):
            action = prop_defs[k]
            if action is None or v is None:
                prop_dict[k] = v
            elif callable(action):
                prop_dict[k] = action(v)
        else:
            pass
    return prop_dict

def parse_date_param(val):
    if isinstance(val, (date, datetime)):
        return val.strftime('%y-%m-%d')
    else:
        return val

