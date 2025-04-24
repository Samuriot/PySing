import pygame


class UI:
    def updateText(self, str):
        text = self.font.render(str, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (1280//2, 100)
        self.text = [text, textRect]
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.running = True
        self.updateText("PySing")
        pygame.mixer.pre_init()
        pygame.mixer.init()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.updateText("you clicked down and played music")
                    pygame.mixer.music.load("music/dabin.mp3")
                    pygame.mixer.music.play()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.updateText("text reset")
            
                self.screen.fill("black")
                
                # render stuff
                self.screen.blit(self.text[0], self.text[1])
                        
                # rendering game    
                pygame.display.flip()
                
                self.clock.tick(60)

game = UI()
game.run()

pygame.quit()