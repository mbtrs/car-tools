from datetime import datetime

current_year, current_month = datetime.now().year, datetime.now().month
# current_day = datetime.now().day

PASS = '\033[1;32;40m'
WARN = '\033[1;33;40m'
FAIL = '\033[1;31;40m'
END = '\033[0m'


def get_int(txt: str) -> int:
    while True:
        try:
            return int(input(txt))
        except ValueError as e:
            print(FAIL + f"Please enter numbers only: {e}" + END)


def year_input():
    while True:
        year = get_int("Year first owner reported: ")
        year_1, year_2 = 1900, current_year
        if year_1 < year <= year_2:
            return year
        print(FAIL + f"{year} does not fall into the year range ({year_1} to {year_2})" + END)


def month_input():
    while True:
        month = get_int("Month first owner reported: ")
        nums = range(1, 13)
        if month in nums:
            return month
        print(FAIL + f"{month} is not a valid month" + END)


def mileage_input():
    while True:
        mileage = get_int("Vehicle's mileage: ")
        return mileage


def mileage_display(max_mileage_1, mileage):
    return f"Max mileage: {max_mileage_1:,d} | Vehicle mileage: {mileage:,d}"


def mileage_display_1(max_mileage_2, mileage):
    return f"Max mileage: {max_mileage_2:,d} | Vehicle mileage: {mileage:,d}"


def mileage_display_2(mileage_average, mileage):
    return f"Max mileage: {mileage_average:,d} | Vehicle mileage: {mileage:,d}"


def warning0():
    return WARN + f"Year entered exceeds current year." + END


def error0():
    return WARN + f"This is not a valid entry." + END


def lines():
    return "\n"*2 + "="*57 + "\n"*2


def calc0():
    return lines() + WARN + f"This vehicle's average mileage and" + \
        " current mileage match." + END + lines()


def calc1(mileage_average, mileage):
    return "\n"*2 + PASS + f"This vehicle is {mileage_average - mileage:,d}km" + \
        " under average." + END + "\n"*2


def calc2(mileage_average, mileage):
    return "\n"*2 + FAIL + f"This vehicle is {mileage - mileage_average:,d}km" + \
        " over average." + END + "\n"*2


def calc4(max_mileage_2, mileage):
    return "\n"*2 + PASS + f"This vehicle is {max_mileage_2 - mileage:,d}km" + \
        " under average." + END + "\n"*2


def calc5(max_mileage_2, mileage):
    return "\n"*2 + FAIL + f"This vehicle is {mileage - max_mileage_2:,d}km" + \
        " over average." + END + "\n"*2


def calc7(max_mileage_1, mileage):
    return "\n"*2 + PASS + f"This vehicle is {max_mileage_1 - mileage:,d}km" + \
        " under average." + END + "\n"*2


def calc8(max_mileage_1, mileage):
    return "\n"*2 + FAIL + f"This vehicle is {mileage - max_mileage_1:,d}km" + \
        " over average." + END + "\n"*2


def find_longest_statement(text):
    longest_statement = max(text, key=len)
    return (len(longest_statement)*"=")
