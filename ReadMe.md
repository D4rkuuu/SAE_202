# ReadMe | SAÉ 202 Exploration algorithmique d’un problème 
## Compression de texte avec l'algorithme de Huffman

## Description

Ce projet implémente l'algorithme de **compression de Huffman** en Python.
Il permet de lire des fichiers texte, de les compresser, puis de comparer la taille initiale et la taille compressée.

Les résultats sont automatiquement enregistrés dans un fichier CSV afin d'analyser les performances de compression.

---

## Fonctionnalités

* Lecture de fichiers `.txt` depuis un dossier
* Suppression des accents pour normaliser le texte
* Encodage ASCII en binaire
* Construction d’un arbre de Huffman
* Génération des codes binaires optimisés
* Compression du texte
* Calcul du taux de compression
* Export des résultats dans un fichier CSV

---

## Structure du projet

```
.
├── Docu
    ├── s202_cahierDesCharges.pdf
    ├── s202_cahierTechniques.txt
    └── s202_presentation.pdf
├── input 
    ├── aLaRechercheDuTempsPerdu.txt
    ├── leCid.txt
    ├── leSavetierEtLeFinancier.txt
    ├── lesMiserables.txt
    └── marcheTrain.txt
├── .gitignore
├── main.py
├── noeud_binaire.py
├── noeud_huffman.py
└── resultats.csv (généré automatiquement)
```

### 🔹 main.py

* Programme principal
* Parcourt les fichiers `.txt`
* Applique la compression
* Calcule les performances
* Sauvegarde les résultats dans un CSV

### 🔹 noeud_binaire.py

* Implémentation d’un arbre binaire
* Gestion des noeuds (gauche, droite, hauteur, etc.)
* Méthodes utilitaires pour manipuler l’arbre
* Possibilité de parcourir l'arbre en largeur, affixe et infixe

### 🔹 noeud_huffman.py

* Hérite de `NoeudBinaire`
* Implémente l’algorithme de Huffman :

  * Comptage des caractères
  * Construction de l’arbre
  * Génération des codes
  * Encodage du texte

---

## Utilisation

### 1. Cloner le projet

```bash
git clone https://github.com/ton-projet.git
cd ton-projet
```

### 2. Lancer le programme

```bash
python main.py chemin/vers/dossier
```

Exemple :

```bash
python main.py input/
```

---

## Résultats

Le programme génère un fichier `resultats.csv` contenant :

* Nom du fichier
* Taille initiale (bits)
* Taille compressée (bits)
* Taux de compression (%)

---

## Détails techniques

### 🔸 Algorithme de Huffman

* Basé sur la fréquence d’apparition des caractères
* Utilise un arbre binaire
* Les caractères fréquents ont des codes courts
* Les caractères rares ont des codes longs

### 🔸 Étapes de compression

1. Nettoyage du texte (suppression des accents)
2. Comptage des occurrences
3. Construction de l’arbre
4. Génération des codes binaires
5. Encodage du texte

---

## Auteur

Projet réalisé dans le cadre de la SAÉ 202 par Le Groupe B1 :

* Emmanuel Appiah
* Akram Ben Abdallah 
* Adrien Roj
