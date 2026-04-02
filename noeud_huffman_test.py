import noeud_huffman as nh

texte = "akramlebgdu94@"

resultat = nh.Huffman.compter_lettres(texte)

print(resultat)

print(nh.Huffman.ascii_vers_base2(texte))