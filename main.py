import turtle
import time

screen = turtle.Screen()
b = turtle.Turtle()
t = turtle.Turtle()
writer = turtle.Turtle()

b.hideturtle()
writer.hideturtle()
t.hideturtle()

b.width(5)
b.speed(2)
t.speed(2)

# cursor coordinates variables, the number of x and o, the list of places on which stands either x (1) or o (0) and the
# points of the first and second player
x_click = 0
y_click = 0
num_x = 0
num_o = 0
list_plc = ['', '', '', '', '', '', '', '', '']
vct = False
score_1 = int()
score_2 = int()


# function for drawing borders
def draw_board():
    screen.tracer(0)
    b.penup()
    b.goto(-300, -300)
    b.pendown()
    b.left(90)
    # drawing outer borders
    for i in range(4):
        b.forward(600)
        b.right(90)
    b.right(90)
    # drawing inner borders
    b.penup()
    b.goto(-300, 100)
    b.pendown()
    b.forward(600)
    b.penup()
    b.goto(-300, -100)
    b.pendown()
    b.forward(600)
    b.penup()
    b.goto(-100, -300)
    b.left(90)
    b.pendown()
    b.forward(600)
    b.penup()
    b.goto(100, -300)
    b.pendown()
    b.forward(600)
    screen.update()


draw_board()


# function updates the board
def update_board():
    global list_plc
    t.clear()
    list_plc = ['', '', '', '', '', '', '', '', '']


# function that shows which player wins or draws
def victory_display(text, player):
    global vct
    global score_1
    global score_2
    writer.clear()
    writer.write(text, font=('Arial', 32, 'normal'))
    t.penup()
    time.sleep(2)
    writer.clear()
    vct = True
    if player == 1:
        score_1 += 1
    elif player == 2:
        score_2 += 1
    update_board()


# the function of determining the victory of either the first player or the second, or a draw
def win():
    global vct
    global score_1
    global score_2
    global list_plc
    writer.penup()
    writer.goto(-300, 310)
    writer.pendown()
    writer.write(f'{score_1}:{score_2}', font=('Arial', 32, 'normal'))
    for i in range(0, len(list_plc), 3):
        if list_plc[i - 3] == 1 and list_plc[i - 2] == 1 and list_plc[i - 1] == 1:
            victory_display('The First Player Won! (X)', 1)
        elif list_plc[i - 3] == 0 and list_plc[i - 2] == 0 and list_plc[i - 1] == 0:
            victory_display('The Second Player Won! (X)', 2)
    for i1 in range(0, 3):
        if list_plc[i1] == 1 and list_plc[i1 + 3] == 1 and list_plc[i1 + 6] == 1:
            victory_display('The First Player Won! (X)', 1)
        elif list_plc[i1] == 0 and list_plc[i1 + 3] == 0 and list_plc[i1 + 6] == 0:
            victory_display('The Second Player Won! (X)', 2)
    if list_plc[0] == 1 and list_plc[4] == 1 and list_plc[8] == 1:
        victory_display('The First Player Won! (X)', 1)
    if list_plc[0] == 0 and list_plc[4] == 0 and list_plc[8] == 0:
        victory_display('The Second Player Won! (X)', 2)
    if list_plc[2] == 1 and list_plc[4] == 1 and list_plc[6] == 1:
        victory_display('The First Player Won! (X)', 1)
    if list_plc[2] == 0 and list_plc[4] == 0 and list_plc[6] == 0:
        victory_display('The Second Player Won! (X)', 2)
    elif '' not in list_plc and not vct:
        writer.clear()
        writer.write('Draw!', font=('Arial', 32, 'normal'))
        time.sleep(2)
        writer.clear()
        update_board()
    vct = False


# function to put either x or o
def x_o(index):
    global num_x
    global num_o
    if num_x == 0:
        if list_plc[index] == '':
            t.write('X', font=('Arial', 90, 'normal'))
            num_x += 1
            list_plc[index] = 1
    elif num_o < num_x:
        if list_plc[index] == '':
            t.write('O', font=('Arial', 90, 'normal'))
            num_o += 1
            list_plc[index] = 0
    else:
        if list_plc[index] == '':
            t.write('X', font=('Arial', 90, 'normal'))
            num_x += 1
            list_plc[index] = 1


# playing with tic-tac-toe and determining the coordinates of the cursor.
def tic_tac_toe(x, y):
    global x_click
    global y_click
    global list_plc
    x_click = int(x // 1)
    y_click = int(y // 1)
    # writing in specific areas x or o
    if -300 <= x_click <= -100 and -300 <= y_click <= -100:
        t.penup()
        t.goto(-240, -270)
        t.pendown()
        x_o(6)
    elif -300 <= x_click <= -100 <= y_click <= 100:
        t.penup()
        t.goto(-240, -70)
        t.pendown()
        x_o(3)
    elif -300 <= x_click <= -100 and 100 <= y_click <= 300:
        t.penup()
        t.goto(-240, 130)
        t.pendown()
        x_o(0)
    elif 100 >= x_click >= -100 >= y_click >= -300:
        t.penup()
        t.goto(-40, -270)
        t.pendown()
        x_o(7)
    elif 100 >= x_click >= -100 <= y_click <= 100:
        t.penup()
        t.goto(-40, -70)
        t.pendown()
        x_o(4)
    elif 100 >= x_click >= -100 <= y_click <= 300:
        t.penup()
        t.goto(-40, 130)
        t.pendown()
        x_o(1)
    elif 100 <= x_click <= 300 and -100 >= y_click >= -300:
        t.penup()
        t.goto(160, -270)
        t.pendown()
        x_o(8)
    elif 100 <= x_click <= 300 and 100 >= y_click >= -100:
        t.penup()
        t.goto(160, -70)
        t.pendown()
        x_o(5)
    elif 100 <= x_click <= 300 and 300 >= y_click >= 100:
        t.penup()
        t.goto(160, 130)
        t.pendown()
        x_o(2)
    win()


turtle.onscreenclick(tic_tac_toe)
screen.mainloop()
