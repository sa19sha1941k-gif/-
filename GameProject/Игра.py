
import turtle

screen = turtle.Screen()
screen.bgcolor('green')
screen.setup(width=1000, height=1000)

screen.addshape("images/Player.gif")
tank = turtle.Turtle()
tank.shape("images/Player.gif")
tank.penup()

screen.addshape("images/bullet.gif")

tank.goto(0, -200)

# Список для хранения пуль
bullets = []


def move_left():
    x = tank.xcor()
    new_x = x - 15
    if new_x >= -500:
        tank.setx(new_x)


def move_right():
    x = tank.xcor()
    new_x = x + 15
    if new_x <= 500:
        tank.setx(new_x)


def shoot():
    # Создаём пулю
    bullet = turtle.Turtle()
    bullet.shape
    bullet.color("red")
    bullet.shapesize(0.5)
    bullet.penup()
    bullet.goto(tank.xcor(), tank.ycor() + 20)
    bullets.append(bullet)

    # Анимация полёта пули
    def move_bullet():
        bullet.sety(bullet.ycor() + 15)
        if bullet.ycor() > 500:
            bullet.hideturtle()
            bullets.remove(bullet)
        else:
            screen.ontimer(move_bullet, 20)

    move_bullet()


screen.listen()
screen.onkeypress(move_left, 'a')
screen.onkeypress(move_right, 'd')
screen.onkeypress(shoot, 'space')

turtle.done()