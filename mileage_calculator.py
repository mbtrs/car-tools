def calculator():
    while True:
        import library as lb

        year = lb.year_input()
        month = lb.month_input()
        mileage = lb.mileage_input()

        year_calc = (lb.current_year - year)

        mileage_average = (year_calc * 19992)
        max_mileage_1 = (lb.current_month * 1666)
        max_mileage_2 = ((year_calc - 1) * 19992) + ((12 - month) * 1666) + (lb.current_month * 1666)

        if lb.current_year == year:
            if month <= lb.current_month:
                print(lb.mileage_display(max_mileage_1, mileage))
                if max_mileage_1 > mileage:
                    text_1 = lb.find_longest_statement([lb.mileage_display(max_mileage_1, mileage), lb.max_mileage_gt_mileage_2(max_mileage_1, mileage)])
                    print(text_1 + lb.max_mileage_gt_mileage_2(max_mileage_1, mileage) + text_1)
                elif max_mileage_1 < mileage:
                    text_2 = lb.find_longest_statement([lb.mileage_display(max_mileage_1, mileage), lb.max_mileage_lt_mileage_2(max_mileage_1, mileage)])
                    print(text_2 + lb.max_mileage_lt_mileage_2(max_mileage_1, mileage) + text_2)
                else:
                    print(lb.max_mileage_equals_mileage())
            else:
                print(lb.error0())
        elif year < lb.current_year:
            if lb.current_month != month:
                print(lb.mileage_display_1(max_mileage_2, mileage))
                if max_mileage_2 > mileage:
                    text_3 = lb.find_longest_statement([lb.mileage_display_1(max_mileage_2, mileage), lb.max_mileage_gt_mileage_1(max_mileage_2, mileage)])
                    print(text_3 + lb.max_mileage_gt_mileage_1(max_mileage_2, mileage) + text_3)
                elif max_mileage_2 < mileage:
                    text_4 = lb.find_longest_statement([lb.mileage_display_1(max_mileage_2, mileage), lb.max_mileage_lt_mileage_1(max_mileage_2, mileage)])
                    print(text_4 + lb.max_mileage_lt_mileage_1(max_mileage_2, mileage) + text_4)
                else:
                    print(lb.max_mileage_equals_mileage())
            elif lb.current_month == month:
                print(lb.mileage_display_2(mileage_average, mileage))
                if mileage_average > mileage:
                    text_5 = lb.find_longest_statement([lb.mileage_display_2(mileage_average, mileage), lb.max_mileage_gt_mileage_3(mileage_average, mileage)])
                    print(text_5 + lb.max_mileage_gt_mileage_3(mileage_average, mileage) + text_5)
                elif mileage_average < mileage:
                    text_6 = lb.find_longest_statement([lb.mileage_display_2(mileage_average, mileage), lb.max_mileage_lt_mileage_3(mileage_average, mileage)])
                    print(text_6 + lb.max_mileage_lt_mileage_3(mileage_average, mileage) + text_6)
                else:
                    print(lb.max_mileage_equals_mileage())
        else:
            print(lb.warning0())


        has_another_vehicle = input("Another vehicle? (y/n): ").lower()
        if has_another_vehicle in ("y", "yes"):
            pass
        else:
            break
