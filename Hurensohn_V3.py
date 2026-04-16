import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
player = pygame.Rect(400, 300, 40, 40)
wallNorth = pygame.Rect(0, 0, 800, 10)

running = True
while running:
    dx, dy = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  dx = -5
    if keys[pygame.K_RIGHT]: dx = +5
    if keys[pygame.K_UP]:    dy = -5
    if keys[pygame.K_DOWN]:  dy = +5

    if player.move(dx, 0).colliderect(wallNorth):
        dx = 0
    if player.move(0, dy).colliderect(wallNorth):
        dy = 0

    player.move_ip(dx, dy)
    # constrain the player to the screen
    player.clamp_ip(screen.get_rect())

    # current coordinates of the player, use `player.x` and `player.y`, or `player.center`
    screen.fill((11, 13, 16))
    
    # visual wall default red
    pygame.draw.rect(screen, (255, 107, 53), player)
    pygame.draw.rect(screen, (255, 0,0 ), wallNorth)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()