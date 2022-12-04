a = ["bmw", "mercedes", "jaguar"]
graph = input("?")
b = ["1 series", "2 series"]
graph2 = input("?")

if graph in a and graph2 in b:
    print(
        "1. 1 series"
        "2. 2 series"
    )
    print("")
else:
    print("none")


# ===========

# xf = re.search(r'\d{4}', str(year))
# if xf:
#     xf = year

# while True:
#     try:
#         xf = re.search(r'[1-3][5-9]{2}[0-9]', str(year))
#         break
#     except ValueError:
#         print(cf.error0())
# return xf
# if xf:
#     xf = year
# year = re.findall(r'[1-3][5-9]{3}', xf)
# if xf:
#     xf = year