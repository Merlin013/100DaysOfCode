from tkinter import *
from PIL import Image, ImageTk
import requests

def get_quote():
    response = requests.get("https://animechan.vercel.app/api/random")
    # raise_for_status to check if the link is correct
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    anime = data["anime"]
    canvas.itemconfig(quote_text, text=f"{anime}:\n\n{quote}")


window = Tk()
window.title("Anime Quote...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Anime Quote Goes HERE", width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

deku = Image.open("deku.png").resize((100, 101))
deku_img = ImageTk.PhotoImage(deku)
deku_button = Button(image=deku_img, highlightthickness=0, command=get_quote)
deku_button.grid(row=1, column=0)



window.mainloop()