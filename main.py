from datetime import datetime

current_year = currentYear = datetime.now().year
current_month = currentMonth = datetime.now().month

year = int(input("Year? "))
month = int(input("Month? "))
mileage = int(input("Mileage? "))

year_calc = (current_year - year )

mileage_average = (year_calc * 20000)

average = current_month - month

if year == current_year:
    print()
    print("===============================================================")
    print()
    print("Year difference: " + str(year_calc) + "; Maximum mileage: " + \
        str(f"{mileage_average:,d}" + (month * 1666)) + "; My mileage: " + str(f"{mileage:,d}"))

    if month == current_month:
        print("Mileage:", str(f"{int(month * 1666):,d}"))
    elif month < current_month:
        print("Mileage:", str(f"{int((month - current_month) * 1666):,d}"))
    else:
        print("NaN")

elif year < current_year:
    print()
    print("===============================================================")
    print()
    print("Year difference: " + str(year_calc) + "; Maximum mileage: " + \
        str(f"{mileage_average:,d}") + "; My mileage: " + str(f"{mileage:,d}"))
    
    if month > current_month:
        if (mileage < mileage_average):
            print("Less than average1")
        elif (mileage == mileage_average):
            print("Perfect mileage1")
        else:
            print("More than average1")
            print(average)
    elif month < current_month:
        if (mileage < mileage_average):
            print("Less than average2")
        elif (mileage == mileage_average):
            print("Perfect mileage2")
        else:
            print("More than average2") 
    else:
        if (mileage < mileage_average):
            print("Less than average3")
        elif (mileage == mileage_average):
            print("Perfect mileage3")
        else:
            print("More than average3")
else:
    print("NaN")