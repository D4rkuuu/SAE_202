import noeud_huffman as nh
import os
import sys

input_dir = sys.argv[1]  # Dossier contenant les *.txt

for f in os.listdir(input_dir):
    if f.endswith('.txt'):
        f_path = os.path.abspath(os.path.join(input_dir, f))

        with open(f_path, 'r', encoding='utf-8') as file:
            content = file.read()

        print(f"\n=== Fichier : {f} ===")

        # Étape 1 — on passe le TEXTE, pas le dossier
        liste_tuples = nh.Huffman.compter_lettres(content)
        liste_tuples_triee = sorted(liste_tuples, key=lambda x: x[1], reverse=True)
        print("Liste des binômes :", liste_tuples_triee)

        # Étape 2 — Construction de l'arbre
        arbreHuffman = nh.Huffman.lettres_noeuds(liste_tuples)
        print("Hauteur de l'arbre:", arbreHuffman.hauteur())

        # Étape 3 — Génération des codes
        codes = arbreHuffman.codes_huffman()
        print("Codes Huffman :", codes)

        # Étape 4 — Compression
        texte_compresse = nh.Huffman.texte_to_code(content, codes)
        print("Texte original   :", len(content) * 8, "bits")
        print("Texte compressé  :", len(texte_compresse), "bits")
        taux = (1 - len(texte_compresse) / (len(content) * 8)) * 100
        print(f"Taux de compression : {taux:.2f}%")