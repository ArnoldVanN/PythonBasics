import datetime
print("Please enter your date of birth:")
print("Day")
day = input()
print("Month")
month = input()
print("Year")
year = input()

date = datetime.date(int(year), int(month), int(day))
b = date.replace(year=date.year + 31, month=date.month + 8, day=date.day + 15) # Closest i could get it without it getting annoying.
print("One gigasecond later...", b)