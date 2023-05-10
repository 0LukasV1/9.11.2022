
import tkinter as tk
import random as rd

heightcan = 300
widthcan = 300
win = tk.Tk()

Canvas = tk.Canvas(win, height=heightcan, width=widthcan, bg='black')
Canvas.pack()

ball = Canvas.create_oval(heightcan / 2, widthcan / 2, (heightcan / 2) - 20, (widthcan / 2) - 20, fill='lime')
vec_x = 3  # input('x:')
vec_y = 3  # input('y:')
print(Canvas.coords(ball)[0])
col = ['red', 'lime', 'cyan', 'blue', 'orange', 'turquoise', 'yellow', 'purple']


def kiki():
    global vec_x
    global vec_y

    Canvas.move(ball, vec_x, vec_y)
    if (Canvas.coords(ball)[2]) > widthcan:
        vec_x *= (-1)
        Canvas.itemconfig(ball, fill=rd.choice(col))
    if (Canvas.coords(ball)[0]) < 0:
        vec_x *= (-1)
        Canvas.itemconfig(ball, fill=rd.choice(col))
    if (Canvas.coords(ball)[3]) > heightcan:
        vec_y *= (-1)
        Canvas.itemconfig(ball, fill=rd.choice(col))
    if (Canvas.coords(ball)[1]) < 0:
        vec_y *= (-1)
        Canvas.itemconfig(ball, fill=rd.choice(col))
    Canvas.after(10, kiki)


kiki()

win.mainloop()
# DU faker, ktory posunie priu dotyku so stenou urcitu suradnicu aby nechodila len
#

