import os
import pygame
import sys

# Initialize Pygame
pygame.init()

# Define the absolute path to the sounds directory
sound_dir = '/Users/mohamedelhajsuliman/PycharmProjects/taxi game/assets/sounds'

# Debug: Print the full path for each sound file
print("Thrust sound path:", os.path.join(sound_dir, 'thrust.wav'))
print("Land sound path:", os.path.join(sound_dir, 'land.wav'))
print("Game Over sound path:", os.path.join(sound_dir, 'game_over.wav'))

# Load sound files using absolute paths
try:
    thrust_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'thrust.wav'))
    land_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'land.wav'))
    game_over_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'game_over.wav'))
    print("Sound files loaded successfully.")
except pygame.error as e:
    print(f"Failed to load sound files: {e}")
    sys.exit()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Taxi')

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

class Taxi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 255, 0))  # Yellow taxi
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.fuel = 100
        self.score = 0

    def update(self):
        self.acceleration = pygame.math.Vector2(0, 0.5)  # Gravity
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.fuel > 0:
            self.acceleration.y = -0.5  # Thrust up
            self.fuel -= 0.1
            thrust_sound.play()
        if keys[pygame.K_LEFT] and self.fuel > 0:
            self.acceleration.x = -0.1  # Thrust left
            self.fuel -= 0.05
            thrust_sound.play()
        if keys[pygame.K_RIGHT] and self.fuel > 0:
            self.acceleration.x = 0.1  # Thrust right
            self.fuel -= 0.05
            thrust_sound.play()

        # Update velocity and position
        self.velocity += self.acceleration
        self.rect.center += self.velocity

        # Keep taxi within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.x = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.velocity.x = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y = 0

        # Check if taxi falls off the screen
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.velocity.y = 0
            return False  # Indicate game over

        # Collision detection
        collisions = pygame.sprite.spritecollide(self, platforms, False)
        if collisions:
            for platform in collisions:
                if self.velocity.y > 0:  # Falling
                    self.rect.bottom = platform.rect.top
                    self.velocity.y = 0
                    self.score += 1  # Increase score when landing on a platform
                    self.fuel = 100  # Refuel when landing
                    land_sound.play()
                elif self.velocity.y < 0:  # Jumping
                    self.rect.top = platform.rect.bottom
                    self.velocity.y = 0
                elif self.velocity.x > 0:  # Moving right
                    self.rect.right = platform.rect.left
                    self.velocity.x = 0
                elif self.velocity.x < 0:  # Moving left
                    self.rect.left = platform.rect.right
                    self.velocity.x = 0
        return True  # Indicate the game is still running

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))  # Red platforms
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Create platforms
platforms = pygame.sprite.Group()
platforms.add(Platform(200, 500, 400, 20))
platforms.add(Platform(100, 300, 200, 20))

# Create a taxi instance
taxi = Taxi()

# Create a sprite group and add the taxi and other sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(taxi)
all_sprites.add(platforms)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    if not taxi.update():
        running = False

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Draw all sprites
    all_sprites.draw(screen)

    # Display the score and fuel level
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {taxi.score}', True, (255, 255, 255))
    fuel_text = font.render(f'Fuel: {taxi.fuel:.2f}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(fuel_text, (10, 50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)

# Play game over sound and wait for 3 seconds before displaying the message
print("Playing game over sound...")
game_over_sound.play()
pygame.time.wait(3000)

# Display Game Over message
screen.fill((0, 0, 0))
font = pygame.font.Font(None, 74)
game_over_text = font.render('Game Over', True, (255, 255, 255))
screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
pygame.display.flip()

# Wait for a few seconds before exiting
pygame.time.wait(3000)

pygame.quit()
sys.exit()
