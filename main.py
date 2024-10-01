import time
from turtle import Screen
from player import Player  # Import Player class
from scoreboard import Scoreboard  # Import Scoreboard class
from car import Car  # Import Car class

# Define screen size and goal line position
SCREENSIZE = [600, 600]
GOAL_LINE = 290

# Initialize the screen
screen = Screen()
screen.setup(SCREENSIZE[0], SCREENSIZE[1])
screen.tracer(0)  # Turn off automatic screen update for performance
screen.title("Cross the Road")


def play():
    """
    This function resets the game and starts a new round
    """
    screen.clear()
    screen.tracer(0)
    screen.listen()  # Start listening for keyboard input

    # Initialize game objects
    score_brd = Scoreboard()
    player = Player()

    # Game variables
    moves = 1  # Tracks player movements
    car_speed = 3.5  # Initial speed of cars
    dose_size = 1 # Number of cars spawned at once
    threshold = 20  # Number of moves to spawn new cars (decreases with level)
    car_list = []  # List to store all Car objects

    # Bind keyboard controls
    screen.onkey(key='Up', fun=player.up)  # Up arrow to move player up

    def not_too_close(this_car):
        """
        Checks if a car is too close to another car on the same y-axis
        """
        close_calls = 0
        for other_car in car_list:
            if abs(this_car.xcor() - other_car.xcor()) < 65 and this_car.ycor() == other_car.ycor():
                close_calls += 1

        return close_calls == 0  # True if not close to another car

    def new_dose(size, this_speed):
        """
        Spawns a new 'dose' (batch) of cars with a given size and speed
        """
        for _ in range(int(size)):
            the_car = Car(this_speed)
            trials = 0

            # Ensure cars are not spawned too close to each other
            while not not_too_close(the_car) and trials < 999 and len(car_list) > 0:
                the_car.new_pos()  # Randomly reposition the car
                trials += 1

            if trials >= 1000:  # Prevent infinite loop if impossible to spawn
                del the_car
                print("deleted")
            else:
                car_list.append(the_car)  # Add the car to the list

    def car_player_same_line(this_car):
        """
        Checks if the player and car are on the same horizontal line
        """
        return player.ycor() - this_car.ycor() == -5  # -5 is the y-offset of player

    def too_close(this_car):
        """
        Checks if the car is too close to the player
        """
        return this_car.distance(player) < 35  # Distance between car and player

    def setup(this_car_speed):
        """
        Initializes the game by spawning cars across the screen
        """
        for i in range(0, 400, 50):
            this_car = Car(this_car_speed)
            this_car.setup_pos(x=i)  # Set initial position for car
            car_list.append(this_car)

    # Initial setup with starting car speed
    setup(car_speed)

    game_on = True  # Flag to keep the game running
    while game_on:  # Main game loop

        for car in car_list[:]:  # Iterate over a copy of the car list to avoid modification issues
            car.move()  # Move the car
            if car.reached_endpoint():  # Check if the car has reached the end of the screen
                car.hideturtle()  # Hide the car
                car_list.remove(car)  # Remove the car from the list

            # Check if the car and player are on the same line and too close
            if car_player_same_line(car) and too_close(car):
                time.sleep(2)  # Pause for 2 seconds
                score_brd.clear()  # Clear the scoreboard
                # Hide and remove all cars
                for every_car in car_list[:]:
                    every_car.hideturtle()
                    car_list.remove(every_car)
                player.hideturtle()  # Hide the player
                score_brd.game_over()  # Display game over message
                game_on = False  # End the game

        # Every 'threshold' number of moves, add a new dose of cars
        if moves % int(threshold) == 0:
            new_dose(dose_size, car_speed)  # Add new cars
            moves = 1  # Reset the move counter

        # Check if the player has reached the goal line
        goal = player.ycor() >= GOAL_LINE

        if goal:  # If the player reaches the goal line
            # Hide and remove all cars
            for car in car_list[:]:
                car.hideturtle()
                car_list.remove(car)
            car_speed += 0.2  # Increase the speed of the cars
            player.take_pos()  # Reset the player's position
            threshold += 0.05  # Increase the move threshold
            score_brd.update_score()  # Update the score
            setup(car_speed)  # Reinitialize the cars with the new speed

        moves += 1  # Increment the move counter
        screen.update()  # Update the screen
        if not game_on:  # If the game has ended
            screen.onkey(key="space", fun=play)  # Restart the game when space is pressed


play()  # Start the game
screen.exitonclick()  # Close the window on click
