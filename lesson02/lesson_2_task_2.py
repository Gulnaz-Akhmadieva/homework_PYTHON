def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


years = [2020, 2021, 2022, 2023, 2024]

for x in years:
    is_leap = is_year_leap(x)
    print("год " + str(x) + ": " + str(is_leap))
