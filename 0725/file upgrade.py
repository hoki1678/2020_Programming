import turtle as t

robot_fn='vaccum_icon.gif'
rx = []
ry = []
move_cnt = 0

arx = [-256,-212,-168,-124,-80,-36,8,52,96,140,184,228,300]
ary = [-256,256]

def auto_move():
    for i in range(0,12):
        if i%2 == 0:
            t.goto(arx[i],ary[0])
            t.goto(arx[i+1],ary[0])
        else:
            t.goto(arx[i],ary[1])
            t.goto(arx[i+1],ary[1])
    t.goto(-256,256)


def move_robot(action):
    t.clear()
    if action == 0:
        for i in range(move_cnt):
            t.goto(rx[i],ry[i])
    elif action == 1:
        for i in range(move_cnt-1,-1,-1):
            t.goto(rx[i],ry[i])
    elif action == 2:
        t.goto(rx[move_cnt-1],ry[move_cnt-1])
    elif action == 3:
        t.goto(rx[0],ry[0])
    elif action == 4:
        auto_move()
    t.penup()

def clicked(x,y):
    global move_cnt
    move_cnt = move_cnt + 1
    rx.append(x)
    ry.append(y)

def list_clear():
    global move_cnt
    del rx[1:move_cnt]
    del ry[1:move_cnt]
    move_cnt = 1


def key_up():
    (x,y) = t.position()
    t.goto(x,y+15)

def key_down():
    (x,y) = t.position()
    t.goto(x,y-15)
    
def key_left():
    (x,y) = t.position()
    t.goto(x-15,y)
    
def key_right():
    (x,y) = t.position()
    t.goto(x+15,y)
    

def key_SP():
    move_robot(0)

def key_BS():
    move_robot(1)

def key_s():
    move_robot(2)

def key_r():
    move_robot(3)

def key_a():
    move_robot(4)

def key_e():
    list_clear()

t.setup(600,600)
s = t.Screen()
t.hideturtle()

s.addshape(robot_fn)
t.shape(robot_fn)
t.speed(6)
t.penup()
clicked(-265,265)
t.goto(-265,265)
t.showturtle()

s.onkey(key_SP, 'space')
s.onkey(key_BS, 'BackSpace')
s.onkey(key_s,'s')
s.onkey(key_r,'r')
s.onkey(key_e,'e')
s.onkey(key_a,'a')
s.onkey(key_right,'Right')
s.onkey(key_left,'Left')
s.onkey(key_up,'Up')
s.onkey(key_down,'Down')
s.onscreenclick(clicked)
s.listen()
