# TODO : Écrire un programme qui demande le pourcentage de charge actuel de la batterie de la Batmobile, calcule le temps restant en minutes en fonction de ce pourcentage, et affiche le résultat au format "XXhYYmin". Assurer la gestion des pourcentages valides et des messages d'erreur appropriés.
niveau_charge=int(input("Entrez le pourcentage de charge actuel de la batterie de la Batmobile :"))

Time=0 #temps en minute que
if 0<=niveau_charge<=100:
    
    if niveau_charge>=51:
        N1min=niveau_charge-50 #(51-1 puisque faut inclure 51% avant qu'il devient 50% ce 1% de difference appartien au intervalle 1 minute)
        Time1=N1min*1
        Time=Time+N1min
        niveau_charge=niveau_charge-N1min

    if 6<=niveau_charge<=50:
        N2min=niveau_charge-5 #(6-1 puisque faut inclure 6% de ce qui reste)
        Time2=N2min*2
        Time=Time+Time2
        niveau_charge=niveau_charge-N2min
        
    if 1<=niveau_charge<=5:
        N3min=niveau_charge
        Time3=N3min*5
        Time=Time+Time3
        niveau_charge=niveau_charge-N3min
        
    h=Time//60
    m=Time%60
    print(" Temps restant :","%01dh%02dmin" % (h, m) )
    4
else:
    print(" Erreur : niveau de charge invalide.")
