

#stupid part, but necessary
#draw background, all vizual effects, etc
""" Draw the current state of the game to the screen.
This involves rendering backgrounds, sprites, UI elements, and any visual effects.
This is where you would typically call render() methods on game objects. """

import pygame
pygame.init()

class RenderEngine:
    def __init__(self, screen):
        self.screen = screen
        self.custom_font = pygame.font.Font("myfont.ttf")

    def startScreen(self, screen):
        screen = pygame.display.set_mode((1280, 720))
        screen.fill("green")
        screen.draw.text("Snake Attack", (50, 30), 
                         color="black", 
                         fontsize=48, 
                         fontname = self.custom_font, 
                         center = True
                         )
        pygame.display.flip()
        return screen

    def playScreen(self, screen):
        screen.fill("black")
        return screen
    
    def gameOverScreen(self, screen):
        screen.fill("black")

        return screen 
    def pauseScreen(self, screen):
        screen.fill("gray")
        return screen
    
    def playerHUD(self, screen):
        
        return screen
    
    