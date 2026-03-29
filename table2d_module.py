"""
Module : table2d_module
Auteur : OpenAI

Ce module permet de :
1) Initialiser une table à deux dimensions avec des valeurs aléatoires.
2) Trier les éléments d'une table 2D selon plusieurs algorithmes.
3) Rechercher un élément dans une table 2D.

Les tris disponibles sont :
- tri à bulle
- tri rapide
- tri par sélection
- tri par insertion
- tri par fusion

Les recherches disponibles sont :
- recherche linéaire
- recherche binaire (itérative)
- recherche par dichotomie (récursive)

Principe choisi pour les tris :
--------------------------------
Pour simplifier le travail sur une table à deux dimensions, chaque algorithme
transforme d'abord la table 2D en une liste 1D, effectue le tri, puis reconstruit
la table 2D avec les mêmes dimensions.

Exemple :
Table 2D de départ
[
    [7, 2, 9],
    [1, 5, 3]
]

Aplatissement en liste 1D : [7, 2, 9, 1, 5, 3]
Après tri croissant         : [1, 2, 3, 5, 7, 9]
Reconstruction en table 2D  :
[
    [1, 2, 3],
    [5, 7, 9]
]

Remarque sur les recherches :
--------------------------------
- La recherche linéaire fonctionne sur n'importe quelle table 2D.
- La recherche binaire et la recherche par dichotomie nécessitent que la table
  ait été triée au préalable, car ces méthodes supposent un ordre croissant.
"""

from __future__ import annotations

import random
from typing import List, Optional, Tuple

Table2D = List[List[int]]
Coordonnee = Tuple[int, int]

# OUTILS GÉNÉRAUX
def generer_tableau_aleatoire(
    lignes: int,
    colonnes: int,
    minimum: int = 0,
    maximum: int = 100,
) -> Table2D:
    """
    Génère une table à deux dimensions initialisée aléatoirement.

    Paramètres :
    - lignes : nombre de lignes du tableau
    - colonnes : nombre de colonnes du tableau
    - minimum : valeur minimale possible
    - maximum : valeur maximale possible

    Retourne :
    - une liste de listes d'entiers

    Exemple :
    >>> generer_tableau_aleatoire(2, 3, 1, 9)
    [
    [4, 8, 1], 
    [6, 2, 7]
    ]
    """
    if lignes <= 0 or colonnes <= 0:
        raise ValueError("Le nombre de lignes et de colonnes doit être positif.")
    if minimum > maximum:
        raise ValueError("Le minimum ne peut pas être supérieur au maximum.")

    return [
        [random.randint(minimum, maximum) for _ in range(colonnes)]
        for _ in range(lignes)
    ]



def dimensions_tableau(tableau: Table2D) -> Tuple[int, int]:
    """
    Vérifie que le tableau 2D est valide et retourne ses dimensions.

    Un tableau 2D valide doit :
    - contenir au moins une ligne
    - contenir au moins une colonne
    - avoir le même nombre de colonnes sur chaque ligne
    """
    if not tableau or not tableau[0]:
        raise ValueError("Le tableau 2D ne doit pas être vide.")

    nb_colonnes = len(tableau[0])
    for ligne in tableau:
        if len(ligne) != nb_colonnes:
            raise ValueError("Toutes les lignes doivent avoir le même nombre de colonnes.")

    return len(tableau), nb_colonnes



def aplatir_tableau(tableau: Table2D) -> List[int]:
    """
    Transforme une table 2D en liste 1D.

    Exemple :
    [[3, 1], [5, 2]] -> [3, 1, 5, 2]
    """
    dimensions_tableau(tableau)
    return [element for ligne in tableau for element in ligne]



def reconstruire_tableau(elements: List[int], lignes: int, colonnes: int) -> Table2D:
    """
    Reconstruit une table 2D à partir d'une liste 1D en gardant les dimensions.

    Exemple :
    [1, 2, 3, 4], 2, 2 -> [[1, 2], [3, 4]]
    """
    if len(elements) != lignes * colonnes:
        raise ValueError("Le nombre d'éléments ne correspond pas aux dimensions demandées.")

    return [elements[i * colonnes:(i + 1) * colonnes] for i in range(lignes)]

def recherche_toutes_occurrences(tableau, valeur):
    positions = []

    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j] == valeur:
                positions.append((i, j))

    return positions
# TRIS

def tri_bulle(tableau: Table2D) -> Table2D:
    """
    Trie une table 2D par TRI À BULLE.

    Idée de l'algorithme :
    - On compare deux éléments voisins.
    - Si l'élément de gauche est plus grand que celui de droite, on les échange.
    - À chaque passage, les plus grands éléments "remontent" progressivement vers la fin.
    - On répète jusqu'à ce que toute la liste soit triée.

    Avec une table 2D :
    1) On l'aplatit en liste 1D.
    2) On applique le tri à bulle.
    3) On reconstruit la table 2D.
    """
    lignes, colonnes = dimensions_tableau(tableau)
    elements = aplatir_tableau(tableau)
    n = len(elements)

    for i in range(n):
        # À chaque tour, le plus grand élément restant se place en fin de liste.
        echange = False
        for j in range(0, n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                echange = True
        # Si aucun échange n'a eu lieu, la liste est déjà triée.
        if not echange:
            break

    return reconstruire_tableau(elements, lignes, colonnes)

def tri_selection(tableau: Table2D) -> Table2D:
    """
    Trie une table 2D par TRI PAR SÉLECTION.

    Idée de l'algorithme :
    - On cherche le plus petit élément dans la partie non triée.
    - On le place au début.
    - On recommence pour la position suivante.

    Avec une table 2D :
    1) Aplatissement.
    2) Tri par sélection.
    3) Reconstruction.
    """
    lignes, colonnes = dimensions_tableau(tableau)
    elements = aplatir_tableau(tableau)
    n = len(elements)

    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if elements[j] < elements[indice_min]:
                indice_min = j
        elements[i], elements[indice_min] = elements[indice_min], elements[i]

    return reconstruire_tableau(elements, lignes, colonnes)

def tri_insertion(tableau: Table2D) -> Table2D:
    """
    Trie une table 2D par TRI PAR INSERTION.

    Idée de l'algorithme :
    - On considère que la partie gauche est déjà triée.
    - On prend l'élément suivant.
    - On l'insère à la bonne place dans la partie déjà triée.

    Avec une table 2D :
    1) Aplatissement.
    2) Tri par insertion.
    3) Reconstruction.
    """
    lignes, colonnes = dimensions_tableau(tableau)
    elements = aplatir_tableau(tableau)

    for i in range(1, len(elements)):
        cle = elements[i]
        j = i - 1

        # On décale vers la droite tous les éléments plus grands que la clé.
        while j >= 0 and elements[j] > cle:
            elements[j + 1] = elements[j]
            j -= 1

        # On place ensuite la clé à la bonne position.
        elements[j + 1] = cle

    return reconstruire_tableau(elements, lignes, colonnes)

def _tri_rapide_liste(elements: List[int]) -> List[int]:
    """Fonction interne : tri rapide sur une liste 1D."""
    # Cas de base : une liste vide ou à un seul élément est déjà triée.
    if len(elements) <= 1:
        return elements[:]

    # On choisit un pivot. Ici, on prend l'élément du milieu.
    pivot = elements[len(elements) // 2]

    # On découpe la liste en trois parties.
    inferieurs = [x for x in elements if x < pivot]
    egaux = [x for x in elements if x == pivot]
    superieurs = [x for x in elements if x > pivot]

    # On trie récursivement les sous-listes puis on les rassemble.
    return _tri_rapide_liste(inferieurs) + egaux + _tri_rapide_liste(superieurs)



def tri_rapide(tableau: Table2D) -> Table2D:
    """
    Trie une table 2D par TRI RAPIDE.

    Idée de l'algorithme :
    - On choisit un pivot.
    - On sépare les éléments en trois groupes :
      * plus petits que le pivot
      * égaux au pivot
      * plus grands que le pivot
    - On applique récursivement la même méthode aux sous-groupes.

    Avec une table 2D :
    1) Aplatissement.
    2) Tri rapide.
    3) Reconstruction.
    """
    lignes, colonnes = dimensions_tableau(tableau)
    elements = aplatir_tableau(tableau)
    elements_tries = _tri_rapide_liste(elements)
    return reconstruire_tableau(elements_tries, lignes, colonnes)


def _fusion(gauche: List[int], droite: List[int]) -> List[int]:
    """Fusionne deux listes triées en une seule liste triée."""
    resultat = []
    i = 0
    j = 0

    # On compare l'élément courant de chaque liste et on ajoute le plus petit.
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1

    # On ajoute les éléments restants.
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat

def _tri_fusion_liste(elements: List[int]) -> List[int]:
    """Fonction interne : tri fusion sur une liste 1D."""
    if len(elements) <= 1:
        return elements[:]

    milieu = len(elements) // 2
    gauche = _tri_fusion_liste(elements[:milieu])
    droite = _tri_fusion_liste(elements[milieu:])
    return _fusion(gauche, droite)

def tri_fusion(tableau: Table2D) -> Table2D:
    """
    Trie une table 2D par TRI PAR FUSION.

    Idée de l'algorithme :
    - On coupe la liste en deux parties.
    - On trie chaque moitié récursivement.
    - On fusionne ensuite les deux moitiés triées.

    Avec une table 2D :
    1) Aplatissement.
    2) Tri fusion.
    3) Reconstruction.
    """
    lignes, colonnes = dimensions_tableau(tableau)
    elements = aplatir_tableau(tableau)
    elements_tries = _tri_fusion_liste(elements)
    return reconstruire_tableau(elements_tries, lignes, colonnes)

# RECHERCHES

def recherche_lineaire(tableau: Table2D, valeur: int) -> Optional[Coordonnee]:
    """
    Recherche une valeur dans une table 2D par RECHERCHE LINÉAIRE.

    Idée de l'algorithme :
    - On parcourt chaque ligne.
    - Dans chaque ligne, on parcourt chaque colonne.
    - Dès qu'on trouve la valeur, on retourne sa position (ligne, colonne).

    Cette méthode fonctionne même si le tableau n'est pas trié.

    Retour :
    - (indice_ligne, indice_colonne) si trouvé
    - None sinon
    """
    dimensions_tableau(tableau)

    for i, ligne in enumerate(tableau):
        for j, element in enumerate(ligne):
            if element == valeur:
                return (i, j)
    return None

def recherche_binaire(tableau: Table2D, valeur: int) -> Optional[Coordonnee]:
    """
    Recherche une valeur dans une table 2D par RECHERCHE BINAIRE itérative.

    Condition importante :
    - Le tableau doit déjà être trié en ordre croissant.

    Idée de l'algorithme :
    - On travaille sur la version aplatie du tableau.
    - On compare la valeur recherchée avec l'élément du milieu.
    - Si la valeur est plus petite, on cherche à gauche.
    - Si elle est plus grande, on cherche à droite.
    - On répète jusqu'à trouver l'élément ou épuiser la recherche.
    """
    lignes, colonnes = dimensions_tableau(tableau)
    elements = aplatir_tableau(tableau)

    gauche = 0
    droite = len(elements) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2

        if elements[milieu] == valeur:
            return (milieu // colonnes, milieu % colonnes)
        if elements[milieu] < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    return None

def _dichotomie_recursive(
    elements: List[int],
    valeur: int,
    gauche: int,
    droite: int,
) -> int:
    """
    Fonction interne : recherche par dichotomie récursive sur une liste triée.

    Retourne l'indice trouvé ou -1.
    """
    if gauche > droite:
        return -1

    milieu = (gauche + droite) // 2

    if elements[milieu] == valeur:
        return milieu
    if valeur < elements[milieu]:
        return _dichotomie_recursive(elements, valeur, gauche, milieu - 1)
    return _dichotomie_recursive(elements, valeur, milieu + 1, droite)

def recherche_dichotomie(tableau: Table2D, valeur: int) -> Optional[Coordonnee]:
    """
    Recherche une valeur dans une table 2D par DICHOTOMIE récursive.

    Condition importante :
    - Le tableau doit déjà être trié en ordre croissant.

    Différence retenue ici :
    - recherche_binaire : version itérative
    - recherche_dichotomie : version récursive

    Retour :
    - (ligne, colonne) si trouvé
    - None sinon
    """
    lignes, colonnes = dimensions_tableau(tableau)
    elements = aplatir_tableau(tableau)
    indice = _dichotomie_recursive(elements, valeur, 0, len(elements) - 1)

    if indice == -1:
        return None

    return (indice // colonnes, indice % colonnes)
# FONCTION D'AFFICHAGE
def afficher_tableau(tableau):
    max_val = max(max(ligne) for ligne in tableau)
    largeur = len(str(max_val)) + 2

    for ligne in tableau:
        print("|", end="")
        for val in ligne:
            print(f"{val:{largeur}}", end="")
        print(" |")



# TESTS SIMPLES LORSQUE LE MODULE EST LANCÉ DIRECTEMENT
if __name__ == "__main__":
    print("=== TEST DU MODULE table2d_module ===")

    tableau = generer_tableau_aleatoire(3, 4, 1, 20)
    print("\nTableau initial :")
    afficher_tableau(tableau)

    print("\nTri à bulle :")
    afficher_tableau(tri_bulle(tableau))

    print("\nTri rapide :")
    afficher_tableau(tri_rapide(tableau))

    print("\nTri par sélection :")
    afficher_tableau(tri_selection(tableau))

    print("\nTri par insertion :")
    afficher_tableau(tri_insertion(tableau))

    print("\nTri par fusion :")
    tableau_trie = tri_fusion(tableau)
    afficher_tableau(tableau_trie)

    valeur = tableau_trie[1][1]
    print(f"\nRecherche linéaire de {valeur} :", recherche_lineaire(tableau, valeur))
    print(f"Recherche binaire de {valeur} :", recherche_binaire(tableau_trie, valeur))
    print(f"Recherche par dichotomie de {valeur} :", recherche_dichotomie(tableau_trie, valeur))
