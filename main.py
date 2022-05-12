from tkinter import *
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)
# row 1
mile_input = Entry(text="0", width=10)
mile_input.grid(column=1, row=1)
mile_label = Label(text="Miles", font=("Arial", 20, "normal"))
mile_label.grid(column=2, row=1)
# row 2
explain = Label(text="is equal to", font=("Arial", 20, "normal"))
explain.grid(column=0, row=2)
kilo_output = Label(text="0")
kilo_output.grid(column=1, row=2)
kilo_label = Label(text="Km", font=("Arial", 20, "normal"))
mile_label.grid(column=2, row=2)


def convert_mile_to_kilo():
    miles_value = int(mile_input.get())
    kilo_value = round(miles_value*1.609)
    kilo_output.config(text=kilo_value)

# row 3
button = Button(text="Calculate", command=convert_mile_to_kilo)
button.grid(column=1, row=3)

window.mainloop()