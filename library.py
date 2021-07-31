from datetime import datetime

current_year, current_month = datetime.now().year, datetime.now().month
# current_day = datetime.now().day


def get_int(txt: str) -> int:
    while True:
        try:
            return int(input(txt))
        except ValueError as e:
            print(f"Please enter numbers only: {e}")


def year_question():
    while True:
        year = get_int("Year first owner reported: ")
        year_1, year_2 = 1900, current_year
        if year_1 < year <= year_2:
            return year
        print(f"{year} does not fall into the year range ({year_1} to {year_2})")


# year = year_question()


# if __name__ == "__main__":
#     year_question()


def month_question():
    while True:
        month = get_int("Month first owner reported: ")
        nums = range(0, 13)
        if month in nums:
            return month
        print(f"{month} does not fall into the month range (1 to 12)")


# month = month_question()


# if __name__ == "__main__":
#     month_question()


def mileage_question():
    while True:
        mileage = get_int("Vehicle's mileage: ")
        return mileage


# mileage = mileage_question()


# if __name__ == "__main__":
#     mileage_question()


def mileage_display(max_1, mil):
    return f"Max mileage: {max_1:,d} | Vehicle mileage: {mil:,d}"


def mileage_display_1(max_2, mil):
    return f"Max mileage: {max_2:,d} | Vehicle mileage: {mil:,d}"


def mileage_display_2(avg, mil):
    return f"Max mileage: {avg:,d} | Vehicle mileage: {mil:,d}"


PASS = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
END = '\033[0m'


def warning0():
    return WARNING + f"Year entered exceeds current year." + END


def error0():
    return WARNING + f"This is not a valid entry." + END


def calc0():
    return WARNING + f"This vehicle's average mileage and current mileage match." + END


def calc1(mileage_average, mileage):
    return PASS + f"This vehicle is {mileage_average - mileage:,d}km under average." + END


def calc2(mileage_average, mileage):
    return FAIL + f"This vehicle is {mileage - mileage_average:,d}km over average." + END


def calc4(max_mileage2, mileage):
    return PASS + f"This vehicle is {max_mileage2 - mileage:,d}km under average." + END


def calc5(max_mileage2, mileage):
    return FAIL + f"This vehicle is {mileage - max_mileage2:,d}km over average." + END


def calc7(max_mileage1, mileage):
    return PASS + f"This vehicle is {max_mileage1 - mileage:,d}km under average." + END


def calc8(max_mileage1, mileage):
    return FAIL + f"This vehicle is {mileage - max_mileage1:,d}km over average." + END


def lines():
    return "\n===============================================================\n"
