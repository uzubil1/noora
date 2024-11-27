

"""PART 3 & 4"""


from turtle import Screen, Turtle as t
from pixart import draw_grid, draw_shape_from_string, draw_shape_from_file

def initialization(turta):
    
    PIXEL_SIZE = 30
    COLUMNS = 20
    ROWS = 20
   
    
    turta.speed(-20)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2)
    turta.setheading(0)
    turta.pendown()
    

def main():
    screen = Screen()  
    turta = t()  
    initialization(turta)  
    
    while True:
        print("\nMenu:")
        print("1. Draw a shape from string input")
        print("2. Draw a grid(checkboard)")
        print("3. Draw a shape from file")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            draw_shape_from_string(turta)
        elif choice == '2':
            draw_grid(turta)
        elif choice == '3':
            draw_shape_from_file(turta)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please choose 1, 2, 3, or 4.")

    screen.mainloop()

if __name__ == "__main__":
    main()
