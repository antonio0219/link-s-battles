import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import player

windowWidth = 1200
windowHeight = 800

menu = True #si es True significa que estamos en el menu principal
modeSelector = False #si es un número positivo significa que estás eligiendo modo de juego, el nº indica cual vas a elegir
combat = False #si es True significa que estamos en combate
princess = 0 #para cambiar la postura de la princesa del menu
currentMoment = 0
finalMoment = 0
roundFinished = False
triforceWaiting = 0

#listas de jugadores
playersWaiting = []
playersFighting = []

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((windowWidth, windowHeight)) #pantalla modo no completa (para actualizar el juego)
#surface = pygame.display.set_mode((windowWidth, windowHeight), pygame.FULLSCREEN) #para modo pantalla completa
pygame.display.set_caption('Links\'s Battles')

#load images
startGame = pygame.image.load("assets/titleScreens/screen.png")
battleField = random.randint(1, 6)
if battleField == 1:
    battleField = pygame.image.load("assets/battlefields/room1.png")
elif battleField == 2:
    battleField = pygame.image.load("assets/battlefields/room2.png")
elif battleField == 3:
    battleField = pygame.image.load("assets/battlefields/room3.png")
elif battleField == 4:
    battleField = pygame.image.load("assets/battlefields/room4.png")
elif battleField == 5:
    battleField = pygame.image.load("assets/battlefields/room5.png")
elif battleField == 6:
    battleField = pygame.image.load("assets/battlefields/room6.png")

#música y sonidos
def menuMusic():
    pygame.mixer.music.load('assets/sounds/music/mainSong.ogg')
    pygame.mixer.music.play(-1)
def battleMusicFirstRound():
    pygame.mixer.music.load('assets/sounds/music/overworld.ogg')
    pygame.mixer.music.play(-1)
def battleMusicSecondRound():
    pygame.mixer.music.load('assets/sounds/music/dungeon.ogg')
    pygame.mixer.music.play(-1)
def battleMusicFinalRound():
    pygame.mixer.music.load('assets/sounds/music/finalBattle.ogg')
    pygame.mixer.music.play(-1)
def battleMusicWinner():
    pygame.mixer.music.load('assets/sounds/music/finalBattle.ogg')
    pygame.mixer.music.play(1)
    
def quitGame(): #para quitar el juego
    pygame.quit()
    sys.exit()
    
menuMusic()
while True:
    if menu:
        surface.blit(startGame, (173,0))
    elif modeSelector >= 0 and modeSelector <= 3: 
        if modeSelector == 0:
            selector = pygame.image.load("assets/titleScreens/selector0.png")
        elif modeSelector == 1:
            if princess == 0:
                selector = pygame.image.load("assets/titleScreens/selector1(0).png")
                princess = 2
            elif GAME_TIME.get_ticks() - currentMoment >= 500:
                if princess == 1:
                    selector = pygame.image.load("assets/titleScreens/selector1(0).png")
                    princess = 2
                    currentMoment = GAME_TIME.get_ticks()
                elif princess == 2:
                    selector = pygame.image.load("assets/titleScreens/selector1(1).png")
                    princess = 1
                    currentMoment = GAME_TIME.get_ticks()
        elif modeSelector == 2:
            if princess == 0:
                selector = pygame.image.load("assets/titleScreens/selector2(0).png")
                princess = 2
            elif GAME_TIME.get_ticks() - currentMoment >= 500:
                if princess == 1:
                    selector = pygame.image.load("assets/titleScreens/selector2(0).png")
                    princess = 2
                    currentMoment = GAME_TIME.get_ticks()
                elif princess == 2:
                    selector = pygame.image.load("assets/titleScreens/selector2(1).png")
                    princess = 1
                    currentMoment = GAME_TIME.get_ticks()
        elif modeSelector == 3:
            if princess == 0:
                selector = pygame.image.load("assets/titleScreens/selector3(0).png")
                princess = 2
            elif GAME_TIME.get_ticks() - currentMoment >= 500:
                if princess == 1:
                    selector = pygame.image.load("assets/titleScreens/selector3(0).png")
                    princess = 2
                    currentMoment = GAME_TIME.get_ticks()
                elif princess == 2:
                    selector = pygame.image.load("assets/titleScreens/selector3(1).png")
                    princess = 1
                    currentMoment = GAME_TIME.get_ticks()
        surface.blit(selector, (173,0))
    if combat:
        if roundFinished or triforceWaiting:
            surface.fill((0,0,0))
        else:
            surface.blit(battleField, (0,0))
        for idx, player in enumerate(playersFighting):
            player.atackMoment(GAME_TIME)
            player.drawLives(surface)
            player.move(GAME_TIME)
            player.drawSword(surface)
            player.drawPlayer(surface, GAME_TIME, roundFinished)
            if idx == 1: 
                otherPlayerIndex = 0
            else:
                otherPlayerIndex = 1
            player.receiveArrow(playersFighting[otherPlayerIndex])
            if player.imDead():
                roundFinished = True
                player.stop('True')
                if triforceWaiting == 0:
                    triforceWaiting = 1
            if roundFinished == True and player.imDead() == False:
                player.stop('True')
                if triforceWaiting == 1 and roundFinished:
                    finalMoment = GAME_TIME.get_ticks()
                    triforceWaiting = 2
                if GAME_TIME.get_ticks() - finalMoment >= 5000:
                    player.stop('False')
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if menu:
                if event.key == pygame.K_SPACE:#para salir del menu                                 
                    menu = False
                    modeSelector = 0
            if modeSelector >= 0 and modeSelector <= 4:
                if event.key == pygame.K_DOWN and modeSelector is not 3:
                    modeSelector += 1
                    princess = 0
                    currentMoment = GAME_TIME.get_ticks()
                if event.key == pygame.K_UP and modeSelector is not 0:
                    modeSelector -= 1
                    princess = 0
                    currentMoment = GAME_TIME.get_ticks()
                if event.key == pygame.K_RETURN and modeSelector == 1:
                    print('entrando en 2 player')
                    playersFighting.append(player.link(pygame, random, 150, 150))
                    playersFighting[0].setSpawn(0)
                    playersFighting.append(player.link(pygame, random, 950, 550))
                    playersFighting[1].setSpawn(1)
                    modeSelector = False
                    combat = True
                    pygame.mixer.music.fadeout(1000)
                    battleMusicFinalRound()
                    for player in playersFighting:
                        player.setInitTime(GAME_TIME)
                if event.key == pygame.K_RETURN and modeSelector == 2:
                    print('entrando en 4 player')
                if event.key == pygame.K_RETURN and modeSelector == 3:
                    print('entrando en 6 player')
                if event.key == pygame.K_RETURN and modeSelector == 4:
                    print('entrando en 8 player')
            if combat:
                #controles para player1
                if event.key == pygame.K_s:
                    playersFighting[0].move('downTrue')
                if event.key == pygame.K_a:
                    playersFighting[0].move('leftTrue')
                if event.key == pygame.K_d:
                    playersFighting[0].move('rightTrue')
                if event.key == pygame.K_e and playersFighting[0].getInventory():
                    playersFighting[0].selectItem('True', 1)
                if event.key == pygame.K_e and playersFighting[0].getInventory() == False:
                    playersFighting[0].weapon(surface, GAME_TIME)
                if event.key == pygame.K_w and playersFighting[0].getInventory():
                    playersFighting[0].selectItem('True', -1)
                if event.key == pygame.K_w and playersFighting[0].getInventory() == False:
                    playersFighting[0].move('upTrue')
                if event.key == pygame.K_LESS:
                    playersFighting[0].atack('True', GAME_TIME, playersFighting[1])
                if event.key == pygame.K_q:
                    playersFighting[0].selectItem('True')
                
                #controles para player2
                if event.key == pygame.K_k:
                    playersFighting[1].move('downTrue')
                if event.key == pygame.K_j:
                    playersFighting[1].move('leftTrue')
                if event.key == pygame.K_l:
                    playersFighting[1].move('rightTrue')
                if event.key == pygame.K_o and playersFighting[1].getInventory():
                    playersFighting[1].selectItem('True', 1)
                if event.key == pygame.K_o and playersFighting[1].getInventory() == False:
                    playersFighting[1].weapon(surface, GAME_TIME)
                if event.key == pygame.K_i and playersFighting[1].getInventory():
                    playersFighting[1].selectItem('True', -1)
                if event.key == pygame.K_i and playersFighting[1].getInventory() == False:
                    playersFighting[1].move('upTrue')
                if event.key == pygame.K_n:
                    playersFighting[1].atack('True', GAME_TIME, playersFighting[0])
                if event.key == pygame.K_u:
                    playersFighting[1].selectItem('True')
            if event.key == pygame.K_ESCAPE:#para quitar el juego
                quitGame()
        if event.type == pygame.KEYUP:
            if combat:
                if event.key == pygame.K_s:
                    playersFighting[0].move('downFalse')
                if event.key == pygame.K_a:
                    playersFighting[0].move('leftFalse')
                if event.key == pygame.K_d:
                    playersFighting[0].move('rightFalse')
                if event.key == pygame.K_w:
                    playersFighting[0].move('upFalse')
                if event.key == pygame.K_q:
                    playersFighting[0].selectItem('False')
                #controles para player2
                if event.key == pygame.K_k:
                    playersFighting[1].move('downFalse')
                if event.key == pygame.K_j:
                    playersFighting[1].move('leftFalse')
                if event.key == pygame.K_l:
                    playersFighting[1].move('rightFalse')
                if event.key == pygame.K_i:
                    playersFighting[1].move('upFalse')
                if event.key == pygame.K_u:
                    playersFighting[1].selectItem('False')
    clock.tick(60)
    pygame.display.update()