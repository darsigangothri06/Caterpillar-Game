import turtle as t
import random as rd

t.bgcolor("yellow")
# defining the turtles
caterpillar = t.Turtle()
caterpillar.shape('square') # combination of three squares
caterpillar.speed(0) # initial speed is 0
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()  # food
# registering a new shape
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))  # shape as a hexagon -- coordinates
t.register_shape('leaf', leaf_shape)
# assigning the new shape to leaf
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

game_started = False # until any key is pressed, game should not start
text_turtle = t.Turtle()
text_turtle.write("Press SPACE to Start", align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    
    (x,y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside
        
def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-100,100))
    leaf.sety(rd.randint(-100,100))
    leaf.showturtle()
    
def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write("Game Over!", align='center', font=('Arial', 30, 'italic'))
    
def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 80
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))
    
def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    
    score = 0
    text_turtle.clear()
    
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()
    
    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length += 1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed += 1
            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break
                
def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)
        
def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)
        
def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)
    
def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)
        
# defining keys
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')

t.listen()
t.mainloop()
