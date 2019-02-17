#-*- coding:utf-8 -*-
from tkinter import messagebox
import random
import tkinter as tk
from tkinter import*
from PIL import Image
from PIL import ImageTk
import time
window = tk.Tk()
window.title('Blackjack Game')
window.geometry('1000x600')
canvas = Canvas(window,width=600,height=600)
canvas.pack()
my_image = PhotoImage(file='/Users/edward/Downloads/blackjack.png')
canvas.create_image(0,0,anchor = NW,image = my_image)
l = tk.Label(window,text='Blackjack Game',bg='yellow',font=('Arial', 30),width=800, height=800).pack()
def start_game():
    window.destroy()# global window2
    global window2
    window2 = tk.Tk()
    window2.title('Blackjack Game')
    window2.geometry('700x400')
    menubar=tk.Menu(window2)
    # filemenu=tk.Menu(menubar,tearoff=0)
    # menubar.add_cascade(label='Game',menu=filemenu)
    # # filemenu.add_command(label='New Game',command=new_game)
    # # filemenu.add_separator()
    # # # filemenu.add_command(label='Exit',command=exit_game)
    tk.Label(window2, text='Banker',font=('Arial', 25)).place(x=50, y=100)
    tk.Label(window2, text='Player',font=('Arial', 25)).place(x=50, y=250)
    tk.Button(window2, text='Get Cards',command=get_cards).place(x=100, y=380)
    tk.Button(window2, text='Add',command=add_cards).place(x=200,y=380)
    tk.Button(window2, text='Finish',command=finish_cards).place(x=300, y=380)
    window2.mainloop()
# def new_game():
#     l_card_1.pack_forget()
    
def get_cards():
    card_1= random.randint(1, 10)
    tk.Label(window2, text=card_1, font=('Arial', 25)).place(x=150, y=100)
    global card_2
    card_2 = random.randint(1, 10)
    tk.Label(window2, text='X', font=('Arial', 25)).place(x=180, y=100)
    card_3 = random.randint(1, 10)
    tk.Label(window2, text=card_3, font=('Arial', 25)).place(x=150, y=250)
    card_4 = random.randint(1, 10)
    tk.Label(window2, text=card_4, font=('Arial', 25)).place(x=180, y=250)
    global a
    a= [card_1,card_2,card_3,card_4]
def add_cards():
    card_banker  = random.randint(1, 10)
    tk.Label(window2, text=card_banker, font=('Arial', 25)).place(x=210, y=100)
    card_player = random.randint(1, 10)
    tk.Label(window2, text=card_player, font=('Arial', 25)).place(x=210, y=250)
    global b
    b= [card_banker,card_player]
def finish_cards():
    banker_points= a[0]+ a[1] + b[0]
    player_points= a[2]+ a[3] + b[1]
    global result
    if banker_points> 21:   #庄家爆
         result='win'
    elif banker_points <21 and player_points<21:#都没爆
        if player_points < banker_points:#庄家比你大
             result='lose'
        elif player_points > banker_points:#庄家比你小
             result='win'
    elif banker_points < 21 and player_points> 21: # 庄家没爆，你爆
         result='lose'
    elif banker_points > 21 and player_points< 21:#庄家爆了，你没爆
         result='win'
    if result == 'win':
        tk.Label(window2, text=card_2, font=('Arial', 25)).place(x=180, y=100)
        tk.messagebox.showinfo(title='Blackjack Game', message='You Win!')
    elif result =='lose':
        tk.Label(window2, text=card_2, font=('Arial', 25)).place(x=180, y=100)
        tk.messagebox.showinfo(title='Blackjack Game', message='Sorry,You Lose')
startgame = tk.Button(window, text='Start Game!',command=start_game).place(x=450, y=450)
window.mainloop()
