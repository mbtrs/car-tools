while True:
    import mileage_calculator
    import mileage_converter
    # import car_directory as dr

    print("\n==========MENU==========\n")
    print("Enter 1 for calculator")
    print("Enter 2 for converter")
    # print("(3) Car directory")
    print("Enter 3 to exit")
    print("\n==========MENU==========\n")

    option = input("Option: ")

    if option == "1":
        mileage_calculator.calculator()
    elif option == "2":
        mileage_converter.converter()
    # elif option == "3":
    #     dr.directory()
    elif option == "3":
        exit()
    else:
        print("This is not a valid entry.")
