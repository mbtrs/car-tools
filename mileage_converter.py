def converter():
    while True:
        import library as lb

        print("\n==========MENU==========\n")
        print("Enter 1 for km to miles")
        print("Enter 2 for miles to km")
        print("\n==========MENU==========\n")

        option = input("Option: ")

        if option == "1":
            try:
                km = int(input("Kilometers: "))
                km_calc = float(km / 1.609344)
                print(f"{km} kilometers is equivalent to {round(km_calc, 4)} miles.")
            except ValueError:
                print(lb.convert0())

        elif option == "2":
            try:
                m = int(input("Miles: "))
                m_calc = float(m * 1.609344)
                print(f"{m} miles is equivalent to {round(m_calc, 4)} kilometers.")
            except ValueError:
                print(lb.convert0())
        else:
            print(l.convert0())

        has_another_calc = input("Another? (y/n): ")
        if has_another_calc.lower() == "y":
            pass
        elif has_another_calc.lower() == "n":
            break
