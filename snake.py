from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] #constants named with all caps
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
#use constants, cos if wanna tweak the game like change move dist or start position, just look at the top and change
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] #must be below create_snake() if not will error, as first item from segments
        #(empty list) is nothing

    def create_snake(self):
        for position in STARTING_POSITIONS:  # first created at 0,0 then move to i.e. -40, 0
            self.add_segment(position)

    def add_segment(self, position): #move one square to position and add its position into the list "segments"
        tim = Turtle(shape="square")
        tim.color("white")
        tim.up()  # dont draw the line as it moves
        tim.goto(position)
        # tim.goto(x=0+(i*-20) ,y=0)
        self.segments.append(tim)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear() #remove all the items in the list
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        #add a new segment to the snake.
        self.add_segment(self.segments[-1].position()) #-1 position gets hold of the last item in the list

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  #(start, stop, step), looping through in reverse
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor() #gets the 2nd to last segment position
            self.segments[seg_num].goto(new_x, new_y)  #tail move towards the head insted of head move then tail follow
            #this method prevents the head from separating from the body when turning
        self.head.forward(MOVE_DISTANCE) #nid to move the first segment forward by 20 paces, if not all at same position

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
