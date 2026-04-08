import pygame
from input import InputHandler
from render import RenderEngine


class Main:
    def __init__(self):
        pygame.init()
        self.screen = RenderEngine.startScreen()
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        pygame.draw.circle(self.screen, "red", self.player_pos, 25)
        pass


    def handleInputEvents(self, player_pos, dt):
        input_handler = InputHandler()
        player_pos = input_handler.key_events(player_pos, dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        return player_pos
    
    def update(self):
        InputHandler.key_events(self.player_pos, self.dt)
        
        return None
    
    def draw(self):
        RenderEngine.playScreen(self.screen)    
        return None

    def main(self, screen, clock):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
                    running = False
            dt = clock.tick(60) / 1000
        pygame.quit()

    if __name__ == "__main__":
        main()