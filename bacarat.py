import tkinter as tk
import card_deck 
import random
window=tk.Tk()
window.title('bacarat game')
window.geometry('600x600')
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
deck=card_deck.Deck()
deck.shuffle()
draw=random.sample(list(deck),1)[0]
val=draw.face.value
if val>10:val=10
lab1=tk.Label(text=f'player({val})')
lab1.grid(row=0,column=0)
window.mainloop()