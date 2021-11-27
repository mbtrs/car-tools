def calculator():
    while True:
        import the_brains

        year = the_brains.year()
        month = the_brains.month()
        mileage = the_brains.mileage()

        year_calc = (the_brains.current_year - year)

        mileage_average = (year_calc * 19992)
        max_mileage_1 = (the_brains.current_month * 1666)
        max_mileage_2 = ((year_calc - 1) * 19992) + ((12 - month) * 1666) + (the_brains.current_month * 1666)

        if the_brains.current_year == year:
            if month <= the_brains.current_month:
                print(the_brains.mileage_display(max_mileage_1, mileage))
                if max_mileage_1 > mileage:
                    text_1 = the_brains.find_longest_statement([the_brains.mileage_display(max_mileage_1, mileage), the_brains.max_mileage_gt_mileage_2(max_mileage_1, mileage)])
                    print(text_1 + the_brains.max_mileage_gt_mileage_2(max_mileage_1, mileage) + text_1)
                elif max_mileage_1 < mileage:
                    text_2 = the_brains.find_longest_statement([the_brains.mileage_display(max_mileage_1, mileage), the_brains.max_mileage_lt_mileage_2(max_mileage_1, mileage)])
                    print(text_2 + the_brains.max_mileage_lt_mileage_2(max_mileage_1, mileage) + text_2)
                else:
                    print(the_brains.max_mileage_equals_mileage())
            else:
                print(the_brains.error0())
        elif year < the_brains.current_year:
            if the_brains.current_month != month:
                print(the_brains.mileage_display_1(max_mileage_2, mileage))
                if max_mileage_2 > mileage:
                    text_3 = the_brains.find_longest_statement([the_brains.mileage_display_1(max_mileage_2, mileage), the_brains.max_mileage_gt_mileage_1(max_mileage_2, mileage)])
                    print(text_3 + the_brains.max_mileage_gt_mileage_1(max_mileage_2, mileage) + text_3)
                elif max_mileage_2 < mileage:
                    text_4 = the_brains.find_longest_statement([the_brains.mileage_display_1(max_mileage_2, mileage), the_brains.max_mileage_lt_mileage_1(max_mileage_2, mileage)])
                    print(text_4 + the_brains.max_mileage_lt_mileage_1(max_mileage_2, mileage) + text_4)
                else:
                    print(the_brains.max_mileage_equals_mileage())
            elif the_brains.current_month == month:
                print(the_brains.mileage_display_2(mileage_average, mileage))
                if mileage_average > mileage:
                    text_5 = the_brains.find_longest_statement([the_brains.mileage_display_2(mileage_average, mileage), the_brains.max_mileage_gt_mileage_3(mileage_average, mileage)])
                    print(text_5 + the_brains.max_mileage_gt_mileage_3(mileage_average, mileage) + text_5)
                elif mileage_average < mileage:
                    text_6 = the_brains.find_longest_statement([the_brains.mileage_display_2(mileage_average, mileage), the_brains.max_mileage_lt_mileage_3(mileage_average, mileage)])
                    print(text_6 + the_brains.max_mileage_lt_mileage_3(mileage_average, mileage) + text_6)
                else:
                    print(the_brains.max_mileage_equals_mileage())
        else:
            print(the_brains.warning0())


        has_another_vehicle = input("Another vehicle? (y/n): ").lower()
        if has_another_vehicle in ("y", "yes"):
            pass
        else:
            break
