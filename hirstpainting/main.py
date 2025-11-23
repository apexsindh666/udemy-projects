# # import colorgram
# # rgbc=[]
# # colors=colorgram.extract('himage.jpg',30)
# # for i in colors:
# #     r=i.rgb.r
# #     g=i.rgb.g
# #     b=i.rgb.b
# #     new_color=(r,g,b)
# #     rgbc.append(new_color)
# #
# # print(rgbc)


import turtle as t
import random

t.colormode(255)
tur = t.Turtle()
tur.speed("fastest")
tur.penup()
tur.hideturtle()

# Color palette
c_list = [
    (248, 238, 219), (223, 155, 90), (214, 240, 228), (240, 206, 90),
    (104, 170, 203), (36, 109, 149), (199, 227, 239), (113, 193, 161),
    (153, 61, 94), (208, 78, 109), (243, 215, 226), (25, 134, 101),
    (224, 81, 59), (205, 133, 155), (184, 59, 43), (177, 166, 36),
    (138, 219, 198), (39, 54, 113), (238, 161, 180), (105, 40, 73),
    (137, 215, 228), (239, 168, 157), (14, 93, 69), (60, 166, 132),
    (27, 47, 88), (53, 157, 186), (109, 116, 170), (72, 36, 65),
    (14, 69, 51), (180, 186, 218)
]

# Settings
dot_size = 20
spacing = 50
dots_per_row =5

# 🟡 Move turtle to start at bottom-left corner
tur.setheading(225)
tur.forward(300)   # Increased from half to full so it’s clearly visible
tur.setheading(0)

# 🟢 Draw 10x10 grid
for dot_count in range(1, dots_per_row ** 2 + 1):
    tur.dot(dot_size, random.choice(c_list))
    tur.forward(spacing)

    # Move up one row after every 10 dots
    if dot_count % dots_per_row == 0:
        tur.setheading(90)
        tur.forward(spacing)
        tur.setheading(180)
        tur.forward(spacing * dots_per_row)
        tur.setheading(0)

screen = t.Screen()
screen.exitonclick()
