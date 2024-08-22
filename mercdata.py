import requests
import pandas as pd
import calendar
from datetime import datetime, timedelta

print("Hello and Welcome to the BreakUpBuddy! We're here to help you find the best time to dump your trash")
year=int( input("Enter the year you are searching for: "))
# bday= input("Please enter the victim's birthday: ")

yy = year

def display_custom_year_calendar(year):
    # Create a TextCalendar object with Sunday as the first day of the week
    cal = calendar.TextCalendar(calendar.SUNDAY)
      # Customize the spacing and print the calendar
    print(cal.formatyear(year, w=3, l=1, c=6, m=3))
    #( stands for width=3, spacing=6, space between columns=2, number of months per row=3)

display_custom_year_calendar(year)



#link with API for boolean mercury retrograde

# > curl https://mercuryretrogradeapi.com?date=2016-09-14
# 		{"is_retrograde":true}

# 		> curl https://mercuryretrogradeapi.com?date=2016-10-01
# 		{"is_retrograde":false}
