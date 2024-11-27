

import pytest
from polygon import Polygon

'''test function to verify that a Polygon object is correctly initialized with values for name and sides.'''

def test_polygon_initialization():
    """
    Test the initialization of the Polygon class.

    Ensures that a Polygon object is correctly initialized with a name and sides.
    """
    p = Polygon("Square",[4,4,4,4])
    assert p.get_name() == "Square"
    assert p.get_sides() == [4,4,4,4]

def test_polygon_GS():
    """
    Test the getter and setter methods of the Polygon class.

    Ensures that attributes can be accessed and updated correctly.
    """
    p = Polygon("Triangle", [3,3,3])

    p.set_name("Hexagon")
    assert p.get_name() == "Hexagon"

    p.set_sides((2,2,2,2,2,2))
    assert p.get_sides() == [2,2,2,2,2,2]

def test_circumference():
    """
    Test the calculate_circumference method.

    Ensures that the circumference is correctly calculated as the sum of the sides.
    """
    obj1 = Polygon("Square", [6.5,6.5,6.5,6.5])
    assert obj1.calculate_circumference() == pytest.approx(26.000000, abs = 1e-4)

def test_polygon__equality():
    """
    Test the equality (__eq__) method.

    Verifies that two Polygon objects with the same name and sides are considered equal.
    """
    p1= Polygon("Square",[4,4,4,4])
    p2= Polygon("Square",[4,4,4,4])
    assert p1 == p2

def test_polygon_inequality():
    """
    Test the inequality (__ne__) method.

    Ensures that two Polygon objects with different attributes are considered not equal.
    """
    p3= Polygon("Hexagon",[2,2,2,2,2,2])
    p4= Polygon("Triangle",[3,3,3])
    assert p3 != p4

def test_polygon_str():
    """
    Test the string representation (__str__) method.

    Ensures the string output matches the expected format for different polygons.
    """
    p1 = Polygon("Triangle", [3,3,3])
    p2 = Polygon("Square", [4,4,4,4])
    p3 = Polygon("Hexagon", [2,2,2,2,2,2])
    assert str(p1) == "Triangle with sides: [3,3,3]"
    assert str(p2) == "Square with sides: [4,4,4,4]"
    assert str(p3) == "Hexagon with sides: [2,2,2,2,2,2]"