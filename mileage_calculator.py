def calculator():
    while True:
        
        from datetime import datetime
        import calc_functions as cf

        current_year = datetime.now().year
        current_month = datetime.now().month
        # current_day = datetime.now().day

        year = int(input("Year first owner reported (e.g. 2020): "))
        month = int(input("Month first owner reported? (e.g. 5 for May): "))
        mileage = int(input("Vehicle's mileage: "))

        year_calc = (current_year - year)

        mileage_average = (year_calc * 19992)
        max_mileage1 = (current_month * 1666)
        max_mileage2 = ((year_calc - 1) * 19992) + ((12 - month) * 1666) + (current_month * 1666)

        def mileage_display():
            return(f"Max mileage: {max_mileage1:,d} | Vehicle mileage: {mileage:,d}")

        def mileage_display1():
            return(f"Max mileage: {max_mileage2:,d} | Vehicle mileage: {mileage:,d}")

        def mileage_display2():
            return(f"Max mileage: {mileage_average:,d} | Vehicle mileage: {mileage:,d}")

        if current_year == year:
            print("\n===============================================================\n")

            if month == current_month:
                if max_mileage1 > mileage:
                    print(cf.success())
                    print(mileage_display())
                    print(cf.calc7(max_mileage1, mileage))
                    print("\n===============================================================\n")
                elif max_mileage1 < mileage:
                    print(cf.nonsuccess())
                    print(mileage_display())
                    print(cf.calc8(max_mileage1, mileage))
                    print("\n===============================================================\n")
                else:
                    print(cf.success())
                    print(mileage_display())
                    print(cf.calc0())
                    print("\n===============================================================\n")
            elif month < current_month:
                if max_mileage1 > mileage:
                    print(cf.success())
                    print(mileage_display())
                    print(cf.calc7(max_mileage1, mileage))
                    print("\n===============================================================\n")
                elif max_mileage1 < mileage:
                    print(cf.nonsuccess())
                    print(mileage_display())
                    print(cf.calc8(max_mileage1, mileage))
                    print("\n===============================================================\n")
                else:
                    print(cf.success())
                    print(mileage_display())
                    print(cf.calc0())
                    print("\n===============================================================\n")
            else:
                print("NaN")

        elif current_year > year:
            print("\n===============================================================\n")

            if current_month == month:
                if mileage_average > mileage:
                    print(cf.success())
                    print(mileage_display2())
                    print(cf.calc1(mileage_average, mileage))
                    print("\n===============================================================\n")
                elif mileage_average < mileage:
                    # print(mileage_average, mileage, "| The car is", (f"{mileage - mileage_average:,d}km"), "over average")
                    print(cf.nonsuccess())
                    print(mileage_display2())
                    print(cf.calc2(mileage_average, mileage))
                    print("\n===============================================================\n")
                else:
                    print(cf.success())
                    print(mileage_display2())
                    print(cf.calc0())
                    print("\n===============================================================\n")
            elif current_month < month:
                if max_mileage2 > mileage:
                    # print(max_mileage2, mileage, "| The car is", (f"{max_mileage2 - mileage:,d}km"), "under average")
                    print(cf.success())
                    print(mileage_display1())
                    print(cf.calc4(max_mileage2, mileage))
                    print("\n===============================================================\n")
                elif max_mileage2 < mileage:
                    # print(max_mileage2, mileage, "| The car is", (f"{mileage - max_mileage2:,d}km"), "over average")
                    print(cf.nonsuccess())
                    print(mileage_display1())
                    print(cf.calc5(max_mileage2, mileage))
                    print("\n===============================================================\n")
                else:
                    print(cf.success())
                    print(mileage_display1())
                    print(cf.calc0())
                    print("\n===============================================================\n")
            else:
                if max_mileage2 > mileage:
                    # print(max_mileage2, mileage, "| The car is", (f"{max_mileage2 - mileage:,d}km"), "under average")
                    print(cf.success())
                    print(mileage_display1())
                    print(cf.calc4(max_mileage2, mileage))
                    print("\n===============================================================\n")
                elif max_mileage2 < mileage:
                    # print(max_mileage2, mileage, "| The car is", (f"{mileage - max_mileage2:,d}km"), "over average")
                    print(cf.nonsuccess())
                    print(mileage_display1())
                    print(cf.calc5(max_mileage2, mileage))
                    print("\n===============================================================\n")
                else:
                    print(cf.success())
                    print(mileage_display1())
                    print(cf.calc0())
                    print("\n===============================================================\n")
        else:
            print("NaN")
        
        cont = input("Another vehicle? (Y/n) ")
        while cont.lower() not in ("y", "n"):
            cont = input("Another vehicle? (Y/n) ")
        if cont == "n":
            break