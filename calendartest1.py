import calendar
from datetime import datetime

def display_year_calendar(year, highlight_dates):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    for month in range(1, 13):
        print(f"\n{calendar.month_name[month]} {year}")
        print("Su Mo Tu We Th Fr Sa")
        
        month_days = cal.monthdayscalendar(year, month)
        for week in month_days:
            row = ""
            for day in week:
                if day == 0:
                    row += "   "
                else:
                    day_date = datetime(year, month, day)
                    if day_date in highlight_dates:
                        day_str = f'\033[92m{day:2}\033[0m'
                    else:
                        day_str = f'{day:2}'
                    row += f'{day_str} '
            print(row)

# Example usage
year = int(input("Enter the year you are searching for: "))
# retrograde_dates = fetch_retrograde_dates(year)
# custom_ranges = fetch_custom_ranges(year)
# birthdays = fetch_birthdays(year)
# full_moons = fetch_full_moons(year)

# Combine all highlight dates
all_highlights = retrograde_dates | custom_ranges | birthdays | full_moons

display_year_calendar(year, all_highlights)

