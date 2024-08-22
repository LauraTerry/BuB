import requests
from datetime import datetime
import calendar

def is_mercury_retrograde(date):
    try:
        response = requests.get(f"https://mercuryretrogradeapi.com?date={date}")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data.get("is_retrograde", False)
    except requests.RequestException as e:
        print(f"Error fetching data for {date}: {e}")
        return False

def fetch_retrograde_dates(year):
    retrograde_dates = set()
    for month in range(1, 13):
        for day in range(1, 32):  # Days from 1 to 31
            try:
                # Construct date string
                date_str = f"{year}-{month:02d}-{day:02d}"
                # Fetch retrograde status
                if is_mercury_retrograde(date_str):
                    retrograde_dates.add(datetime.strptime(date_str, '%Y-%m-%d'))
            except ValueError:
                # Handle invalid dates, like 31st of February
                pass
    return retrograde_dates

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
                        day_str = f'\033[92m{day:2}\033[0m'  # Highlight retrograde dates
                    else:
                        day_str = f'{day:2}'
                    row += f'{day_str} '
            print(row)

# Example usage
year = int(input("Enter the year you are searching for: "))
retrograde_dates = fetch_retrograde_dates(year)
display_year_calendar(year, retrograde_dates)