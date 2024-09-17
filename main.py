"""
Exercice 5 - Palindromes
"""

#### Fonction secondaire

import string

def ispalindrome(s:str):
    """
    entrée:une chaine de caractère
    sortie:un booléen qui indique si la chaine est un palindrome
    """
    s=s.lower()
    accents=s.maketrans('àâäéèêëîïôöùûüç', 'aaaeeeeiioouuuc')
    ponctuation=s.maketrans('','', string.punctuation + ' ')
    traduite=s.translate(accents)
    s_finale=traduite.translate(ponctuation)
    if s_finale==s_finale[::-1]:
        return True
    return False

#### Fonction principale

def main():
    """
    fonction qui sert à appeler la fonction secondaire
    """
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
