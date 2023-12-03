import re
import random

def my_algorithm(chemin_fichier):
    # Liste des caractères spéciaux
    caracteres_speciaux = ['أ', 'Б', 'シ', 'د', 'イ', 'ف', 'ج', 'ハ', 'И', 'ジ', 'ك', 'Л', 'م', 'Н', 'オ', 'П', 'ق', 'Р', 'セ', 'ت', 'У', 'В', 'و', 'クス', 'У', 'ز']

    # Fonction pour substituer une lettre par un caractère spécial aléatoire
    def substituer_lettre(lettre):
        if lettre.isalpha():
            return random.choice(caracteres_speciaux)
        else:
            return lettre

    def chiffrement_substitution(message):
        message_chiffre = ""
        for caractere in message:
            message_chiffre += substituer_lettre(caractere)

        return message_chiffre

    def chiffrement_substitution_fichier(chemin_fichier):
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu_original = fichier.read()
                contenu_chiffre = chiffrement_substitution(contenu_original)

                # Afficher le résultat de la première substitution
                print(f"Résultat de la première substitution:\n{contenu_chiffre}\n")

                # Ajouter l'étape de découpage et mélange
                contenu_mele = decoupage_et_melange(contenu_chiffre)

                # Afficher le résultat du découpage et mélange
                print(f"Résultat du découpage et du mélange:\n{contenu_mele}")

                return contenu_mele
        except FileNotFoundError:
            return f"Le fichier {chemin_fichier} n'a pas été trouvé."

    def decoupage_et_melange(texte_chiffre):
        # Diviser le texte en morceaux (par exemple, des mots)
        morceaux = re.findall(r'\b\w+\b', texte_chiffre)

        # Mélanger les morceaux de manière aléatoire
        random.shuffle(morceaux)

        # Reconstruire le texte à partir des morceaux mélangés
        texte_mele = ' '.join(morceaux)

        return texte_mele

    # Appeler la fonction principale et retourner le résultat
    return chiffrement_substitution_fichier(chemin_fichier)

# Appeler la fonction globale avec le chemin du fichier
chemin_fichier = 'texte.txt'
message_chiffre_mele = my_algorithm(chemin_fichier)