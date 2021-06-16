def calculator():

    while True:
        from datetime import datetime
        import calc_functions as cf

        current_year = datetime.now().year
        current_month = datetime.now().month
        # current_day = datetime.now().day

        while True:
            try:
                year = int(input("Year first owner reported (e.g. 2020): "))
                break
            except ValueError:
                print(cf.convert0())
        while True:
            try:
                month = int(input("Month first owner reported? (e.g. 5 for May): "))
                break
            except ValueError:
                print(cf.convert0())
        while True:
            try:
                mileage = int(input("Vehicle's mileage: "))
                break
            except ValueError:
                print(cf.convert0())

        year_calc = (current_year - year)

        mileage_average = (year_calc * 19992)
        max_mileage1 = (current_month * 1666)
        max_mileage2 = ((year_calc - 1) * 19992) + ((12 - month) * 1666) + (current_month * 1666)

        def mileage_display():
            return f"Max mileage: {max_mileage1:,d} | Vehicle mileage: {mileage:,d}"

        def mileage_display1():
            return f"Max mileage: {max_mileage2:,d} | Vehicle mileage: {mileage:,d}"

        def mileage_display2():
            return f"Max mileage: {mileage_average:,d} | Vehicle mileage: {mileage:,d}"

        if current_year == year:
            print("\n===============================================================\n")

            if month == current_month or month < current_month:
                print(mileage_display())
                if max_mileage1 > mileage:
                    print(cf.calc7(max_mileage1, mileage))
                    print("\n===============================================================\n")
                elif max_mileage1 < mileage:
                    print(cf.calc8(max_mileage1, mileage))
                    print("\n===============================================================\n")
                else:
                    print(cf.calc0())
                    print("\n===============================================================\n")
            else:
                print("NaN")

        elif current_year > year:
            print("\n===============================================================\n")

            if current_month == month:
                print(mileage_display2())
                if mileage_average > mileage:
                    print(cf.calc1(mileage_average, mileage))
                    print("\n===============================================================\n")
                elif mileage_average < mileage:
                    print(cf.calc2(mileage_average, mileage))
                    print("\n===============================================================\n")
                else:
                    print(cf.calc0())
                    print("\n===============================================================\n")
            elif current_month < month or current_month > month:
                print(mileage_display1())
                if max_mileage2 > mileage:
                    print(cf.calc4(max_mileage2, mileage))
                    print("\n===============================================================\n")
                elif max_mileage2 < mileage:
                    print(cf.calc5(max_mileage2, mileage))
                    print("\n===============================================================\n")
                else:
                    print(cf.calc0())
                    print("\n===============================================================\n")
        else:
            print(cf.warning0())

        has_another_vehicle = input("Another? (y/n): ")
        if has_another_vehicle.lower() == "y":
            pass
        elif has_another_vehicle.lower() == "n":
            break
