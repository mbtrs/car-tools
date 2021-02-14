def calculator():
    while True:
        
        from datetime import datetime

        current_year = datetime.now().year
        current_month = datetime.now().month
        # current_day = datetime.now().day

        year = int(input("Year first owner reported (e.g. 2020): "))
        month = int(input("Month first owner reported? (e.g. 5): "))
        mileage = int(input("Mileage of vehicle: "))

        year_calc = (current_year - year)

        mileage_average = (year_calc * 19992)
        max_mileage1 = (current_month * 1666)
        max_mileage2 = ((year_calc - 1) * 19992) + ((12 - month) * 1666) + (current_month * 1666)

        # class bcolors:
        #     HEADER = '\033[95m'
        #     OKBLUE = '\033[94m'
        #     OKCYAN = '\033[96m'
        #     OKGREEN = '\033[92m'
        #     WARNING = '\033[93m'
        #     FAIL = '\033[91m'
        #     ENDC = '\033[0m'
        #     BOLD = '\033[1m'
        #     UNDERLINE = '\033[4m'

        # TGREEN =  '\033[32;1m' # Green Text
        # TRED =  '\033[31;1m' # Red Text


        def calc0():
            return(f"The vehicle's average mileage and current mileage match.")

        def calc1(mileage_average, mileage):
            return(f"The vehicle is {mileage_average - mileage:,d}km under average.")

        def calc2(mileage_average, mileage):
            return(f"The vehicle is {mileage - mileage_average:,d}km over average.")

        def calc4(max_mileage2, mileage):
            return(f"The vehicle is {max_mileage2 - mileage:,d}km under average.")

        def calc5(max_mileage2, mileage):
            return(f"The vehicle is {mileage - max_mileage2:,d}km over average.")

        def calc7(max_mileage1, mileage):
            return(f"The vehicle is {max_mileage1 - mileage:,d}km under average.")

        def calc8(max_mileage1, mileage):
            return(f"The vehicle is {mileage - max_mileage1:,d}km over average.")

        if current_year == year:
            print("\n===============================================================\n")

            if month == current_month:
                if max_mileage1 > mileage:
                    print("Success")
                    print("Max mileage:", (f"{max_mileage1:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc7(max_mileage1, mileage))
                    print("\n===============================================================\n")
                elif max_mileage1 < mileage:
                    print("Fail")
                    print("Max mileage:", (f"{max_mileage1:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc8(max_mileage1, mileage))
                    print("\n===============================================================\n")
                else:
                    print("Success")
                    print("Max mileage:", (f"{max_mileage1:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc0())
                    print("\n===============================================================\n")
            elif month < current_month:
                if max_mileage1 > mileage:
                    print("Success")
                    print("Max mileage:", (f"{max_mileage1:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc7(max_mileage1, mileage))
                    print("\n===============================================================\n")
                elif max_mileage1 < mileage:
                    print("Fail")
                    print("Max mileage:", (f"{max_mileage1:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc8(max_mileage1, mileage))
                    print("\n===============================================================\n")
                else:
                    print("Success")
                    print("Max mileage:", (f"{max_mileage1:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc0())
                    print("\n===============================================================\n")
            else:
                print("NaN")

        elif current_year > year:
            print("\n===============================================================\n")

            if current_month == month:
                if mileage_average > mileage:
                    print("Success")
                    print("Max mileage:", (f"{mileage_average:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc1(mileage_average, mileage))
                    print("\n===============================================================\n")
                elif mileage_average < mileage:
                    # print(mileage_average, mileage, "| The car is", (f"{mileage - mileage_average:,d}km"), "over average")
                    print("Nonsuccess")
                    print("Max mileage:", (f"{mileage_average:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc2(mileage_average, mileage))
                    print("\n===============================================================\n")
                else:
                    print("Success")
                    print("Max mileage:", (f"{mileage_average:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc0())
                    print("\n===============================================================\n")
            elif current_month < month:
                if max_mileage2 > mileage:
                    # print(max_mileage2, mileage, "| The car is", (f"{max_mileage2 - mileage:,d}km"), "under average")
                    print("Success")
                    print("Max mileage:", (f"{max_mileage2:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc4(max_mileage2, mileage))
                    print("\n===============================================================\n")
                elif max_mileage2 < mileage:
                    # print(max_mileage2, mileage, "| The car is", (f"{mileage - max_mileage2:,d}km"), "over average")
                    print("Nonsuccess")
                    print("Max mileage:", (f"{max_mileage2:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc5(max_mileage2, mileage))
                    print("\n===============================================================\n")
                else:
                    print("Success")
                    print("Max mileage:", (f"{max_mileage2:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc0())
                    print("\n===============================================================\n")
            else:
                if max_mileage2 > mileage:
                    # print(max_mileage2, mileage, "| The car is", (f"{max_mileage2 - mileage:,d}km"), "under average")
                    print("Success")
                    print("Max mileage:", (f"{max_mileage2:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc4(max_mileage2, mileage))
                    print("\n===============================================================\n")

                elif max_mileage2 < mileage:
                    # print(max_mileage2, mileage, "| The car is", (f"{mileage - max_mileage2:,d}km"), "over average")
                    print("Nonsuccess")
                    print("Max mileage:", (f"{max_mileage2:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc5(max_mileage2, mileage))
                    print("\n===============================================================\n")
                else:
                    print("Success")
                    print("Max mileage:", (f"{max_mileage2:,d}"), "|", "Vehicle mileage:", (f"{mileage:,d}"))
                    print(calc0())
                    print("\n===============================================================\n")
        else:
            print("NaN")
        
        cont = input("Another vehicle? (y/n) ")
        while cont.lower() not in ("y", "n"):
            cont = input("Another vehicle? (y/n) ")
        if cont == "n":
            break