# include option for month

# calculate mileage under 1 year

# python split number into decimal if greater then 3 zeroes

from datetime import datetime

current_year = currentYear = datetime.now().year
# current_month = currentMonth = datetime.now().month

year = int(input("Year? "))

year_calc = current_year - year
mileage_average = year_calc * 20000

if year == current_year:
    print("year == current_year")

elif year < current_year:
    print("Year difference: " + str(year_calc) + " (current_year - year)")
    print("Average mileage: " + str(f"({mileage_average:,d}") + " (year_calc * 20000)")

else:
    print("Nan")

# month = int(input("What is the month of the car? "))

# mileage = int(input("What is the mileage? "))

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