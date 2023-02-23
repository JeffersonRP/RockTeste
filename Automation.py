import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
base_font = pygame.font.Font(None,32)
user_text = 'Dungeon Jeff Hahaha'


pygame.display.set_caption("Dungeon Jeff")

while True:
    for event in pygame.event.get():
        pygame.display.update()

        if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
        
        

        screen.fill((0,0,0))
        text_surface = base_font.render(user_text, True, (255,255,255))
        screen.blit(text_surface,(0,0))



       
    






    