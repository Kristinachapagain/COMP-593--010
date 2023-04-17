import tkinter as tk
import requests
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import math
import os
import inspect

window = tk.Tk()
window.title('Pokemon Viewer')


frame_bg = ImageTk.PhotoImage(Image.open("honey.png"))
frame3 = tk.Frame(window, highlightbackground="gray", width=300, height=300)
label = tk.Label(frame3, image = frame_bg, width=300, height=300)
label.pack()
frame1 = tk.Frame(window)
btn_increase = tk.Button(master=frame1, text="Set as Desktop Image", state=tk.DISABLED)
combobox = ttk.Combobox(master=frame1)
icon = ImageTk.PhotoImage(Image.open("pokemon.ico"))
window.iconphoto(False, icon)

def main():
    frame3.pack(side=tk.TOP, padx=10, pady=10)

    #frame1 = tk.Frame(window)
    frame1.pack(side=tk.BOTTOM, padx=10, pady=10)
    #entry = tk.Entry(master=frame1)
    
    
    combobox.pack()
    btn_increase.pack()
    btn_increase.configure(command = change_bg)
    combobox.bind("<<ComboboxSelected>>", download_image)
    load_names()
    window.mainloop()

def load_names():
    try:
        url = "https://pokeapi.co/api/v2/item?limit=10000"
        pokemon_data = requests.get(url).json()["results"]
        combobox["values"] = [i["name"] for i in pokemon_data]
        return pokemon_data
    except Exception as e:
        return False
    return False

def download_image(event):
    pokemon_name = event.widget.get()
    btn_increase["state"] = tk.NORMAL
    #print(pokemon_name)
    return

def change_bg():
    name = f"{combobox.get()}.png"
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/{name}"
    path = os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename))
    image_data = requests.get(image_url).content
    image = open(os.path.join(path, name), "wb")
    image.write(image_data)
    image.close()
    new_frame_bg = ImageTk.PhotoImage(Image.open(name))
    label.configure(image = new_frame_bg)
    label.image = new_frame_bg
    return

if __name__ == '__main__':
   main()
