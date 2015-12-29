# Hint:  use Google to find python function
from datetime import datetime


def days_between(d1, d2, date_format):
    """ Returns the number of days between two dates given in the same format.
    date_format: string describing the date format to consider.
    """
    d1 = datetime.strptime(d1, date_format)
    d2 = datetime.strptime(d2, date_format)
    return abs((d2 - d1).days)


# a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

print (days_between(date_start, date_stop, "%m-%d-%Y"))

# b)
date_start = '12312013'
date_stop = '05282015'

print (days_between(date_start, date_stop, "%m%d%Y"))

# c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

print (days_between(date_start, date_stop, "%d-%b-%Y"))
