#-*- coding:utf-8 -*-
from PIL import ImageTk,Image
from tkinter import messagebox
import random
import tkinter as tk
from tkinter import Canvas,PhotoImage,Label
from  cards import blackjack
#-----------------------------------------#
#构造初始窗口，增加图片，定义大小
window = tk.Tk()
window.title('Blackjack Game')
window.geometry('1000x600')
canvas = Canvas(window,width=800,height=600)
canvas.pack()
my_image = PhotoImage(file='/Users/edward/Downloads/blackjack.png')
canvas.create_image(400,200,image = my_image)
l = tk.Label(window,text='Blackjack Game',bg='yellow',font=('Arial', 30),width=800, height=800).pack()
#-----------------------------------------#
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
    # window2.mainloop()
def get_cards():
    global cards
    global cards_picked
    cards = ['a', 'a', 'a', 'a', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5',
                 '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9',
                 '9', '9', '9', '10', '10', '10', '10', 'j', 'j', 'j', 'j', 'q', 'q', 'q', 'q', 'k', 'k', 'k', 'k']
    number = 4
    cards_picked = []
    for n in range(number):
        ran_position = random.randint(1, len(cards))
        cards_picked.append(cards[ran_position])
        del cards[ran_position]
        print(cards_picked)
    for m in range(2):
      if cards_picked[0]=='a'or cards_picked[1]=='a':
        cards_picked[m]=='11'
    tk.Label(window2, text=cards_picked[0], font=('Arial', 25)).place(x=150, y=100)
    tk.Label(window2, text='X', font=('Arial', 25)).place(x=210, y=100)
    tk.Label(window2, text=cards_picked[2], font=('Arial', 25)).place(x=150, y=250)
    tk.Label(window2, text=cards_picked[3], font=('Arial', 25)).place(x=210, y=250)
    global a
    a= cards_picked
    if a[2] == 'a':
        option_1 = tk.Radiobutton(window2, text='1', value='1',command=a2_decision_make_1).place(x=150,y=300)
        option_2= tk.Radiobutton(window2, text='11', value='11', command=a2_decision_make_11).place(x=150, y=320)
    elif a[3]== 'a':
        option_1 = tk.Radiobutton(window2, text='1', value='1', command=a3_decision_make_1).place(x=210, y=300)
        option_2 = tk.Radiobutton(window2, text='11', value='11', command=a3_decision_make_11).place(x=210, y=320)

def add_cards(): #此处卡片为随机生成，没有从卡组里面扣除。改进！！
    card_banker  = random.randint(1, 10)
    tk.Label(window2, text=card_banker, font=('Arial', 25)).place(x=270, y=100)
    card_player = random.randint(1, 10)
    tk.Label(window2, text=card_player, font=('Arial', 25)).place(x=270, y=250)
    global b
    b= [card_banker,card_player]
def finish_cards():
    value = []
    for m in range(4):
        if cards_picked[m] == 'j' or cards_picked[m] == 'q' or cards_picked[m] == 'k':
            value_transfer = 10
            value.append(value_transfer)
        elif cards_picked[m] == '2' or cards_picked[m] == '3' or cards_picked[m] == '4' or cards_picked[m] == '5' or \
                cards_picked[m] == '6' or \
                cards_picked[m] == '7' or cards_picked[m] == '8' or cards_picked[m] == '9' or cards_picked[
            m] == '10'or cards_picked[m] == '1'or cards_picked[m] == '11':
            value_transfer = int(cards_picked[m])
            value.append(value_transfer)

    banker_points= value[0]+value[1] + b[0]
    player_points= value[2]+value[3]+ b[1]
    print(banker_points,player_points)
    global result
    if banker_points> 21:   #庄家爆
         result='win'
    elif banker_points <21 and player_points<=21:#都没爆
        if player_points < banker_points:#庄家比你大
             result='lose'
        elif player_points > banker_points:#庄家比你小
             result='win'
    elif banker_points < 21 and player_points> 21: # 庄家没爆，你爆
         result='lose'
    elif banker_points > 21 and player_points<= 21:#庄家爆了，你没爆
         result='win'
    elif banker_points==player_points:#平手
         result='draw'
    if result == 'win':
        tk.Label(window2, text=cards_picked[1], font=('Arial', 25)).place(x=210, y=100)
        tk.messagebox.showinfo(title='Blackjack Game', message='You Win!')
        # canvas_3 = Canvas(window2, width=200, height=200)
        # canvas_3.pack()
        # my_image_2 = PhotoImage(file='/Users/edward/Downloads/dusheng.png')
        # canvas_3.create_image(0,100, anchor=NW, image=my_image_2)
        load = Image.open('/Users/edward/Downloads/dusheng.png')  # 我图片放桌面上
        render = ImageTk.PhotoImage(load)
        img = Label(window2, image=render)
        img.image = render
        img.place(x=400, y=0)
        window2.mainloop()
    elif result =='lose':
        tk.Label(window2, text=cards_picked[1], font=('Arial', 25)).place(x=210, y=100)
        tk.messagebox.showinfo(title='Blackjack Game', message='Sorry,You Lose')
    elif result=='draw':
        tk.Label(window2, text=cards_picked[1], font=('Arial', 25)).place(x=210, y=100)
        tk.messagebox.showinfo(title='Blackjack Game', message='Draw,take back you bets!')
def a2_decision_make_1():
    a[2]='1'
def a2_decision_make_11():
    a[2]='11'
def a3_decision_make_1():
    a[3]='1'
def a3_decision_make_11():
    a[3]='11'

startgame = tk.Button(window, text='Start Game!',command=start_game).place(x=450, y=450)
window.mainloop()

# 改进方向：
# 1.实现new的menu bar
# 2.实现荷官策略，实现玩家不愿意加牌的选项##
