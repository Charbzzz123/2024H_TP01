# TODO : Analyser le message crypté de l'Empire, compter le nombre d'occurrences des voyelles "a", "e", "i", "o", "u" et "y", puis assembler les résultats en une coordonnée galactique.

message = input("Entrez le message de l'Empire : ")
a=message.count('a')+message.count('A')
e=message.count('e')+message.count('E')
i=message.count('i')
o=message.count('o')
u=message.count('u')
y=message.count('y')+message.count('Y')
print('Les coordonnees galactiques sont' ,str(a)+"."+str(e)+"."+str(i)+"."+str(o)+"."+str(u)+"."+str(y)+".")
