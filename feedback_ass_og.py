from tkinter import *

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

line_count = 0
question_idx = 0

feedback_scores = [IntVar(main_window, 0) for i in range(len(questions_dict))]

for question, data in questions_dict.items():
    question_label = Label(main_window, text=question, anchor="w")
    question_label.grid(row=line_count, column=0)
    Label(main_window, text="").grid(row=line_count, column=1)
    line_count += 1

    option_col_idx = 0
    for i, option in enumerate(data["options"]):
        Radiobutton(main_window, text=option,
                    variable=feedback_scores[question_idx], value=data["weights"][i]).grid(row=line_count, column=option_col_idx)
        option_col_idx += 1

    line_count += 1
    question_idx += 1


# Label(main_window, text="hello world").grid(row=0, column=0)
# Radiobutton(main_window, text="0",
#             variable=feedback_scores[0]).grid(row=1, column=0)
# Radiobutton(main_window, text="1",
#             variable=feedback_scores[1]).grid(row=1, column=1)
# Radiobutton(main_window, text="2",
#             variable=feedback_scores[2]).grid(row=1, column=2)
# Label(main_window, text="hello world2").grid(row=2, column=0)


main_window.mainloop()
