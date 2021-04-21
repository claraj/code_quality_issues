"""
CLI program convert state names to abbreviations and vice versa
"""

import json


def main():
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    with open('data.json','r') as file:
        abbreviation_json = file.read()
        state_abbreviations = json.loads(abbreviation_json)
    print(state_abbreviations)
    
    state_names = {}
    # State key is the key in the state dictionary. State value is the value in the dictionary.
    for abbreviation, name in state_abbreviations.items():
        state_names[name] = abbreviation

    while True:
        print('1. Convert state to abbreviation')
        print('2. Convery abreviasion to state')
        print('3. Quit')
        choice =   input('Enter choice: ')
        if choice == '1':
            convert_state_to_abbreviation(state_names)
        elif  choice == '2':
            convert_abbreviation_to_state(state_abbreviations)
        elif choice == '3':
            break
        else:
            print('Try again')


def convert_state_to_abbreviation(dictionary):
    selection = input('Enter state name').capitalize()
    result = dictionary.get(selection)
    if result is None:
        print('State not found')
    else:
        print (f'The abbreviation for {selection} is {result}')


def convert_abbreviation_to_state(dictionary):
    selection = input('Enter abbrviation name').upper()
    result = dictionary.get(selection)
    if result is None:
        print('Abreviation not found')
    else:
        print(f'The state with the abbreviation {selection} is {result}')


if __name__ == "__main__":
    main()
