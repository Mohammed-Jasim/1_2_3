#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def drop_apple():
    wn.tracer(False)
    draw_an_A()
    
    apple.penup()
    wn.tracer(True)
    apple.goto(0, -200)
    apple.pendown()
    apple.clear()
def draw_an_A():
    
    apple.hideturtle()
    ok = apple.xcor()
    alr = apple.ycor()
    apple.penup()
    apple.goto(ok-18, alr+40)
    apple.pendown()
    apple.color("white")
    apple.write("A", font=("Arial", 55, "bold")) 
    apple.showturtle()
    
#-----function calls-----
draw_apple(apple)
wn.onkeypress(drop_apple, "a")
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()