import noeud_huffman as nh

texte = "bonjourbonsoir"

resultat = nh.Huffman.compter_lettres(texte)

print(resultat)

noeuds = []

for lettre, poids in resultat.items():
    noeuds.append(nh.Huffman(lettre, poids, None, None))

arbre = nh.Huffman.lettres_noeuds(noeuds)

print(noeuds)
print(arbre)

