# -*- coding: utf-8 -*-
"""
PRORAMATION PYHON
Fruit Basket
fichier créer le lundi 27 avril 2020
RONDEAU Maxime/ PRABEL Loris
FGE1 Groupe DB1

definition des classes Game et Player pour main.py

code réalisé entre le 27 avril et le 13 mai
utilisation de pygame
"""

import pygame
pygame.init()

class Game:
    
    def __init__(self):
        #générer le personnage
        self.player = Player() 
        self.pressed = {} 
        
        
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/perso.png') # charge l'image du joueur
        self.rect = self.image.get_rect() # recupere les coordonnées du joueur
        self.rect.x = 650 # coordonnées du joueur en x au début
        self.rect.y = 420 # coordonnées du joueur en y au début
        self.all_projectiles = pygame.sprite.Group()  
        
