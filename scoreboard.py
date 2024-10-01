from turtle import Turtle


class Scoreboard(Turtle):
    """
    This class manages the scoreboard for the 'Cross the Road' game.

    It inherits from the Turtle class to utilize its drawing capabilities for displaying the
    current level and game over message on the screen.
    """

    def __init__(self):
        """
        This constructor initializes the scoreboard object.

        - Inherits from the Turtle class to utilize its drawing capabilities.
        - Initializes the level attribute to 1, representing the starting level.
        - Sets the turtle properties for efficient use:
            - penup(): Lifts the pen to avoid drawing while positioning.
            - speed(0): Sets the animation speed to the fastest (0).
            - hideturtle(): Hides the turtle object itself on the screen.
            - goto(): Positions the turtle at the specified coordinates (-280, 260).
        - Calls the write_level() function to display the initial level on the screen.
        """
        super().__init__()
        self.level = 1
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(-280, 260)
        self.write_level()

    def write_level(self):
        """
        This function writes the current score (level) to the screen.

        - Uses the write method from the Turtle class to display formatted text.
        - The formatted text includes "Level: " followed by the current level value.
        - Sets the font to Arial, size 20, and bold style for better visibility.
        """
        self.write(arg=f"Level: {self.level}", font=("Arial", 20, "bold"))

    def update_score(self):
        """
        This function updates the score (level) by 1 and displays the new score.

        - Increments the level attribute by 1 to represent progress.
        - Clears the previously written score using the clear method from Turtle.
        - Calls the write_level function to display the updated level on the screen.
        """
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        """
        This function displays a "GAME OVER" message and restart instructions.

        - Positions the turtle at the center of the screen (0, 0) for better visibility.
        - Changes the color to red to highlight the "GAME OVER" message.
        - Writes "GAME OVER" in large, bold font (Arial, 40, bold) for emphasis.
        - Positions the turtle below the "GAME OVER" message (-120 on the y-axis).
        - Lifts the pen to avoid drawing a line while moving.
        - Positions the turtle at the starting point for the horizontal line.
        - Puts the pen down (pendown()) to start drawing a line.
        - Draws a horizontal line under the "GAME OVER" message for separation.
        - Changes the color to black for the restart instructions.
        - Writes instructions to "Press space to restart" with smaller font (Arial, 20, normal).
        - Positions the turtle on the right side of the screen for restart instructions (98 on the x-axis).
        """
        self.goto(-125, 0)
        self.color("red")
        self.write(arg="GAME OVER", font=("Arial", 40, "bold"))
        self.goto(x=0, y=-120)
        self.penup()
        self.goto(x=-98, y=-120)
        self.color("black")
        self.write(arg="Press space to restart", font=("Arial", 20, "normal"))
        self.goto(x=98, y=-120)
