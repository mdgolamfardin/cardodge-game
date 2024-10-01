from turtle import Turtle
import random

CAR_LENGTH = 2.5  # Length of the car
CAR_WIDTH = 1.5   # Width of the car
END_POINT = -325  # X-coordinate where car reaches the end of the screen
COLORS = ['yellow', 'red', 'green', 'purple', 'blue', 'orange', 'brown']  # Available car colors

# Pre-calculated starting positions for cars on the y-axis (spread across the screen)
STARTING_Y_POINTS = [i for i in range(-210, 270, int((20 * CAR_WIDTH)))]

# Pre-calculated starting positions for cars on the x-axis (off-screen to the right)
STARTING_X_POINTS = [i for i in range(300, 900, 10)]


class Car(Turtle):
    """
    This class represents a car object in the 'Cross the Road' game.

    It inherits from the Turtle class to utilize its movement capabilities.
    Each car instance has a random color, specific size, and movement speed.
    """

    def __init__(self, car_speed):
        """
        This constructor initializes a car object.

        - Inherits from the Turtle class with a square shape for the car.
        - Sets the animation speed to the fastest (0) for smooth movement.
        - Chooses a random color for the car from the available 'COLORS' list.
        - Lifts the pen to avoid drawing while positioning the car.
        - Sets the size of the car based on pre-defined length and width.
        - Assigns the initial movement speed based on the provided argument.
        - Calls the new_pos() function to set a random starting position for the car.
        """
        super().__init__("square")
        self.speed(0)
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_len=CAR_LENGTH, stretch_wid=CAR_WIDTH)
        self.move_speed = car_speed
        self.new_pos()

    def move(self):
        """
        This function moves the car to the left by its current speed.

        - Uses the goto() method from Turtle to update the car's position.
        - The new X-coordinate is calculated by subtracting the move_speed from the current X-coordinate.
        - The Y-coordinate remains unchanged as the car moves horizontally.
        """
        self.goto(self.xcor() - self.move_speed, self.ycor())

    def reached_endpoint(self):
        """
        This function checks if the car has reached the end of the screen (left side).

        - Compares the current X-coordinate of the car with the END_POINT constant.
        - Returns True if the car's X-coordinate is less than or equal to the END_POINT, indicating it's off-screen.
        """
        return self.xcor() <= END_POINT

    def new_pos(self, x=320):
        """
        This function sets a new random starting position for the car (off-screen to the right).

        - Takes an optional 'x' argument, allowing for specific positioning during setup.
        - If no argument is provided, it chooses a random X-coordinate from the pre-calculated STARTING_X_POINTS list.
        - Sets a random Y-coordinate for the car from the pre-calculated STARTING_Y_POINTS list.
        - Uses goto() to move the car to the new position.
        """
        if x == 320:
            self.goto(random.choice(STARTING_X_POINTS), random.choice(STARTING_Y_POINTS))
        else:
            self.goto(x, -210)  # Used during initial setup to position all cars at the bottom

    def setup_pos(self, x):
        """
        This function sets a starting position for the first set of cars at the bottom of the screen
        (used during initial setup).

        It
        - Takes an 'x' argument representing the desired X-coordinate for the car.
        - Sets the Y-coordinate to -210, placing the car at the bottom of the screen.
        - Uses goto() to move the car to the specified position.
        """
        self.goto(x, -150)
