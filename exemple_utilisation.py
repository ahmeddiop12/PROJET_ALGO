import table2d_module as t2d

# CREATION DU TABLEAU
tableau = t2d.generer_tableau_aleatoire(6, 6, 1, 100)
print("=== TABLEAU INITIAL ===")
t2d.afficher_tableau(tableau)

# CHOIX DU TRI
print("\n=== CHOIX DU TRI ===")
print("1 - Tri à bulle")
print("2 - Tri rapide")
print("3 - Tri par sélection")
print("4 - Tri par insertion")
print("5 - Tri par fusion")

choix_tri = input("Choisissez un type de tri : ")

if choix_tri == "1":
    tableau_trie = t2d.tri_bulle(tableau)
elif choix_tri == "2":
    tableau_trie = t2d.tri_rapide(tableau)
elif choix_tri == "3":
    tableau_trie = t2d.tri_selection(tableau)
elif choix_tri == "4":
    tableau_trie = t2d.tri_insertion(tableau)
elif choix_tri == "5":
    tableau_trie = t2d.tri_fusion(tableau)
else:
    print("Choix invalide, tri fusion par défaut.")
    tableau_trie = t2d.tri_fusion(tableau)

print("\n=== TABLEAU TRIÉ ===")
t2d.afficher_tableau(tableau_trie)

# CHOIX DE LA VALEUR A CHERCHER
print("\n=== RECHERCHE ===")
valeur = int(input("Entrez la valeur à rechercher : "))

# CHOIX DU TYPE DE RECHERCHE
print("\n=== TYPE DE RECHERCHE ===")
print("1 - Recherche linéaire")
print("2 - Recherche binaire")
print("3 - Recherche par dichotomie")

choix_recherche = input("Choisissez une méthode : ")

if choix_recherche == "1":
    resultat = t2d.recherche_lineaire(tableau, valeur)

elif choix_recherche == "2":
    resultat = t2d.recherche_binaire(tableau_trie, valeur)

elif choix_recherche == "3":
    resultat = t2d.recherche_dichotomie(tableau_trie, valeur)

else:
    print("Choix invalide pour la recherche.")
    resultat = None
# RESULTAT
# if resultat is not None:
#     ligne, colonne = resultat
#     print(" Valeur trouvée à la position (Ligne, Colonne) : ({ligne}, {colonne})")
# else:
#     print("\n Valeur non trouvée dans le tableau.")
# RESULTAT AVEC OCCURRENCES
positions = t2d.recherche_toutes_occurrences(tableau_trie, valeur)

# RESULTAT AVEC TOUTES LES OCCURRENCES
positions = t2d.recherche_toutes_occurrences(tableau_trie, valeur)

if positions:
    if len(positions) > 1:
        print("La valeur recherchée a plusieurs occurrences :")
    else:
        print("La valeur recherchée a une seule occurrence :")

    # afficher toutes les positions
    for ligne, colonne in positions:
        print(f"→ Position (Ligne, Colonne) : ({ligne}, {colonne})")

else:
    print("Valeur non trouvée dans le tableau.")