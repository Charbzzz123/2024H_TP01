# TODO : Calculer les quantités de matériaux nécessaires pour fabriquer un nombre donné de baguettes magiques.

nombre_baguettes = int(input("Nombre de baguette a fabriquer: "))
# 3 piece de bois et 1 coeur de creature et 10ml de vernir par baguette
bois=3*nombre_baguettes
coeur=nombre_baguettes
vernie=10*nombre_baguettes
print('Voici les materiaux requis pour la fabrication de ',nombre_baguettes, 'baguettes magiques:')
print(bois,'piece(s) de bois')
print(coeur,'coeur(s) de creatures magiques')
print(vernie,'ml de vernis')