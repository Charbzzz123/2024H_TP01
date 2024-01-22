# TODO : Créer un système d'alerte qui demande le niveau de charge de la batterie, affiche une représentation graphique si la charge est entre 0 et 100%, et affiche un message d'erreur en cas de charge en dehors de la plage normale.

niveau_charge = int(input("Entrez le niveau de charge actuel de la batterie :"))
if 0<=niveau_charge<=100:
    print(round(niveau_charge/10)*"❚")
else:
    print("Erreur : niveau de charge invalide.")
    
