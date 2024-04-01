#imports
import pygame
from sys import exit
from player import Player
from general_combat_manager import GCM
from damage_calculator import Damage_calculator #just for test
import Map_manager 

#general setup
pygame.init()
FPS = pygame.time.Clock()
#creates the screen
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

#creates the other systems
player = Player()
gcm = GCM()
damage_calculator = Damage_calculator()
gcm.spawn_enemy()

face_images = {
    "1" : pygame.transform.scale(pygame.image.load("dice_images/1_face.png"),(100,100)),
    "2" : pygame.transform.scale(pygame.image.load("dice_images/2_face.png"),(100,100)),
    "3" : pygame.transform.scale(pygame.image.load("dice_images/3_face.png"),(100,100)),
    "4" : pygame.transform.scale(pygame.image.load("dice_images/4_face.png"),(100,100)),
    "5" : pygame.transform.scale(pygame.image.load("dice_images/5_face.png"),(100,100)),
    "6" : pygame.transform.scale(pygame.image.load("dice_images/6_face.png"),(100,100))
}

#DEBUG SHIT
dice = [[[1, "sock"],[2],[3,"hat"],[4],[5],[6]],[[1],[2],[3,"sock"],[4],[5],[6,"hat"]]]
damage = 0

#gameloop
while True:
    #sets fps to 60
    FPS.tick(60)
    #loops over all pygame events
    map_keys = []
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #if escape key is pressed exit the game
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)

            if event.key == pygame.K_SPACE:
                damage_calculator.calculate_damage(dice,0,0)

            if event.key == pygame.K_s:
                map_keys.append("s")

            if event.key == pygame.K_d:
                damage = damage_calculator.calculate_damage(dice,0,0)
                print(damage)
                gcm.damage(damage[0],player)

    Map_manager.map(map_keys)

    #updates everything
    player.update()

    if damage != 0:
        screen.blit(face_images[str(damage[1][0])],(100,100))
        screen.blit(face_images[str(damage[1][1])],(300,100))
        print(damage)

    #draws the screen
    pygame.display.flip()
    screen.fill((0,0,0))