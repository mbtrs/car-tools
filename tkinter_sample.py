from tkinter import *

top = Tk()
top.geometry("415x300")

year = Label(top, text = "Year first owner reported (e.g. 2020):").place(x = 40, y = 60)   

month = Label(top, text = "Month first owner reported? (e.g. 5):").place(x = 40, y = 100)

mileage = Label(top, text = "Mileage of vehicle:").place(x = 40, y = 140)
    
submit_button = Button(top, text = "Submit").place(x = 40, y = 170) 
    
year_input_area = Entry(top, width = 5).place(x = 275, y = 60)   
    
month_entry_area = Entry(top, width = 5).place(x = 270, y = 100)   

mileage_entry_area = Entry(top, width = 7).place(x = 160, y = 140)   

top.mainloop()