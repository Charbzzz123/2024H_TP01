# TODO : Créer un système d'alerte qui demande le niveau de charge de la batterie, affiche une représentation graphique si la charge est entre 0 et 100%, et affiche un message d'erreur en cas de charge en dehors de la plage normale.

niveau_charge = int(input("Entrez le niveau de charge actuel de la batterie :"))
niveau_chargea=niveau_charge
t=' ['
if 0<=niveau_chargea<=100:
    r=round(niveau_chargea/10)
    t=t+r*'❚'
    
    print(t+(10-r)*' '+']')
    print(str(niveau_charge)+'%')
else:
    print(" Erreur : niveau de charge invalide.")
