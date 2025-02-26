# program4.8
import turtle
t=turtle.Pen()
turtle.bgcolor('black')

name_str=str('Leo,Lily,Tom,Alex,Max'.split(','))
name_list=eval(name_str)
colors='yellow,green,white,brown,gray'.split(',')

for x in range(150):
    t.pencolor(colors[x%len(name_list)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(name_list[x%len(name_list)],font=('Arial',int((x+4)/4)))
    t.left(360/len(name_list)+3)
