'''
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

# we can ignore the nursery rhyme (too unfocused for me)
from datetime import datetime

# so initialize dates and count
current_date = datetime(1901, 1, 1)
end_date = datetime(2000, 12, 31)
sunday_count = 0

SUNDAY = 6
DECEMBER = 12

if __name__ == '__main__':
    # for each month (in considered time-frame)
    # we count how many Sunday's we have
    while current_date <= end_date:
        if current_date.day == 1 and current_date.weekday() == SUNDAY:  # How many Sundays fell on the first of the month...
            sunday_count += 1
        if current_date.month == DECEMBER:
            # move to next year
            current_date = datetime(current_date.year + 1, 1, 1)
        else:
            # move to next month
            current_date = datetime(current_date.year, current_date.month + 1, 1)

print(sunday_count)

