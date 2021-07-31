def calculator():

    while True:

        import library as lb

        year = lb.year_question()
        month = lb.month_question()
        mileage = lb.mileage_question()

        year_calc = (lb.current_year - year)

        mileage_average = (year_calc * 19992)
        max_mileage_1 = (lb.current_month * 1666)
        max_mileage_2 = ((year_calc - 1) * 19992) + ((12 - month) * 1666) + (lb.current_month * 1666)

        if lb.current_year == year:
            print(lb.lines())

            if month <= lb.current_month:
                print(lb.mileage_display(max_mileage_1, mileage))
                if max_mileage_1 > mileage:
                    print(lb.calc7(max_mileage_1, mileage))
                elif max_mileage_1 < mileage:
                    print(lb.calc8(max_mileage_1, mileage))
                else:
                    print(lb.calc0())
            else:
                print(lb.error0())

            print(lb.lines())

        elif year < lb.current_year:
            print(lb.lines())

            if lb.current_month != month:
                print(lb.mileage_display_1(max_mileage_2, mileage))
                if max_mileage_2 > mileage:
                    print(lb.calc4(max_mileage_2, mileage))
                elif max_mileage_2 < mileage:
                    print(lb.calc5(max_mileage_2, mileage))
                else:
                    print(lb.calc0())
            elif lb.current_month == month:
                print(lb.mileage_display_2(mileage_average, mileage))
                if mileage_average > mileage:
                    print(lb.calc1(mileage_average, mileage))
                elif mileage_average < mileage:
                    print(lb.calc2(mileage_average, mileage))
                else:
                    print(lb.calc0())

            print(lb.lines())

        else:
            print(lb.warning0())

        has_another_vehicle = input("Another vehicle? ").lower()
        if has_another_vehicle in ("y", "yes"):
            pass
        else:
            break
