# include option for month

# calculate mileage under 1 year

from datetime import datetime

current_year = currentYear = datetime.now().year
current_month = currentMonth = datetime.now().month

year = int(input("Year? "))
month = int(input("Month? "))
# mileage = int(input("Mileage? "))

year_calc = current_year - year
year_calc_for_2021 = (year_calc + 1) * 1666

mileage_average = year_calc * 20000

if year == current_year:
    print(year_calc_for_2021)

elif year < current_year:
    print()
    print("==================================================================")
    print()
    print("Year difference: " + str(year_calc))
    print("Average mileage: " + str(f"({mileage_average:,d})"))
    
    if month > current_month:
        print(int((current_year - year)*20000) - int((12 - month)*1666))
    else:
        print("test")

else:
    print("NaN")

# average_mileage = ((current_year - year) * 1666)

# todays_car = "Current month: " + str(current_month) + "; Current year: " + str(current_year)
# car_in_question = "Month of car: " + str(month) + "; Year of car: " + str(year)

# year_calc = current_year - year
# month_calc = current_month - month

# my_car_month_calc = month_calc * 1666

# mileage_average = year_calc * 20000
# mileage_calc = mileage_average - mileage
# # same_year_mileage_calc = mileage

# if year == current_year:
#     print()
#     print("==================================================================")
#     print()    
#     # print("This car is brand new with " + str(mileage) + " mileage.")
#     # print("The average mileage is " + str(same_year_mileage_calc) + ".")

# elif mileage_calc < 0:
#     print()
#     print("==================================================================")
#     print()
#     print("Mileage difference: " + str(mileage_calc))
#     # print(month_calc)
#     print(my_car_month_calc)
# else:
#     print()
#     print("==================================================================")
#     print()
#     print(todays_car)
#     print(car_in_question)
#     print("Month difference: " + (str(int(int(current_month) - (int(month))) * -1)) + "; Year difference: " + str(int(current_year) - int(year)))
#     print()
#     print("==================================================================")
#     print()
#     # print("This car is " + str(year_calc) + " years old with " + str(mileage) + " mileage.")
#     print("The average mileage is " + str(mileage_average) + ".")
#     print("Mileage difference: " + str(mileage_calc))