import turtle #وارد کردن کتابخانه turtle
import math #وارد کردن کتابخانه math
wn = turtle.Screen() # ایجاد صفحه
wn.bgcolor("white") # تنظیم رنگ پس زمینه
wn.title("Maze Game") # تنظیم عنوان صفحه
wn.setup(700,700) # تنظیم ابعاد صفحه
turtle.register_shape("r.gif") # ثبت شکل trash.gif
turtle.register_shape("l.gif") # ثبت شکل trash.gif
turtle.register_shape("home.gif") # ثبت شکل trash.gif
turtle.register_shape("wall.gif") # ثبت شکل trash.gif
class Pen(turtle.Turtle): # ایجاد کلاس Pen
    def __init__(self): # تابع ایجاد
        turtle.Turtle.__init__(self) # ایجاد تابع Turtle
        self.shape("square") # تنظیم شکل
        self.color("black") # تنظیم رنگ
        self.penup() # برداشتن قلم
        self.speed(0) # تنظیم سرعت
        
class Player(turtle.Turtle): # ایجاد کلاس Player
    def __init__(self): # تابع ایجاد
        turtle.Turtle.__init__(self) # ایجاد تابع Turtle
        self.shape("r.gif") # تنظیم شکل
        self.color("blue") # تنظیم رنگ
        self.penup() # برداشتن قلم
        self.speed(0) # تنظیم سرعت
        self.gold = 0 # تعریف متغیر gold
    def go_up(self): # تابع go_up
        move_to_x = player.xcor() # تعریف move_to_x
        move_to_y = player.ycor() + 24 # تعریف move_to_y
        if (move_to_x, move_to_y) not in walls: # اگر (move_to_x, move_to_y) در walls نبود
            self.goto(move_to_x, move_to_y) # انتقال به (move_to_x, move_to_y)
    def go_down(self): # تابع go_down
        move_to_x = player.xcor() # تعریف move_to_x
        move_to_y = player.ycor() - 24 # تعریف move_to_y
        if (move_to_x, move_to_y) not in walls: # اگر (move_to_x, move_to_y) در walls نبود
            self.goto(move_to_x, move_to_y) # انتقال به (move_to_x, move_to_y)
    def go_left(self): # تابع go_left
        move_to_x = player.xcor() - 24 # تعریف move_to_x
        move_to_y = player.ycor() # تعریف move_to_y
        self.shape("l.gif") # تنظیم شکل
        if (move_to_x, move_to_y) not in walls: # اگر (move_to_x, move_to_y) در walls نبود
            self.goto(move_to_x, move_to_y) # انتقال به (move_to_x, move_to_y)
    def go_right(self): # تابع go_right
        move_to_x = player.xcor() + 24 # تعریف move_to_x
        move_to_y = player.ycor() # تعریف move_to_y
        self.shape("r.gif") # تنظیم شکل
        if (move_to_x, move_to_y) not in walls: # اگر (move_to_x, move_to_y) در walls نبود
            self.goto(move_to_x, move_to_y) # انتقال به (move_to_x, move_to_y)
    def home1(self, other): # تابع home1
        a = self.xcor() - other.xcor() # تعریف a
        b = self.ycor() - other.ycor() # تعریف b
        distance = math.sqrt((a ** 2) + (b ** 2)) # تعریف distance
        if distance < 5: # اگر distance کمتر از 5 بود
            return True # برگرداندن True
        else: # در غیر این صورت
            return False # برگرداندن False

class home(turtle.Turtle): # ایجاد کلاس home
    def __init__(self, x, y): # تابع ایجاد
        turtle.Turtle.__init__(self) # ایجاد تابع Turtle
        self.shape("home.gif") # تنظیم شکل
        self.color("gold") # تنظیم رنگ
        self.penup() # برداشتن قلم
        self.speed(0) # تنظیم سرعت
        self.gold = 100 # تعریف gold
        self.goto(x, y) # انتقال به (x, y)
    def destroy(self): # تابع destroy
        self.goto(2000, 2000) # انتقال به (2000, 2000)
        self.hideturtle() # پنهان کردن

levels = [""] # ایجاد لیست levels
levels_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX       XXXXXXXX",
"X  XXXXXXX  XXX        XX",
"X       XX  XXX  XXXXX XX",
"XXXXXX  XX  XXX  XXXXX XX",
"XXXXXX  XX  XXX    XXX XX",
"XXXXXX  XX  XXX  XXXXX XX",
"XXXXXX  XX  XXX  XXXXX XX",
"X  XXX        XXXXXXXX XX",
"X  XXX  XXXXXXXXXXXXX  XX",
"X         XXXXXXXXXX  XXX",
"X                XXX  XXX",
"XXXXXXXXXXXX     XXX  XXX",
"XXXXXXXXXXXX     XXX    X",
"XX  XXXXXXXX     XXX    X",
"XX  XXXXXXXXXX         XX",
"XX         XXXXX   XXXXXX",
"XX         XXXXX   XXXXXX",
"XX  XXXXX  XXXXX   XXXXXX",
"XX  XXXXX               X",
"XX          XXXXXXXXXXXXX",
"XX              XXXXXXXXX",
"XX  XXXXXXXXXX          X",
"XX  XXXXXXXXXXX  TXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]# ایجاد لیست levels_1
homes = [] # ایجاد لیست homes
levels.append(levels_1) # اضافه کردن لیست levels_1 به لیست levels
def setup_maze(level): # تابع setup_maze
    for y in range(len(level)): # برای هر y در لیست level
        for x in range(len(level[y])): # برای هر x در لیست level
            character = level[y][x] # تعریف character
            screen_x = -288 + (x * 24) # تعریف screen_x
            screen_y = 288 - (y * 24) # تعریف screen_y

            if character == "X": # اگر character = X
                pen.goto(screen_x, screen_y) # رفتن به موقعیت screen_x و screen_y
                pen.shape("wall.gif") # تنظیم شکل
                pen.stamp() # نقاشی کردن
                walls.append((screen_x, screen_y)) # اضافه کردن موقعیت به لیست walls
            if character == "P": # اگر character = P
                player.goto(screen_x, screen_y) # رفتن به موقعیت screen_x و screen_y
            if character == "T": # اگر character = T
                homes.append(home(screen_x, screen_y)) # اضافه کردن موقعیت به لیست homes

pen= Pen() # ایجاد pen
player = Player() # ایجاد player
walls = [] # ایجاد لیست walls
setup_maze(levels[1]) # اجرای تابع setup_maze
turtle.listen() # شنیدن
turtle.onkey(player.go_left, "Left") # اجرای تابع go_left با کلید Left
turtle.onkey(player.go_right, "Right") # اجرای تابع go_right با کلید Right
turtle.onkey(player.go_up, "Up") # اجرای تابع go_up با کلید Up
turtle.onkey(player.go_down, "Down") # اجرای تابع go_down با کلید Down
wn.tracer(0) # تنظیم tracer
while True: # برای همیشه
    for home in homes: # برای هر home در لیست homes
        if player.home1(home): # اگر player در home بود
            print('win') # چاپ win
            quit() # خروج
            
    wn.update() # بروزرسانی صفحه