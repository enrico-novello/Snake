from tkinter import*
import random

GAME_WIDTH=1000
GAME_HEIGHT=700
SPEED=50
SPACE_SIZE=50
BODY_PARTS=3
SNAKE_COLOR="green"
FOOD_COLOR="red"
BGCOLOR="black"


class Snake:
    def __init__(self):
        self.bosySize=BODY_PARTS
        self.coordinates = []
        self.squares=[]
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        x=random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y= random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
        self.coordinates=[x,y]
        canvas.create_oval(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR,tags="food")

def nextTurn(snake, food):
    x,y=snake.coordinates[0]
    if direction=="up":
        y-=SPACE_SIZE
    elif direction=="down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x,y))
    square=canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food=Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if checkCollisions(snake):
        gameOver()
    else:
        w.after(SPEED, nextTurn, snake, food)

def changeDirection(newDirection):
    global direction
    if newDirection=='left':
        if direction!='right':
            direction= newDirection
    elif newDirection == 'right':
        if direction != 'left':
            direction = newDirection
    elif newDirection == 'up':
        if direction != 'down':
            direction = newDirection
    elif newDirection == 'down':
        if direction != 'up':
            direction = newDirection
def checkCollisions(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>= GAME_WIDTH:
        return True
    elif y<0 or y>= GAME_HEIGHT:
        return True
    for bodyPart in snake.coordinates[1:]:
        if x==bodyPart[0] and y==bodyPart[1]:
            return True
    return False
def gameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
                       font=("American Typewriter", 70), text="GAME OVER", fill="red", tag="gameover")


w=Tk()
w.title("Snake")
w.resizable(False, False)
score=0
direction='down'
label=Label(w, text="Score:{}".format(score), font=("American Typewriter", 40))
label.pack()
canvas=Canvas(w, bg=BGCOLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
w.update()
w_width= w.winfo_width()
w_height= w.winfo_height()
screenWidth=w.winfo_screenwidth()
screenHeight=w.winfo_screenheight()
x=int((screenWidth/2)-(w_width/2))
y=int((screenHeight/2)-(w_height/2))
w.geometry(f"{w_width}x{w_height}+{x}+{y}")
w.bind('<Left>', lambda event: changeDirection('left'))
w.bind('<Right>', lambda event: changeDirection('right'))
w.bind('<Up>', lambda event: changeDirection('up'))
w.bind('<Down>', lambda event: changeDirection('down'))
snake=Snake()
food=Food()
nextTurn(snake, food)



w.mainloop()