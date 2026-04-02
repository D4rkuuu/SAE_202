import noeud_nh.huffman  as nh

texte = "Ô rage ! ô désespoir ! ô vieillesse ennemie ! N’ai-je donc tant vécu que pour cette infamie ? Le Cid, Corneille Acte I, scène 4"

resultat = nh.huffman .compter_lettres(texte)

print(resultat)

print(nh.huffman .ascii_vers_base2(texte))

noeuds = []

for lettre, poids in resultat.items():
    noeuds.append(nh.huffman (lettre, poids, None, None))

arbre = nh.huffman .lettres_noeuds(noeuds)

print(noeuds)
print(arbre)

# Pipeline complet
compteur = nh.nh.huffman .compter_lettres(texte)
noeuds = [nh.nh.huffman (lettre, freq) for lettre, freq in compteur.items()]
racine = nh.nh.huffman .lettres_noeuds(noeuds)

# Générer les codes
codes = racine.codes_nh.huffman ()
for lettre, code in codes.items():
    print(f"'{lettre}' -> {code}")

    compteur = nh.huffman .compter_lettres(texte)
    noeuds = [nh.huffman (lettre, freq) for lettre, freq in compteur.items()]
    racine = nh.huffman .lettres_noeuds(noeuds)
    codes = racine.codes_nh.huffman ()

    # Étape 2 : encoder le texte avec nh.huffman 
    texte_encode = ""
    for c in texte:
        texte_encode += codes[c]
    print("huffman    :", texte_encode)

    # Étape 3 : convertir le texte original en binaire ASCII
    texte_ascii = nh.huffman .ascii_vers_base2(texte)
    print("ASCII bin :", texte_ascii)

    # Étape 4 : comparer les tailles
    print(f"\nTaille ASCII   : {len(texte_ascii)} bits")
    print(f"Taille nh.huffman  : {len(texte_encode)} bits")
    print(f"Gain           : {len(texte_ascii) - len(texte_encode)} bits")