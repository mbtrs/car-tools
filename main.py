from datetime import datetime

current_year = datetime.now().year
current_month = datetime.now().month
current_day = datetime.now().day

year = int(input("Year? "))
month = int(input("Month? "))
mileage = int(input("Mileage? "))

year_calc = (current_year - year)

# average = current_month - month
mileage_average = (year_calc * 19992)
# max_mileage1 = mileage_average - (month * 1666)
max_mileage1 = (current_month * 1666)
max_mileage2 = ((year_calc - 1) * 19992) + ((12 - month) * 1666) + (current_month * 1666)
# mileage_diff = max_mileage2 - mileage

if current_year == year:
    print()
    print("===============================================================")
    print()
    # print("Year difference: " + str(year_calc) + "; Maximum mileage: " + \
    #     str(int(f"{mileage_average:,d}") + int(month * 1666)) + "; My mileage: " + \
    #     str(f"{mileage:,d}"))

    if month == current_month:
        # print("Mileage:", str(f"{int(month * 1666):,d}"))
        if max_mileage1 > mileage:
            print(max_mileage1, mileage)
            print("max_mileage1 > mileage")
        elif max_mileage1 < mileage:
            print(max_mileage1, mileage)
            print("max_mileage1 < mileage")
        else:
            print(max_mileage1, mileage)
            print("perfect mileage")
    elif month < current_month:
        # print("Mileage:", str(f"{int((month - current_month) * 1666):,d}"))
        if max_mileage1 > mileage:
            print(max_mileage1, mileage)
            print("max_mileage1 > mileage")
        elif max_mileage1 < mileage:
            print(max_mileage1, mileage)
            print("max_mileage1 < mileage")
        else:
            print(max_mileage1, mileage)
            print("perfect mileage")
    else:
        print("NaN")

elif current_year > year:
    print()
    print("===============================================================")
    print()

    if current_month == month:
        if mileage_average > mileage:
            print(mileage_average, mileage)
            print("mileage_average > mileage")
        elif mileage_average < mileage:
            print(mileage_average, mileage)
            print("mileage_average < mileage")
        else:
            print(mileage_average, mileage)
            print("perfect mileage")
    elif current_month < month:
        if max_mileage2 > mileage:
            print(max_mileage2, mileage)
            print("===========")
            print("Good")
        elif max_mileage2 < mileage:
            print(max_mileage2, mileage)
            print("max_mileage2 < mileage")
        else:
            print(mileage_average, mileage)
            print("perfect mileage")
    else:
        print("")
#     print("Year difference: " + str(year_calc) + "; Maximum mileage: " + \
#         str(f"{max_mileage2:,d}") + "; My mileage: " + \
#         str(f"{mileage:,d}") + "; Mileage diff: " + \
#         str(f"{mileage_diff:,d}"))
    
#     if month > current_month:
#         if (mileage < max_mileage2):
#             print("Less than average1")
#             print("Mileage: " + str(mileage), "; Max mileage: " + str(max_mileage2))
#         elif (mileage == max_mileage2):
#             print("Perfect mileage1")
#         else:
#             print("More than average1")
#     elif month > current_month:
#         if (mileage < mileage_average):
#             print("Less than average1")
#         elif (mileage == mileage_average):
#             print("Perfect mileage1")
#         else:
#             print("More than average1")
#     elif month < current_month:
#         if (mileage < mileage_average):
#             print("Less than average2")
#         elif (mileage == mileage_average):
#             print("Perfect mileage2")
#         else:
#             print("More than average2") 
#     else:
#         if (mileage < mileage_average):
#             print("Less than average3")
#         elif (mileage == mileage_average):
#             print("Perfect mileage3")
#         else:
#             print("More than average3")
else:
    print("NaN")