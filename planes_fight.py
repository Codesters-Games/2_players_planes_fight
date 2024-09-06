# Choose the background and disable all walls
stage.set_background("scrollingspace")
stage.disable_all_walls()

# Set up the sprites for both players
# Player 1's sprite (Dinoship) setup
p1_sprite = "https://i.ibb.co/4N3tSDH/Bevouliin-dino-spaceship-flying-game-character.png"
p1 = codesters.Sprite(p1_sprite, -220, 0)  # Position Dinoship on the left
p1.set_size(0.1)  # Set Dinoship size
p1.lives = 3  # Initialize Player 1's lives

# Player 2's sprite (Sharkship) setup
p2_sprite = "https://i.ibb.co/PTsxxr3/Bevouliin-smiling-spaceship-game-character.png"
p2 = codesters.Sprite(p2_sprite, 220, 0)  # Position Sharkship on the right
p2.set_size(0.1)  # Set Sharkship size
p2.flip_right_left()  # Flip Sharkship to face left
p2.lives = 3  # Initialize Player 2's lives

# Initialize firing status for both players
left_firing = False
right_firing = False

# Function to fire a laser for Player 1
def left_fire():
    global left_firing
    if left_firing is not True:  # Check if Player 1 is not already firing
        left_firing = True  # Set firing status to True
        # Create a blue laser shot from Player 1's position
        laser = codesters.TriangleIso(p1.get_x(), p1.get_y(), 5, 10, "blue")
        laser.turn_right(90)  # Turn the laser to the right
        laser.set_x_speed(10)  # Set laser speed moving right
        left_firing = False  # Reset firing status after firing

# Function to fire a laser for Player 2
def right_fire():
    global right_firing
    if right_firing is not True:  # Check if Player 2 is not already firing
        right_firing = True  # Set firing status to True
        # Create a yellow laser shot from Player 2's position
        laser = codesters.TriangleIso(p2.get_x(), p2.get_y(), 5, 10, "yellow")
        laser.turn_left(90)  # Turn the laser to the left
        laser.set_x_speed(-10)  # Set laser speed moving left
        right_firing = False  # Reset firing status after firing

# Controls for Player 1 (Dinoship)
def w_key():
    p1.move_up(10)  # Move Dinoship up
stage.event_key("w", w_key)  # Bind 'W' key to move up

def s_key():
    p1.move_down(10)  # Move Dinoship down
stage.event_key("s", s_key)  # Bind 'S' key to move down

# Firing control for Player 1
def d_key():
    left_fire()  # Fire laser
stage.event_key("d", d_key)  # Bind 'D' key to fire

# Controls for Player 2 (Sharkship)
def up_key():
    p2.move_up(10)  # Move Sharkship up
stage.event_key("up", up_key)  # Bind 'Up' arrow key to move up

def down_key():
    p2.move_down(10)  # Move Sharkship down
stage.event_key("down", down_key)  # Bind 'Down' arrow key to move down

# Firing control for Player 2
def left_key():
    right_fire()  # Fire laser
stage.event_key("left", left_key)  # Bind 'Left' arrow key to fire

# Collision detection for Player 1
def left_collision(sprite, hit_sprite):
    if hit_sprite.get_color() == "yellow":  # Check if hit by Player 2's laser
        p1.lives -= 1  # Decrease Player 1's lives
        stage.remove_sprite(hit_sprite)  # Remove the laser sprite

# Collision detection for Player 2
def right_collision(sprite, hit_sprite):
    if hit_sprite.get_color() == "blue":  # Check if hit by Player 1's laser
        p2.lives -= 1  # Decrease Player 2's lives
        stage.remove_sprite(hit_sprite)  # Remove the laser sprite

# Register collision events
p1.event_collision(left_collision)
p2.event_collision(right_collision)

# Main game loop to check game state and display winner
def game():
    # Display initial game instruction text
    display = codesters.Text("Destroy your opponent!!", 0, 220, "red")
    while p1.lives > 0 and p2.lives > 0:  # Continue the game while both players have lives
        stage.wait(0.0001)  # Wait briefly between each check
    # Check which player wins
    if p1.lives > 0:
        display.set_text("<<<<< Sharkship (Player1) wins!")  # Player 1 wins message
    else:
        display.set_text("Dinoship (Player 2) wins! >>>>>")  # Player 2 wins message
    display.go_to(0, 0)  # Move the message to the center
game()  # Start the game



