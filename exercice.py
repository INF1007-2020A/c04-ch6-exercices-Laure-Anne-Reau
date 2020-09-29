#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string


def order(values: list = None) -> list:
#    if values is None:
#        # TODO: demander les valeurs ici
#        Liste = input("veuillez entrer les valeurs séparées par une virgule: ")
        
        pass

#    return 


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        pass

    return False


def contains_doubles(items: list) -> bool:
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
#    best_student = dict()
#    for key, value in student_grades.items():
#        avg = sum(value) / len(value)
#        #if len(best_student) == 0 or list(best_student.values())[0] < avg:
#        #    best_student = {key: avg}
#        student_grades[key] = avg

#    best_student = max(student_grades, key=student_grades, )    
#    return {best_student: student_grades[best_student]}
    pass

def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequency = dict()

    for letter in sentence :
        frequency[letter] = sentence.count(letter)

    sorted_keys = sorted(frequency, key=frequency.__getitem__, reverse=True)

    for key in sorted_keys:
        if frequency[key] > 5:
            print("Le caractère {0} revient {1} fois.".format(key, frequency[key]))

    return {}


def get_recipes(dictionnaire):
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Entrez le nom de votre recette.\n")
    ingrediants = input("Entrez la liste d'ingrédients de la recette, svp séparer les ingrédients par une virgule.\n")

    return {name: ingrediants}



def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
#    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
