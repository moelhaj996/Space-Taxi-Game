import unittest
import pygame
from main import Taxi, Platform

class TestGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def test_taxi_initial_position(self):
        taxi = Taxi()
        self.assertEqual(taxi.rect.center, (self.screen_width // 2, self.screen_height // 2))

    def test_taxi_update(self):
        taxi = Taxi()
        initial_y = taxi.rect.y
        taxi.update()
        self.assertNotEqual(taxi.rect.y, initial_y)

    def test_platform_initial_position(self):
        platform = Platform(300, 500, 200, 20)
        self.assertEqual(platform.rect.topleft, (300, 500))

    def test_platform_update(self):
        platform = Platform(300, 500, 200, 20)
        initial_x = platform.rect.x
        keys = pygame.key.get_pressed()
        platform.update()
        if keys[pygame.K_LEFT]:
            self.assertEqual(platform.rect.x, initial_x - 5)
        elif keys[pygame.K_RIGHT]:
            self.assertEqual(platform.rect.x, initial_x + 5)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
