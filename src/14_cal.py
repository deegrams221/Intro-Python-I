"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
# from datetime import datetime

# args = len(sys.argv)
# print(len(sys.argv))
# x = input('''Please use the following format: '14_cal.py [month] [year]'.''')
# if args == 1:
#     month = datetime.today().month
#     year = datetime.today().year
# elif args == 2:
#     month = int(sys.argv[1])
#     year = datetime.now().year
# elif args == 3:
#     month = int(sys.argv[1])
#     year = int(sys.argv[2])
# else:
#     print('''Please use the following format: '14_cal.py [month] [year]'.''')

# print(calendar.TextCalendar().formatmonth(year, month))

# decided to try out "try" and "except"

from datetime import datetime

cur_year = datetime.now().year
cur_month = datetime.now().month

if len(sys.argv) == 3:
    month = sys.argv[1]
    year = sys.argv[2]
    try:
        print(calendar.TextCalendar().formatmonth(int(month), int(year)))
    except:
        sys.exit('''Invalid input: please use numbers 1-12 for month and a four digit numeric year''')
elif len(sys.argv) == 2:
    month = sys.argv[1]
    try:
        print(calendar.TextCalendar().formatmonth(cur_year, int(month)))
    except:
        sys.exit('''Invalid input: please use numbers 1-12 for month''')
elif len(sys.argv) == 1:
    try:
        print(calendar.TextCalendar().formatmonth(cur_year, cur_month))
    except:
        sys.exit('''Please try again.''')
else:
    sys.exit('''Please use the following format: '14_cal.py [month] [year]'.''')