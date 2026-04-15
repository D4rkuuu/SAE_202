import sys
import os

dossier_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, dossier_parent)

import noeud_huffman as nh
from noeud_huffman import Huffman

print("\n\n-----------------------------------Test fonctionnalités noeud huffman")


texte = Huffman.enlever_accents("Je pense que nous avons enfin fini la SAÉ")

print(f"Texte à encoder : {texte}")

print("\n------------Étape 1 — Effectif de chaque caractère du texte")
liste_tuples = nh.Huffman.compter_lettres(texte) # Génère les tuples (Caractère, effectif)
liste_tuples_triee = sorted(liste_tuples, key=lambda x: x[1], reverse=True) # Trie la liste dans l'ordre décroissant des effectifs

print ("Liste des binômes (Caractère, effectif) :",liste_tuples_triee)    # Affiche la liste de tuples (Caractère, effectif)

print(nh.Huffman.ascii_vers_base2(texte))

print("\n------------Étape 2 — Construction de l’arbre de Huffman")
arbreHuffman = nh.Huffman.lettres_noeuds(liste_tuples) # Construit l'arbre
print (arbreHuffman)                                   # Affiche l'arbre
print("Nombre de noeuds présent dans l'arbre:", nh.Huffman.nb_NoeudHuffman)
print("Hauteur de l'arbre:", arbreHuffman.hauteur())


# Génération des codes pour l'encodage
codes = arbreHuffman.codes_huffman()

# Affichage des codes
print("\nListe des codes de Huffman du texte:", codes)

# Affichage du texte en base 2 et encodé
print(f"Texte en base 2  : {Huffman.ascii_vers_base2(texte)}")
print(f"Encodage Huffman : {Huffman.texte_to_code(texte,codes)}")

# Différents parcours de l'arbre
print("\nParcours en largeur :")
arbreHuffman.parcoursLargeur()
print("Parcours infixe :")
arbreHuffman.parcoursInfixe()
print("Parcours suffixe :")
arbreHuffman.parcoursSuffixe()
print("Parcours préfixe :")
arbreHuffman.parcoursPrefixe()
