#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        my_list = []
        while len(my_list) < 10:
            my_list.append(input("please enter a value: "))
    return sorted(my_list)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        word1 = input("Please enter a first word: ")
        word2 = input("Please enter a second word: ")
        my_words = [word1, word2]
        return sorted(my_words[0]) == sorted(my_words[1])


def contains_doubles(items: list) -> bool:
    for c in items:
        return items.count(c) > 1
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict()
    for key, value in student_grades.items():
        average = sum(value) / len(value)
        if len(best_student) == 0 or average > list(best_student.values())[0]:
            best_student = {key: average}
    return best_student


def frequence(sentence: str) -> dict:
    my_dict = dict()
    for letter in sentence:
        my_dict[letter] = sentence.count(letter)
    sorted_keys = sorted(my_dict, key=my_dict.__getitem__, reverse=True)
    print(sorted_keys)
    for key in sorted_keys:
        if my_dict[key] > 5:
            print(f"The character '{key}' appears {my_dict[key]} times in the sentence.")
    return my_dict


def get_recipes(dictionnaire):
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Please enter the name of your recipe: ")
    ingredients = input("Please enter the ingredients separated by a comma: ").split(",")
    return {name: ingredients}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recipe = input("What would you like for dinner? Please tell me: ")
    if recipe in ingredients:
        print(ingredients[recipe])
    else:
        print("Sorry, we don't have this recipe...")
        print_recipe(ingredients)




def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    (frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes({})
    recipes = get_recipes(recipes)
    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
