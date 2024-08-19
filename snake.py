from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):

        self.boxes = []
        self.create_snake()



    def create_snake(self):

        for i in STARTING_POSITIONS:
            box = Turtle("square")
            box.color("white")
            box.penup()
            box.goto(i)
            self.boxes.append(box)


    
    def move_snake(self):

        l = len(self.boxes)
        
        for i in range(l-1, 0, -1):
            new_x = self.boxes[i-1].xcor()
            new_y = self.boxes[i-1].ycor()
            self.boxes[i].goto(new_x,new_y)
        self.boxes[0].forward(MOVE_DISTANCE)
    
    def increase_length(self, boxes):
        l = len(boxes)
        box1 = Turtle("square")
        box1.color("white")
        box1.penup()
        box1.goto(self.boxes[l-1].xcor(), self.boxes[l-1].ycor())
        self.boxes.append(box1)
       


    