"""
CLI program convert state names to abbreviations and vice versa
"""

import json


def main():
    """Allow user to get conversions from dicts"""
    state_abbreviations, state_names = get_names_and_abbreviations()

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


def get_names_and_abbreviations():
    """
    Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states
    """
    with open('data.json','r') as file:
        abbreviation_json = file.read()
        state_abbreviations = json.loads(abbreviation_json)
    print(state_abbreviations)
    
    # Name is key in name dict, value in abbreviation dict. 
    # Abbreviation is key in abbreviation dict, value in state dict.
    state_names = {}
    for abbreviation, name in state_abbreviations.items():
        state_names[name] = abbreviation


def convert_state_to_abbreviation(dictionary):
    """Convert user selected state to abbreviation"""
    selection = input('Enter state name').capitalize()
    result = dictionary.get(selection)
    if result is None:
        print('State not found')
    else:
        print (f'The abbreviation for {selection} is {result}')


def convert_abbreviation_to_state(dictionary):
    """Convert user selected abbreviation to state"""
    selection = input('Enter abbrviation name').upper()
    result = dictionary.get(selection)
    if result is None:
        print('Abreviation not found')
    else:
        print(f'The state with the abbreviation {selection} is {result}')


if __name__ == "__main__":
    main()
