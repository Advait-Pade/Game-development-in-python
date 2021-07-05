import pygame
import os

width,height = 1500,500

GScreen = pygame.display.set_mode((width,height))
pygame.display.set_caption(("First"))
FPS = 60
pic = pygame.image.load(os.path.join('resources','1.png'))
#we can load image and song using 2 methods that are used here 
song = os.path.join(os.getcwd(),'resources/1.mp3')

def mydraw():
    GScreen.fill((251,0,60))
    GScreen.blit(pic,(0,0))

    pygame.display.update()

def main():
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        mydraw()
    
if __name__ == "__main__":
    main()
