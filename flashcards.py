from peewee import *
from main import Country
import random

countries = []

for country in Country.select():
    country_dict = {
        'name': country.name,
        'capital': country.capital,
    }
    countries.append(country_dict)

card_count = len(countries)

print("World Capitals Flashcards\n")

path = input("Would you like to (a) play the flashcards, or (b) make new cards? ")


def capitals_game(turns):

    correct = 0
    incorrect = 0

    random.shuffle(countries)

    if turns == 0 or turns > len(countries) or turns < 0:
        turns = len(countries)

    print("Guess the capitals of each country and test your knowledge!")

    for i in range(0, turns):
        guess = input(f"What is the capital of {countries[i]['name']}: ")

        answer = countries[i]["capital"]

        while guess != answer:
            incorrect += 1
            guess = input(f"WRONG!\nCorrect: {correct} Incorrect: {incorrect}\nWhat is the capital of {countries[i]['name']}: ")

        correct += 1
        print(f"RIGHT!\nCorrect: {correct} Incorrect: {incorrect}")

    print(f"Your final score is {correct - incorrect}!")
    new_game = input('Would you like to play again? Yes (y) or No (n): ')

    if new_game == 'y':
        capitals_game()
    else:
        print("Thank you for playing my game! Goodbye!")


def add_suggestion():

    def find_country_by_name(country_name):
        try:
            return Country.get(Country.name == country_name)
        except Country.DoesNotExist:
            return None

    country_name = input("Enter the name of the country: ")

    existing_country = find_country_by_name(country_name)

    if existing_country:
        print(f"Country '{country_name}' already exists in the database.")
    else:
        country_capital = input("Enter the capital of the country: ")
        suggestion = Country(name=country_name, capital=country_capital)
        suggestion.save()
        print(f"Suggestion added: {country_name} - {country_capital}")

if path == 'a':
    card_count = int(input(f"How many cards do you want to play? (Select 0 to play all {card_count} flashcards) "))
    capitals_game(card_count)
elif path == 'b':
    add_suggestion()
else:
    print("sorry")