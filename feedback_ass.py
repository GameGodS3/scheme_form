"""
Developed by:

Ajay Krishna KV         Roll No. 07
Nandakishor M Pai       Roll No. 45
Paurnami Pradeep        Roll No. 50
Sudev Suresh Sreedevi   Roll No. 60

"""

from tkinter import *
from tkinter import messagebox


main_window = Tk()
questions_dict = {
    "knowledge of the teacher in the subject": {
        "options": ["excellent", "good", "fair", "poor", "i don't know", "rather not answer"],
        "weights": [4, 3, 2, 1, 0, -1]
    },
    "clarity and understandability of teacher's explanations": {
        "options": ["excellent", "good", "fair", "poor", "i don't know", "rather not answer"],
        "weights": [4, 3, 2, 1, 0, -1]
    },
    "teacher's willingness to help": {
        "options": ["excellent", "good", "fair", "poor", "i don't know", "rather not answer"],
        "weights": [4, 3, 2, 1, 0, -1]
    },
    "teacher's ability to organize lectures": {
        "options": ["excellent", "good", "fair", "poor", "i don't know", "rather not answer"],
        "weights": [4, 3, 2, 1, 0, -1]
    },
    "overall teaching effectiveness of the teacher": {
        "options": ["excellent", "good", "fair", "poor", "i don't know", "rather not answer"],
        "weights": [4, 3, 2, 1, 0, -1]
    },
    "whether the teacher provides videos, PPTs or notes without proper explanation": {
        "options": ["yes", "no", "i don't know"],
        "weights": [-1, 1, 0]
    },
    "approximate percentage of classes not engaged by the teacher": {
        "options": ["less than 10%", "10% to 25%", "more than 25%"],
        "weights": [3, 2, 1]
    },
    "speed of presentation": {
        "options": ["just right", "too fast", "too slow"],
        "weights": [3, -1, -1]
    },
    "does the teacher encourage questioning?": {
        "options": ["yes", "sometimes", "no"],
        "weights": [1, 0, -1]
    },
    "behaviour of the teacher": {
        "options": ["pleasant", "indifferent", "unpleasant"],
        "weights": [1, 0, -1]
    },
    "sincerity of the teacher": {
        "options": ["sincere", "insincere", "unable to judge"],
        "weights": [1, -1, 0]
    }
}
feedback_scores = [IntVar(main_window, 0) for i in range(len(questions_dict))]


def submit():
    if(tf1.get() == ""):
        messagebox.showinfo("ERROR", "Please Enter Name!")
    else:
        if(tf2.get() == ""):
            messagebox.showinfo("ERROR", "Please Enter Attendance!")
        else:
            if(float(tf2.get()) < 65.0):
                messagebox.showinfo("ERROR", "Attendance too low!")
            else:
                global mark8
                global total
                if(mark8 == 0):
                    messagebox.showinfo(
                        "RESULT", "The score is:"+str(round(total, 2))+"/200\nspeed of presentaion is just right")
                elif mark8 > 0:
                    messagebox.showinfo(
                        "RESULT", "The score is:"+str(round(total, 2))+"/200\nspeed of presentaion should be reduced")
                else:
                    messagebox.showinfo("RESULT", "The score is:"+str(
                        round(total, 2))+"/200\nspeed of presentaion should be increased")


def select1():
    if(feedback_scores[0].get() == 1):
        mark1 = 20
    elif feedback_scores[0].get() == 2:
        mark1 = 15
    elif feedback_scores[0].get() == 3:
        mark1 = 10
    elif feedback_scores[0].get() == 4:
        mark1 = 5
    else:
        mark1 = 0
    global total
    total = total+mark1


def select2():
    if(feedback_scores[1].get() == 6):
        mark2 = 20
    elif feedback_scores[1].get() == 7:
        mark2 = 15
    elif feedback_scores[1].get() == 8:
        mark2 = 10
    elif feedback_scores[1].get() == 9:
        mark2 = 5
    else:
        mark2 = 0
    global total
    total = total+mark2


def select3():
    if(feedback_scores[2].get() == 11):
        mark3 = 20
    elif feedback_scores[2].get() == 12:
        mark3 = 15
    elif feedback_scores[2].get() == 13:
        mark3 = 10
    elif feedback_scores[2].get() == 14:
        mark3 = 5
    else:
        mark3 = 0
    global total
    total = total+mark3


def select4():
    if(feedback_scores[3].get() == 16):
        mark4 = 20
    elif feedback_scores[3].get() == 17:
        mark4 = 15
    elif feedback_scores[3].get() == 18:
        mark4 = 10
    elif feedback_scores[3].get() == 19:
        mark4 = 5
    else:
        mark4 = 0
    global total
    total = total+mark4


def select5():
    if(feedback_scores[4].get() == 21):
        mark5 = 20
    elif feedback_scores[4].get() == 22:
        mark5 = 15
    elif feedback_scores[4].get() == 23:
        mark5 = 10
    elif feedback_scores[4].get() == 24:
        mark5 = 5
    else:
        mark5 = 0
    global total
    total = total+mark5


def select6():
    if(feedback_scores[5].get() == 26):
        mark6 = 20
    else:
        mark6 = 0
    global total
    total = total+mark6


def select7():
    st_att = float(tf2.get())
    if(feedback_scores[6].get() == 28):
        mark7 = (st_att/100.0)*20
    elif(feedback_scores[6].get() == 29):
        mark7 = (st_att/82.5)*12.5
    else:
        mark7 = (st_att/70.0)*5
    global total
    total = total+mark7


def select8():
    global mark8
    if(feedback_scores[7].get() == 31):
        mark8 += 0
    elif(feedback_scores[7].get() == 32):
        mark8 += 1
    else:
        mark8 -= 1


def select9():
    if(feedback_scores[8].get() == 34):
        mark9 = 20
    elif(feedback_scores[8].get() == 35):
        mark9 = 10
    else:
        mark9 = 0
    global total
    total = total+mark9


def select10():
    if(feedback_scores[9].get() == 37):
        mark10 = 20
    elif(feedback_scores[9].get() == 38):
        mark10 = 10
    else:
        mark10 = 0
    global total
    total = total+mark10


def select11():
    if(feedback_scores[10].get() == 40):
        mark11 = 20
    elif(feedback_scores[10].get() == 41):
        mark11 = 0
    else:
        mark11 = 10
    global total
    total = total+mark11


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

main_window.title("Faculty Evaluation")

lb1 = Label(main_window, text="COLLEGE OF ENGINEERING TRIVANDRUM").grid(
    row=1, columnspan=6, sticky="NSEW", pady=5)

lb2 = Label(main_window, text="STUDENTS' EVALUATION OF TEACHERS").grid(
    row=2, columnspan=6, sticky="NSEW", pady=5)

lb3 = Label(main_window, text="CST201:DATA STRUCTURES").grid(
    row=3, columnspan=6, sticky="NSEW", pady=5)

lb4 = Label(main_window, text="NAME OF STUDENT:").grid(row=4, sticky="NSEW")
t1 = StringVar(main_window)
tf1 = Entry(main_window, textvariable=t1, width=30)
tf1.grid(row=4, column=1, sticky="W", padx=10, pady=5, columnspan=2)


lb5 = Label(main_window, text="ATTENDANCE:").grid(row=5, sticky="NSEW")
t2 = StringVar(main_window)
tf2 = Entry(main_window, textvariable=t2, width=30)
tf2.grid(row=5, column=1, sticky="W", padx=10, pady=5, columnspan=2)


line_count = 6
question_idx = 0
default_val = 0

for question, data in questions_dict.items():
    question_label = Label(main_window, text=question.capitalize())
    question_label.grid(row=line_count, column=0, sticky="E")
    Label(main_window, text="").grid(row=line_count, column=1)
    line_count += 1

    option_col_idx = 1
    for i, option in enumerate(data["options"]):
        Radiobutton(main_window, text=option.capitalize(),
                    variable=feedback_scores[question_idx], value=default_val).grid(row=line_count, column=option_col_idx)
        option_col_idx += 1
        default_val += 1

    line_count += 1
    question_idx += 1

btn = Button(main_window, text="SUBMIT", command=submit).grid(
    row=line_count, column=1, columnspan=2, sticky="NSEW", pady=5)

main_window.mainloop()
