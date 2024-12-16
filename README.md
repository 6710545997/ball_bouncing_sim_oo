# EATMYBALL GAME

## Project Title
## EATMYBALL GAME##  – A fun interactive simulation where players control a ball that grows by eating food and smaller balls, while avoiding larger balls controlled by bots.

## Project Description
## EATMYBALL GAME##  is an interactive simulation where players control a ball that moves around the screen, eating food and smaller balls to grow in size. Bots, represented by other balls, move randomly and can eat smaller balls. The goal is to grow your ball while avoiding bots that are larger than you. The game features dynamic difficulty as the bots grow in size, and the player must adapt to survive.

### Features:
- ## Player-Controlled Ball## : You control the player ball to move it around using the keyboard.
- ## Random Bots## : Bots move randomly and eat smaller balls to grow larger.
- ## Food Collection## : The player ball can eat food items to increase its size and score.
- ## Ball Collision Mechanics## : Balls can collide with other balls, and larger balls can eat smaller ones.
- ## Dynamic Difficulty## : Bots get stronger as they grow by eating smaller balls.
- ## Score System## : The player's score increases as they consume food and other balls.

### Gameplay Overview:
Controls
Control the Player Ball: Use arrow keys to move the player ball around the screen.
Eat Food: Move the player ball toward food items to eat them and grow larger.
Avoid Bots: Bots grow larger by eating smaller balls, so avoid them if they are larger than your ball!
Objective
Start the game with one player ball and multiple bots.
Use the arrow keys to control the player ball and move it toward the food items.
As you grow by eating food, avoid collisions with larger bots that could eat you.
The more food and smaller balls you eat, the larger your ball becomes, increasing your chances of surviving.

## How to Install and Run the Project

### Requirements:
- Python 3.x
- `turtle` graphics library (usually pre-installed with Python)

### Installation Steps:
1. ## Clone the Repository ## :
   ```bash
   cd to where you want to download game folder
   git clone https://github.com/yourusername/eatmyball-game.git
2. ## Run the Game:## :
    Execute the main.py file to start the game:
    python main.py
3. ## Exit the Game:## 
    Close the turtle graphics window to stop the game.
Usage

### Demonstrate Video Link :
You can watch a demo of the game in action here:

UML Class Diagram
Class Descriptions:

1. Ball Class:
Attributes:
x, y: Coordinates of the ball.
radius: Size of the ball.
color: Color of the ball for display purposes.
speed: Speed at which the ball moves.
Methods:
move_left(), move_right(), move_up(), move_down(): Move the ball in the respective direction.
grow(size_increase): Increase the size of the ball when it eats food or another ball.
check_collision(other_ball): Checks if this ball collides with another ball, useful for detecting if a ball eats another.

2. Bot Class (Inherits Ball)
Attributes:
Inherits all attributes from the Ball class.
bot_id: Unique identifier for each bot.
direction: The direction in which the bot is currently moving.
Methods:
random_move(): Moves the bot randomly in one of the four directions (up, down, left, right).
eat_ball(other_ball): Checks if the bot collides with another ball and eats it if the bot is larger.

3. Food Class
Attributes:
x, y: Coordinates of the food.
radius: Size of the food.
color: Color of the food for display.
Methods:
check_boundaries(width, height): Ensures the food stays within the game boundaries.
spawn_new_food(width, height): Spawns new food at random coordinates within the game area.

4. Game Class
This is the central class of the game, managing the interaction between all the elements (balls, bots, food) and maintaining the game state.
Attributes:
width, height: Dimensions of the game screen.
balls: A list of all balls in the game, including player and bots.
food_items: A list of food items available for the player to eat.
score: The current score of the player.
Methods:
add_ball(ball): Adds a new ball (player or bot) to the game.
spawn_food(): Spawns a new food item at a random location.
check_collisions(): Checks and handles collisions between balls and food or balls.
game_over(): Checks if the game is over (when a bot eats the player).

## Interaction Between Classes: ##
Ball and Bot: Both inherit from Ball class. Bots move randomly and can eat other balls that are smaller than them.
Ball and Food: The player ball eats food, growing in size and increasing the score.
Game Class: It manages the interaction between all balls (players and bots), food, and the game state.

## Summary:## 
Ball Class: Represents both the player and bot balls.
Bot Class: Inherits from Ball and controls the bot's behavior.
Food Class: Handles food objects that can be consumed by the balls.
Game Class: Manages the overall game logic and interactions between balls, bots, and food.

## Modifications and Extensions:## 
This project recreated a simple ball-bouncing simulator into a full interactive game:

Bot Movement: Bots move randomly and can eat smaller balls.

Player Control: Players use arrow keys to move their ball around the screen.

Growth Mechanism: Balls grow in size when they eat food or smaller balls.

Game Boundaries: Balls stay within the defined boundaries of the screen.

## Testing:## 
Automated Unit Tests: This project currently doesn't include unit tests, but it can be extended using frameworks such as unittest or pytest.
Manual Testing: Manual testing involves checking if balls collide properly, if bots behave as expected, and if the player can grow by eating food and other balls.

## Known Issues:## 
There is a minor bug where balls might sometimes overlap or pass through each other when colliding. This will be addressed in future versions.
Project Sophistication Level.

## Rating## 
I rate the sophistication of this project at 90.
Reasoning: The project involves  game mechanics (movement, growth, collision detection), but it introduces multiple interacting objects (player ball, bots, food)  a dynamic difficulty level and theme. it provides a fun and engaging experience.

## Credits## 

Developer :Inthat Niramarn 6710545997

Libraries Used: Python Turtle


