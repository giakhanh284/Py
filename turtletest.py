import turtle as t

# Vẽ hình chữ nhật (thân nhà)
t.pensize(3)
t.pencolor('black')
t.fillcolor('orange')
t.begin_fill()

for _ in range(4):
    t.forward(150)
    t.right(90)

t.end_fill()

# Vẽ mái nhà
t.fillcolor('red')
t.begin_fill()
t.left(45)
t.forward(106)
t.right(90)
t.forward(106)

t.end_fill()

# Vẽ cửa
t.penup()
t.goto(70,-150)
t.pendown()
t.right(135)
t.pencolor('brown')
t.fillcolor('brown')
t.begin_fill()

for _ in range(2):
    t.forward(40)
    t.right(90)
    t.forward(70)
    t.right(90)

t.end_fill()

# Vẽ cửa sổ 1
t.penup()
t.goto(120, -100)
t.pendown()
t.pencolor('blue')
t.fillcolor('blue')
t.begin_fill()

for _ in range(4):
    t.forward(30)
    t.right(90)

t.end_fill()

# Vẽ cửa sổ 2
t.penup()
t.goto(120, -60)
t.pendown()
t.pencolor('blue')
t.fillcolor('blue')
t.begin_fill()

for _ in range(4):
    t.forward(30)
    t.right(90)

t.end_fill()

# Đưa bút vẽ về điểm ban đầu
t.penup()
t.goto(0, 0)
t.pendown()

# Ẩn bút vẽ
t.hideturtle()

# Hiển thị hình vẽ
t.done()

