"""
Developed by:

Ajay Krishna KV         Roll No. 07
Nandakishor M Pai       Roll No. 45
Paurnami Pradeep        Roll No. 50
Sudev Suresh Sreedevi   Roll No. 60

"""

from tkinter import *
from tkinter import messagebox


def submit():
    if(tf1.get() == ""):
        messagebox.showinfo("ERROR", "Please Enter Name!")
    else:
        global mark8
        global total
        if(mark8 == 0):
            messagebox.showinfo(
                "RESULT", "The score is:"+str(round(total, 2))+"/200.0\n")
        elif mark8 > 0:
            messagebox.showinfo(
                "RESULT", "The score is:"+str(round(total, 2))+"/200.0\n")
        else:
            messagebox.showinfo("RESULT", "The score is:"+str(
                round(total, 2))+"/200.0\n")


def select1():
    if(var.get() == 1):
        mark1 = 20
    elif var.get() == 2:
        mark1 = 15
    elif var.get() == 3:
        mark1 = 10
    elif var.get() == 4:
        mark1 = 5
    else:
        mark1 = 0
    global total
    total = total+mark1


def select2():
    if(var1.get() == 6):
        mark2 = 20
    elif var1.get() == 7:
        mark2 = 15
    elif var1.get() == 8:
        mark2 = 10
    elif var1.get() == 9:
        mark2 = 5
    else:
        mark2 = 0
    global total
    total = total+mark2


def select3():
    if(var2.get() == 11):
        mark3 = 20
    elif var2.get() == 12:
        mark3 = 15
    elif var2.get() == 13:
        mark3 = 10
    elif var2.get() == 14:
        mark3 = 5
    else:
        mark3 = 0
    global total
    total = total+mark3


def select4():
    if(var3.get() == 16):
        mark4 = 20
    elif var3.get() == 17:
        mark4 = 15
    elif var3.get() == 18:
        mark4 = 10
    elif var3.get() == 19:
        mark4 = 5
    else:
        mark4 = 0
    global total
    total = total+mark4


def select5():
    if(var4.get() == 21):
        mark5 = 20
    elif var4.get() == 22:
        mark5 = 15
    elif var4.get() == 23:
        mark5 = 10
    elif var4.get() == 24:
        mark5 = 5
    else:
        mark5 = 0
    global total
    total = total+mark5


def select6():
    if(var5.get() == 26):
        mark6 = 20
    else:
        mark6 = 0
    global total
    total = total+mark6


def select7():
    if(var6.get() == 28):
        mark7 = 20
    elif(var6.get() == 29):
        mark7 = 10
    else:
        mark7 = 5
    global total
    total = total+mark7


def select8():
    global mark8
    if(var7.get() == 31):
        mark8 += 0
    elif(var7.get() == 32):
        mark8 += 1
    else:
        mark8 -= 1


def select9():
    if(var8.get() == 34):
        mark9 = 20
    elif(var8.get() == 35):
        mark9 = 10
    else:
        mark9 = 0
    global total
    total = total+mark9


def select10():
    if(var9.get() == 37):
        mark10 = 20
    elif(var9.get() == 38):
        mark10 = 10
    else:
        mark10 = 0
    global total
    total = total+mark10


def select11():
    if(var10.get() == 40):
        mark11 = 20
    elif(var10.get() == 41):
        mark11 = 0
    else:
        mark11 = 10
    global total
    total = total+mark11


screen = Tk()
total = 0
mark1 = 0
mark2 = 0
mark3 = 0
mark4 = 0
mark5 = 0
mark6 = 0
mark7 = 0
mark8 = 0
mark9 = 0

screen.title("Faculty Evaluation")

lb1 = Label(screen, text="COLLEGE OF ENGINEERING TRIVANDRUM").grid(
    row=1, columnspan=6, sticky="NSEW", pady=5)

lb2 = Label(screen, text="STUDENTS' EVALUATION OF TEACHERS").grid(
    row=2, columnspan=6, sticky="NSEW", pady=5)

lb3 = Label(screen, text="CST201:DATA STRUCTURES").grid(
    row=3, columnspan=6, sticky="NSEW", pady=5)

lb4 = Label(screen, text="NAME OF STUDENT:").grid(row=4, sticky="NSEW")
t1 = StringVar(screen)
tf1 = Entry(screen, textvariable=t1, width=30)
tf1.grid(row=4, column=1, sticky="W", padx=10, pady=5, columnspan=2)


# lb5 = Label(screen, text="ATTENDANCE:").grid(row=5, sticky="NSEW")
# t2 = StringVar(screen)
# tf2 = Entry(screen, textvariable=t2, width=30)
# tf2.grid(row=5, column=1, sticky="W", padx=10, pady=5, columnspan=2)

var = IntVar()
lb6 = Label(screen, text="Knowledge of the Teacher in the Subject").grid(
    row=6, sticky="E")
r1 = Radiobutton(text="Excellent ", variable=var, value=1,
                 command=select1, width=10).grid(row=6, column=1)
r2 = Radiobutton(text="Good ", variable=var, value=2,
                 command=select1, width=10).grid(row=6, column=2)
r3 = Radiobutton(text="Fair ", variable=var, value=3,
                 command=select1, width=10).grid(row=6, column=3)
r4 = Radiobutton(text="Poor ", variable=var, value=4,
                 command=select1, width=10).grid(row=6, column=4)
r5 = Radiobutton(text="Blank ", variable=var, value=5,
                 command=select1, width=10).grid(row=6, column=5)

var1 = IntVar()
lb7 = Label(
    screen, text="Clarity and Understandability of Teacher's explanations")
lb7.grid(row=7, sticky="E")
r6 = Radiobutton(text="Excellent ", variable=var1, value=6,
                 command=select2, width=10).grid(row=7, column=1)
r7 = Radiobutton(text="Good ", variable=var1, value=7,
                 command=select2, width=10).grid(row=7, column=2)
r8 = Radiobutton(text="Fair ", variable=var1, value=8,
                 command=select2, width=10).grid(row=7, column=3)
r9 = Radiobutton(text="Poor ", variable=var1, value=9,
                 command=select2, width=10).grid(row=7, column=4)
r10 = Radiobutton(text="Blank ", variable=var1, value=10,
                  command=select2, width=10).grid(row=7, column=5)

var2 = IntVar()
lb8 = Label(screen, text="Teacher's willingness to help").grid(
    row=8, sticky="E")
r11 = Radiobutton(text="Excellent ", variable=var2, value=11,
                  command=select3, width=10).grid(row=8, column=1)
r12 = Radiobutton(text="Good ", variable=var2, value=12,
                  command=select3, width=10).grid(row=8, column=2)
r13 = Radiobutton(text="Fair ", variable=var2, value=13,
                  command=select3, width=10).grid(row=8, column=3)
r14 = Radiobutton(text="Poor ", variable=var2, value=14,
                  command=select3, width=10).grid(row=8, column=4)
r15 = Radiobutton(text="Blank ", variable=var2, value=15,
                  command=select3, width=10).grid(row=8, column=5)

var3 = IntVar()
lb9 = Label(screen, text="Teacher's ability to organize lectures").grid(
    row=9, sticky="E")
r16 = Radiobutton(text="Excellent ", variable=var3, value=16,
                  command=select4, width=10).grid(row=9, column=1)
r17 = Radiobutton(text="Good ", variable=var3, value=17,
                  command=select4, width=10).grid(row=9, column=2)
r18 = Radiobutton(text="Fair ", variable=var3, value=18,
                  command=select4, width=10).grid(row=9, column=3)
r19 = Radiobutton(text="Poor ", variable=var3, value=19,
                  command=select4, width=10).grid(row=9, column=4)
r20 = Radiobutton(text="Blank ", variable=var3, value=20,
                  command=select4, width=10).grid(row=9, column=5)

var4 = IntVar()
lb10 = Label(screen, text="Overall teaching effectiveness of the Teacher").grid(
    row=10, sticky="E")
r21 = Radiobutton(text="Excellent ", variable=var4, value=21,
                  command=select5, width=10).grid(row=10, column=1)
r22 = Radiobutton(text="Good ", variable=var4, value=22,
                  command=select5, width=10).grid(row=10, column=2)
r23 = Radiobutton(text="Fair ", variable=var4, value=23,
                  command=select5, width=10).grid(row=10, column=3)
r24 = Radiobutton(text="Poor ", variable=var4, value=24,
                  command=select5, width=10).grid(row=10, column=4)
r25 = Radiobutton(text="Blank ", variable=var4, value=25,
                  command=select5, width=10).grid(row=10, column=5)

var5 = IntVar()
lb11 = Label(
    screen, text="Whether teacher provides videos,PPTs without proper explanation")
lb11.grid(row=11, sticky="E")
r26 = Radiobutton(text="Yes ", variable=var5, value=26,
                  command=select6, width=10).grid(row=11, column=1)
r27 = Radiobutton(text="No ", variable=var5, value=27,
                  command=select6, width=10).grid(row=11, column=2)

var6 = IntVar()
lb12 = Label(screen, text="Approximate % of classes not engaged bythe Teacher")
lb12.grid(row=12, sticky="E")
r28 = Radiobutton(text="< 10 %", variable=var6, value=28,
                  command=select7, width=10).grid(row=12, column=1)
r29 = Radiobutton(text="10-25 % ", variable=var6, value=29,
                  command=select7, width=10).grid(row=12, column=2)
r30 = Radiobutton(text="> 25 % ", variable=var6, value=30,
                  command=select7, width=10).grid(row=12, column=3)

var7 = IntVar()
mark8 = 0
lb13 = Label(screen, text="Speed of Presentation").grid(row=13, sticky="E")
r31 = Radiobutton(text="Just right", variable=var7, value=31,
                  command=select8, width=10).grid(row=13, column=1)
r32 = Radiobutton(text="Too fast ", variable=var7, value=32,
                  command=select8, width=10).grid(row=13, column=2)
r33 = Radiobutton(text="Too slow", variable=var7, value=33,
                  command=select8, width=10).grid(row=13, column=3)

var8 = IntVar()
lb14 = Label(screen, text="Does the teacher encourage questioning?").grid(
    row=14, sticky="E")
r34 = Radiobutton(text="Yes", variable=var8, value=34,
                  command=select9, width=10).grid(row=14, column=1)
r35 = Radiobutton(text="Sometimes ", variable=var8, value=35,
                  command=select9, width=10).grid(row=14, column=2)
r36 = Radiobutton(text="No ", variable=var8, value=36,
                  command=select9, width=10).grid(row=14, column=3)

var9 = IntVar()
lb15 = Label(screen, text="Behavior of the Teacher").grid(row=15, sticky="E")
r37 = Radiobutton(text="Pleasant ", variable=var9, value=37,
                  command=select10, width=10).grid(row=15, column=1)
r38 = Radiobutton(text="Indifferent ", variable=var9, value=38,
                  command=select10, width=10).grid(row=15, column=2)
r39 = Radiobutton(text="Unpleasant ", variable=var9, value=39,
                  command=select10, width=10).grid(row=15, column=3)

var10 = IntVar()
lb16 = Label(screen, text="Sincerity of the Teacher").grid(row=16, sticky="E")
r40 = Radiobutton(text="Sincere ", variable=var10, value=40,
                  command=select11, width=10).grid(row=16, column=1)
r41 = Radiobutton(text="Unsincere ", variable=var10, value=41,
                  command=select11, width=10).grid(row=16, column=2)
r42 = Radiobutton(text="unable to judge ", variable=var10,
                  value=42, command=select11, width=15).grid(row=16, column=3)

btn = Button(screen, text="SUBMIT", command=submit).grid(
    row=17, column=1, columnspan=2, sticky="NSEW", pady=5)

screen.mainloop()
