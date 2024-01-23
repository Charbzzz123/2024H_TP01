# TODO : Calculer la distance que chaque rocher lancé par les catapultes peut atteindre en utilisant la formule de la portée d'un projectile.
from math import *
vitesse_initiale = float(input('Entrez la vitesse initiale (en m/s) : '))
angle_lancement = float(input("Entrez l'angle de lancement (en degres) : "))
rad=angle_lancement*pi/180
g=9.81
x=(vitesse_initiale**2)*sin(2*rad)/g
print("La distance parcourue par le projectile est de",f"{x:.2f}","metres.")


