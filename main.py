#   a123_apple_1.py
import turtle as trtl
import random
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple1 = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()
apple4 = trtl.Turtle()
apple5 = trtl.Turtle()
apple1.shape(apple_image)
apple2.shape(apple_image)
apple3.shape(apple_image)
apple4.shape(apple_image)
apple5.shape(apple_image)
apple1.penup()
apple1.goto(0, 0)
apple2.penup()
apple2.goto(100, 0)
apple3.penup()
apple3.goto(200, 0)
apple4.penup()
apple4.goto(-100, 0)
apple5.penup()
apple5.goto(-200, 0)

letters=['a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't','u', 'v', 'w','x','y','z']
letter1 = letters[random.randint(1, 26)]
letter2 = letters[random.randint(1, 26)]
letter3 = letters[random.randint(1, 26)]
letter4 = letters[random.randint(1, 26)]
letter5 = letters[random.randint(1, 26)]
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def drop_apple():
    wn.tracer(False)
    draw_an_A()
    
    apple1.penup()
    wn.tracer(True)
    apple1.goto(0, -200)
    apple1.pendown()
    apple1.clear()
def draw_an_A():
    
    apple1.hideturtle()
    ok = apple1.xcor()
    alr = apple1.ycor()
    apple1.penup()
    apple1.goto(ok-18, alr+40)
    apple1.pendown()
    apple1.color("white")
    apple1.write(letter1, font=("Arial", 55, "bold")) 
    apple1.showturtle()

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def drop_apple():
    wn.tracer(False)
    draw_an_A()
    
    apple1.penup()
    wn.tracer(True)
    apple1.goto(0, -200)
    apple1.pendown()
    apple1.clear()
def draw_an_A():
    
    apple1.hideturtle()
    ok = apple1.xcor()
    alr = apple1.ycor()
    apple1.penup()
    apple1.goto(ok-18, alr+40)
    apple1.pendown()
    apple1.color("white")
    apple1.write(letter1, font=("Arial", 55, "bold")) 
    apple1.showturtle()
    
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def drop_apple1():
    apple1.goto(0, -200)
    apple1.pendown()
def drop_apple2():
    apple2.goto(100, -200)
    apple2.pendown()
def drop_apple3():
    apple3.goto(200, -200)
    apple3.pendown()
def drop_apple4():
    apple4.goto(-100, -200)
    apple4.pendown()
def drop_apple5():
    apple5.goto(-200, -200)
    apple5.pendown()

def draw_a_letter(a_apple, letter):
    
    a_apple.hideturtle()
    ok = a_apple.xcor()
    alr = a_apple.ycor()
    a_apple.penup()
    a_apple.goto(ok-18, alr+40)
    a_apple.color("white")
    a_apple.write(letter, font=("Arial", 55, "bold")) 
    a_apple.goto(ok+18, alr-40)
    a_apple.showturtle()

#-----function calls-----
draw_a_letter(apple1, letter1)
draw_a_letter(apple2, letter2)
draw_a_letter(apple3, letter3)
draw_a_letter(apple4, letter4)
draw_a_letter(apple5, letter5)

wn.onkeypress(drop_apple1, letter1)
wn.onkeypress(drop_apple2, letter2)
wn.onkeypress(drop_apple3, letter3)
wn.onkeypress(drop_apple4, letter4)
wn.onkeypress(drop_apple5, letter5)
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()
