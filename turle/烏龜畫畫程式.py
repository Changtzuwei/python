import turtle
#把 turtle的套件匯入
pen = turtle.Turtle()
#建立一支筆
turtle.setup(800,800)
#建立視窗大小
pen.penup()
#把筆拿起來
#pen.goto(-400,400)
pen.pendown()
#把筆放下去,開始畫
pen.color('yellow')
#畫筆的顏色
pen.begin_fill()
#開始做填充
pen.fillcolor(0,0,0)
#填充成黑色
for i in range(4):
    pen.forward(100)
#forward前進
    pen.right(90)
#right向右
pen.end_fill()
#結束填滿
turtle.done()
#完成畫圖把筆收起來
turtle.exitonclick()
#可以點擊結束