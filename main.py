import pandas as pd
from tkinter import *
import random


#loading data
try :
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError :
    data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn[:3])

RANDOM_DATA = {}
BACKGROUND_COLOR = "#B1DDC6"

def show_new_card() :
    global RANDOM_DATA , flip_timer
    if flip_timer :
        window.after_cancel(flip_timer)
    RANDOM_DATA = random.choice(to_learn)
    canvas.itemconfig(title , text = "French")
    canvas.itemconfig(word , text = RANDOM_DATA["French"])
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(RANDOM_DATA)
    df = pd.DataFrame(to_learn)
    df.to_csv("words_to_learn.csv")
    show_new_card()


def flip_card():
    canvas.itemconfig(canvas_image , image = back )
    canvas.itemconfig(title, text = "English")
    canvas.itemconfig(word,text=RANDOM_DATA["English"])

window = Tk()
window.title("Language Buddy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(height=526 , width=800 , bg=BACKGROUND_COLOR , highlightthickness= 0 )
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263,image = front)
title = canvas.create_text(400,100,text = "Language", font=("Ariel", 40, "italic"))
word = canvas.create_text(400,220,text="Word", font=("Ariel", 40, "italic"))
canvas.grid(row=0,column=0,columnspan=2)

#Buttons
wrong_img = PhotoImage(file = "images/wrong.png")
wrong_button = Button(image=wrong_img , command= show_new_card)
wrong_button.grid(row=1,column=0)

tick_img = PhotoImage(file = "images/right.png")
tick_button = Button(image = tick_img , command = is_known)
tick_button.grid(row=1,column=1)

show_new_card()
window.mainloop()