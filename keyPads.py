# https://wiki.python.org/moin/TkInter
from tkinter import *
import os

originalPath = os.getcwd()
os.chdir(".\Keys")

root = Tk()

label0 = Label(root, text="Press the four symbols your module has")
label1 = Label(root, text="Press the following buttons in the following order:")
order = [0, 0, 0, 0]


def exchange(var):
    var = var.replace("l", "b")
    return var


def keypad2(code):  # determines which buttons to press
    c1 = ("l1", "l2", "l3", "l4", "l5", "l6", "l7")
    c2 = ("l8", "l1", "l7", "l9", "l10", "l6", "l11")
    c3 = ("l12", "l13", "l9", "l14", "l15", "l3", "l10")
    c4 = ("l16", "l17", "l18", "l5", "l14", "l11", "l19")
    c5 = ("l20", "l19", "l18", "l21", "l17", "l22", "l23")
    c6 = ("l16", "l8", "l24", "l25", "l20", "l26", "l27")
    answer = []
    dct = {'l1': b1, 'l2': b2, 'l3': b3, 'l4': b4, 'l5': b5, 'l6': b6, 'l7': b7, 'l8': b8, 'l9': b9, 'l10': b10,
           'l11': b11,
           'l12': b12, 'l13': b13, 'l14': b14, 'l15': b15, 'l16': b16, 'l17': b17, 'l18': b18, 'l19': b19, 'l20': b20,
           'l21': b21, 'l22': b22, 'l23': b23, 'l24': b24, 'l25': b25, 'l26': b26,
           'l27': b27, }  # variables with their images
    if all(i in c1 for i in code):  # if all four entered keys are in the first column
        for i in c1:  # if a column item is in the code, append it to the answer
            if i in code:
                answer.append(i)
    elif all(i in c2 for i in code):  # if all four entered keys are in the second column
        for i in c2:
            if i in code:
                answer.append(i)
    elif all(i in c3 for i in code):
        for i in c3:
            if i in code:
                answer.append(i)
    elif all(i in c4 for i in code):
        for i in c4:
            if i in code:
                answer.append(i)
    elif all(i in c5 for i in code):
        for i in c5:
            if i in code:
                answer.append(i)
    elif all(i in c6 for i in code):
        for i in c6:
            if i in code:
                answer.append(i)
    else:
        print("Error")
    ans1.configure(image=dct[answer[0]])  # set the answer to the right images
    ans2.configure(image=dct[answer[1]])
    ans3.configure(image=dct[answer[2]])
    ans4.configure(image=dct[answer[3]])


def p(param):  # add the clicked item to the list and make sure it does not exceed 4 items
    if param not in order:
        order.insert(0, param)
        del order[-1]


# Make the images----------------
b1 = PhotoImage(file='l1.png')
b2 = PhotoImage(file='l2.png')
b3 = PhotoImage(file='l3.png')
b4 = PhotoImage(file='l4.png')
b5 = PhotoImage(file='l5.png')
b6 = PhotoImage(file='l6.png')
b7 = PhotoImage(file='l7.png')
b8 = PhotoImage(file='l8.png')
b9 = PhotoImage(file='l9.png')
b10 = PhotoImage(file='l10.png')
b11 = PhotoImage(file='l11.png')
b12 = PhotoImage(file='l12.png')
b13 = PhotoImage(file='l13.png')
b14 = PhotoImage(file='l14.png')
b15 = PhotoImage(file='l15.png')
b16 = PhotoImage(file='l16.png')
b17 = PhotoImage(file='l17.png')
b18 = PhotoImage(file='l18.png')
b19 = PhotoImage(file='l19.png')
b20 = PhotoImage(file='l20.png')
b21 = PhotoImage(file='l21.png')
b22 = PhotoImage(file='l22.png')
b23 = PhotoImage(file='l23.png')
b24 = PhotoImage(file='l24.png')
b25 = PhotoImage(file='l25.png')
b26 = PhotoImage(file='l26.png')
b27 = PhotoImage(file='l27.png')
blank = PhotoImage(file='blank.png')
# ----------------------------------

# make the buttons------------------
button1 = Button(root, image=b1, borderwidth=0, command=lambda: p("l1"))
button2 = Button(root, image=b2, borderwidth=0, command=lambda: p("l2"))
button3 = Button(root, image=b3, borderwidth=0, command=lambda: p("l3"))
button4 = Button(root, image=b4, borderwidth=0, command=lambda: p("l4"))
button5 = Button(root, image=b5, borderwidth=0, command=lambda: p("l5"))
button6 = Button(root, image=b6, borderwidth=0, command=lambda: p("l6"))
button7 = Button(root, image=b7, borderwidth=0, command=lambda: p("l7"))
button8 = Button(root, image=b8, borderwidth=0, command=lambda: p("l8"))
button9 = Button(root, image=b9, borderwidth=0, command=lambda: p("l9"))
button10 = Button(root, image=b10, borderwidth=0, command=lambda: p("l10"))
button11 = Button(root, image=b11, borderwidth=0, command=lambda: p("l11"))
button12 = Button(root, image=b12, borderwidth=0, command=lambda: p("l12"))
button13 = Button(root, image=b13, borderwidth=0, command=lambda: p("l13"))
button14 = Button(root, image=b14, borderwidth=0, command=lambda: p("l14"))
button15 = Button(root, image=b15, borderwidth=0, command=lambda: p("l15"))
button16 = Button(root, image=b16, borderwidth=0, command=lambda: p("l16"))
button17 = Button(root, image=b17, borderwidth=0, command=lambda: p("l17"))
button18 = Button(root, image=b18, borderwidth=0, command=lambda: p("l18"))
button19 = Button(root, image=b19, borderwidth=0, command=lambda: p("l19"))
button20 = Button(root, image=b20, borderwidth=0, command=lambda: p("l20"))
button21 = Button(root, image=b21, borderwidth=0, command=lambda: p("l21"))
button22 = Button(root, image=b22, borderwidth=0, command=lambda: p("l22"))
button23 = Button(root, image=b23, borderwidth=0, command=lambda: p("l23"))
button24 = Button(root, image=b24, borderwidth=0, command=lambda: p("l24"))
button25 = Button(root, image=b25, borderwidth=0, command=lambda: p("l25"))
button26 = Button(root, image=b26, borderwidth=0, command=lambda: p("l26"))
button27 = Button(root, image=b27, borderwidth=0, command=lambda: p("l27"))
pbutton = Button(root, text="Done", command=lambda: keypad2(order))  # the execute button
# --------------------------------

# make the final answer block
ans1 = Label(root, image=blank)
ans2 = Label(root, image=blank)
ans3 = Label(root, image=blank)
ans4 = Label(root, image=blank)
# ---------------------

# put the buttons in the grid-
label0.grid(row=0, columnspan=9)
button1.grid(row=1)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=1, column=3)
button5.grid(row=1, column=4)
button6.grid(row=1, column=5)
button7.grid(row=1, column=6)
button8.grid(row=1, column=7)
button9.grid(row=1, column=8)
button10.grid(row=2)
button11.grid(row=2, column=1)
button12.grid(row=2, column=2)
button13.grid(row=2, column=3)
button14.grid(row=2, column=4)
button15.grid(row=2, column=5)
button16.grid(row=2, column=6)
button17.grid(row=2, column=7)
button18.grid(row=2, column=8)
button19.grid(row=3)
button20.grid(row=3, column=1)
button21.grid(row=3, column=2)
button22.grid(row=3, column=3)
button23.grid(row=3, column=4)
button24.grid(row=3, column=5)
button25.grid(row=3, column=6)
button26.grid(row=3, column=7)
button27.grid(row=3, column=8)
pbutton.grid(row=4, column=4)
label1.grid(row=5, columnspan=9)
ans1.grid(row=6, column=3)
ans2.grid(row=6, column=4)
ans3.grid(row=6, column=5)
ans4.grid(row=6, column=6)
# -----------------------------


root.mainloop()
os.chdir(originalPath)
