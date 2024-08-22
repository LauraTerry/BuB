import requests
from datetime import datetime
import calendar
import csv

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
    retrograde_dates = []
    for month in range(1, 13):
        for day in range(1, 32):  # Days from 1 to 31
            try:
                # Construct date string
                date_str = f"{year}-{month:02d}-{day:02d}"
                # Fetch retrograde status
                if is_mercury_retrograde(date_str):
                    retrograde_dates.append(datetime.strptime(date_str, '%Y-%m-%d').date())
            except ValueError:
                # Handle invalid dates, like 31st of February
                pass
    return retrograde_dates

def save_to_csv(dates, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Year"])  # CSV headers
        for date in dates:
            writer.writerow([date, date.year])

def fetch_and_save_retrograde_dates(start_year, end_year, filename):
    all_retrograde_dates = []
    for year in range(start_year, end_year + 1):
        retrograde_dates = fetch_retrograde_dates(year)
        all_retrograde_dates.extend(retrograde_dates)
    save_to_csv(all_retrograde_dates, "retrogradedates.csv")

# Example usage:
start_year = 2024
end_year = 2025
fetch_and_save_retrograde_dates(start_year, end_year, f'mercury_retrograde_{start_year}_{end_year}.csv')
