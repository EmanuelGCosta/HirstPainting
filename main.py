# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 20)
#
# for color in colors:
#
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)
from turtle import Turtle, Screen
from random import choice

color_list = [(226, 231, 236), (58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191)]
tim = Turtle()
tim.penup()
screen = Screen()
screen.colormode(255)
tim.goto(-200, -200)


def desenhar():
    for _ in range(10):
        random_color = choice(color_list)
        tim.pencolor(random_color)
        tim.dot(20)
        tim.forward(50)


for _ in range(10):

    desenhar()
    tim.left(90)
    tim.forward(50)
    tim.goto(-200, tim.ycor())
    tim.right(90)

screen.exitonclick()

