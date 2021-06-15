while True:
    import mileage_calculator as mc
    import convert as km
    # import car_directory as dr

    print("\n==========MENU==========\n")
    print("Enter 1 for calculator")
    print("Enter 2 for converter")
    # print("(3) Car directory")
    print("\n==========MENU==========\n")

    option = input("Option: ")

    if option == "1":
        mc.calculator()
    elif option == "2":
        km.convert()
    # elif option == "3":
    #     dr.directory()
    else:
        print("This is not a valid entry.")
