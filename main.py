import pygame

import sys
from core.world import World
from core.config import Config

class LifeEngine:
    def __init__(self):
        pygame.init()
        self.config = Config()
        self.screen = pygame.display.set_mode((self.config.WINDOW_WIDTH, self.config.WINDOW_HEIGHT))
        pygame.display.set_caption("Life Engine")
        self.clock = pygame.time.Clock()
        self.world = World(self.config)
        self.running = True
        self.paused = False
        self.speed = 1.0  # Initial speed multiplier
        self.font = pygame.font.SysFont('Arial', 20)
        self.keys = pygame.key.get_pressed()  # Track key states

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r:
                    self.world.reset()
                elif event.key == pygame.K_q:
                    self.running = False
        
        # Check for held keys
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP]:
            self.speed = min(5.0, self.speed + 0.1)  # More gradual speed increase
        if self.keys[pygame.K_DOWN]:
            self.speed = max(0.1, self.speed - 0.1)  # More gradual speed decrease

    def update(self):
        if not self.paused:
            # Update multiple times based on speed
            for _ in range(int(self.speed)):
                self.world.update()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.world.render(self.screen)
        
        # Display speed and other info
        speed_text = self.font.render(f"Speed: {self.speed:.1f}x", True, (255, 255, 255))
        self.screen.blit(speed_text, (10, 10))
        
        if self.paused:
            pause_text = self.font.render("PAUSED", True, (255, 0, 0))
            self.screen.blit(pause_text, (10, 40))
        
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.config.FPS)  # Keep base FPS constant

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = LifeEngine()
    game.run() 