import tkinter as tk
import card_deck 
import random
import time
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
pnum=0
bnum=0
step=1
lab1=tk.Label(text=f'player({pnum})')
lab1.grid(row=0,column=0,columnspan=3)
lab2=tk.Label(text=f'banker({bnum})')
lab2.grid(row=0,column=3,columnspan=3)
def game():
    global pnum, bnum, step
    if step > 6:return
    draw=random.sample(list(deck),1)[0]
    deck.remove(draw)
    val=draw.face.value
    print(draw.suit.name)
    if val>9:val=0
    if step==1 or step==3:pnum=(pnum+val)%10
    elif step==2 or step==4:bnum=(bnum+val)%10
    if step==5:
        if pnum==8 or pnum==9 or bnum==8 or bnum==9:
            update_labels()
            return
    if step==5 and pnum<6:pnum=(pnum+val)%10
    if step==6:
        if pnum<6:
            if bnum <= 2:
                bnum=(bnum+val)%10
            elif bnum == 3 and val != 8:
                bnum=(bnum+val)%10
            elif bnum == 4 and val in [2, 3, 4, 5, 6, 7]:
                bnum=(bnum+val)%10
            elif bnum == 5 and val in [4, 5, 6, 7]:
                bnum=(bnum+val)%10
            elif bnum == 6 and val in [6, 7]:
                bnum=(bnum+val)%10
        elif bnum<=5:bnum=(bnum+val)%10
    update_labels()
    step+=1
    window.after(1000,game)
def update_labels():
    lab1.config(text=f'player({pnum})')
    lab2.config(text=f'banker({bnum})')
window.after(1000,game)
window.mainloop()