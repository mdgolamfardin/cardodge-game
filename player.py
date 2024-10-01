from turtle import Turtle

TURTLE_COLOR = 'black'
STARTING_POSITION = (0, -275)  # X-coordinate, Y-coordinate
STRETCH = 1.1  # Stretching factor for player size
STEP_SIZE = 30  # Movement distance for each up/down action


class Player(Turtle):
    """
    This class represents the player character in the 'Cross the Road' game.

    It inherits from the Turtle class to utilize its drawing and movement capabilities.
    The player is a turtle object with a specific color, size, and movement control.
    """

    def __init__(self):
        """
        This constructor initializes the player object.

        - Inherits from the Turtle class with a "turtle" shape for the player.
        - Sets the animation speed to the fastest (0) for smooth movement.
        - Sets the player's starting direction to move upwards (heading 90 degrees).
        - Defines the player's size based on pre-defined stretching factors for width and length.
        - Sets the player's color using the TURTLE_COLOR constant.
        - Lifts the pen to avoid drawing while positioning the player.
        - Calls the take_pos() function to set the player's initial starting position.
        """
        super().__init__("turtle")
        self.speed(0)
        self.setheading(90)
        self.shapesize(stretch_wid=STRETCH, stretch_len=STRETCH)
        self.color(TURTLE_COLOR)
        self.penup()
        self.take_pos()

    def take_pos(self):
        """
        This function moves the player to its starting position.

        - Uses the goto() method from Turtle to set the player's coordinates.
        - The coordinates are retrieved from the STARTING_POSITION constant,
        representing the X and Y coordinates where the player starts the game.
        """
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])

    def up(self):
        """
        This function moves the player upwards by a defined step size.

        - Uses the forward() method from Turtle to move the player forward.
        - The forward movement is determined by the STEP_SIZE constant,
        which controls the distance the player moves with each "up" action.
        """
        self.forward(STEP_SIZE)
