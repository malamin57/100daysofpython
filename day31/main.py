from tkinter import * 
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_Color = "#B1DDC6"


try:
    flash_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = flash_df.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text= "French")
    canvas.itemconfig(card_word, text=current_card['French'] )
    canvas.itemconfig(card_background, image=back_image)
    flip_timer = window.after(3000, func = flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itmeconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


canvas = Canvas(height= 600, width=800)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_Color)

flip_timer = window.after(3000, func=flip_card)

front_image = PhotoImage(file="card_front.png")
back_image = PhotoImage(file='card_back.png')
canvas.create_image(400, 263, image=front_image)
card_title =  canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(  400, 265, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_Color, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='wrong.png')
unknow_button = Button(image=cross_image, highlightthickness=0, command = next_card)
unknow_button.grid(row=1, column=0, columnspan=2)

check_image = PhotoImage(file='right.png')
known_button = Button(image=check_image, highlightthickness=0, command = next_card)
known_button.grid(row = 1, column = 1, columnspan=2)

next_card()






window.mainloop()