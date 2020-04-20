from tkinter import *
root = Tk()
canvas = Canvas()
canvas.pack()
root.title("Tic Tac Toe")
win_width=600
win_height=600
bgcolor='black'
normalcolor='white'
circlesize=10
canvas.config(width=win_width,height=win_height,bg=bgcolor)
for i in range(3):
    canvas.create_line(0,i/3*win_height,win_width,i/3*win_height,fill=normalcolor)
    canvas.create_line(i / 3 * win_width,0, i / 3 * win_width, win_height, fill=normalcolor)
def coordinates(eventorigin):
    global coordinate_x
    global coordinate_y
    coordinate_x=eventorigin.x
    coordinate_y=eventorigin.y
canvas.bind('<Button 1>',coordinates)
coordinate_x=NO
coordinate_y=NO
while True:
    for i in range(3):
        if (coordinate_x>win_width*i/3 and coordinate_x<win_width*(i+1)/3) and coordinate_y>win_height*0/3 and coordinate_y<win_height*1/3:
            canvas.create_oval(win_width*i/3,win_height*0/3,win_width*(i+1)/3,win_height*1/3,fill=normalcolor)
            canvas.create_oval(win_width *(i)/ 3+circlesize, win_height *0/ 3+circlesize, win_width * (i+1) / 3-circlesize, win_height * 1 / 3-circlesize, fill=bgcolor)
    for i in range(3):
        if (coordinate_x>win_width*i/3 and coordinate_x<win_width*(i+1)/3) and coordinate_y>win_height/3 and coordinate_y<win_height*2/3:
            canvas.create_oval(win_width*i/3,win_height/3,win_width*(i+1)/3,win_height*2/3,fill=normalcolor)
            canvas.create_oval(win_width *(i)/ 3+circlesize, win_height / 3+circlesize, win_width * (i+1) / 3-circlesize, win_height * 2 / 3-circlesize, fill=bgcolor)
    for i in range(3):
        if (coordinate_x>win_width*i/3 and coordinate_x<win_width*(i+1)/3) and coordinate_y>win_height*2/3 and coordinate_y<win_height*3/3:
            canvas.create_oval(win_width*i/3,win_height*2/3,win_width*(i+1)/3,win_height*3/3,fill=normalcolor)
            canvas.create_oval(win_width *(i)/ 3+circlesize, win_height*2 / 3+circlesize, win_width * (i+1) / 3-circlesize, win_height * 3/ 3-circlesize, fill=bgcolor)
    canvas.update()
