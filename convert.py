def convert():
    
    print("=====MENU=====")
    print("(1) km to miles")
    print("(2) miles to km")
    print("=====MENU=====")

    option = input("Option: ")

    if option == "1":
        km = int(input("Kilometers: "))
        km_calc = float(km/1.60934)
        print(f'{km} kilometers is equivalent to {round(km_calc,0)} miles.')
    elif option == "2":
        m = int(input("Miles: "))
        m_calc = float(m*1.60934)
        print(f'{m} miles is equivalent to {round(m_calc,0)} kilometers.')

    else:
        print("This is not a valid entry")