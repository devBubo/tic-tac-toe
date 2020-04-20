from tkinter import *
root = Tk()
canvas = Canvas()
canvas.pack()
root.title("Tic Tac Toe")
win_width=600
win_height=600
canvas.config(width=win_width,height=win_height,bg='black')
for i in range(3):
    canvas.create_line(0,i/3*win_height,win_width,i/3*win_height,fill='white')
    canvas.create_line(i / 3 * win_width,0, i / 3 * win_width, win_height, fill='white')




canvas.mainloop()