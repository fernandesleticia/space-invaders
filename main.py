import pygame

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invaders")

#todo: fix that, is not applying the icon
icon = pygame.image.load('assets/ufo-64px.png')
pygame.display.set_icon(icon)

#player ship
playerImg = pygame.image.load('assets/space-invaders-player-64px.png')
playerX = 400
playerY = 500
playerX_change = 0

#player enemy
enemyImg = pygame.image.load('assets/ufo-64px.png')
enemyX = 400
enemyY = 50
enemyX_change = 0

def player(x,y):
	screen.blit(playerImg, (x,y))


def enemy(x,y):
	screen.blit(enemyImg, (x,y))


# game loop
running = True
while running:

	# RGB 
	screen.fill((0,0,0))
    
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -0.3	
			if event.key == pygame.K_RIGHT:
				playerX_change = 0.3			
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0		
	
	playerX += playerX_change

	if playerX <= 0:
	   playerX = 0
	elif playerX >= 736:
		playerX = 736   

	player(playerX, playerY)
	enemy(enemyX, enemyY)
	pygame.display.update()

