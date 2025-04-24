import pygame

def updateText(str):
    text = font.render(str, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (1280//2, 100)
    return [text, textRect]

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
running = True
text = updateText("PySing")

pygame.mixer.pre_init()
pygame.mixer.init()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            text = updateText("you clicked down and played music")
            pygame.mixer.music.load("music/dabin.mp3")
            pygame.mixer.music.play()
        if event.type == pygame.MOUSEBUTTONUP:
            text = updateText("text reset")
    
    screen.fill("black")
    
    # render stuff
    screen.blit(text[0], text[1])
            
    # rendering game    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()