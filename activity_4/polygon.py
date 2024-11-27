"""
This activity contains 5 steps, with 
Step 1 for Defining Class Members, Constructor, Getters, and Setters
Step 2 for Implementing Equality (__eq__) and Inequality (__ne__) Methods 
Step 3 for Implementing String Representation (__str__) Method
Step 4 for Implementing the calculate_circumference Method 
Step 5 for creating main function
"""

class Polygon:
    """
    A class to represent a polygon with a name and a list of side lengths.
    """

    def __init__(self, name, sides):
        """
        Initializes a Polygon object with a name and a list of sides.
        """
        self.__name = name
        self.__sides = sides

    def get_name(self):
        """
        Returns the name of the polygon.
        """
        return self.__name
    
    def set_name(self, name):
        """
        Sets the name of the polygon.
        """
        self.__name = name 
    
    def get_sides(self):
        """
        Returns the sides of the polygon.
        """
        return self.__sides
    
    def set_sides(self, sides):
        """
        Sets the sides of the polygon.
        """
        self.__sides = sides

    def __eq__(self, other):
        """
        Compares two Polygon objects for equality.
        """
        if type(self) == type(other):
            return self.__name == other.__name and self.__sides == other.__sides
        return False
        
    def __ne__(self, other):
        """
        Checks if two Polygon objects are not equal.
        """
        return not self.__eq__(other)
    
    def __str__(self):
        """
        Returns a string representation of the polygon.
        """
        return f"{self.__name} with sides: {self.__sides}"
    
    def calculate_circumference(self):
        """
        Calculates the circumference of the polygon as the sum of its sides.
        """
        return sum(self.__sides)

def main():
    """
    Demonstrates the functionality of the Polygon class.

    Creates and prints three Polygon objects (triangle, square, hexagon) along
    with their calculated circumferences.
    """
    triangle_obj = Polygon('Triangle', [9, 8, 9])
    square_obj = Polygon('Square', [25, 25, 25, 25])
    hexagon_obj = Polygon('Hexagon', [10, 10, 10, 10, 10, 10])
    
    print(triangle_obj)
    print(square_obj)
    print(hexagon_obj)
    
    print(triangle_obj.calculate_circumference())
    print(square_obj.calculate_circumference())
    print(hexagon_obj.calculate_circumference())

if __name__ == '__main__':
    main()
