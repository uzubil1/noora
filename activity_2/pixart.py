"""Group 9 
Musaeva Safiia
El Amouri, Youssef
Saad, Mohammad"""


from turtle import Screen, Turtle 

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

def initialization(turta):
    '''Function which sets the speed, pencolor and the starting point of the turtle to start drawing'''
    turta.speed(-20)  
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2) 
    turta.setheading(0) 
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)

"""PART 1"""

def get_color(x):
    
    if x == '0':
        return 'black'
    elif x == '1':
        return 'white'
    elif x == '2':
        return 'red'
    elif x == '3':
        return 'yellow'
    elif x == '4':
        return 'orange'
    elif x == '5':
        return 'green'
    elif x == '6':
        return 'yellowgreen'
    elif x == '7':
        return 'sienna'
    elif x == '8':
        return 'tan'
    elif x == '9':
        return 'gray'
    elif x == 'A':
        return 'darkgray'
    else:
        return None  

def draw_color_pixel(color_string, turta):
    
    turta.color(color_string)
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(PIXEL_SIZE)  
        turta.right(90)
    turta.end_fill()

def draw_pixel(char_x, turta):
    
    color_string = get_color(char_x)
    if color_string:
        draw_color_pixel(color_string, turta)
    else:
        print(f"Invalid color character: {char_x}")

def draw_line_from_string(color_string, turta):
    
    for x in color_string:
        if get_color(x) is None:
            print(f"Invalid character '{x}' in string. Stopping drawing.")
            return False
        draw_pixel(x, turta)
        turta.penup()
        turta.forward(PIXEL_SIZE)  
        turta.pendown()
       
    return True

def draw_shape_from_string(turta):
   
    while True:
        color_string = input("Enter a string of colors (or press Enter to quit): ")
        if not color_string:
            print("No more input. Exiting.")
            break
        
        
        start_position = turta.position()
        
        draw_line_from_string(color_string, turta)

        
        turta.penup()
        turta.goto(start_position[0] + PIXEL_SIZE * len(color_string), start_position[1])  
        turta.setheading(0)  
        turta.pendown()
       


"""PART 2"""


def draw_grid(turta):
 
  
    for row in range(ROWS):
        if row % 2 == 0:
            draw_line_from_string('0202020202020202020202', turta)
        else:
            draw_line_from_string('2020202020202020202020', turta)  
        turta.penup()
        turta.goto(-PIXEL_SIZE * COLUMNS / 2, turta.ycor() - PIXEL_SIZE)
        turta.pendown()
      


def draw_shape_from_file(turta):

    file_path = input("Enter the path of the file: ")

    try:

        with open(file_path, 'r') as file:
            
            for line in file:
                color_string = line.strip()

               
                draw_line_from_string(color_string, turta)

                
                turta.penup()
                turta.goto(-PIXEL_SIZE * COLUMNS / 2, turta.ycor() - PIXEL_SIZE)
                turta.pendown()  
                

    except FileNotFoundError:
        print(f"File not found: {file_path}")


