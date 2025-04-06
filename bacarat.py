import tkinter as tk
import card_deck 
import random
import time
import requests
from io import BytesIO
from PIL import Image,ImageTk
from tkinter import messagebox as mbox
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
lab1=tk.Label(text=f'player({pnum})',font=('arial',14,'bold'),width=24,bg='blue')
lab1.grid(row=0,column=0,columnspan=3,sticky='we')
lab2=tk.Label(text=f'banker({bnum})',font=('arial',14,'bold'),width=24,bg='red')
lab2.grid(row=0,column=3,columnspan=3,sticky='we')
car1=tk.Label()
car1.grid(row=1,column=0)
car3=tk.Label()
car3.grid(row=1,column=1)
car5=tk.Label()
car5.grid(row=1,column=2)
car2=tk.Label()
car2.grid(row=1,column=3)
car4=tk.Label()
car4.grid(row=1,column=4)
car6=tk.Label()
car6.grid(row=1,column=5)
card_labels = {
    1: car1,
    2: car2,
    3: car3,
    4: car4,
    5: car5,
    6: car6,
}
def result():
    if pnum>bnum:mbox.showinfo('result','player win')
    elif pnum<bnum:mbox.showinfo('result','banker win')
    else:mbox.showinfo('result','tie')
def game():
    global pnum, bnum, step
    if step==5:
        if pnum==8 or pnum==9 or bnum==8 or bnum==9:
            update_labels()
            result()
            return
    if step > 6:
        result()
        return
    draw=random.sample(list(deck),1)[0]
    deck.remove(draw)
    rank_name = draw.face.name
    rank_map = {
        'ACE': 'A',
        'TWO': '2',
        'THREE': '3',
        'FOUR': '4',
        'FIVE': '5',
        'SIX': '6',
        'SEVEN': '7',
        'EIGHT': '8',
        'NINE': '9',
        'TEN': '0',
        'JACK': 'J',
        'QUEEN': 'Q',
        'KING': 'K',
    }
    rank = rank_map[rank_name]

    if rank == 'T': rank = '10'
    suit_map = {'HEARTS': 'H', 'DIAMONDS': 'D', 'CLUBS': 'C', 'SPADES': 'S'}
    suit=suit_map[draw.suit.name]
    img_url = f"https://deckofcardsapi.com/static/img/{rank}{suit}.png"
    # print(f'{rank}{suit}')
    response=requests.get(img_url)
    data=response.content
    img=Image.open(BytesIO(data))
    img=img.resize((90,135))
    tkimg=ImageTk.PhotoImage(img)
    card_labels[step].config(image=tkimg)
    card_labels[step].image=tkimg
    val=draw.face.value
    print()
    if val>9:val=0
    if step==1 or step==3:pnum=(pnum+val)%10
    elif step==2 or step==4:bnum=(bnum+val)%10
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