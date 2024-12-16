import random
import turtle
import math
import time

# Screen width and height
SCREEN_WIDTH = 1400  # Full screen width
SCREEN_HEIGHT = 900  # Full screen height
SCREEN_X_BOUNDARY = SCREEN_WIDTH // 2
SCREEN_Y_BOUNDARY = SCREEN_HEIGHT // 2

class Ball:
    def __init__(self, radius, x, y, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.speed = 5
        self.shape = turtle.Turtle()
        self.shape.speed("fastest")
        self.shape.penup()
        self.shape.goto(self.x, self.y - self.radius)  # Correct positioning
        self.shape.shape("circle")
        self.shape.shapesize(self.radius / 10)
        self.shape.color(self.color)
        self.earth = False
        self.id = id(self)

    def distance(self, that):
        # Calculate the distance from the edge of one object to the edge of the other
        x1, y1 = self.x, self.y
        x2, y2 = that.x, that.y
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def move_left(self):
        self.x -= self.speed
        self.check_boundaries()
        self.update_position()

    def move_right(self):
        self.x += self.speed
        self.check_boundaries()
        self.update_position()

    def move_up(self):
        self.y += self.speed
        self.check_boundaries()
        self.update_position()

    def move_down(self):
        self.y -= self.speed
        self.check_boundaries()
        self.update_position()

    def check_boundaries(self):
        # Ensure the ball stays within the screen boundaries
        if self.x - self.radius < -SCREEN_X_BOUNDARY:  # Left boundary
            self.x = -SCREEN_X_BOUNDARY + self.radius
        elif self.x + self.radius > SCREEN_X_BOUNDARY:  # Right boundary
            self.x = SCREEN_X_BOUNDARY - self.radius

        if self.y - self.radius < -SCREEN_Y_BOUNDARY:  # Bottom boundary
            self.y = -SCREEN_Y_BOUNDARY + self.radius
        elif self.y + self.radius > SCREEN_Y_BOUNDARY:  # Top boundary
            self.y = SCREEN_Y_BOUNDARY - self.radius

    def update_position(self):
        self.shape.goto(self.x, self.y - self.radius)

    def eat_food(self, food):
        """Check if the ball eats a food item."""
        distance_to_food = self.distance(food)
        if distance_to_food < self.radius + food.radius:  # Collision detected
            food.shape.hideturtle()  # Hide the food item
            food.eaten = True  # Mark the food as eaten
            self.radius += 1  # Increase the player's ball size
            if self.speed > 5:
                self.speed -= 0.25
            else:
                pass
            self.shape.shapesize(self.radius / 10)  # Update ball size

            return True
        return False

    def eat_ai(self, other_ai):
        """Allow one AI to eat another if it is larger."""
        distance_to_ai = self.distance(other_ai)
        if distance_to_ai < self.radius + other_ai.radius:  # Collision detection
            if self.radius >= other_ai.radius:  # Larger ball eats the smaller one
                other_ai.shape.hideturtle()  # Hide the smaller ball
                other_ai.eaten = True  # Mark it as eaten
                self.radius += other_ai.radius / 3  # Grow the larger ball
                self.shape.shapesize(self.radius / 10)  # Update the shape size
                print(f"AI ball {self.id} at ({self.x}, {self.y}) ate AI ball {other_ai.id} at ({other_ai.x}, {other_ai.y})")
            else:
                print(f"AI ball {self.id} at ({self.x}, {self.y}) tried to eat a bigger AI ball!")
    


class AI(Ball):
    def __init__(self, radius, x, y, color, id):
        super().__init__(radius, x, y, color)
        self.id = id
        self.eaten = False
        self.direction = random.choice(["left", "right", "up", "down"])  # Initial random direction
        self.duration = random.uniform(0.5, 10)  # Random duration for the movement in seconds
        self.last_move_time = time.time()  # Store the last move time to track duration

    def random_move(self):
        current_time = time.time()

        # Check if the AI should change direction based on the duration
        if current_time - self.last_move_time > self.duration:
            # Change direction and reset duration
            self.direction = random.choice(["left", "right", "up", "down"])
            self.duration = random.uniform(1, 3.0)  # Randomize duration for the next movement
            self.last_move_time = current_time  # Update the last move time

        # Move the AI ball in the current direction
         # Random speed 
        random_speed = random.uniform(0.1, 0.7)

        if self.direction == "left":
            self.x -= random_speed
        elif self.direction == "right":
            self.x += random_speed
        elif self.direction == "up":
            self.y += random_speed
        elif self.direction == "down":
            self.y -= random_speed

        self.check_boundaries()  # Ensure AI ball stays within screen
        self.update_position()
    def eat_food(self, food):
        """Check if the AI eats a food item."""
        distance_to_food = self.distance(food)
        if distance_to_food < self.radius + food.radius:  # Collision detected
            food.shape.hideturtle()  # Hide the food item
            food.eaten = True  # Mark the food as eaten
            self.radius += 1  # Increase the AI's ball size
            self.shape.shapesize(self.radius / 10)  # Update ball size
            return True
        return False


class Food:
    def __init__(self, radius, x, y, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.shape = turtle.Turtle()
        self.shape.speed("fastest")
        self.shape.penup()
        self.shape.goto(self.x, self.y - self.radius)  # Position food correctly
        self.shape.shape("circle")
        self.shape.shapesize(self.radius / 10)
        self.shape.color(self.color)
        self.eaten = False  # Flag to track if the food has been eaten

    def check_boundaries(self):
        # Ensure the food stays within the screen boundaries
        if self.x - self.radius < -SCREEN_X_BOUNDARY:  # Left boundary
            self.x = -SCREEN_X_BOUNDARY + self.radius
        elif self.x + self.radius > SCREEN_X_BOUNDARY:  # Right boundary
            self.x = SCREEN_X_BOUNDARY - self.radius

        if self.y - self.radius < -SCREEN_Y_BOUNDARY:  # Bottom boundary
            self.y = -SCREEN_Y_BOUNDARY + self.radius
        elif self.y + self.radius > SCREEN_Y_BOUNDARY:  # Top boundary
            self.y = SCREEN_Y_BOUNDARY - self.radius

        self.shape.goto(self.x, self.y - self.radius)


class Game:
    def __init__(self):
        self.ball = Ball(10, 10000, 0, "#C0392B")
        self.ai_balls = []
        self.food_items = []
        self.color_options =[
                               "#F1C40F",  # Gold
                               "#E67E22",  # Orange
                                "#2980B9",  # Blue
                                "#8E44AD",  # Purple
                                "#9B59B6",  # Violet
                                "#F39C12",  # Sunflower
                                "#D35400",  # Pumpkin
                                "#C0392B",  # Red
                                "#7F8C8D",  # Grey
                                "#2C3E50",  # Dark Blue (Midnight)
                                "#F2C9AC",  # Soft Peach
                                "#B03A2E",  # Brick Red
                                "#D5DBDB",  # Light Grey
                                "#1F618D",  # Denim Blue
                                "#E74C3C",  # Bright Red
                                "#9AE3D0",  # Light Turquoise
                                "#E0B0FF",  # Lavender
                                "#F1948A",  # Light Pink
                                "#A569BD",  # Purple (Lavender shade)
                                ]

        self.setup_ai_balls()
        self.setup_food()
        self.player_name = self.ask_for_name()
        self.display_name()


        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.bgcolor("white")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.listen()


        # Set up keyboard bindings
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")
        self.screen.onkey(self.move_up, "Up")
        self.screen.onkey(self.move_down, "Down")
        self.screen.onkey(self.move_left, "a")
        self.screen.onkey(self.move_right, "d")
        self.screen.onkey(self.move_up, "w")
        self.screen.onkey(self.move_down, "s")

        self.last_time = time.time()
        self.fps = 60  # Target 60 FPS
        self.frame_duration = 1 / self.fps  # 60 FPS = 1/60 seconds per frame
        self.screen.tracer(0)  # Disable auto update for smoother rendering
        self.score = 0


    def ask_for_name(self):
        """Prompt the user to enter their name."""
        player_name = turtle.textinput("Enter Your Name", "Please enter your name:")
        if player_name:
            return player_name
        return "Player"  # Default name if the input is empty
    def display_name(self):
        """Display the player's name at the top of the screen."""
        name_display = turtle.Turtle()
        name_display.hideturtle()
        name_display.penup()
        name_display.goto(0, SCREEN_Y_BOUNDARY - 40)
        name_display.write(f"Player: {self.player_name}", align="center", font=("Arial", 24, "normal"))
    
    def setup_ai_balls(self):
        for _ in range(100):
            self.spawn_new_ball()

    def spawn_new_ball(self):
        new_id = 0  # Initialize new_id outside of the loop
        center_size = 0  # The size of the region to avoid (200x200 area around (0, 0))
        random_color = random.choice(self.color_options)
        random_radius = random.randint(10, 10)
        # Generate random x avoiding dthe center area
        random_x = random.randint(-700, -center_size) if random.random() < 0.5 else random.randint(center_size, 700)
        # Generate random y avoiding the center area
        random_y = random.randint(-400, -center_size) if random.random() < 0.5 else random.randint(center_size, 400)
        ai_ball = AI(random_radius, random_x, random_y, random_color, new_id)
        self.ai_balls.append(ai_ball)
        new_id += 1  # Increment ID for each new AI ball
    

    def setup_food(self):
        for _ in range(150):
            self.spawn_new_food()

    def spawn_new_food(self):
        random_radius = random.randint(5, 5)  # Randomize food size
        random_x = random.randint(-700, 700)
        random_y = random.randint(-400, 400)
        food = Food(random_radius, random_x, random_y, "#27AE60")
        self.food_items.append(food)

    def move_left(self):
        self.ball.move_left()

    def move_right(self):
        self.ball.move_right()

    def move_up(self):
        self.ball.move_up()

    def move_down(self):
        self.ball.move_down()

    def random_move_balls(self):
        for ai_ball in self.ai_balls:
            ai_ball.random_move()


    def check_food_eaten(self):
        """Check if the ball has eaten any food."""
        for food in self.food_items:
            if not food.eaten:
                if self.ball.eat_food(food):
                    print(f"Food at {food.x}, {food.y} eaten!")
                    self.spawn_new_food()

    def check_ai_eaten(self):
        """Check if the ball has eaten any AI ball."""
        for ai_ball in self.ai_balls:
            if not ai_ball.eaten:
                if self.ball.eat_ai(ai_ball):
                    print(f"AI Ball at {ai_ball.x}, {ai_ball.y} eaten!")

    def check_collision_with_ai(self):
        """Check if the player ball has been eaten by an AI ball."""
        for ai_ball in self.ai_balls:
            if self.ball.eat_by_ai(ai_ball):
                self.game_over()
                return True
        return False
    def check_ai_eats_food(self):
        """Check if any AI ball has eaten food."""
        for ai_ball in self.ai_balls:
            for food in self.food_items:
                if not food.eaten:
                    if ai_ball.eat_food(food):
                        print(f"AI Ball {ai_ball.id} at ({ai_ball.x}, {ai_ball.y}) ate food!")
                        self.spawn_new_food()  # Spawn new food after one is eaten



    def game_loop(self):
        """Main game loop."""
        while True:
            current_time = time.time()
            if current_time - self.last_time > self.frame_duration:
                self.last_time = current_time
                self.random_move_balls()
                self.check_food_eaten()  # Check if player ball eats food
                self.check_ai_eaten()  # Check if AI balls eat each other

                # Check if any AI eats food
                self.check_ai_eats_food()

                # Check if AI balls eat each other
                for ai_ball in self.ai_balls:
                    if not ai_ball.eaten:
                        for other_ai_ball in self.ai_balls:
                            if ai_ball != other_ai_ball and not other_ai_ball.eaten:
                                ai_ball.eat_ai(other_ai_ball)  # Check AI eats AI

                self.screen.update()

            time.sleep(0.001)


# Create the game instance and start the game loop
game = Game()
game.game_loop()
