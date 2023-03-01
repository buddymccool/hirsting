import colorgram
import turtle as t
import random

t.colormode(255)

# colors = colorgram.extract('hirstsass.png', 30)
# hirst_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     hirst_colors.append(new_color)
#
# print(hirst_colors)

color_list2 = [
    (215, 225, 221),
    (225, 218, 211),
    (194, 211, 219),
    (178, 161, 141),
    (44, 37, 30),
    (109, 97, 73),
    (192, 146, 160),
    (155, 178, 188),
    (229, 211, 217),
    (156, 177, 165),
    (135, 78, 93),
    (182, 96, 122),
    (217, 176, 188),
    (140, 148, 71),
    (32, 52, 35),
    (82, 103, 83),
    (52, 32, 37),
    (207, 201, 146),
    (173, 199, 204),
    (174, 202, 193),
    (77, 94, 120),
    (29, 35, 51),
    (210, 183, 179),
    (72, 73, 39),
    (103, 44, 54),
    (173, 109, 94),
    (43, 78, 48),
    (183, 188, 208),
    (111, 146, 98),
    (90, 51, 46)
]

color_list = [
    (212, 203, 210),
    (134, 81, 73),
    (182, 162, 171),
    (180, 129, 119),
    (169, 108, 98),
    (67, 39, 36),
    (55, 33, 36),
    (89, 51, 48),
    (203, 184, 194),
    (124, 80, 83),
    (217, 206, 204),
    (212, 210, 216),
    (88, 50, 53),
    (153, 111, 115),
    (205, 184, 183)
]

turt = t.Turtle()
turt.ht()
turt.pu()
turt.setposition(-250, -250)
turt.pensize(5)
turt.speed("fastest")

for _ in range(100):
    random_color = random.choice(color_list2)
    turt.dot(25, random_color)
    turt.fd(50)
    if turt.xcor() >= 250:
        turt.setx(-250)
        turt.sety(turt.ycor() + 50)

### ------- playing with other algos below -------- ###

# d_size = 20
# numby = 2
# for _ in range(100):
#     random_color = random.choice(color_list2)
#     turt.dot(d_size, random_color)
#     turt.fd(50+numby)
#     if turt.xcor() >= 250:
#         turt.setx(-250)
#         turt.sety(turt.ycor() + 50)
#     if d_size >= 30:
#         numby = numby * -1
#     elif d_size <= 10:
#         numby = numby * -1
#     d_size += numby

# for _ in range(100):
#     random_color = random.choice(color_list2)
#     rand_int = random.randint(30, 50)
#     turt.dot(rand_int, random_color)
#     turt.fd(rand_int)
#     if turt.xcor() >= 250:
#         turt.setx(-250)
#         turt.sety(turt.ycor() + rand_int)

# value = 2
# for _ in range(100):
#     rand_int = random.randint(-10, 10)
#     rand_int2 = random.randint(-10, 10)
#     # rand_int3 = random.randint(1, 5)
#     dot_size = value
#     random_color = random.choice(color_list2)
#     turt.dot(dot_size, random_color)
#     turt.setx(rand_int + (value*-1))
#     turt.sety(rand_int2 + (value*-1))
#     value += 2

screen = t.Screen()
screen.exitonclick()
