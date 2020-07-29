import datetime as dt


years = [1967, 1978, 2000, 1987, 2010, 1977]
ages = [dt.date.today().year - y for y in years]

print(ages)
