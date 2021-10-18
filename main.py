from tkinter import *
# Creating a new window and configurations

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


entry = Entry(width=15, font=("Courier", 12))
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
entry.grid(column=2, row=2)

# Label 2
label2 = Label(text="Miles", font=("Courier", 12))
label2.grid(column=3, row=2)
label2.config(padx=30)

# Label 3
label3 = Label(text="is equal to", font=("Courier", 12))
label3.grid(column=1, row=3)
label3.config(padx=30)

# Label 4
label3 = Label(text=0)
label3.grid(column=2, row=3)
label3.config(padx=30)

# Label 5
label5 = Label(text="Km", font=("Courier", 12))
label5.grid(column=3, row=3)
label5.config(padx=30)


def calculate():
    mile = 1.609
    my_entry = float(entry.get())
    miles = round(my_entry * mile)
    label3.config(text=miles)


# Button
button = Button(text="Calculate", font=("Courier", 12, "bold"), command=calculate)
button.grid(column=2, row=4)
button.config(padx=30)


window.mainloop()
