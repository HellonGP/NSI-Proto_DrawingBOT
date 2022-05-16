from PIL import Image, ImageFilter
from tkinter import Tk, filedialog
import cv2
import turtle
import os

#Récupération Image + Transformation en binaire
root = Tk()
root.withdraw()

open_file = filedialog.askopenfilenames(filetypes=[("Image Files", ".png .jfif, .jpg, .jpeg")])       #On demande le fichier voulu et ça récupère (en tuple) le chemin du fichier
path = open_file[0]                                                                                   #On récupère le "path" en str et pas en tuple
img = cv2.imread(path, 2)                                                                             #On récup l'image dans python (et je la met en noir et blanc)
bin_image = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY ,11,2)    #Alors là en gros je scanne l'image, si il y'a un pixel d'une intensité de moins de 127 il est mis à 255 (blanc) sinon il est mit à 0 (noir), l'image est binaire comme sur un tableau (blanc ou noir)
hauteur = img.shape[0] 
largeur = img.shape[1]
cv2.imshow("image", bin_image)                                                                        #Affichage de l'image
cv2.waitKey(0)  

#Turtle
screen = turtle.Screen()
screen.screensize(largeur/-2, hauteur/2)
tortue = turtle.Turtle()
screen.tracer(2,0)

#Dessin Turtle 
for i in range(int(hauteur/2), int(hauteur/-2), -1):                                                  #On parcourt l'écran turtle de la hauteur max (hauteur/2 parce que c comme un graphique) à la hauteur minimale (hauteur/-2) avec un pas de -1, donc à reculons
    tortue.penup()                                                                                    #Faut bien que le stylo soit levé de base
    tortue.goto(int(largeur/-2),i)                                                                    #On va à tout à gauche de la hauteur actuelle (en gros on va au x le plus faible du y actuel)
    for l in range(int(largeur/-2), int(largeur/2)):                                                  #On parcourt le x de la hauteur actuelle (on va faire toutes les valeurs de x pour le y actuel)
        pixel_l = l + int(largeur/2)                                                                  #Là juste on convertit valeur turtle (donc en mode graphique) vers valeur image (donc sans valeur négatives) pour avoir le pixel largeur actuel
        pixel_h = int(hauteur/2) - i                                                                  #Même chose sauf que c'est pour la hauteur actuelle
        if bin_image[pixel_h,pixel_l] == 0:                                                           #En gros on check le pixel actuel sur l'image et on regarde si c'est noir bah on dessine le pixel alors
            tortue.pendown()
            tortue.forward(1)
        else:                                                                                         #Sinon on fait rien et on continue
            tortue.penup()
            tortue.forward(1)
    screen.update()

    
turtle.done()