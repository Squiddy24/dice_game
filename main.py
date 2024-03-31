#imports
import pygame
from sys import exit
from player import Player
from general_combat_manager import GCM
from damage_calculator import Damage_calculator #just for test
#general setup
pygame.init()
FPS = pygame.time.Clock()

#creates the screen
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

#creates the other systems
player = Player()
gcm = GCM()
damage_calculator = Damage_calculator()

#test to make sure github works (DONT FORGET TO NAME COMMIT OF EVERYTHING BREAKS)
#DEBUG SHIT
dice = [[[1, "imbue"],[2],[3,"imbue"],[4],[5],[6]],[[1],[2],[3,"imbue"],[4],[5],[6,"imbue"]]]

#gameloop
while True:
    #sets fps to 60
    FPS.tick(60)

    #loops over all pygame events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #if escape key is pressed exit the game
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)
            if event.key == pygame.K_SPACE:
                damage_calculator.calculate_damage(dice,0)

    #updates everything
    player.update()
    gcm.update()

    #draws the screen
    pygame.display.flip()
    screen.fill((0,0,0))