#RIVER

###########################
#IMPORT MODULES PYGAME
import pygame
from pygame.locals import *
from random import*
from random import randrange
import time
pygame.init()
##########################  


##########################    DEFINITIONS    ##########################

#FONCTIONS CONTENU PAGES
def PAm(): #CONTENU PAGE D'ACCUEIL
    fondmenu=pygame.image.load("Graphismes/pagedaccueil.jpg").convert()
    fenetre.blit(fondmenu,(0,0))
    affichagepiecesmenu = police.render(str(totalpieces) + " pieces", 1, (255,255,255))
    positionpiecesmenu = affichagepiecesmenu.get_rect()
    positionpiecesmenu.topright = (1270,10)
    fenetre.blit(affichagepiecesmenu, positionpiecesmenu)
    pygame.display.flip()

def P1() : #CONTENU PAGE BOUTIQUE
    fondmenu=pygame.image.load("Graphismes/boutique.jpg").convert() #convert= convertisseur au bon format
    fenetre.blit(fondmenu,(0,0))
    positionpiecesmenu.topright = (1270,10)
    fenetre.blit(affichagepiecesmenu, positionpiecesmenu)
    pygame.display.flip()

def P2() : #CONTENU PAGE RESERVES
    fenetre.blit(imagereserve,(0,0))
    positionpiecesmenu.topright = (1270,10)
    fenetre.blit(affichagepiecesmenu, positionpiecesmenu)
    pygame.display.flip()

#FONCTIONS OUVERTURE PAGES + ZONES CLIQUABLES
def boutique():
    global a
    x=0
    while x!=1:
        P1()
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1 and event.pos[0]<130 and event.pos[1]<65:
                    x=1
    a="sortie"

def reserve():
    global a
    global bateau
    global imagereserve
    x=0
    while x!=1:
        P2()
        for event in pygame.event.get():    
            if event.type == MOUSEBUTTONDOWN :
                if event.button == 1 :
                    if event.pos[0]<1230 and event.pos[0]>907 and event.pos[1]<250 and event.pos[1]>196  :
                        bateau=bateau0
                        imagereserve=imagereserve0
                        fenetre.blit(imagereserve,(0,0))
                    if event.pos[0]<1230 and event.pos[0]>907 and event.pos[1]<338 and event.pos[1]>278  :
                        bateau=bateau1
                        imagereserve=imagereserve1
                        fenetre.blit(imagereserve,(0,0))
                    if event.pos[0]<1230 and event.pos[0]>907 and event.pos[1]<421 and event.pos[1]>366  :
                        bateau=bateau2
                        imagereserve=imagereserve2
                        fenetre.blit(imagereserve,(0,0))
                    if event.pos[0]<1230 and event.pos[0]>907 and event.pos[1]<506 and event.pos[1]>450  :
                        bateau=bateau3
                        imagereserve=imagereserve3
                        fenetre.blit(imagereserve,(0,0))

                if event.button==1 and event.pos[0]<130 and event.pos[1]<65:
                    x=1        

    a="sortie"

def jeu():  #JEU ENTIER
    global a
    x=0
    #REINITIALISER A CHAQUE NOUVELLE PARTIE
    gameover = 0
    score = 0
    pieces=0
    collisionpiece=0
    afficherpiece=0
    taillex1A=taillex2A=taillex3A=taillex4A=taillex5A=taillex6A=4     #TAILLES XA ICEBERGS DEPART
    tailley1A=tailley2A=tailley3A=tailley4A=tailley5A=tailley6A=2.4     #TAILLES YA ICEBERGS DEPART
    affichericeberg1A=affichericeberg2A=affichericeberg3A=affichericeberg4A=affichericeberg5A=affichericeberg6A=1
    b = 1           #COEFFICIENT MULTIPLICATEUR BONUS
    bonus=""        #AUCUN BONUS AU DEPART
        
    #AFFICHER LE FOND
    fenetre.blit(fondjeu,(0,0))
    
    #PLACER BATEAU
    positionbateau = bateau.get_rect()
    positionbateau.centerx = 640
    positionbateau.centery = 600
    fenetre.blit(bateau, positionbateau)

    #PIECES
    positionbitcoin = bitcoin.get_rect()
    positionbitcoin.centerx = 0
    positionbitcoin.centery = 800

    #RAFFRACHIR
    pygame.display.flip()
    pygame.key.set_repeat(200, 10) #RELEVER TOUCHES CLAVIER PENDANT 20MS TOUS LES 10MS

    while x!=1:     #CONTINUER DE BOUCLER PAR DEFAUT

        if gameover == 0 :

            for event in pygame.event.get():
    
                if event.type == QUIT:
                    continuer = 0
                    
                if event.type == plusunscore :  #SI EVENEMENT, SCORE + 1
                    score = score + 1*b

                #CREATIONS NOUVEAUX ICEBERGS
                if event.type == nouveliceberg :
                    piste = randrange(1,7) #7 exclu
                    if piste == 1 :
                        if 'iceberg1A' in locals() :        #SI DEJA ICEBERG
                            if affichericeberg1A == 0 :    #SI LE PRECEDENT EST SORTI ALORS ON PEUT L'UTILISER
                                iceberg1A=pygame.transform.scale(iceberg,(int(round(taillex1A)),int(round(tailley1A))))
                                posx1A=530
                                posy1A=272
                                positioniceberg1A.centerx=posx1A
                                positioniceberg1A.centery=posy1A
                                time.sleep(0.1)
                                affichericeberg1A = 1
                                fenetre.blit(iceberg1A, positioniceberg1A)
                        else :                                                      #SI PAS D'ICEBERG (PREMIERE FOIS)
                            iceberg1A=pygame.transform.scale(iceberg,(4,int(2.4)))    #CREER ICEBERG
                            positioniceberg1A=iceberg1A.get_rect()
                            iceberg1A=pygame.transform.scale(iceberg,(int(round(taillex1A)),int(round(tailley1A))))
                            posx1A=530
                            posy1A=272
                            positioniceberg1A.centerx=posx1A
                            positioniceberg1A.centery=posy1A
                            fenetre.blit(iceberg1A, positioniceberg1A)
                    if piste == 2 :
                        if 'iceberg2A' in locals() :
                            if affichericeberg2A == 0 :
                                iceberg2A=pygame.transform.scale(iceberg,(int(round(taillex2A)),int(round(tailley2A))))
                                posx2A=574
                                posy2A=272
                                positioniceberg2A.centerx=posx2A
                                positioniceberg2A.centery=posy2A
                                time.sleep(0.1)
                                affichericeberg2A = 1
                                fenetre.blit(iceberg2A, positioniceberg2A)
                        else :
                            iceberg2A=pygame.transform.scale(iceberg,(4,int(2.4)))
                            positioniceberg2A=iceberg2A.get_rect()
                            iceberg2A=pygame.transform.scale(iceberg,(int(round(taillex2A)),int(round(tailley2A))))
                            posx2A=574
                            posy2A=272
                            positioniceberg2A.centerx=posx2A
                            positioniceberg2A.centery=posy2A
                            fenetre.blit(iceberg2A, positioniceberg2A)
                    if piste == 3 :
                        if 'iceberg3A' in locals() :
                            if affichericeberg3A == 0 :
                                iceberg3A=pygame.transform.scale(iceberg,(int(round(taillex3A)),int(round(tailley3A))))
                                posx3A=618
                                posy3A=272
                                positioniceberg3A.centerx=posx3A
                                positioniceberg3A.centery=posy3A
                                time.sleep(0.1)
                                affichericeberg3A = 1
                                fenetre.blit(iceberg3A, positioniceberg3A)      
                        else :
                            iceberg3A=pygame.transform.scale(iceberg,(4,int(2.4)))
                            positioniceberg3A=iceberg3A.get_rect()
                            iceberg3A=pygame.transform.scale(iceberg,(int(round(taillex3A)),int(round(tailley3A))))
                            posx3A=618
                            posy3A=272
                            positioniceberg3A.centerx=posx3A
                            positioniceberg3A.centery=posy3A
                            fenetre.blit(iceberg3A, positioniceberg3A)
                    if piste == 4 :
                        if 'iceberg4A' in locals() :
                            if affichericeberg4A == 0 :
                                iceberg4A=pygame.transform.scale(iceberg,(int(round(taillex4A)),int(round(tailley4A))))
                                posx4A=662
                                posy4A=272
                                positioniceberg4A.centerx=posx4A
                                positioniceberg4A.centery=posy4A
                                time.sleep(0.1)
                                affichericeberg4A = 1
                                fenetre.blit(iceberg4A, positioniceberg4A)
                        else :
                            iceberg4A=pygame.transform.scale(iceberg,(4,int(2.4)))
                            positioniceberg4A=iceberg4A.get_rect()
                            iceberg4A=pygame.transform.scale(iceberg,(int(round(taillex4A)),int(round(tailley4A))))
                            posx4A=662
                            posy4A=272
                            positioniceberg4A.centerx=posx4A
                            positioniceberg4A.centery=posy4A
                            fenetre.blit(iceberg4A, positioniceberg4A)
                    if piste == 5 :
                        if 'iceberg5A' in locals() :
                            if affichericeberg5A == 0 :
                                iceberg5A=pygame.transform.scale(iceberg,(int(round(taillex5A)),int(round(tailley5A))))
                                posx5A=705
                                posy5A=272
                                positioniceberg5A.centerx=posx5A
                                positioniceberg5A.centery=posy5A
                                time.sleep(0.1)
                                affichericeberg5A = 1
                                fenetre.blit(iceberg5A, positioniceberg5A)
                        else :
                            iceberg5A=pygame.transform.scale(iceberg,(4,int(2.4)))
                            positioniceberg5A=iceberg5A.get_rect()
                            iceberg5A=pygame.transform.scale(iceberg,(int(round(taillex5A)),int(round(tailley5A))))
                            posx5A=705
                            posy5A=272
                            positioniceberg5A.centerx=posx5A
                            positioniceberg5A.centery=posy5A
                            fenetre.blit(iceberg5A, positioniceberg5A)
                    if piste == 6 :
                        if 'iceberg6A' in locals() :
                            if affichericeberg6A == 0 :
                                iceberg6A=pygame.transform.scale(iceberg,(int(round(taillex6A)),int(round(tailley6A))))
                                posx6A=747
                                posy6A=272
                                positioniceberg6A.centerx=posx6A
                                positioniceberg6A.centery=posy6A
                                time.sleep(0.1)
                                affichericeberg6A = 1
                                fenetre.blit(iceberg6A, positioniceberg6A)
                        else :
                            iceberg6A=pygame.transform.scale(iceberg,(4,int(2.4)))
                            positioniceberg6A=iceberg6A.get_rect()
                            iceberg6A=pygame.transform.scale(iceberg,(int(round(taillex6A)),int(round(tailley6A))))
                            posx6A=747
                            posy6A=272
                            positioniceberg6A.centerx=posx6A
                            positioniceberg6A.centery=posy6A
                            fenetre.blit(iceberg6A, positioniceberg6A)

                #CREATIONS NOUVELLES PIECES
                if event.type == nouvellepiece :
                    endroit= randrange(200,1081) #1081 exclu et de 200 à 1081 car le bateau se deplace comme ca a partir de 200
                    positionbitcoin.centerx = endroit
                    positionbitcoin.centery = 600
                    afficherpiece=1

                #DEPLACEMENTS ICEBERGS
                if event.type == deplacementiceberg1A:
                    if 'positioniceberg1A' in locals() :
                        posx1A=posx1A-0.9                               #POSITION
                        posy1A=posy1A+1                                 #POSITION
                        positioniceberg1A.centerx=round(posx1A)         #POSITION
                        positioniceberg1A.centery=round(posy1A)         #POSITION
                        taillex1A=int((posy1A-267)*ratiox)              #TAILLE(-267 pour revenir à la ligne de départ + 5)
                        tailley1A=int((posy1A-267)*ratioy)              #TAILLE
                        iceberg1A=pygame.transform.scale(iceberg,(int(round(taillex1A)),int(round(tailley1A)))) #TAILLE
                        if positioniceberg1A.top > 720 :
                            affichericeberg1A = 0
                if event.type == deplacementiceberg2A:
                    if 'positioniceberg2A' in locals() :
                        posx2A=posx2A-0.5                               #POSITION
                        posy2A=posy2A+1                                 #POSITION
                        positioniceberg2A.centerx=round(posx2A)         #POSITION
                        positioniceberg2A.centery=round(posy2A)         #POSITION
                        taillex2A=int((posy2A-267)*ratiox)              #TAILLE
                        tailley2A=int((posy2A-267)*ratioy)              #TAILLE
                        iceberg2A=pygame.transform.scale(iceberg,(int(round(taillex2A)),int(round(tailley2A)))) #TAILLE
                        if positioniceberg2A.top > 720 :
                            affichericeberg2A = 0
                if event.type == deplacementiceberg3A:
                    if 'positioniceberg3A' in locals() :
                        posx3A=posx3A-0.2                               #POSITION
                        posy3A=posy3A+1                                 #POSITION
                        positioniceberg3A.centerx=round(posx3A)         #POSITION
                        positioniceberg3A.centery=round(posy3A)         #POSITION
                        taillex3A=int((posy3A-267)*ratiox)              #TAILLE
                        tailley3A=int((posy3A-267)*ratioy)              #TAILLE
                        iceberg3A=pygame.transform.scale(iceberg,(int(round(taillex3A)),int(round(tailley3A)))) #TAILLE
                        if positioniceberg3A.top > 720 :
                            affichericeberg3A = 0
                if event.type == deplacementiceberg4A:
                    if 'positioniceberg4A' in locals() :
                        posx4A=posx4A+0.2                               #POSITION
                        posy4A=posy4A+1                                 #POSITION
                        positioniceberg4A.centerx=round(posx4A)         #POSITION
                        positioniceberg4A.centery=round(posy4A)         #POSITION
                        taillex4A=int((posy4A-267)*ratiox)              #TAILLE
                        tailley4A=int((posy4A-267)*ratioy)              #TAILLE
                        iceberg4A=pygame.transform.scale(iceberg,(int(round(taillex4A)),int(round(tailley4A)))) #TAILLE
                        if positioniceberg4A.top > 720 :
                            affichericeberg4A = 0
                if event.type == deplacementiceberg5A:
                    if 'positioniceberg5A' in locals() :
                        posx5A=posx5A+0.5                               #POSITION
                        posy5A=posy5A+1                                 #POSITION
                        positioniceberg5A.centerx=round(posx5A)         #POSITION
                        positioniceberg5A.centery=round(posy5A)         #POSITION
                        taillex5A=int((posy5A-267)*ratiox)              #TAILLE
                        tailley5A=int((posy5A-267)*ratioy)              #TAILLE
                        iceberg5A=pygame.transform.scale(iceberg,(int(round(taillex5A)),int(round(tailley5A)))) #TAILLE
                        if positioniceberg5A.top > 720 :
                            affichericeberg5A = 0
                if event.type == deplacementiceberg6A:
                    if 'positioniceberg6A' in locals() :
                        posx6A=posx6A+0.9                               #POSITION
                        posy6A=posy6A+1                                 #POSITION
                        positioniceberg6A.centerx=round(posx6A)         #POSITION
                        positioniceberg6A.centery=round(posy6A)         #POSITION
                        taillex6A=int((posy6A-267)*ratiox)              #TAILLE
                        tailley6A=int((posy6A-267)*ratioy)              #TAILLE
                        iceberg6A=pygame.transform.scale(iceberg,(int(round(taillex6A)),int(round(tailley6A)))) #TAILLE
                        if positioniceberg6A.top > 720 :
                            affichericeberg6A = 0

                #COLISSIONS BATEAU - ICEBERGS
                #Points du bateau : A en haut à droite, B en haut à gauche, C en bas à gauche
                xb=positionbateau.centerx-75
                yb=positionbateau.centery-45
                xa=positionbateau.centerx+75
                ya=positionbateau.centery-45
                yc=positionbateau.centery+45              
                if "positioniceberg1A" in locals(): 
                    xa1=positioniceberg1A.centerx+100
                    ya1=positioniceberg1A.centery+50
                    if (xb-20<=xa1<=xa+20 and yb-65<=ya1<=yc):
                        gameover=1
                if "positioniceberg2A" in locals(): 
                    xa2=positioniceberg2A.centerx+100
                    ya2=positioniceberg2A.centery+50
                    if (xb-20<=xa2<=xa+20 and yb-65<=ya2<=yc):
                        gameover=1
                if "positioniceberg3A" in locals(): 
                    xa3=positioniceberg3A.centerx+100
                    ya3=positioniceberg3A.centery+50
                    if (xb-20<=xa3<=xa+20 and yb-65<=ya3<=yc):
                        gameover=1
                if "positioniceberg4A" in locals(): 
                    xa4=positioniceberg4A.centerx+100
                    ya4=positioniceberg4A.centery+50
                    if (xb-20<=xa4<=xa+20 and yb-65<=ya4<=yc):
                        gameover=1
                if "positioniceberg5A" in locals(): 
                    xa5=positioniceberg5A.centerx+100
                    ya5=positioniceberg5A.centery+50
                    if (xb-20<=xa5<=xa+20 and yb-65<=ya5<=yc):
                        gameover=1
                if "positioniceberg6A" in locals(): 
                    xa6=positioniceberg6A.centerx+100
                    ya6=positioniceberg6A.centery+50
                    if (xb-20<=xa6<=xa+20 and yb-65<=ya6<=yc+150):
                        gameover=1

                if positionbateau.colliderect(positionbitcoin):
                    collisionpiece=1
                    
                if collisionpiece==1 :
                    afficherpiece=0
                    pieces=pieces+1
                    positionbitcoin.center = (800,0)
                    collisionpiece=0

                if event.type == KEYDOWN :
                    if event.key == K_LEFT :
                        positionbateau = positionbateau.move(-10,0)
                    if positionbateau.left<200:
                        positionbateau.left=200
                    if event.key == K_RIGHT :
                        positionbateau = positionbateau.move(10,0)
                    if positionbateau.right>1080:
                        positionbateau.right=1080

                if event.type == QUIT:
                    continuer = 0
                    pygame.display.quit()
                    pygame.quit()

            #CALCUL DU SCORE
            #if bonus == "score15" :
            #    b=2
            #    time.sleep(15)
            #    b=1
            #if bonus == "score30" :
            #    b=2
            #    time.sleep(30)
            #    b=1
            #if bonus == "score60" :
            #    b=2
            #    time.sleep(60)
            #    b=1
                    

            police = pygame.font.Font("Quantify.ttf", 50)
            affichagepieces = police.render("Pieces : " + str(pieces), 1, (255,255,255))
            affichagescore = police.render("Score : " + str(score), 1, (255,255,255))

            #RECOLLAGE
            fenetre.blit(fondjeu,(0,0))                    #FOND
            fenetre.blit(bateau, positionbateau)        #PERSO
            if afficherpiece==1 :
                fenetre.blit(bitcoin, positionbitcoin)
            fenetre.blit(affichagepieces, (10, 10))     #PIECES
            fenetre.blit(affichagescore, (1025, 10))    #SCORE
            if 'iceberg1A' in locals() :
                if affichericeberg1A == 1 :
                    fenetre.blit(iceberg1A, positioniceberg1A)    #ICEBERG1A
            if 'iceberg2A' in locals() :
                if affichericeberg2A == 1 :
                    fenetre.blit(iceberg2A, positioniceberg2A)    #ICEBERG2A
            if 'iceberg3A' in locals() :
                if affichericeberg3A == 1 :
                    fenetre.blit(iceberg3A, positioniceberg3A)    #ICEBERG3A
            if 'iceberg4A' in locals() :
                if affichericeberg4A == 1 :
                    fenetre.blit(iceberg4A, positioniceberg4A)    #ICEBERG4A
            if 'iceberg5A' in locals() :
                if affichericeberg5A == 1 :
                    fenetre.blit(iceberg5A, positioniceberg5A)    #ICEBERG5A
            if 'iceberg6A' in locals() :
                if affichericeberg6A == 1 :
                    fenetre.blit(iceberg6A, positioniceberg6A)    #ICEBERG6A
            #RAFRAICHIR
            pygame.display.flip()

        else :      #QUAND GAMEOVER
            scorefinal=score
            fenetre.blit(imggameover,(0,0))             #FOND GAME OVER
            fenetre.blit(affichagepieces, (10, 10))     #PIECES
            fenetre.blit(affichagescore, (1025, 10))    #SCORE
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN :
                    if event.button == 1 :      #QUAND CLIQUE GAUCHE
                        if event.pos[0]<870and event.pos[0]>410 and event.pos[1]>360 and event.pos[1]<550:
                            #Retourner au menu
                            x=1
                if event.type == QUIT:
                    continuer = 0
                    pygame.display.quit()
                    pygame.quit()

             
    a="sortie"
    return pieces
    print ("return pieces", pieces)

##########################  INITIALISATIONS  ##########################

a="dedans"
gameover = 0
score = 0
scorefinal = 0
pieces = 0
piecesobtenues = 0
#global totalpieces
totalpieces = 0
ratiox = 0.8
ratioy = 0.5
taillex1A=taillex2A=taillex3A=taillex4A=taillex5A=taillex6A=4     #TAILLES XA ICEBERGS DEPART
tailley1A=tailley2A=tailley3A=tailley4A=tailley5A=tailley6A=2.4     #TAILLES YA ICEBERGS DEPART
posx1A=posx1B=posx1C=posx1D=posx1E=posx1F=0
posy1A=posy1B=posy1C=posy1D=posy1E=posy1F=0
vitessegrandissement=0.5
b = 1           #COEFFICIENT MULTIPLICATEUR BONUS
bonus=""        #AUCUN BONUS AU DEPART
plusiceberg = 4000      #NOUVEL ICEBERG TOUTES LES 4 SECONDES
vitesse = 50

police = pygame.font.Font("Quantify.ttf", 50)
affichagepieces = police.render("Pieces : " + str(pieces), 1, (255,255,255))
affichagepiecesmenu = police.render(str(totalpieces) + " pieces", 1, (255,255,255))
positionpiecesmenu = affichagepiecesmenu.get_rect()
affichagescore = police.render("Score : " + str(score), 1, (255,255,255))
affichagescorefinal = police.render("Score : " + str(scorefinal), 1, (255,255,255))



##########################     EVENEMENTS     ##########################

#CRÉER EVENEMENTS ASSIGNÉS À NUMERO
plusunscore=1 
nouveliceberg=9
nouvellepiece=10

#PROGRAMMER EVENEMENT SCORE REPETITIF
pygame.time.set_timer(plusunscore,1000) #FAIRE PLUSUN TOUTES LES SECONDES
pygame.time.set_timer(nouveliceberg,plusiceberg) #NOUVEL ICEBERG TOUTES LES X SECONDES
pygame.time.set_timer(nouvellepiece,10000) #NOUVELLE PIECE TOUTES LES 10 SECONDES

#DEPLACEMENT ICEBERGS
deplacementiceberg1A=3
pygame.time.set_timer(deplacementiceberg1A,vitesse)
deplacementiceberg2A=4
pygame.time.set_timer(deplacementiceberg2A,vitesse)
deplacementiceberg3A=5
pygame.time.set_timer(deplacementiceberg3A,vitesse)
deplacementiceberg4A=6
pygame.time.set_timer(deplacementiceberg4A,vitesse)
deplacementiceberg5A=7
pygame.time.set_timer(deplacementiceberg5A,vitesse)
deplacementiceberg6A=8
pygame.time.set_timer(deplacementiceberg6A,vitesse)


##########################     PROGRAMME      ##########################

#OUVRIR FENETRE
fenetre=pygame.display.set_mode((1280,720))
pygame.display.set_caption("River")

#CHARGER TOUTES LES IMAGES :
fondmenu=pygame.image.load("Graphismes/pagedaccueil.jpg").convert()     #FOND MENU
fondjeu = pygame.image.load("Graphismes/fond.png").convert()            #FOND JEU
imggameover = pygame.image.load("Graphismes/gameover.jpg").convert()    #FOND GAME OVER
iceberg=pygame.image.load("Graphismes/Glace.png").convert_alpha()       #ICEBERG
bitcoin=pygame.image.load("Graphismes/bitcoin.png").convert_alpha()
bitcoin=pygame.transform.scale(bitcoin,(50,35))
imagereserve0=pygame.image.load("Graphismes/reservebateau1.jpg").convert()
imagereserve1=pygame.image.load("Graphismes/reservebateau2.jpg").convert()
imagereserve2=pygame.image.load("Graphismes/reservebateau3.jpg").convert()
imagereserve3=pygame.image.load("Graphismes/reservebateau4.jpg").convert()
imagereserve=imagereserve0



#Charger bateau : 
bateau0 = pygame.image.load("Graphismes/Bateau.png").convert_alpha()     #BATEAU BOIS
bateau1 = pygame.image.load("Graphismes/Bateau1.png").convert_alpha()     #BATEAU BLEU
bateau2 = pygame.image.load("Graphismes/Bateau2.png").convert_alpha()     #BATEAU ROUGE
bateau3 = pygame.image.load("Graphismes/Bateau3.png").convert_alpha()     #BATEAU VERT
bateau = bateau0


#AFFICHER LE FOND DU MENU + PIECES
fenetre.blit(fondmenu,(0,0))
positionpiecesmenu.topright = (1270,10)
fenetre.blit(affichagepiecesmenu, positionpiecesmenu)

#FICHIER SCORES
#open("scores.txt","w").write("{}")
#with open("scores.txt","r") as fichier: #OUVRIR FICHIER EN LECTURE
#    listescores = eval(fichier.read()) #RECUPERER VARIABLE ET TRANSFORMER EN DICTIONNAIRE
#    print(listescores)
#
#bestscore = listescores[1]      #RECUPERER MEILLEUR SCORE
#if score > bestscore:           #SI SCORE MEILLEUR
#    listescores[1] = score      #REMPLACER
# 
#with open("scores.txt","w") as fichier: #OUVRIR FICHIER EN ECRITURE
#    fichier.write(str(listescores))


#RAFFRACHIR
pygame.display.flip()
pygame.key.set_repeat(200, 10)

#BOUCLE PRINCIPALE
continuer = 1
while continuer == 1:  #BOUCLE INFINIE QUI TOURNE EN CONTINU
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN :
            if event.button == 1 :      #QUAND CLIQUE GAUCHE
           
                if event.pos[0]<853 and event.pos[0]>628 and event.pos[1]<455 and event.pos[1]>365:
                    #Ouvrir boutique
                    boutique()
                    
                if event.pos[0]<618 and event.pos[0]>393 and event.pos[1]<455 and event.pos[1]>365:
                    #Ouvrir réserves
                    reserve()
                
                if event.pos[0]<853 and event.pos[0]>393 and event.pos[1]>165 and event.pos[1]<355:
                    #Lancer jeu
                    pieces=jeu()
                    totalpieces=totalpieces+pieces

                if a=="sortie":
                    PAm()

                if event.type == QUIT:
                    continuer = 0
                    pygame.display.quit()
                    pygame.quit()

        

#FERMER FENETRE

