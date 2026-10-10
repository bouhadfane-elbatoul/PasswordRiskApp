# 🔐 Password Risk Predictor

Application web (Streamlit) qui estime le temps de craquage d'un mot de passe
et lui attribue un niveau de risque (Critique / Élevé / Modéré / Fort).

## Comment ça marche
- Détection du jeu de caractères (minuscules, majuscules, chiffres, symboles)
- Calcul de l'entropie : longueur × log2(taille du jeu de caractères)
- Régression linéaire (équation normale, NumPy) qui prédit le log du temps de craquage
- Entraînement sur un dataset synthétique de 2000 échantillons (10⁹ essais/s)

## Installation
pip install -r requirements.txt
streamlit run app.py

## Limites
Le modèle ne détecte pas les mots de passe courants ni les patterns
(ex. Password1!). Projet à but éducatif.

## Auteur
Bouhadfane Elbatoul
