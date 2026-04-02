import noeud_huffman as nh

texte = "akramlebgdu94@"

resultat = nh.Huffman.compter_lettres(texte)

print(resultat)

<<<<<<< HEAD
print(nh.Huffman.ascii_vers_base2(texte))
=======
noeuds = []

for lettre, poids in resultat.items():
    noeuds.append(nh.Huffman(lettre, poids, None, None))

arbre = nh.Huffman.lettres_noeuds(noeuds)

print(noeuds)
print(arbre)

>>>>>>> origin/dev_adrien
