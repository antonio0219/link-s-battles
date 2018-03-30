class link():
    def __init__(self, pygame, random, x, y):
        self.x = x
        self.y = y
        self.height = 100
        self.width = 100
        self.swordHeight = 44
        self.swordWidth = 100
        self.health = 10 #diez vidas son 5 corazones completos
        self.maxHearts = 5 #estos son los corazones maximos que se pueden tener
        self.posHearts = [(100, 25), (800, 750)] #una lista con las posiciones x e y de los corazones dependiendo del spawn que te haya tocado
        self.arrowPos = [self.x, self.y] #lista con las posiciones x e y de la flecha
        self.arrowDirection = 'Right'
        self.existArrow = False
        self.spaceHearts = 40 #esta variable indica el espacio que se va a guardar entre la posición en X de un corazón y la posX del siguiente
        self.color = random.randint(1,3) #esta variable puede ser green(1), red(2) o white(3), de esto dependerá que el jugador tenga un color u otro
        self.costume = pygame.image.load("assets/player/green/linkWalkingDown1.png")
        self.direction = 'right' #para saber la direccion a la que mira el jugador
        self.costumeTime = False
        self.spawn = False
        self.itemSelected = 0 #con esta variable se sabe que arma está seleccionada
        self.inventory = 'False' #con esta variable se sabe si el inventario está abierto
        self.numBottles = 3 #indica el número de pociones que tendrá cada jugador al prinicipio
        self.numPotions = self.numBottles #indica el número de pociones que tiene el jugador (botellas rellenas)
        self.rupies = 10 #indica las rupias que tienes
        self.sword = {'right':(( self.width - int((self.width/16) * 5), int((self.height/16) * 6) ),(self.swordWidth,self.swordHeight)),
                      'left': ((int((self.width/16) * 5) - self.swordWidth, int((self.height/16) * 6)),(self.swordWidth,self.swordHeight)),
                      'down': (( int((self.width/16) * 5) , self.height - int((self.height/16) * 5) ),(self.swordHeight,self.swordWidth)),
                      'up': (( int((self.width/16) * 3) , self.height - int((self.height/16) * 28)),(self.swordHeight,self.swordWidth))}
                        #con este diccionario de tupples se almacena las posiciones x e y de el punto de la esquina donde se dibuja la
                        #espada y la anchura y la altura de esta, todo dependiendo de la dirección a la que apunte
        self.potion = pygame.image.load("assets/items/potion.png")
        self.emptyBottle = pygame.image.load("assets/items/emptyBottle.png")
        
        self.fullLive = pygame.image.load("assets/items/fullLive.png")
        self.live = pygame.image.load("assets/items/Live.png")
        self.noLive = pygame.image.load("assets/items/noLive.png")
        
        self.toLeft = False
        self.toRight = False
        self.toUp = False
        self.toDown = False
        self.toAtack = False
        self.moving = True #esta variable indicará cuando el jugador puede moverse y cuando no
        
        #sounds
        self.swordBlow = pygame.mixer.Sound('assets/sounds/player/swordBlow.ogg') #sonido para el golpe de espada
        self.playerHurt = pygame.mixer.Sound('assets/sounds/player/playerHurt.ogg') #sonido para cuando te hacen daño
        self.shieldDeflecting = pygame.mixer.Sound('assets/sounds/player/shieldDeflecting.ogg') #sonido para cuando te cubres con el escudo
        
        #abajo se importan las imagenes correspondientes dependiendo del color que haya tocado
        if self.color == 1:
            self.image_up = [pygame.image.load("assets/player/green/linkWalkingUp.png")]
            self.image_down = [pygame.image.load("assets/player/green/linkWalkingDown1.png"),pygame.image.load("assets/player/green/linkWalkingDown2.png")]
            self.image_left = [pygame.image.load("assets/player/green/linkWalkingLeft1.png"), pygame.image.load("assets/player/green/linkWalkingLeft2.png")]
            self.image_right = [pygame.image.load("assets/player/green/linkWalkingRight1.png"), pygame.image.load("assets/player/green/linkWalkingRight2.png")]
            self.atRight = pygame.image.load("assets/player/green/linkRightAt.png")
            self.atLeft = pygame.image.load("assets/player/green/linkLeftAt.png")
            self.atDown = pygame.image.load("assets/player/green/linkDownAt.png")
            self.atUp = pygame.image.load("assets/player/green/linkUpAt.png")
            self.lastImage = pygame.image.load("assets/player/green/linkWalkingDown1.png")
            #armas:
            self.swordImageRight = pygame.image.load("assets/player/green/swordRight.png")
            self.swordImageLeft = pygame.image.load("assets/player/green/swordLeft.png")
            self.swordImageDown = pygame.image.load("assets/player/green/swordDown.png")
            self.swordImageUp = pygame.image.load("assets/player/green/swordUp.png")
            self.arrow = [pygame.image.load("assets/player/green/arrowRight.png"), pygame.image.load("assets/player/green/arrowLeft.png"), pygame.image.load("assets/player/green/arrowUp.png"), pygame.image.load("assets/player/green/arrowDown.png")]
        if self.color == 2:
            self.image_up = [pygame.image.load("assets/player/red/linkWalkingUp.png")]
            self.image_down = [pygame.image.load("assets/player/red/linkWalkingDown1.png"),pygame.image.load("assets/player/red/linkWalkingDown2.png")]
            self.image_left = [pygame.image.load("assets/player/red/linkWalkingLeft1.png"), pygame.image.load("assets/player/red/linkWalkingLeft2.png")]
            self.image_right = [pygame.image.load("assets/player/red/linkWalkingRight1.png"), pygame.image.load("assets/player/red/linkWalkingRight2.png")]
            self.atRight = pygame.image.load("assets/player/red/linkRightAt.png")
            self.atLeft = pygame.image.load("assets/player/red/linkLeftAt.png")
            self.atDown = pygame.image.load("assets/player/red/linkDownAt.png")
            self.atUp = pygame.image.load("assets/player/red/linkUpAt.png")
            self.lastImage = pygame.image.load("assets/player/red/linkWalkingDown1.png")
            #armas:
            self.swordImageRight = pygame.image.load("assets/player/red/swordRight.png")
            self.swordImageLeft = pygame.image.load("assets/player/red/swordLeft.png")
            self.swordImageDown = pygame.image.load("assets/player/red/swordDown.png")
            self.swordImageUp = pygame.image.load("assets/player/red/swordUp.png")
            self.arrow = [pygame.image.load("assets/player/red/arrowRight.png"), pygame.image.load("assets/player/red/arrowLeft.png"), pygame.image.load("assets/player/red/arrowUp.png"), pygame.image.load("assets/player/red/arrowDown.png")]
        if self.color == 3:
            self.image_up = [pygame.image.load("assets/player/white/linkWalkingUp.png")]
            self.image_down = [pygame.image.load("assets/player/white/linkWalkingDown1.png"),pygame.image.load("assets/player/white/linkWalkingDown2.png")]
            self.image_left = [pygame.image.load("assets/player/white/linkWalkingLeft1.png"), pygame.image.load("assets/player/white/linkWalkingLeft2.png")]
            self.image_right = [pygame.image.load("assets/player/white/linkWalkingRight1.png"), pygame.image.load("assets/player/white/linkWalkingRight2.png")]
            self.atRight = pygame.image.load("assets/player/white/linkRightAt.png")
            self.atLeft = pygame.image.load("assets/player/white/linkLeftAt.png")
            self.atDown = pygame.image.load("assets/player/white/linkDownAt.png")
            self.atUp = pygame.image.load("assets/player/white/linkUpAt.png")
            self.lastImage = pygame.image.load("assets/player/white/linkWalkingDown1.png")
            #armas:
            self.swordImageRight = pygame.image.load("assets/player/white/swordRight.png")
            self.swordImageLeft = pygame.image.load("assets/player/white/swordLeft.png")
            self.swordImageDown = pygame.image.load("assets/player/white/swordDown.png")
            self.swordImageUp = pygame.image.load("assets/player/white/swordUp.png")
            self.arrow = [pygame.image.load("assets/player/white/arrowRight.png"), pygame.image.load("assets/player/white/arrowLeft.png"), pygame.image.load("assets/player/white/arrowUp.png"), pygame.image.load("assets/player/white/arrowDown.png")]
        #items:
        self.items = [pygame.image.load("assets/player/itemSelector/itemSelector0.png"),pygame.image.load("assets/player/itemSelector/itemSelector1.png"),pygame.image.load("assets/player/itemSelector/itemSelector2.png"),pygame.image.load("assets/player/itemSelector/itemSelector3.png"),pygame.image.load("assets/player/itemSelector/itemSelector4.png")]
        
        self.initTime = 0
        self.atackTime = 0
        self.step = 0
    
    def setInitTime(self, GAME_TIME): #con esta función se almacena el instante justo cuando se crea un objeto jugador
        self.initTime = GAME_TIME.get_ticks()
    def selectItem(self, item, nextlast = 0):
        if self.moving:
            self.inventory = item
            if nextlast == -1 and self.itemSelected > 0:
                self.itemSelected -= 1
            if nextlast == 1 and self.itemSelected < 4:
                self.itemSelected += 1
    def getInventory(self):
        if self.inventory == 'True':
            return True
        if self.inventory == 'False':
            return False
    def stop(self, i):
        if i == 'False':
            self.moving = True
        elif i == 'True':
            self.moving = False
    def move(self, direction):
        #aquí se cambian las variables para detectar si quieres moverte
        if direction == 'upTrue':
            self.toUp = True
            self.direction == 'up'
        if direction == 'downTrue':
            self.toDown = True
            self.direction == 'down' 
        if direction == 'rightTrue':
            self.toRight = True
            self.direction == 'right'
        if direction == 'leftTrue':
            self.toLeft = True
            self.direction == 'left'
        if direction == 'upFalse':
            self.toUp = False
        if direction == 'downFalse':
            self.toDown = False
        if direction == 'rightFalse':
            self.toRight = False
        if direction == 'leftFalse':
            self.toLeft = False
        #aquí se interpretan dichas variables para mover al objeto
        if self.toAtack == False and self.inventory == 'False' and self.moving == True:
            if self.toUp == True and self.y >= (160 - self.height):
                self.y -= 20
            if self.toDown == True and self.y <= (665 - self.height):
                self.y += 20
            if self.toLeft == True and self.x >= 120:
                self.x -= 20
            if self.toRight == True and self.x <= (1085 - self.width):
                self.x += 20
        if self.existArrow:
            if self.arrowDirection == 'right' and self.arrowPos[0] < 1200:
                self.arrowPos[0] += 60
            elif self.arrowDirection == 'left' and self.arrowPos[0] > 0:
                self.arrowPos[0] -= 60
            elif self.arrowDirection == 'down' and self.arrowPos[1] < 800:
                self.arrowPos[1] += 60
            elif self.arrowDirection == 'up' and self.arrowPos[1] > 0:
                self.arrowPos[1] -= 60
            else:
                self.existArrow = False
        if self.lastImage == self.image_right[self.step]:
            self.direction = 'right'
        if self.lastImage == self.image_up[0]:
            self.direction = 'up'
        if self.lastImage == self.image_down[self.step]:
            self.direction = 'down'
        if self.lastImage == self.image_left[self.step]:
            self.direction = 'left'
    def atackMoment(self, GAME_TIME): #con esta función se almacena el instante en el que el jugador empezó su ataque
        if GAME_TIME.get_ticks() - self.atackTime > 500:
                self.toAtack = False
                self.atackTime = 0
    def atack(self, at, GAME_TIME, otherPlayer): #esta función sirve para que podamos cambiar la variable toAtack desde fuera de la clase
        if at == 'True' and self.toAtack == False and self.inventory == 'False':
            otherPlayer.receiveDamage(self.direction, ((self.sword[self.direction][0][0]+self.x,self.sword[self.direction][0][1]+self.y),(self.sword[self.direction][1])))
            self.toAtack = True
            self.swordBlow.play() #para tocar el sonido de la espada cuando toAtack se pone a True
            self.atackTime = GAME_TIME.get_ticks()
    def setSpawn(self, spawn):
        self.spawn = spawn
    def inside(self,sq1, sq2):
        return ((sq1[0][0] + sq1[1][0]) > sq2[0][0]) and (sq1[0][0] < (sq2[0][0] + sq2[1][0])) and ((sq1[0][1] + sq1[1][1]) > sq2[0][1]) and (sq1[0][1] < (sq2[0][1] + sq2[1][1]))
    def receiveDamage(self, dir, pos):
        if dir == 'right':
            if self.inside(pos, ((self.x, self.y),(self.width, self.height))):
                if self.direction == 'left' and self.toAtack == False:
                    self.shieldDeflecting.play()
                else:
                    self.modifyLive(-2)
        if dir == 'left':
            if self.inside(pos, ((self.x, self.y),(self.width, self.height))):
                if self.direction == 'right' and self.toAtack == False:
                    self.shieldDeflecting.play()
                else:
                    self.modifyLive(-2)
        if dir == 'up':
            if self.inside(pos, ((self.x, self.y),(self.width, self.height))):
                if self.direction == 'down' and self.toAtack == False:
                    self.shieldDeflecting.play()
                else:
                    self.modifyLive(-2)
        if dir == 'down':
            if self.inside(pos, ((self.x, self.y),(self.width, self.height))):
                if self.direction == 'up' and self.toAtack == False:
                    self.shieldDeflecting.play()
                else:
                    self.modifyLive(-2)
    def modifyLive(self, num): #a esta función se le debe pasar como argumento el número de corazones que vas a perder
        if num is 'Full':
            self.health = (self.maxHearts * 2)
        else:
            self.health += num
            if self.health > 0:
                self.playerHurt.play()
            else:
                self.health = 0
    def imDead(self):
        if self.health <= 0:
            return True
        else:
            return False
    def drawLives(self, surface): #con esta función se dibujarán las vidas
        numberFullHearts = self.health//2 #si pones dos / haces una división que no coja decimales (se queda con un resto
        numberHalfHearts = self.health%2 #si pones % puedes pedir el resto de una división
        numberEmptyHearts = self.maxHearts - numberFullHearts - numberHalfHearts
        posx = self.posHearts[self.spawn][0]
        posy = self.posHearts[self.spawn][1]
        for i in range(numberFullHearts):
            surface.blit(self.fullLive, (posx, posy))
            posx += self.spaceHearts
        if numberHalfHearts == 1:
            surface.blit(self.live, (posx, posy))
            posx += self.spaceHearts
        for i in range(numberEmptyHearts):
            surface.blit(self.noLive, (posx, posy))
            posx += self.spaceHearts
        for i in range(self.numPotions): #para dibujar las botellas
            surface.blit(self.potion, (posx, posy))
            posx += self.spaceHearts
        for i in range(self.numBottles - self.numPotions): #para dibujar las botellas
            surface.blit(self.emptyBottle, (posx, posy))
            posx += self.spaceHearts
    def weapon(self, surface):
        #arco
        if self.itemSelected == 1:
            if self.existArrow == False:
                if self.direction == 'right':
                    self.arrowPos = [self.x + 10, (self.y + 10 + self.height / 2 - 25)]
                    self.existArrow = True
                if self.direction == 'left':
                    self.arrowPos = [self.x + 10, (self.y + self.height / 2 - 25)]
                    self.existArrow = True
                if self.direction == 'up':
                    self.arrowPos = [(self.x + self.width / 2 - 10), self.y]
                    self.existArrow = True
                if self.direction == 'down':
                    self.arrowPos = [(self.x + self.width / 2 - 10), self.y]
                    self.existArrow = True
                self.arrowDirection = self.direction
        #boomerang
        if self.itemSelected == 2:
            print('boomerang 7u7')
        #bomba
        if self.itemSelected == 3:
            print('bomb 7u7')
        #poción de vida
        if self.itemSelected == 4 and self.health >= ((self.maxHearts * 2) - 2) and self.health < (self.maxHearts * 2):
            if self.health == ((self.maxHearts * 2) - 2):
                self.health += 2
            elif self.health == ((self.maxHearts * 2) - 1):
                self.health += 1
            self.numPotions -= 1
        elif self.itemSelected == 4 and self.health < (self.maxHearts * 2):
            self.health += 4
            self.numPotions -= 1
    def drawSword(self, surface):
        if self.toAtack == True and self.direction == 'right' and self.inventory == 'False' and self.moving or self.moving == False and self.direction == 'right' and self.imDead() == False: #si está mirando a la derecha
            self.swordY = self.y + int((self.height/16) * 6)
            self.swordX = (self.x + self.width) - int((self.width/16) * 5)
            surface.blit(self.swordImageRight, (self.swordX, self.swordY))
        if self.toAtack == True and self.direction == 'left' and self.inventory == 'False' and self.moving or self.moving == False and self.direction == 'left' and self.imDead() == False: #si está mirando a la izquierda
            self.swordY = self.y + int((self.height/16) * 6)
            self.swordX = (self.x - self.width) - int((self.width/16) * -5)
            surface.blit(self.swordImageLeft, (self.swordX, self.swordY))
        if self.toAtack == True and self.direction == 'down' and self.inventory == 'False' and self.moving or self.moving == False and self.direction == 'down' and self.imDead() == False: #si está mirando a abajo
            self.swordY = self.y + self.height - int((self.height/16) * 5)
            self.swordX = self.x + int((self.width/16) * 5)
            surface.blit(self.swordImageDown, (self.swordX, self.swordY))
        if self.toAtack == True and self.direction == 'up' and self.inventory == 'False' and self.moving or self.moving == False and self.direction == 'up' and self.imDead() == False: #si está mirando arriba 
            self.swordY = self.y + self.height - int((self.height/16) * 28)
            self.swordX = self.x + int((self.width/16) * 3)
            surface.blit(self.swordImageUp, (self.swordX, self.swordY))
    def drawPlayer(self, surface, GAME_TIME, roundFinished):
        if self.inventory == 'True':
            surface.blit(self.items[self.itemSelected], (self.x, self.y - 30))
        if self.existArrow:
            if self.arrowDirection == 'right':
                surface.blit(self.arrow[0], (self.arrowPos[0], self.arrowPos[1]))
            if self.arrowDirection == 'left':
                surface.blit(self.arrow[1], (self.arrowPos[0], self.arrowPos[1]))
            if self.arrowDirection == 'up':
                surface.blit(self.arrow[2], (self.arrowPos[0], self.arrowPos[1]))
            if self.arrowDirection == 'down':
                surface.blit(self.arrow[3], (self.arrowPos[0], self.arrowPos[1]))
        if self.toAtack == False and self.inventory == 'False'and self.moving:
            if GAME_TIME.get_ticks() - self.initTime > 200:
                if self.step == 0:
                    self.step = 1
                else:
                    self.step=0
                self.initTime = GAME_TIME.get_ticks()
            if self.toUp:
                surface.blit(self.image_up[0], (self.x, self.y))
                self.lastImage = self.image_up[0]
            elif self.toDown:
                surface.blit(self.image_down[self.step], (self.x, self.y))
                self.lastImage = self.image_down[self.step]
            elif self.toLeft:
                surface.blit(self.image_left[self.step], (self.x, self.y))
                self.lastImage = self.image_left[self.step]
            elif self.toRight:
                surface.blit(self.image_right[self.step], (self.x, self.y))
                self.lastImage = self.image_right[self.step]
            else: #este else se encarga de ponerle al jugador el último dizfraz que tenía
                surface.blit(self.lastImage, (self.x, self.y))
        elif self.inventory == 'False' and self.imDead() == False:
            if self.direction == 'right':
                surface.blit(self.atRight, (self.x, self.y))
                if roundFinished:
                    self.lastImage = self.atRight
            if self.direction == 'left':
                surface.blit(self.atLeft, (self.x, self.y))
                if roundFinished:
                    self.lastImage = self.atLeft
            if self.direction == 'down':
                surface.blit(self.atDown, (self.x, self.y))
                if roundFinished:
                    self.lastImage = self.atDown
            if self.direction == 'up':
                surface.blit(self.atUp, (self.x, self.y))
                if roundFinished:
                    self.lastImage = self.atUp
        elif self.inventory == 'True' or self.moving == False: #si el inventario está abierto no debe cambiar de dizfraz
            surface.blit(self.lastImage, (self.x, self.y))