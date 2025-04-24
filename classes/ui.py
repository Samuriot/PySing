import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
running = True
text = font.render("PySing!", True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (1280//2, 100)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")
    
    # render stuff
    screen.blit(text, textRect)
            
    # rendering game    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()