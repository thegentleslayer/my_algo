import re
import random

caracteres_speciaux = ['أ', 'Б', 'シ', 'د', 'イ', 'ف', 'ج', 'ハ', 'И', 'ジ', 'ك', 'Л', 'م', 'Н', 'オ', 'П', 'ق', 'Р', 'セ', 'ت', 'У', 'В', 'و', 'Ку', 'У', 'з']

# Fonction pour substituer une lettre par un caractère spécial aléatoire
def substituer_lettre(lettre):
    if lettre.isalpha():
        return random.choice(caracteres_speciaux)
    else:
        return lettre

# Fonction pour déchiffrer un caractère spécial vers la lettre d'origine
def dechiffrer_caractere(caractere_chiffre):
    if caractere_chiffre in caracteres_speciaux:
        return 'X'  # Remplacez 'X' par la lettre d'origine associée à caractere_chiffre
    else:
        return caractere_chiffre

# Fonction de déchiffrement
def dechiffrement_substitution(message_chiffre):
    message_dechiffre = ""
    for caractere_chiffre in message_chiffre:
        message_dechiffre += dechiffrer_caractere(caractere_chiffre)

    return message_dechiffre

# Exemple d'utilisation avec un fichier texte.txt
def dechiffrement_substitution_fichier(chemin_fichier):
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            contenu_chiffre = fichier.read()

            # Afficher le texte chiffré
            print(f"Texte chiffré :\n{contenu_chiffre}\n")

            # Déchiffrer le texte
            contenu_dechiffre = dechiffrement_substitution(contenu_chiffre)

            # Afficher le résultat du déchiffrement
            print(f"Résultat du déchiffrement:\n{contenu_dechiffre}")

            return contenu_dechiffre
    except FileNotFoundError:
        return f"Le fichier {chemin_fichier} n'a pas été trouvé."

# Exemple d'utilisation avec un fichier texte.txt
chemin_fichier = 'texte.txt'
message_dechiffre = dechiffrement_substitution_fichier(chemin_fichier)
