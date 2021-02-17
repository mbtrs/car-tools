def calc0():
    return(f"The vehicle's average mileage and current mileage match.")

def calc1(mileage_average, mileage):
    return(f"The vehicle is {mileage_average - mileage:,d}km under average.")

def calc2(mileage_average, mileage):
    return(f"The vehicle is {mileage - mileage_average:,d}km over average.")

def calc4(max_mileage2, mileage):
    return(f"The vehicle is {max_mileage2 - mileage:,d}km under average.")

def calc5(max_mileage2, mileage):
    return(f"The vehicle is {mileage - max_mileage2:,d}km over average.")

def calc7(max_mileage1, mileage):
    return(f"The vehicle is {max_mileage1 - mileage:,d}km under average.")

def calc8(max_mileage1, mileage):
    return(f"The vehicle is {mileage - max_mileage1:,d}km over average.")

class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
    PASS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

def success():
    return(bcolors.PASS + "Success" + bcolors.ENDC)

def nonsuccess():
    return(bcolors.FAIL + "Nonsuccess" + bcolors.ENDC)