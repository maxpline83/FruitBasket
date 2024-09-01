import pygame
import numpy as np
import cmath
import scipy.integrate as SI
import time
import pickle
from player import Player
from game import Game
from scripts.scripts import load_highscore

pygame.init()

clock = pygame.time.Clock()  # importer horloge pygame
FPS = 60
temps = 0  # variable des différentes positions du fruit du fruit
lancement_fruit = False
calibri_font = pygame.font.SysFont("Calibri", 50)  # création police écriture
validation_panier = False
nb_panier_valide = 0  # nombre de paniers validés
score = 0
position_player = 1  # position du joueur (1-2-3-4)
panier_deja_mis = False
niveau = 1
zs = np.array([[0] * 100, [0] * 100, [0] * 100, [0] * 100])
def_fruit = False
cpt = 0
son = True  # lancer le son dans le jeu


# ------------------------------------------------------------------------------------------


def zdot(z, t):
    """Calcul de la dérivée de z=(x, y, vx, vy) à l'instant t."""
    x, y, vx, vy = z
    alphav = alpha * np.hypot(vx, vy)
    return vx, vy, -alphav * vx, -g - alphav * vy  # dz/dt = (vx,vy,x..,y..)

def launch_projectile(projectile):
    player.all_projectiles.add(projectile)

highscore = load_highscore()

player = Player()
game = Game()

# startkicks
start_ticks = pygame.time.get_ticks()  # commence à compter le nombre de tick à partir de ca moment

# Screen creating & Assets loading

pygame.display.set_caption("Fruit Basket Game")
screen = pygame.display.set_mode((1080, 720))  # taille fenêtre

ecrasement = pygame.mixer.Sound('../assets/sounds/ecrasement.ogg')
applaudissements = pygame.mixer.Sound('../assets/sounds/applaudissements.wav')
background = pygame.image.load('../assets/others/background.png')
panier = pygame.image.load('../assets/others/hoop.png')
game_over = pygame.image.load('../assets/others/game_over.png')

running = True
while running:
    clock.tick(FPS)

    if def_fruit == False:  # permet de définir le nouveau fruit en fonction du nombre de paniers marqués, de la position et du niveau.
        def_fruit = True
        if niveau == 1:
            if position_player == 1:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
            if position_player == 2:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
                if nb_panier_valide == 3:
                    fruit = Ananas(player, game)
            if position_player == 3:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
                if nb_panier_valide == 3:
                    fruit = Ananas(player, game)
                if nb_panier_valide == 4:
                    fruit = Banane(player, game)
            if position_player == 4:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
                if nb_panier_valide == 3:
                    fruit = Ananas(player, game)
                if nb_panier_valide == 4:
                    fruit = Banane(player, game)
                if nb_panier_valide == 5:
                    fruit = Pomme(player, game)

        if niveau == 2:
            if position_player == 1:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
                if nb_panier_valide == 3:
                    fruit = Fraise(player, game)
            if position_player == 2:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
                if nb_panier_valide == 3:
                    fruit = Fraise(player, game)
                if nb_panier_valide == 4:
                    fruit = Ananas(player, game)
            if position_player == 3:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
                if nb_panier_valide == 3:
                    fruit = Fraise(player, game)
                if nb_panier_valide == 4:
                    fruit = Ananas(player, game)
                if nb_panier_valide == 5:
                    fruit = Banane(player, game)
            if position_player == 4:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
                if nb_panier_valide == 3:
                    fruit = Fraise(player, game)
                if nb_panier_valide == 4:
                    fruit = Ananas(player, game)
                if nb_panier_valide == 5:
                    fruit = Banane(player, game)
                if nb_panier_valide == 6:
                    fruit = Pomme(player, game)

        if niveau == 3:
            if position_player == 1:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
                if nb_panier_valide == 3:
                    fruit = Fraise(player, game)
                if nb_panier_valide == 4:
                    fruit = Kiwi(player, game)
            if position_player == 2:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
                if nb_panier_valide == 3:
                    fruit = Fraise(player, game)
                if nb_panier_valide == 4:
                    fruit = Kiwi(player, game)
                if nb_panier_valide == 5:
                    fruit = Ananas(player, game)
            if position_player == 3:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
                if nb_panier_valide == 3:
                    fruit = Fraise(player, game)
                if nb_panier_valide == 4:
                    fruit = Kiwi(player, game)
                if nb_panier_valide == 5:
                    fruit = Ananas(player, game)
                if nb_panier_valide == 6:
                    fruit = Banane(player, game)
            if position_player == 4:
                if nb_panier_valide == 0:
                    fruit = Citron(player, game)
                if nb_panier_valide == 1:
                    fruit = Framboise(player, game)
                if nb_panier_valide == 2:
                    fruit = Melon(player, game)
                if nb_panier_valide == 3:
                    fruit = Fraise(player, game)
                if nb_panier_valide == 4:
                    fruit = Kiwi(player, game)
                if nb_panier_valide == 5:
                    fruit = Ananas(player, game)
                if nb_panier_valide == 6:
                    fruit = Banane(player, game)
                if nb_panier_valide == 7:
                    fruit = Pomme(player, game)

                    # timer de 40sec
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculer temps écoulé depuis lancement du jeu
    if seconds > 43:  # si plus de 43 secondes, ferme le jeu
        seconds = 43
        background.blit(game_over, (1080 / 2 - 238, 720 / 2 - 266))  # affiche game over

        if score > highscore:  # permet d'échanger le highscore s'il est battu
            highscore = score
            with open('../score.dat', 'wb') as file:  # écrire highscore dans un fichier
                pickle.dump(score, file)

    background.blit(calibri_font.render("Fruit Basket", True, (255, 255, 0)), (425, 1))  # affiche le titre du jeu

    if seconds > 3:  # temps de la partie
        pygame.draw.rect(background, (255, 255, 255), (800, 0, 300, 43))  # créer rectangle
        background.blit(calibri_font.render("temps: " + str(int(40 - seconds + 3)), True, (0, 0, 0)),
                        (800, 0))  # affiche le temps dans le rectangle

    if seconds < 3:  # compte à rebour de 3 secondes avant le lancement de la partie de 40 secondes
        pygame.draw.rect(background, (255, 255, 255), (800, 0, 300, 43))
        background.blit(calibri_font.render("debut dans:  " + str(int(4 - seconds)), True, (0, 0, 0)), (800, 0))

    pygame.draw.rect(background, (255, 255, 255), (0, 0, 225, 43))  # rectangle pour afficher le score
    background.blit(calibri_font.render("Score : " + str(score), True, (0, 0, 0)), (10, 0))  # afficher le score
    if seconds < 43:  # si on est dans le jeu
        pygame.draw.rect(background, (255, 255, 255), (0, 44, 300, 43))  # rectangle
        background.blit(calibri_font.render("HighScore : " + str(highscore), True, (0, 0, 0)),
                        (10, 44))  # affiche highscore
    if score > highscore:  # si score>highscore, mise à jour highscore en temps réelle
        pygame.draw.rect(background, (255, 255, 255), (0, 44, 410, 43))
        background.blit(calibri_font.render("New HighScore : " + str(score), True, (0, 0, 0)), (10, 44))

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (-5, 0))

    # applique panier dans le jeu
    screen.blit(panier, (870, 144))

    # appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # affichage fruit
    screen.blit(fruit.image, fruit.rect)

    # acceptation du panier distance avec oanier
    distance_fruit_panier = np.sqrt((955 - (fruit.rect.x + (fruit.scale) / 2)) ** 2 + (
                148 - (fruit.rect.y + (fruit.scale) / 2)) ** 2)  # distance entre le fruit et le panier
    if distance_fruit_panier <= fruit.tol and temps < 99:  # si distance entre fruit et panier est inférieure à la tolérance
        if zs[temps][1] > zs[temps + 1][1]:  # si la position à t+1 est inférieure
            if panier_deja_mis == False:
                validation_panier = True
    if lancement_fruit == True:
        if temps >= cpt - 10:
            if son:  # pour jouer 1 seule fois le son
                if not validation_panier:
                    ecrasement.play()  # jouer le son

    if nb_panier_valide == 3 + position_player - 1 + niveau - 1:  # savoir quand changer de position
        nb_panier_valide = 0  # recommence à 0
        if position_player == 4:  # si la position = 4, reviens à 1 et passe niveau supérieur
            position_player = 1
            niveau += 1
            break
        if position_player != 4:  # si position différente de 4, rajoute 1 position
            position_player += 1

    if validation_panier:  # jouer les applaudissements si le panier est marqué
        applaudissements.play()
        son = False  # pour jouer le son qu'une fois

        nb_panier_valide += 1
        score += fruit.score  # ajoute le score en fonction du fruit
        validation_panier = False
        panier_deja_mis = True  # empeche de marquer plusieurs fois par lancer

    if position_player == 1:  # définir la position du joueur
        if temps == cpt:  # attend que le lancer soit finis
            game.player.rect.x = 650  # variable en x de chaque position du joueur

    if position_player == 2:
        if temps == cpt:
            game.player.rect.x = 433

    if position_player == 3:
        if temps == cpt:
            game.player.rect.x = 216

    if position_player == 4:
        if temps == cpt:
            game.player.rect.x = 1

    if niveau == 4:  # si on arrive au niveau 4, ferme le jeu
        running = False
        pygame.quit()

        # récupérer les projectiles.
    for projectile in player.all_projectiles:

        if temps >= cpt:  # si le lancer est terminé, remet le fruit dans sa position initiale
            fruit.rect.x = game.player.rect.x + 90
            fruit.rect.y = game.player.rect.y + 90
            lancement_fruit = False
            def_fruit = False  # redemande une définition du fruit
            temps = 0  # remet le temps du lancer à 0
            if position_player == 1:  # si la position joueur = 1, alors position en x du joueur = 650
                game.player.rect.x = 650

            if position_player == 2:
                game.player.rect.x = 433

            if position_player == 3:
                game.player.rect.x = 216

            if position_player == 4:
                game.player.rect.x = 1

        if lancement_fruit:
            projectile.move(temps)  # fait bouger le fruit en fonction du temps
            screen.blit(fruit.image, fruit.rect)  # affiche imag en fonction de la position sur l'écran
            temps += 1
            time.sleep(0.01)

            # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # si joueur ferme la fenêtre, ferme pygame
            running = False  # le jeu s'arrête
            pygame.quit()

        elif event.type == pygame.KEYDOWN:  # si appuie sur une touche du clavier
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:  # si c'est la barre espace
                if seconds >= 3 and seconds < 43:  # si c'est compris dans les 40 secondes de la partie
                    lancement_fruit = True
                    validation_panier = False
                    panier_deja_mis = False
                    launch_projectile(fruit)  # lance le projectile
                    son = True  # active les sons

    # calcul de la distance entre le centre du fruit et le clic de la souris
    # évènement si on appuie sur bouton gauche de la souris et que sa position est dans la fenêtre. Action prise en compte au relachement du boutton : mousebuttonup
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and event.pos[0] < 1080 and event.pos[1] < 720:
        if seconds >= 3 and seconds < 43:
            # lancement d'un fruit
            g = 9.81
            cx = 0.45  # Coefficient de frottement d'une sphère
            rhoAir = 1.2
            rad = fruit.diameter / 1000
            rho = 6.23e3  # Masse volumique du fruit
            mass = fruit.weight / 8  # Masse du fruit
            alpha = 0.5 * cx * rhoAir * np.pi * rad ** 2 / mass  # Coefficient de frottement par unité de masse
            cpt = 0
            z = event.pos[0] - (game.player.rect.x + 90 + fruit.scale / 2) + (
                        event.pos[1] - (game.player.rect.y + 90 + fruit.scale / 2)) * 1j  # définition de z imaginaire
            Zpolar = cmath.polar(z)
            v0 = Zpolar[0] * 3  # définition vitesse initiale
            alt = -Zpolar[1] * 180 / np.pi  # définition de l'angle de lancer
            alt *= np.pi / 180.
            z0 = (0., 0., v0 * np.cos(alt), v0 * np.sin(alt))
            tc = np.sqrt(mass / (g * alpha))  # temps caractéristique
            t = np.linspace(0, tc, 100)
            zs = SI.odeint(zdot, z0, t)  # intègre pour obtenir l'équation de la trajectoire
            ypos = zs[:, 1] >= 0
            for i in range(len(ypos)):  # compte tant que y>0
                if ypos[i] == True:
                    cpt += 1
