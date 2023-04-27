# FLAPPY_BİRD
#### video Demo:
## Description
-   To create a Flappy Bird game in Python using the Pygame library, you would need to design the game mechanics, create the graphics and audio, and write the code to implement the game logic. This would involve creating the bird and pipe objects, setting up collision detection, handling user input, and updating the game state every frame.

## Folder Contents
- **project.py**: This file contains the ```main``` function, along with several other helper functions necessary to implement the game.
- **test_project.py**: This contains test functions written using the ```pytest``` library for the project.py file.
- **requirements.txt**: All ```pip```-installable libraries that I used for this project are listed here.

## How to Play
-   The code starts by displaying a message that invites the player to start the game, and waits for the player to press the space bar or the up arrow key. Then, the game loop starts, where the bird moves up and down according to the player's input and gravity, and the pipes and ground move to the left to simulate the bird's flight. The game ends if the bird hits a pipe or the ground.

## Game Mechanics

In every game,The code also includes several variables that define the dimensions of the game window, the speed of the game, and the gravity that affects the bird. Additionally, the code includes sound effects that play when the bird flaps its wings or hits an obstacle.

#### map info
-   The pygame library is used to create the game window, load images and sounds, draw sprites, and detect user input events. The random library is used to generate random pipe heights.
-   The Pygame module is initialized, and the screen is set with the given dimensions. The game's background and bird images are loaded from the assets directory, and the bird and ground objects are created and added to their respective sprite groups. The pipes are created using the get_random_pipes function.

#### character's stats info
-   '__init__()': This method initializes the Bird object. It loads the bird sprite image, sets its initial position, velocity and gravity.
-   'update()': This method updates the bird's position based on its velocity and gravity. It is called every frame of the game loop to animate the bird's motion.
-   'bump()': This method increases the bird's velocity when the user presses the space or up arrow key to make the bird jump.

## what test functions do
-   The "test_bird_initialization()" test checks if the Bird class initializes correctly by verifying that the bird's starting position is at the correct coordinates on the screen.

-   The "test_bird_bump()" test checks if the Bird bump function works by verifying that the bird's speed changes when it is called.

-   The "test_ground_initialization()" test checks if the Ground class initializes correctly by verifying that the ground's starting position is at the correct coordinates on the screen.

-   The "test_pipe_initialization()" test checks if the Pipe class initializes correctly by verifying that the pipe's starting position is at the correct coordinates on the screen.

-   The "test_get_random_pipes()" test checks if the get_random_pipes function returns two Pipe instances by verifying that the objects returned are instances of the Pipe class.

## Contribution
If you find any issues or want to contribute to this project, feel free to create a pull request or submit an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
