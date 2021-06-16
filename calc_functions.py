PASS = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
END = '\033[0m'


def warning0():
    return WARNING + f"Year entered exceeds current year." + END


def convert0():
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