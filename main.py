# somme de deux valeurs
import math


def sum_two_values(value_one: int, value_two: int):
    print(value_one + value_two)

# l'utilisateur , saisie deux valeurs et on affiche la somme
# nous pouvons varier cela avec une soustraction ou encore multiplication
def user_write_sum():
    value_one = int(input("valeur une :"))
    value_two = int(input("valeur deux :"))
    sum_two_values(value_one,value_two)


def show_max_value(value_one: int, value_two: int):
    if value_one > value_two:
        print(value_one)
    else:
        print(value_two)


def major_or_not_major():
    #l'utilisateur saisi son age, dans un nombre entier et on lui affiche un texte selon son age
    # si son age est à 18 ou plus : "Vous êtes majeur" , sinon, "vous êtes mineur !"
    age : int = int(input("Entrez votre age : "))
    if age >= 18:
        print('Vous êtes majeur')
    else:
        print('Vous êtes mineur')

#José va bientot passer son bac, il effectue en ce moment une anti-seche en python qui lui permet de lui donner
# la longueur de l'hypothenuse
# vous devez utiliser le théorème de Pythagore et afficher la longueur de l'hypothenuse
def pythagore(cote_un : float, cote_deux : float):
    hypothenuse : float = math.sqrt(cote_un **2 + cote_deux **2)
    print('l\'hypothenuse est : ' + str(hypothenuse))


# José, désire un programme qui permet de lui donner la mention en fonction de la note
# Vous devrez concevoir un algorithme qui demandera une note à l'utilisateur et affichera un texte selon le bareme
# en dessous de 8 : refusé
# entre 8 inclus et 10 exclus : rattrapage
# entre 10 inclus et 12 exlus : pas de mention
# entre 12 inclus et 14 exclus : mention assez bien
# entre 14 inclus et 16 exclus : mention bien
# au dela de 16 inclus : très bien
def mention_bac():
    note = float(input("Veuillez entrez votre note : "))
    if note < 8:
        print('refusé')
    elif 8 <= note < 10:
        print('rattrapage')
    elif 10 <= note and note < 12:
        print('pas de mention')
    elif 12 <= note < 14:
        print('mention assez bien')
    elif 14 <= note and note < 16:
        print('mention bien')
    elif note >= 16:
        print('tres bien')


#José, après avoir eu son bac, a fait une grosse fete
# il culpabilise car il a trop mangé et souhaite connaitre son IMC.
# demander les le poid ainsi que la taille à l'utilisateur et affichez son IMC
# L'imc est le poid (en kg) divisé ar la taille (en m) au carré.
def imc():
    poid: float = float(input("Entrez votre poid en kg"))
    taille: float = float(input("Entrez votre taille en m"))
    value_imc: float = poid / (taille**2)
    print("votre IMC est de " + str(value_imc))

def pair_or_impar():
    # l'utilisateur doit saisir un nombre entier: on lui affiche s'il est pair ou impair
    # pair si quand il est divisé par deux, le reste est de 0
    nombre: int = int(input("Entrez un nombre entier"))

    if nombre % 2 == 0:
        print('pair')
    else:
        print('impair')


# division, attention au 0 !
# Pour rappel, une division par 0 est interdite
def division_two_values(numerator: int, denumerator: int):
    # TODO


#José est revenu pour nous tester un peu !
# Il a constaté que vous avez fait pas mal d'exercice en Python.
# Ainsi, il vous demande de lui donner la clef de controle de sa carte de sécurité sociale
# la clef de controle = 97 - (numero de sécurité sociale modulo 97) (le numero de securité sociale est de 13 chiffres)
# exemple : pour le code sécurité sociale 1921071123456 la clef est de 15.
def key_control_health(securite_social_num : int):
    # TODO

def premier_or_not_premier():
    # on demande à l'utilisateur un nombre entier, on lui affiche s'il est premier ou non
    # regle : un nombre est premier seulement s'il est divisible par 1 et lui-même , 1 exclu
    nombre: int = int(input("Entrez un nombre entier"))
    if nombre == 1:
        print('non premier')
    else:
        for i in range(2,nombre):
            if i % nombre == 0 and nombre != i:
                print('ce n\'est pas un nombre premier')
                break
            else:
                print('c\'est un nombre premier')
