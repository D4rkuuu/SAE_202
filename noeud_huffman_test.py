import noeud_huffman as nh

texte = "bonjourbonsoir"

# Compte les lettres et renvoie une liste de tuples triée
liste_tuples = nh.Huffman.compter_lettres(texte)
print (liste_tuples)

# Construit l'arbre
racine = nh.Huffman.lettres_noeuds(liste_tuples)
print (racine)

# Génère les codes pour l'encodage
codes = racine.codes_huffman()


# Affichage
print("\nListe des codes de Huffman")
print (codes)