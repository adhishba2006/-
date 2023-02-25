from tkinter import messagebox as mb
import tkinter as tk
import random

r = tk.Tk()
r.geometry('700x550')
r.title('Игра в кости')
c = tk.Canvas(r, width=700, height=550)
c.pack()

def roll_dice():
    global bttn_clicks
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d = {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}
    die1 = random.choice(dice)
    die2 = random.choice(dice)
    ldice.configure(text=f'{die1} {die2}')
    c.create_window(350, 250, window=ldice)
    res = d[die1]+d[die2]
    label2.configure(text="У тебя "+str(res))
    bttn_clicks +=1
    label1['text'] = "Кубик брошен: " + str(bttn_clicks) + " раз"
    if (bttn_clicks == 10 and res !=10):
        rollbutton.configure(state='disabled')
        mb.showerror("Игра окончена", "Попробуй снова")
    elif (res == 10):
        rollbutton.configure(state='disabled')
        mb.showinfo("Победитель", "Ты выиграл!")

def restart():
    global bttn_clicks
    bttn_clicks=0
    label1.configure(text="")
    label2.configure(text="Ещё не кинуто")
    rollbutton.configure(state='normal')
    
ldice = tk.Label(r, text='', font=('Times', 120),fg='green')
rollbutton = tk.Button(r, text='Кинуть кости', font=('times',20,"bold"),state="disabled",background="brown",foreground='yellow', height=1,width=15, command=roll_dice)
c.create_window(350,120, window=rollbutton)
button1 = tk.Button(r, text='Новая игра', font=('times', 20, "bold"),background="green",foreground='red',height=1, width=15, command=restart)
c.create_window(350, 50, window=button1)
label1 = tk.Label(r, text='', font=('Times',20,'bold'),fg='brown')
c.create_window(180, 410, window=label1)
label2 = tk.Label(r, text='Ещё не кинуто', font=('Times',20,"bold"),bg='purple',fg='yellow',width=12)
c.create_window(480,410, window=label2)

r.mainloop()
                    
                    


