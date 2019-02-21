# https://wiki.python.org/moin/TkInter
from tkinter import *

root = Tk()


def ask_question():
    ans_label.configure(text="Is the last digit of the serial number odd? (y/n)")
    entX.grid(row=7, column=2)
    q_button.grid(row=7, column=3)


def make_answer():
    t_inp = []
    t_inp.extend((ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get(), ent6.get()))  # add input to the list
    while "" in t_inp:  # trim the input
        t_inp.remove("")
    # ---------------------the main decision mechnism
    if len(t_inp) == 3:
        if not ("r" in t_inp):  # If there are no red wires, cut the second wire
            ans_label.configure(text="Cut the second wire")
        elif t_inp[-1] == "w":
            ans_label.configure(text="Cut the last wire")
        elif t_inp.count('b') > 1:  # Otherwise, if there is more than one blue wire, cut the last blue wire
            ans_label.configure(text="Cut the last blue wire")
        else:  # Otherwise, cut the last wire
            ans_label.configure(text="Cut the last wire")

    elif len(t_inp) == 4:
        if t_inp.count('r') > 1:  # If there is more than one red wire...
            # serial = input("Is the last digit of the serial number odd? (y/n)")
            ask_question()
            # if serial == "y": #...and the last digit of the serial number is odd, cut the last red wire.
            #    ans_label.configure(text="Cut the last red wire")
        elif (t_inp[-1] == 'y' and not ("r" in t_inp)) or t_inp.count(
                "b") == 1:  # Otherwise, if the last wire is yellow and there are no red wires, cut the first wire. & Otherwise, if there is exactly one blue wire, cut the first wire.
            ans_label.configure(text="Cut the first wire")
        elif t_inp.count('y') > 1:  # Otherwise, if there is more than one yellow wire, cut the last wire.
            ans_label.configure(text="Cut the last wire")
        else:  # Otherwise, cut the second wire.
            ans_label.configure(text="Cut the second wire")

    elif len(t_inp) == 5:
        if t_inp[
            -1] == 'x':  # If the last wire is black and the last digit of the serial number is odd, cut the fourth wire.
            serial = input("Is the last digit of the serial number odd? (y/n)")
            if serial == "y":
                ans_label.configure(text="Cut the fourth wire")
        elif t_inp.count("r") == 1 and t_inp.count(
                "y") > 1:  # Otherwise, if there is exactly one red wire and there is more than one yellow wire, cut the first wire.
            ans_label.configure(text="Cut the last wire")
        elif not ("x" in t_inp):  # Otherwise, if there are no black wires, cut the second wire.
            ans_label.configure(text="Cut the second wire")
        else:  # Otherwise, cut the first wire.
            ans_label.configure(text="Cut the first wire")

    elif len(t_inp) == 6:
        if not ("y" in t_inp):  # If there are no yellow wires...
            serial = input("Is the last digit of the serial number odd? (y/n)")
            if serial == "y":  # ...and the last digit of the serial number is odd, cut the third wire.
                ans_label.configure(text="Cut the third wire")
        elif t_inp.count("y") == 1 and t_inp.count(
                "w") > 1:  # Otherwise, if there is exactly one yellow wire and there is more than one white wire, cut the fourth wire.
            ans_label.configure(text="Cut the fourth wire")
        elif not ("r" in t_inp):  # Otherwise, if there are no red wires, cut the last wire.
            ans_label.configure(text="Cut the last wire")
        else:  # Otherwise, cut the fourth wire.
            ans_label.configure(text="Cut the fourth wire")

    else:
        ans_label.configure(text="This is not a valid input, please try again")


label0 = Label(root, text="Enter which wires you have in front of you. If there is none, leave the field blank")
label00 = Label(root, text="r (red), b (blue), g (green), y (yellow), w (white), x (black) ")
label1 = Label(root, text="Wire 1")
label2 = Label(root, text="Wire 2")
label3 = Label(root, text="Wire 3")
label4 = Label(root, text="Wire 4")
label5 = Label(root, text="Wire 5")
label6 = Label(root, text="Wire 6")
ent1 = Entry(root, width=2)
ent2 = Entry(root, width=2)
ent3 = Entry(root, width=2)
ent4 = Entry(root, width=2)
ent5 = Entry(root, width=2)
ent6 = Entry(root, width=2)
button1 = Button(root, text='Done', command=make_answer)
ans_label = Label(root, text="...")
entX = Entry(root, width=2)


def send_ans():
    ans = entX.get().lower


q_button = Button(root, text='Okay', command=send_ans)

label0.grid(row=0, columnspan=6)
label00.grid(row=1, columnspan=6)
label1.grid(row=2)
ent1.grid(row=3)
label2.grid(row=2, column=1)
ent2.grid(row=3, column=1)
label3.grid(row=2, column=2)
ent3.grid(row=3, column=2)
label4.grid(row=2, column=3)
ent4.grid(row=3, column=3)
label5.grid(row=2, column=4)
ent5.grid(row=3, column=4)
label6.grid(row=2, column=5)
ent6.grid(row=3, column=5)
ans_label.grid(row=4, columnspan=6)
button1.grid(row=6, columnspan=6)

root.mainloop()
