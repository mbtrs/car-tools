def calculator():
    while True:
        import the_brains

        the_brains.year
        the_brains.month
        the_brains.mileage

        if the_brains.current_year == the_brains.year:
            if the_brains.month <= the_brains.current_month:
                print(the_brains.mileage_display(the_brains.max_mileage_1, the_brains.mileage))
                if the_brains.max_mileage_1 > the_brains.mileage:
                    text_1 = the_brains.find_longest_statement([the_brains.mileage_display(the_brains.max_mileage_1, the_brains.mileage), the_brains.max_mileage_gt_mileage_2(the_brains.max_mileage_1, the_brains.mileage)])
                    print(text_1 + the_brains.max_mileage_gt_mileage_2(the_brains.max_mileage_1, the_brains.mileage) + text_1)
                elif the_brains.max_mileage_1 < the_brains.mileage:
                    text_2 = the_brains.find_longest_statement([the_brains.mileage_display(the_brains.max_mileage_1, the_brains.mileage), the_brains.max_mileage_lt_mileage_2(the_brains.max_mileage_1, the_brains.mileage)])
                    print(text_2 + the_brains.max_mileage_lt_mileage_2(the_brains.max_mileage_1, the_brains.mileage) + text_2)
                else:
                    print(the_brains.max_mileage_equals_mileage())
            else:
                print(the_brains.error0())
        elif the_brains.year < the_brains.current_year:
            if the_brains.current_month != the_brains.month:
                print(the_brains.mileage_display_1(the_brains.max_mileage_2, the_brains.mileage))
                if the_brains.max_mileage_2 > the_brains.mileage:
                    text_3 = the_brains.find_longest_statement([the_brains.mileage_display_1(the_brains.max_mileage_2, the_brains.mileage), the_brains.max_mileage_gt_mileage_1(the_brains.max_mileage_2, the_brains.mileage)])
                    print(text_3 + the_brains.max_mileage_gt_mileage_1(the_brains.max_mileage_2, the_brains.mileage) + text_3)
                elif the_brains.max_mileage_2 < the_brains.mileage:
                    text_4 = the_brains.find_longest_statement([the_brains.mileage_display_1(the_brains.max_mileage_2, the_brains.mileage), the_brains.max_mileage_lt_mileage_1(the_brains.max_mileage_2, the_brains.mileage)])
                    print(text_4 + the_brains.max_mileage_lt_mileage_1(the_brains.max_mileage_2, the_brains.mileage) + text_4)
                else:
                    print(the_brains.max_mileage_equals_mileage())
            elif the_brains.current_month == the_brains.month:
                print(the_brains.mileage_display_2(the_brains.mileage_average, the_brains.mileage))
                if the_brains.mileage_average > the_brains.mileage:
                    text_5 = the_brains.find_longest_statement([the_brains.mileage_display_2(the_brains.mileage_average, the_brains.mileage), the_brains.max_mileage_gt_mileage_3(the_brains.mileage_average, the_brains.mileage)])
                    print(text_5 + the_brains.max_mileage_gt_mileage_3(the_brains.mileage_average, the_brains.mileage) + text_5)
                elif the_brains.mileage_average < the_brains.mileage:
                    text_6 = the_brains.find_longest_statement([the_brains.mileage_display_2(the_brains.mileage_average, the_brains.mileage), the_brains.max_mileage_lt_mileage_3(the_brains.mileage_average, the_brains.mileage)])
                    print(text_6 + the_brains.max_mileage_lt_mileage_3(the_brains.mileage_average, the_brains.mileage) + text_6)
                else:
                    print(the_brains.max_mileage_equals_mileage())
        else:
            print(the_brains.warning0())

        has_another_vehicle = input("Another vehicle? (y/n): ").lower()
        if has_another_vehicle in ("y", "yes"):
            pass
        else:
            break
