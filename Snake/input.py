import pygame

class InputHandler:
    def __init__(self):
        pass

    def key_events(self, player_pos, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_pos.x += 300 * dt

        return player_pos
    
    