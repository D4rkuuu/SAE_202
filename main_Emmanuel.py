import noeud_huffman as nh
import os
import sys

input_dir = sys.argv[1]  # Dossier contenant les *.txt

for f in os.listdir(input_dir):
    if f.endswith('.txt'):
        f_path = os.path.abspath(os.path.join(input_dir, f))

        with open(f_path, 'r', encoding='utf-8') as file:
            content = file.read()

        print(f"\nFichier input/{f} chargé.")

        # Encodage du texte en ASCII
        encodageASCII = nh.Huffman.ascii_vers_base2(content)
        print("Encodage du texte ASCII OK.")

        # Calcul de la fréquence d'apparition de chaque caractère du texte
        liste_tuples = nh.Huffman.compter_lettres(content)

        # Construction de l'arbre de Huffman et compression du texte
        print("Construction de l'arbre de Huffman. Compression du texte.")
            # Construit l'arbre de Huffman le stocke dans la variable arbreHuffman
        arbreHuffman = nh.Huffman.lettres_noeuds(liste_tuples)
            # Génère les codes qui seront utilisés pour l'encodage
        codes = arbreHuffman.codes_huffman()
        print("Construction de l'arbre OK.         Compression OK.")

        # Compression du fichier txt
        texte_compresse = nh.Huffman.texte_to_code(content, codes)
        print("Taille initiale :     ", len(content) * 8, "bits")
        print("Taille compressée :   ", len(texte_compresse), "bits")
            # Calcul le taux de compression par rapport à la taille initiale du texte
        taux = (1 - len(texte_compresse) / (len(content) * 8)) * 100
        print(f"Taux de compression :  {taux:.2f}%")