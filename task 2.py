def is_leap_year(year):
    # Check if a year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    # Return the number of days in a given month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        raise ValueError("Invalid month")

def days_between_dates(date1, date2):
    # Swap dates if date1 is greater than date2
    if date1 > date2:
        date1, date2 = date2, date1

    day1, month1, year1 = map(int, date1.split('/'))
    day2, month2, year2 = map(int, date2.split('/'))

    days = 0

    # Calculate days in the first year
    for month in range(month1 + 1, 13):
        days += days_in_month(month, year1)

    days += days_in_month(month1, year1) - day1

    # Calculate days for the full years in between
    for year in range(year1 + 1, year2):
        days += 365 if not is_leap_year(year) else 366

    # Calculate days in the last year
    for month in range(1, month2):
        days += days_in_month(month, year2)

    days += day2 - 1  # Exclude the end date

    return days

# Example usage:
date1 = "15/02/2023"
date2 = "15/02/2024"

result = days_between_dates(date1, date2)
print(f"Number of days between {date1} and {date2}: {result} days")
