class bcolors:
    #     HEADER = '\033[95m'
    #     OKBLUE = '\033[94m'
    #     OKCYAN = '\033[96m'
    PASS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

    #   BOLD = '\033[1m'
    #   UNDERLINE = '\033[4m'


def calc0():
    return bcolors.WARNING + f"This vehicle's average mileage and current mileage match." + bcolors.END


def calc1(mileage_average, mileage):
    return bcolors.PASS + f"This vehicle is {mileage_average - mileage:,d}km under average." + bcolors.END


def calc2(mileage_average, mileage):
    return bcolors.FAIL + f"This vehicle is {mileage - mileage_average:,d}km over average." + bcolors.END


def calc4(max_mileage2, mileage):
    return bcolors.PASS + f"This vehicle is {max_mileage2 - mileage:,d}km under average." + bcolors.END


def calc5(max_mileage2, mileage):
    return bcolors.FAIL + f"This vehicle is {mileage - max_mileage2:,d}km over average." + bcolors.END


def calc7(max_mileage1, mileage):
    return bcolors.PASS + f"This vehicle is {max_mileage1 - mileage:,d}km under average." + bcolors.END


def calc8(max_mileage1, mileage):
    return bcolors.FAIL + f"This vehicle is {mileage - max_mileage1:,d}km over average." + bcolors.END
