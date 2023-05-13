import time
import sys
import pygame
from Tiles import Tile
from setting import tile_size, screen_width, screen_height, obstacle_size
from player import Player
from objet import obstacle,drapeau

class Level:

    def __init__(self,level1,level_tuto,surface):
        #Debut du niveau

        #configuration du niveau
        self.display_surface = surface
        self.level_data = level1
        self.setup_level(level1)
        self.shift = 0
        self.map_level1 = level1
        self.map_leveltuto = level_tuto

        #temps du niveua
        self.temps = 0
        self.start_time = 0
        self.debut_compteur = False

        #debut/fin des niveaux:
        self.Classement = False
        self.game_over = False
        self.win =False
        self.Regle = False
        self.Page_Level = False
        #compteur
        self.cpt = 0
        #----------------------------------------------------------------
        #menu
        # boulen pour savoir si les bouton du menu sont activé
        self.Lancement = True
        self.Level1 = False
        self.Level_Tuto = False
        # initialisation du fond blanc
        self.baniere = pygame.image.load("fond.png")

        # initialisation du bouton jouer
        self.bouton_jouer = pygame.image.load("start_btn.png")
        self.bouton_jouer_rect = self.bouton_jouer.get_rect()


        # initialisation du bouton exit
        self.bouton_exit = pygame.image.load("exit_btn.png")
        self.bouton_exit_rect = self.bouton_exit.get_rect()

        # initialisation de l'ecran de  mort
        self.ecran_de_mort = pygame.image.load("fond.png")
        self.ecran_game_over = pygame.image.load("game-over.png")
        self.bouton_restart = pygame.image.load("Restart.png")
        self.bouton_restart_rect = self.bouton_restart.get_rect()

        #initialisation de l'image de fond d'ecran
        self.fond_ecran = pygame.image.load("game-background-game-design.png")


    def lancement(self,surface):

        surface.blit(self.fond_ecran,(0,0))
        surface.blit(self.bouton_jouer,(250,125))
        surface.blit(self.bouton_exit,(250,600))
        rect_x1, rect_y1, rect_height1, rect_width1 = 250, 125, 126, 279
        rect_x2, rect_y2, rect_height2, rect_width2 = 250, 600, 126, 279
        rect_x3, rect_y3, rect_height3, rect_width3 = 1000, 125, 126, 279
        rect_x4, rect_y4, rect_height4, rect_width4 = 1000, 600, 126, 279
        #pygame.draw.rect(surface, (0, 0, 0), (rect_x2, rect_y2, rect_width2, rect_height2))
        #pygame.draw.rect(surface, (0, 0, 0), (rect_x1, rect_y1, rect_width1, rect_height1))
        pygame.draw.rect(surface,(0,0,0),(rect_x3,rect_y3,rect_width3,rect_height3))
        pygame.draw.rect(surface, (0, 0, 0), (rect_x4, rect_y4, rect_width4, rect_height4))

        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect_x1 < mouse_x < rect_x1 + rect_width1 and rect_y1 < mouse_y < rect_y1 + rect_height1:
                self.Lancement = False
                self.Page_Level = True

            if rect_x2 < mouse_x < rect_x2 + rect_width2 and rect_y2 < mouse_y < rect_y2 + rect_height2:
                pygame.quit()
                sys.exit()

            if rect_x3 < mouse_x < rect_x3 + rect_width3 and rect_y3 < mouse_y < rect_y3 + rect_height3:
                self.Lancement = False
                self.Regle = True
            if rect_x4 < mouse_x < rect_x4 + rect_width4 and rect_y4 < mouse_y < rect_y4 + rect_height4:
                self.Lancement = False
                self.Classement = True
    def setup_level(self,layout):
        self.Tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.monstres = pygame.sprite.GroupSingle()
        self.obstacles = pygame.sprite.Group()
        self.drapeau = pygame.sprite.Group()

        for row_index,row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'X':
                    tile = Tile((x,y),tile_size)
                    self.Tiles.add(tile)
                if col == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if col == 'O':
                    obs = obstacle((x, y), obstacle_size)
                    self.obstacles.add(obs)
                if col == 'D':
                    Drapeau = drapeau((x,y),obstacle_size)
                    self.drapeau.add(Drapeau)


    def scroll_x(self):
        player = self.player.sprite
        Position_x = player.rect.centerx

        if (Position_x < (screen_width / 6)):
            self.shift = 800
            player.rect.x += 800

        elif (Position_x > (screen_width - (screen_width / 6))):
            self.shift = -800
            player.rect.x -= 800
            self.cpt +=1
            print(self.cpt)

        else:
            self.shift = 0


    def horizontal_collision(self,surface):
        player = self.player.sprite

        enemies = self.monstres.sprites()
        obstacles = self.obstacles.sprites()
        colision_p = self.Tiles.sprites()
        Drapeau = self.drapeau.sprites()

        for sprite in self.Tiles.sprites():
            if sprite.rect.colliderect(player.rect):


                if abs(player.rect.right - sprite.rect.left) < 10 and player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.direction.x = -10

                if abs(player.rect.left - sprite.rect.right) < 10 and player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = 10



                if abs(player.rect.bottom - sprite.rect.top) < 20 and player.direction.y < 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.direction.x = 0
                    player.saut = False
                    player.stop_traj = False
                if abs(player.rect.top - sprite.rect.bottom)<20 and player.direction.y > 0:
                    if player.direction.x > 0:
                        player.rect.left = sprite.rect.right
                        player.direction.x = 10

                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0


        #vie du joueur
        for ob in obstacles:
            if player.rect.colliderect(ob.rect):
                self.game_over = True
                self.Level1 = False
        for col in colision_p:
            if player.rect.colliderect(col.rect):
                Player.saut = False

        for col in Drapeau:
            if player.rect.colliderect(col.rect):
                self.Level1 = False
                self.Level_Tuto = False
                self.win = True
                self.debut_compteur = True

    def reset_pos_perso(self):
        player = self.player.sprite
        player.saut = False
        player.direction.x = 0
        player.direction.y = 0
        self.setup_level(self.level_data)


    def gameover(self,surface):
        if self.game_over == True:
            self.reset = True
            player = self.player.sprite
            surface.fill('black')
            surface.blit(self.ecran_game_over,(500,100))

            surface.blit(self.bouton_restart,(550,300))
            rect_x,rect_y,rect_height,rect_width = 550,300,126,240
            if pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if rect_x < mouse_x < rect_x + rect_width and rect_y < mouse_y < rect_y + rect_height:

                    self.game_over = False
                    self.Level1 = True
                    self.reset_pos_perso()
                    #print(player.rect.x)
                    #print(player.rect.y)

    def fin_de_jeu(self,surface):
        surface.fill('black')
        if self.debut_compteur == True:
            self.temps = pygame.time.get_ticks() - self.start_time
            self.temps /=1000
            print("Temps écoulé : {:.2f} secondes".format(self.temps))
            int(self.temps)
            self.classement()
            self.debut_compteur = False
        rect_x, rect_y, rect_height, rect_width = 550, 350, 126, 240
        pygame.draw.rect(surface, (250, 250, 250), (rect_x, rect_y, rect_width, rect_height))
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect_x < mouse_x < rect_x + rect_width and rect_y < mouse_y < rect_y + rect_height:
                self.win = False
                self.Lancement = True

    def regle(self,surface):
        self.Lancement = False
        surface.fill('black')
        police = pygame.font.SysFont("monospace",20)
        txt = police.render("Le but du jeu est d'atteindre la ligne d'arrivé."
                            " La touche R vous permet de reset la postion du joueur.",1,(250,250,250))
        surface.blit(txt,(200,200))

        rect_x, rect_y, rect_height, rect_width = 550, 350, 126, 240
        pygame.draw.rect(surface,(250,250,250),(rect_x, rect_y, rect_width, rect_height))
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect_x < mouse_x < rect_x + rect_width and rect_y < mouse_y < rect_y + rect_height:
                self.Regle = False
                self.Lancement = True


    def page_levels(self,surface):
        surface.blit(self.fond_ecran,(0,0))
        #dinitialisation des rectangle
        rect_x1, rect_y1, rect_height1, rect_width1 = 600, 0, 100, 279
        rect_x2, rect_y2, rect_height2, rect_width2 = 600, 150, 100, 279
        rect_x3, rect_y3, rect_height3, rect_width3 = 600, 300, 100, 279
        rect_x4, rect_y4, rect_height4, rect_width4 = 600, 450, 100, 279
        rect_x5, rect_y5, rect_height5, rect_width5 = 600, 600, 100, 279
        rect_x6, rect_y6, rect_height6, rect_width6 = 600, 750, 100, 279

        police = pygame.font.SysFont("monospace", 20)
        leveltuto =  police.render("TUTO ",1,(250,250,250))
        level1 = police.render("1 ",1,(250,250,250))
        level2 = police.render("2 ",1,(250,250,250))
        level3 = police.render("3 ",1,(250,250,250))
        level4 = police.render("4 ", 1, (250, 250, 250))

        pygame.draw.rect(surface, (0, 0, 0), (rect_x1, rect_y1, rect_width1, rect_height1))
        pygame.draw.rect(surface, (0, 0, 0), (rect_x2, rect_y2, rect_width2, rect_height2))
        pygame.draw.rect(surface, (0, 0, 0), (rect_x3, rect_y3, rect_width3, rect_height3))
        pygame.draw.rect(surface, (0, 0, 0), (rect_x4, rect_y4, rect_width4, rect_height4))
        pygame.draw.rect(surface, (0, 0, 0), (rect_x5, rect_y5, rect_width5, rect_height5))
        pygame.draw.rect(surface,(250,0,0),(rect_x6, rect_y6, rect_width6, rect_height6))
        surface.blit(leveltuto, (722, 50))
        surface.blit(level1, (725, 200))
        surface.blit(level2, (725, 350))
        surface.blit(level3, (725, 500))
        surface.blit(level4, (725, 650))


        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect_x1 < mouse_x < rect_x1 + rect_width1 and rect_y1 < mouse_y < rect_y1 + rect_height1:
                self.setup_level(self.map_leveltuto)
                self.Page_Level = False
                self.Level_Tuto = True

            if rect_x2 < mouse_x < rect_x2 + rect_width2 and rect_y2 < mouse_y < rect_y2 + rect_height2:
                self.setup_level(self.map_level1)
                self.Page_Level = False
                self.Level1 = True

            if rect_x6 < mouse_x < rect_x6 + rect_width6 and rect_y6 < mouse_y < rect_y6 + rect_height6:
                self.Page_Level = False
                self.Lancement = True
    def classement(self):
        f = open("Classement.txt", "a")
        if self.temps >60:
            self.temps /= 60
            f.write("X : {:.2f} minutes \n".format(self.temps))
        else:
            f.write("X : {:.2f} secondes \n".format(self.temps))
        f.close()


    def print_classement(self,surface):

        # Création de la police de caractères
        font = pygame.font.SysFont("monospace", 30)
        text_surface = font.render("Classement : ", True, (255, 255, 255))
        surface.fill('black')
        surface.blit(text_surface, (50, 50))

        f = open("Classement.txt", "r")
        for i, line in enumerate(f):
            text_surface = font.render(line, True, (255, 255, 255))
            surface.blit(text_surface, (50, 100 + i * 30))
        f.close()

        rect_x, rect_y, rect_height, rect_width = 550, 650, 126, 240
        pygame.draw.rect(surface, (250, 250, 250), (rect_x, rect_y, rect_width, rect_height))
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect_x < mouse_x < rect_x + rect_width and rect_y < mouse_y < rect_y + rect_height:
                self.Classement = False
                self.Lancement = True


    def run(self):
        #level
        self.Tiles.update(self.shift)
        self.Tiles.draw(self.display_surface)
        self.scroll_x()

        #obsacle
        self.obstacles.update(self.shift)
        self.obstacles.draw(self.display_surface)

        #drapeau
        self.drapeau.update(self.shift)
        self.drapeau.draw(self.display_surface)
        #Capacity


        #player
        self.player.update()
        self.horizontal_collision(self.display_surface)
        self.player.draw(self.display_surface)

        #game over
        self.gameover(self.display_surface)

        #enemie
        self.monstres.draw(self.display_surface)
        self.monstres.update()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            self.reset_pos_perso()
        player = self.player.sprite

        if keys[pygame.K_x]:
            player.rect.x +=50
        if keys[pygame.K_c]:
            player.rect.x -=50




    def update(self,surface,level):
        if self.Lancement:
            self.lancement(surface)
        if self.Page_Level:
            self.page_levels(surface)
        if self.game_over:
            self.gameover(surface)
        if self.win:
            self.fin_de_jeu(surface)
        if self.Regle:
            self.regle(surface)
        if self.Classement:
            self.print_classement(surface)
        if self.Level1:
            surface.blit(self.fond_ecran,(0,0))
            level.run()
        if self.Level_Tuto:
            surface.blit(self.fond_ecran,(0,0))
            level.run()
            self.start_time = 0
            self.start_time = pygame.time.get_ticks()

