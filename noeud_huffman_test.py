import noeud_huffman as nh

texte = "Ô rage ! ô désespoir ! ô vieillesse ennemie ! N’ai-je donc tant vécu que pour cette infamie ? Le Cid, Corneille Acte I, scène 4"

resultat = nh.Huffman.compter_lettres(texte)

print(resultat)

print(nh.Huffman.ascii_vers_base2(texte))

noeuds = []

for lettre, poids in resultat.items():
    noeuds.append(nh.Huffman(lettre, poids, None, None))

arbre = nh.Huffman.lettres_noeuds(noeuds)

print(noeuds)
print(arbre)

# Pipeline complet
compteur = nh.Huffman.compter_lettres(texte)
noeuds = [nh.Huffman(lettre, freq) for lettre, freq in compteur.items()]
racine = nh.Huffman.lettres_noeuds(noeuds)

# Générer les codes
codes = racine.codes_huffman()
for lettre, code in codes.items():
    print(f"'{lettre}' -> {code}")

