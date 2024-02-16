from tkinter import *

root = Tk()


# function for button command
def value():
    print(f"( Name : {namevar.get()},  MobileNo. : {mobilevar.get()},   Gender : {gendervar.get()},   Time : {timevar.get()}, Fees :{feesvar.get()}, yes(1)/no(0) : {yogavar.get()})")

    # using this to save the data into text file
    with open ("details.txt" , "a" ) as f:
        f.write(f"( Name : {namevar.get()},  MobileNo. : {mobilevar.get()},   Gender : {gendervar.get()},   Time : {timevar.get()}, Fees : {feesvar.get()}, yes(1)/no(0) : {yogavar.get()})\n")


# geometry
root.geometry("500x300")

# label
Label(root, text="Power Zone Gym", font="comicsans 13 bold italic underline", borderwidth=5, relief=SUNKEN).grid(row=0,
                                                                                                                 column=2,
                                                                                                                 pady=15)

# label form names grid
name = Label(root, text="Name :", font="comicsans 10 bold").grid(row=1, column=0)
mobile = Label(root, text="MobileNo. :", font="comicsans 10 bold").grid(row=2, column=0)
gender = Label(root, text="Gender :", font="comicsans 10 bold").grid(row=3, column=0)
time = Label(root, text="Time :", font="comicsans 10 bold").grid(row=4, column=0)
fees = Label(root, text="Fees :", font="comicsans 10 bold").grid(row=5, column=0)

# entry type for labels

namevar = StringVar()
mobilevar = IntVar()
gendervar = StringVar()
timevar = StringVar()
feesvar = IntVar()
yogavar = IntVar()

# input from user via Entry

nameent = Entry(root, textvariable=namevar).grid(row=1, column=2)
mobileent = Entry(root, textvariable=mobilevar).grid(row=2, column=2)
genderent = Entry(root, textvariable=gendervar).grid(row=3, column=2)
timeent = Entry(root, textvariable=timevar).grid(row=4, column=2)
feesent = Entry(root, textvariable=feesvar).grid(row=5, column=2)

# checkButton use

yoga = Checkbutton(root, text="want to do yoga ", variable=yogavar).grid(row=6, column=2)

# submit button use

button = Button(root, text="submit", command=value).grid(row=7, column=2)

root.mainloop()