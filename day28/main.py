
from tkinter import * 
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

def start_time():
    count_down(5* 60)

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)



def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg = GREEN, bg = YELLOW , font=(FONT_NAME, 50))
title_label.grid(column=2, row=0)

canvas = Canvas(width = 200, height = 200, bg = YELLOW, highlightthickness=0) 
tomato_pic = PhotoImage(file='/Users/malamin/100days/100days/bin/day28/tomato.png')

canvas.create_image(100,90, image=tomato_pic)
timer_text = canvas.create_text(100,110, text="00:00", fill='white',font =(FONT_NAME, 35, "bold"))
canvas.grid(column= 2, row= 2)

button_1 = Button(text="Start ", bg= PINK, command=start_time )
button_1.grid(column = 1, row = 3)

button_2 = Button(text="Reset ")
button_2.grid(column = 3, row = 3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)





window.mainloop()
