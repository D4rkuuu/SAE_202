import noeud_binaire as nb

g = nb.NoeudBinaire('G', None, None) # Arbre de valeur 'G', sans sous-arbre (feuille)
# Arbre de valeur 'F'. Sous-arbre gauche : g. Pas sous-arbre droit.
f = nb.NoeudBinaire('F', g, None)
# Arbre de valeur 'E'. Pas de sous-arbre gauche. Sous-arbre droit : f
e = nb.NoeudBinaire('E', None, f)
d = nb.NoeudBinaire('D', None, None) # Arbre de valeur 'D', sans sous-arbres (feuille)
c = nb.NoeudBinaire('C', None, None) # Arbre de valeur 'C', sans sous-arbres (feuille)
# Arbre de valeur 'B', sous-arbre gauche : c. Sous-arbre droit : d.
b = nb.NoeudBinaire('B', c, d)
# Arbre de valeur 'A', sous-arbre gauche : b. Sous-arbre droit : e.
a = nb.NoeudBinaire('A', b, e)

print(a.hauteur())