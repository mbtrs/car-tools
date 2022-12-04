import json

cars = json.loads(cars.json)

pbmw = input("?p")
qbmw = input("?q")

if pbmw == "bmw":
    print(cars["car"][0]["brand"])
    if qbmw == "1":
        print(cars["car"][0]["model"])
        print(cars["car"][0]["body_style"])
    elif qbmw == "2":
        print(cars["car"][1]["model"])
        print(cars["car"][1]["body_style"])
    else:
        print("none")
else:
    print("not")
