import noeud_huffman as nh
import os
import sys
import csv

input_dir = sys.argv[1]  # Dossier contenant les *.txt
output_csv = "resultats.csv"

for f in os.listdir(input_dir):
    if f.endswith('.txt'):
        f_path = os.path.abspath(os.path.join(input_dir, f))

        with open(f_path, 'r', encoding='utf-8') as file:
            content = file.read()

        print(f"\nFichier input/{f} chargé.")

        # Encodage du texte en ASCII
        encodageASCII = nh.Huffman.ascii_vers_base2(content)
        print("Encodage du texte ASCII OK.")

        # Supression des accents du texte
        new_content = nh.Huffman.enlever_accents(content)

        # Calcul de la fréquence d'apparition de chaque caractère du texte
        liste_tuples = nh.Huffman.compter_lettres(new_content)

        # Construction de l'arbre de Huffman et compression du texte
        print("Construction de l'arbre de Huffman. Compression du texte.")
            # Construit l'arbre de Huffman le stocke dans la variable arbreHuffman
        arbreHuffman = nh.Huffman.lettres_noeuds(liste_tuples)
            # Génère les codes qui seront utilisés pour l'encodage
        codes = arbreHuffman.codes_huffman()
        print("Construction de l'arbre OK.         Compression OK.")

        # Compression du fichier txt
        texte_compresse = nh.Huffman.texte_to_code(new_content, codes)
        taille_initiale = len(new_content) * 8
        taille_compresse = len(texte_compresse)
        print("Taille initiale :     ", taille_initiale, "bits")
        print("Taille compressée :   ", taille_compresse, "bits")
            # Calcul le taux de compression par rapport à la taille initiale du texte
        taux = (1 - taille_compresse / taille_initiale) * 100
        print(f"Taux de compression :  {taux:.2f}%")


        #--- CSV ---
        fichier_existe = os.path.isfile(output_csv)

        with open(output_csv, mode="a", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier, delimiter=';')

            if not fichier_existe:
                writer.writerow(["Texte", "Taille initiale", "Taille compressée", "Taux de compression"])

            writer.writerow([f, f"{taille_initiale} bits", f"{taille_compresse} bits", f"{round(taux, 2)}%"])

        print(f"Résultat enregistré dans le CSV: {f}, {taille_initiale} bits, {taille_compresse} bits, {round(taux, 2)}%")