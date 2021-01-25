from datetime import datetime

current_year = currentYear = datetime.now().year
current_month = currentMonth = datetime.now().month

year = int(input("Year? "))
month = int(input("Month? "))
# mileage = int(input("Mileage? "))

year_calc = current_year - year

mileage_average = year_calc * 20000

if year == current_year:
    print()
    print("==================================================================")
    print()

    if month == current_month:
        print("Mileage:", int(month * 1666))
    elif month < current_month:
        print("Mileage:", int((month - current_month) * 1666))
    else:
        print("NaN")

elif year < current_year:
    print()
    print("==================================================================")
    print()
    print("Year difference: " + str(year_calc), "Average mileage: " + str(f"{mileage_average:,d}"))
    
    if month > current_month:
        print("Mileage:", int((year_calc)*20000) - int((month - current_month) * 1666))
    # elif month < current_month:
    #     print("Mileage:", int((year_calc)*20000) - int((current_month - month)*1666)) 
    else:
        print("Mileage:", int((year_calc)*20000) - int((current_month - month) * 1666))
else:
    print("NaN")