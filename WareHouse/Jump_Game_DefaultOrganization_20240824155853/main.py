import pygame
from ball import Ball

def main():
    pygame.init()
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Falling Ball Game")
    clock = pygame.time.Clock()
    ball = Ball(window_width // 2, 50)
    score = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if ball.rect.collidepoint(mouse_x, mouse_y):
                    ball.jump()
                    score += 1
        
        ball.update()
        
        # Reset score when the ball touches the ground
        if ball.y == 550:
            score = 0
        
        window.fill((255, 255, 255))
        ball.draw(window)
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        window.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
