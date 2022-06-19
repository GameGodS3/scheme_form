from tkinter import *

main_window = Tk()
main_window.geometry("700x700")

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

idx = 1

feedback_scores = [IntVar(main_window, 0) for i in range(len(questions_dict))]

for question, data in questions_dict.items():
    Label(main_window, text=question).grid(row=idx-1, column=1)
    if idx < len(questions_dict):
        idx += 1
    for i, option in enumerate(data["options"]):
        Radiobutton(main_window, text=option,
                    variable=feedback_scores[idx-1], value=data["weights"][i]).grid(row=idx-1, column=10)


main_window.mainloop()
