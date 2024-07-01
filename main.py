import os
import pygame
import sys

# Initialize Pygame
pygame.init()

# Define the absolute path to the sounds directory
sound_dir = '/Users/mohamedelhajsuliman/PycharmProjects/taxi game/assets/sounds'

# Load sound files using absolute paths
try:
    thrust_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'thrust.wav'))
    land_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'land.wav'))
    game_over_sound = pygame.mixer.Sound(os.path.join(sound_dir, 'game_over.wav'))
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
        self.velocity = pygame.math.Vector2(0, 5)  # Initial downward velocity
        self.direction = 1  # 1 for down, -1 for up
        self.score = 0

    def update(self):
        # Change direction when hitting top or bottom of the screen
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.direction *= -1

        # Move up or down at a constant speed
        self.velocity.y = 5 * self.direction if self.direction == 1 else 2 * self.direction
        self.rect.y += self.velocity.y

        # Check if taxi falls below the screen
        if self.rect.top > screen_height:
            return False  # Indicate game over

        # Collision detection
        collisions = pygame.sprite.spritecollide(self, platforms, False)
        if collisions:
            for platform in collisions:
                if self.velocity.y > 0 and self.rect.bottom <= platform.rect.top + 5:  # Falling and touching the top of the platform
                    self.rect.bottom = platform.rect.top
                    self.direction = -1  # Change direction to up
                    self.score += 1  # Increase score when landing on a platform
                    land_sound.play()
                elif self.velocity.y < 0 and self.rect.top >= platform.rect.bottom - 5:  # Jumping and touching the bottom of the platform
                    self.rect.top = platform.rect.bottom
                    self.direction = 1  # Change direction to down
                    self.score += 1  # Increase score when hitting the bottom of a platform
                    land_sound.play()
        return True  # Indicate the game is still running

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))  # Red platform
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Keep platform within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

# Create platforms
platforms = pygame.sprite.Group()
platform = Platform(300, 500, 200, 20)
platforms.add(platform)

# Create a taxi instance
taxi = Taxi()

# Create a sprite group and add the taxi and other sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(taxi)
all_sprites.add(platforms)

# Main game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Update all sprites
        if not taxi.update():
            game_over = True

        platforms.update()  # Update platform movement

        # Check if the taxi falls below the platform
        if taxi.rect.top > platform.rect.bottom:
            game_over = True

        # Fill the screen with black color
        screen.fill((0, 0, 0))

        # Draw all sprites
        all_sprites.draw(screen)

        # Display the score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {taxi.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        clock.tick(60)

    else:
        # Play game over sound and wait for a second before displaying the message
        game_over_sound.play()
        pygame.time.wait(1000)

        # Display Game Over message
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        game_over_text = font.render('Game Over', True, (255, 255, 255))
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()

        # Wait for a second before exiting
        pygame.time.wait(1000)
        running = False

pygame.quit()
sys.exit()
