import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = 0.5
        self.radius = 20  # Define the radius of the ball
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
    
    def jump(self):
        self.velocity = -10
    
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        # Ensure the ball does not fall below the ground
        if self.y >= 550:
            self.y = 550
            self.velocity = 0
        # Update the rect position based on the new ball position
        self.rect.topleft = (self.x - self.radius, self.y - self.radius)
    
    def draw(self, window):
        pygame.draw.circle(window, (255, 0, 0), (int(self.x), int(self.y)), self.radius)
