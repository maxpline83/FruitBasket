import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../assets/others/player.png') # charge l'image du joueur
        self.rect = self.image.get_rect() # recupere les coordonnées du joueur
        self.rect.x = 650 # coordonnées du joueur en x au début
        self.rect.y = 420 # coordonnées du joueur en y au début
        self.all_projectiles = pygame.sprite.Group()  