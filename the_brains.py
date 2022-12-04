from datetime import datetime


current_year, current_month = datetime.now().year, datetime.now().month
# current_day = datetime.now().day


PASS = '\033[1;37;40m'
WARN = '\033[1;37;40m'
FAIL = '\033[1;37;40m'
END = '\033[0m'


# https://ozzmaker.com/add-colour-to-text-in-python/


# def get_int(txt: str) -> int:
#     while True:
#         try:
#             return int(input(txt))
#         except ValueError as e:
#             print(f"{FAIL}Please enter numbers only: {e}{END}")


def year_input():
    # while True:
    # year = get_int("Year first owner reported: ")
    # oldest_year = 1900
    # if oldest_year < year <= current_year:
    #     return year
    # print(f"{FAIL}{year} does not fall within the range ({oldest_year} to {current_year}).{END}")
    while True:
        year = input("Year first owner reported: ")
        oldest_year = 1900
        try:
            year = int(year)
        except ValueError:
            print(f"{FAIL}Please use numeric digits.{END}")
            continue
        nums = range(oldest_year, current_year + 1)
        if year in nums:
            return year
        # if oldest_year > year > current_year:
        print(f"{FAIL}{year} does not fall within the range ({oldest_year} to {current_year}).{END}")
        continue
        break
    return year


year = year_input()


# if __name__ == "__main__":
#     year_input()


def month_input():
    # while True:
    # month = get_int("Month first owner reported: ")
    # nums = range(1, 13)
    # if month in nums:
    #     return month
    # print(f"{FAIL}{month} is not a valid month.{END}")

    while True:
        month = input("Month first owner reported: ")
        try:
            month = int(month)
        except ValueError:
            print(f"{FAIL}Please use numeric digits.{END}")
            continue
        nums = range(1, 13)
        if month in nums:
            return month
        print(f"{FAIL}{month} does not fall within the range (1 to 12).{END}")
        continue
        break
    return month


month = month_input()


# def mileage_input():
#     while True:
#         mileage = get_int("Vehicle's mileage: ")
#         return mileage

def mileage_input():
    while True:
        mileage = input("Vehicle's mileage: ")
        try:
            mileage = int(mileage)
        except ValueError:
            print(f"{FAIL}Please use numeric digits.{END}")
            continue
        if mileage < 0:
            print(f"{FAIL}{mileage} does not fall within the range (1 to 12).{END}")
            continue
        break
    return mileage


mileage = mileage_input()


def mileage_display(max_mileage_1, mileage):
    return f"Max mileage: {max_mileage_1:,d} | Vehicle mileage: {mileage:,d}"


def mileage_display_1(max_mileage_2, mileage):
    return f"Max mileage: {max_mileage_2:,d} | Vehicle mileage: {mileage:,d}"


def mileage_display_2(mileage_average, mileage):
    return f"Max mileage: {mileage_average:,d} | Vehicle mileage: {mileage:,d}"


def warning0():
    return f"{WARN}Year entered exceeds current year.{END}"


def error0():
    return f"{WARN}This is not a valid entry.{END}"


def lines():
    return "\n"*2 + "="*57 + "\n"*2


def max_mileage_equals_mileage():
    return lines() + f"{WARN}This vehicle's average mileage and current mileage match.{END}" + lines()


def max_mileage_gt_mileage_3(mileage_average, mileage):
    return "\n"*2 + f"{PASS}This vehicle is {mileage_average - mileage:,d}km under average.{END}" + "\n"*2


def max_mileage_lt_mileage_3(mileage_average, mileage):
    return "\n"*2 + f"{FAIL}This vehicle is {mileage - mileage_average:,d}km over average.{END}" + "\n"*2


def max_mileage_gt_mileage_1(max_mileage_2, mileage):
    return "\n"*2 + f"{PASS}This vehicle is {max_mileage_2 - mileage:,d}km under average.{END}" + "\n"*2


def max_mileage_lt_mileage_1(max_mileage_2, mileage):
    return "\n"*2 + f"{FAIL}This vehicle is {mileage - max_mileage_2:,d}km over average.{END}" + "\n"*2


def max_mileage_gt_mileage_2(max_mileage_1, mileage):
    return "\n"*2 + f"{PASS}This vehicle is {max_mileage_1 - mileage:,d}km under average.{END}" + "\n"*2


def max_mileage_lt_mileage_2(max_mileage_1, mileage):
    return "\n"*2 + f"{FAIL}This vehicle is {mileage - max_mileage_1:,d}km over average.{END}" + "\n"*2


def find_longest_statement(text):
    longest_statement = max(text, key=len)
    return (len(longest_statement)*"=")


year_calc = current_year - year
mileage_average = year_calc * 19992
max_mileage_1 = current_month * 1666
max_mileage_2 = ((year_calc - 1) * 19992) + ((12 - month) * 1666) + (current_month * 1666)
