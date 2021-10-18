from tkinter import *
# Creating a new window and configurations

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
entry.grid(column=2, row=2)

# Label 2
label2 = Label(text="Miles")
label2.grid(column=3, row=2)
label2.config(padx=30)

# Label 3
label3 = Label(text="is equal to")
label3.grid(column=1, row=3)
label3.config(padx=30)

# Label 4
label3 = Label(text=0)
label3.grid(column=2, row=3)
label3.config(padx=30)

# Label 5
label5 = Label(text="Km")
label5.grid(column=3, row=3)
label5.config(padx=30)


def calculate():
    mile = 1.609
    my_entry = int(entry.get())
    miles = my_entry * mile
    label3.config(text=miles)


# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=4)
button.config(padx=30)


window.mainloop()
