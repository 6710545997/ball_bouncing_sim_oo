import random
import turtle
import math
import time

# Screen width and height
SCREEN_WIDTH = 1440  # Full screen width
SCREEN_HEIGHT = 900  # Full screen height
SCREEN_X_BOUNDARY = SCREEN_WIDTH // 2
SCREEN_Y_BOUNDARY = SCREEN_HEIGHT // 2

class Ball:
    def __init__(self, radius, x, y, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.speed = 4.5
        self.shape = turtle.Turtle()
        self.shape.speed("fastest")
        self.shape.penup()
        self.shape.goto(self.x, self.y - self.radius)  # Correct positioning
        self.shape.shape("circle")
        self.shape.shapesize(self.radius / 10)
        self.shape.color(self.color)
        self.earth = False
        self.id = id
        self.score = self.radius

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
            self.score += food.radius  # Increase score based on food radius
            if self.speed > 3.5:
                self.speed -= 0.15
            else:
                pass
            self.shape.shapesize(self.radius / 10)  # Update ball size

            return True
        return False

    def eat_BOT(self, other_BOT):
        """Allow one BOT to eat another if it is larger."""
        distance_to_BOT = self.distance(other_BOT)
        if distance_to_BOT < self.radius + other_BOT.radius:  # Collision detection
            if self.radius >= other_BOT.radius:  # Larger ball eats the smaller one
                other_BOT.shape.hideturtle()  # Hide the smaller ball
                other_BOT.eaten = True  # Mark it as eaten
                self.radius += other_BOT.radius / 3  # Grow the larger ball
                self.score += other_BOT.radius  # Increase score based on food radius
                self.shape.shapesize(self.radius / 10)  # Update the shape size
                print(f"BOT ball {self.id} at ({self.x:.2f}, {self.y:.2f}) ate BOT ball {other_BOT.id} at ({other_BOT.x:.2f}, {other_BOT.y:.2f})")
    
    def eat_by_BOT(self, BOT_ball):
        """Check if the player ball has been eaten by an BOT ball."""
        distance_to_BOT = self.distance(BOT_ball)
        if distance_to_BOT < self.radius + BOT_ball.radius and BOT_ball.radius > self.radius:
            self.shape.hideturtle()  # Hide player ball
            print(f"Player ball at {self.x:.2f}, {self.y:.2f} eaten by BOT ball!")
            return True
        return False

class BOT(Ball,):
    def __init__(self, radius, x, y, color,id, difficulty):
        super().__init__(radius, x, y, color)
        self.eaten = False
        self.direction = random.choice(["left", "right", "up", "down"])  # Initial random direction
        self.duration = random.uniform(0.5, 10)  # Random duration for the movement in seconds
        self.last_move_time = time.time()  # Store the last move time to track duration
        self.id = id
        self.score = radius
        self.difficulty = difficulty 

    def random_move(self):
        current_time = time.time()

        # Check if the BOT should change direction based on the duration
        if current_time - self.last_move_time > self.duration:
            # Change direction and reset duration
            self.direction = random.choice(["left", "right", "up", "down"])
            self.duration = random.uniform(1, 3.0)  # Randomize duration for the next movement
            self.last_move_time = current_time  # Update the last move time

        # Move the BOT ball in the current direction
         # Random speed 
        random_speed = random.uniform(0.1,self.difficulty)  # Use game difficulty

        if self.direction == "left":
            self.x -= random_speed
        elif self.direction == "right":
            self.x += random_speed
        elif self.direction == "up":
            self.y += random_speed
        elif self.direction == "down":
            self.y -= random_speed

        self.check_boundaries()  # Ensure BOT ball stays within screen
        self.update_position()
    def eat_food(self, food):
        """Check if the BOT eats a food item."""
        distance_to_food = self.distance(food)
        if distance_to_food < self.radius + food.radius:  # Collision detected
            food.shape.hideturtle()  # Hide the food item
            food.eaten = True  # Mark the food as eaten
            self.radius += 1  # Increase the BOT's ball size
            self.score += food.radius  # Increase score based on food radius
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
        self.BOT_balls = []
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
        
        # Initialize screen early in the constructor
        self.screen = turtle.Screen()
        self.screen.bgcolor(self.select_game_theme())
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

        random_player_color = random.choice(self.color_options)
        self.ball = Ball(10, 0, 0, random_player_color)
        self.difficulty = 0.7
        self.select_difficulty()
        self.setup_BOT_balls()
        self.setup_food()
        self.player_name = self.ask_for_name()
        self.display_name()

        food_color = self.food_color(self.screen.bgcolor())  
        self.display_leaderboard()
        # Initialize score_display here
        self.score_display = turtle.Turtle()
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(-SCREEN_X_BOUNDARY + 10, SCREEN_Y_BOUNDARY - 40)

        # Initialize rank_display
        self.rank_display = turtle.Turtle()
        self.rank_display.penup()
        self.rank_display.hideturtle()
        self.rank_display.goto(SCREEN_X_BOUNDARY - 150, SCREEN_Y_BOUNDARY - 100)
        self.update_score()


        # Set up keyboard bindings
        self.screen.listen()
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



    def ask_for_name(self):
        """Prompt the user to enter their name."""
        player_name = turtle.textinput("Enter Your Name", "Please enter your name:")
        if player_name:
            return player_name
        return "Player"  # Default name if the input is empty
    def display_name(self):
        """Display the player's name at the top center of the screen."""
        name_display = turtle.Turtle()
        name_display.hideturtle()
        name_display.penup()
        name_display.goto(0, SCREEN_Y_BOUNDARY - 40)  # Center at top
        name_display.write(f"Player: {self.player_name}", align="center", font=("Pacifico", 19, "normal"))

    def select_game_theme(self):
        # Prompt for theme selection
        game_theme = turtle.textinput("Select Game Theme","Theme: (Default, Space, Field):")

        if game_theme is None or game_theme == "" or game_theme == "Default":
            return "white"  # Default if input is empty or cancelled

        # If user types "Space", set background to black
        if game_theme == "Space":
            self.screen.bgcolor("black")  # Change background to black
            return "black"  # Return the theme name for further usage
        if game_theme == "Field":
            self.screen.bgcolor("green")
            return "green"
        return game_theme

    def select_difficulty(self):
        difficulty = turtle.textinput("Select Game Difficulty","Difficulty: (normal),(impossible)")
        if difficulty is None or difficulty == "" or difficulty == "normal":
            self.difficulty = 0.7  # Normal difficulty
        elif difficulty == "impossible":
            self.difficulty = 3.0  # Harder difficulty
        else:
            self.difficulty = float(difficulty)  # Allow custom numeric input for flexibility
        return self.difficulty
        
    def food_color(self, game_theme):
        food_color = "#27AE60"
        if game_theme == "black":
            food_color = "white"
        if game_theme == "green":
            food_color = food_color
        return food_color

    def display_leaderboard(self):
        header_display = turtle.Turtle()
        header_display.hideturtle()
        header_display.penup()
        header_display.goto(SCREEN_X_BOUNDARY - 20, SCREEN_Y_BOUNDARY - 40)  
        header_display.write("LEADERBOARD", align="right", font=("Pacifico", 16, "normal"))

    def update_score(self):
        # Clear the previous score display before updating
        self.score_display.clear()
        self.score_display.write(f"Score: {self.ball.score}", font=("Pacifico", 16, "normal"))

    def rank_score(self):
        # Sort BOT balls based on their score
        self.BOT_balls.sort(key=lambda BOT_ball: BOT_ball.score, reverse=True)

        # Clear previous ranking display
        self.rank_display.clear()

        # Display the top 5 BOT Balls ranking on the screen
        y_position = SCREEN_Y_BOUNDARY - 10

        for i, BOT_ball in enumerate(self.BOT_balls[:5]):
            self.rank_display.goto(SCREEN_X_BOUNDARY - 140, y_position - 45)
            self.rank_display.write(f"{i + 1}. Ball {BOT_ball.id:.0f}: Score {BOT_ball.score:.0f}", font=("Pacifico", 14, "normal"))
            y_position -= 20  # Distance between ranked


    
    def setup_BOT_balls(self):
        new_id = 0 
        for _ in range(50): #number of bot_ball that you want to generate
            self.spawn_new_ball(new_id)
            new_id +=1
            BOT.id = new_id
            print(new_id)
            
        

    def spawn_new_ball(self,new_id):
        center_size = 100  # The size of the region to avoid (200x200 area around (0, 0)
        random_color = random.choice(self.color_options)
        random_radius = random.randint(6, 25) #size of bot_ball
        # Generate random x avoiding dthe center area
        random_x = random.randint(-SCREEN_X_BOUNDARY, -center_size) if random.random() < 0.5 else random.randint(center_size, SCREEN_X_BOUNDARY)
        # Generate random y avoiding the center area
        random_y = random.randint(-SCREEN_Y_BOUNDARY, -center_size) if random.random() < 0.5 else random.randint(center_size, SCREEN_Y_BOUNDARY)
        BOT_ball = BOT(random_radius, random_x, random_y, random_color,new_id,self.difficulty)
        self.BOT_balls.append(BOT_ball)
        # Collect the radius of all balls and return them
        return [ball.radius for ball in self.BOT_balls]
        

    def setup_food(self):#create food to map
        for _ in range(125): #number of food
            self.spawn_new_food()


    def spawn_new_food(self):
        food_color = self.food_color(self.screen.bgcolor())
        random_radius = random.randint(5, 5)  # Randomize food size
        random_x = random.randint(-SCREEN_X_BOUNDARY, SCREEN_X_BOUNDARY)
        random_y = random.randint(-SCREEN_Y_BOUNDARY, SCREEN_Y_BOUNDARY)
        food = Food(random_radius, random_x, random_y, food_color)
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
        for BOT_ball in self.BOT_balls:
            BOT_ball.random_move()



    def game_over(self):
        """Display full game over screen and hide game screen."""
        # Clear the screen and display the game over message
        self.screen.clear()
        self.screen.bgcolor("black")  # Set background to black
        game_over_display = turtle.Turtle()
        game_over_display.color("white")
        game_over_display.penup()
        game_over_display.goto(0, 0)
        game_over_display.write("GAME OVER\nPress 'Q' to EXIT GAME", align="center", font=("Arial", 24, "bold"))
        game_over_display.hideturtle()
        time.sleep(20)
        if self.screen.onkey(self.quit_game, "q"):
            self.screen.bye()


        # Wait a bit before closing the screen or restarting
        
          # Close the game window after displaying the message
        
    def check_food_eaten(self):
        """Check if the ball has eaten any food."""
        for food in self.food_items:
            if not food.eaten:
                if self.ball.eat_food(food):
                    print(f"Food at {food.x:.2f}, {food.y:.2f} eaten!")
                    self.spawn_new_food()
                    self.update_score()

    def check_BOT_eaten(self):
        """Check if the ball has eaten any BOT ball."""
        for BOT_ball in self.BOT_balls:
            if not BOT_ball.eaten:
                if self.ball.eat_BOT(BOT_ball):
                    print(f"BOT Ball at {BOT_ball.x:.2f}, {BOT_ball.y:.2f} eaten!")
                    self.spawn_new_food()
                    self.update_score()

    def check_collision_with_BOT(self):
        """Check if the player ball has been eaten by an BOT ball."""
        for BOT_ball in self.BOT_balls:
            if self.ball.eat_by_BOT(BOT_ball):
                self.game_over()
                return True
        return False
    
    def check_BOT_eats_food(self):
        """Check if any BOT ball has eaten food."""
        for BOT_ball in self.BOT_balls:
            for food in self.food_items:
                if not food.eaten:
                    if BOT_ball.eat_food(food):
                        print(f"BOT Ball {BOT_ball.id} at ({BOT_ball.x}, {BOT_ball.y}) ate food!")
                        self.spawn_new_food()
                        self.update_score()

    def check_BOT_eats_BOT(self):
        # Check if BOT balls eat each other
        for BOT_ball in self.BOT_balls:
            if not BOT_ball.eaten:
                for other_BOT_ball in self.BOT_balls:
                    if BOT_ball != other_BOT_ball and not other_BOT_ball.eaten:
                        BOT_ball.eat_BOT(other_BOT_ball)  # Check BOT eats BOT
                        self.update_score()

                
    def game_loop(self):
        """game loop."""
        while True:
            current_time = time.time()
            if current_time - self.last_time > self.frame_duration:
                self.last_time = current_time
                self.random_move_balls()
                self.check_food_eaten()  # Check if player ball eats food
                self.check_BOT_eaten()  # Check if BOT balls eat each other
                self.check_BOT_eats_food() # Check if any BOT eats food
                self.check_BOT_eats_BOT() #self.check_collision_with_BOT()
                self.check_collision_with_BOT()
                self.rank_score()
                self.update_score()
                print(len(self.food_items))
              
   


                self.screen.update()

            time.sleep(0.001)


# Create the game instance and start the game loop
game = Game()
game.game_loop()
