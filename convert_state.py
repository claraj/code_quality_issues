"""Program that converts state names to abbreviations and vice versa"""

import json


def main():
    """Reading in json data"""

    with open('data.json', 'r') as file:
        state_json = file.read()
        abbr_to_names = json.loads(state_json)
    
    # Create a dictionary of states (abbreviations, and a dictionary of abbreviations)
    state_abbr = abbr_to_names
    state_dict = {}
    # Below are key and value pairs for the state dictionary
    for state_key,  state_value in state_abbr.items():
        state_dict[state_value] = state_key

    # loop that continuously presents the menu
    while True:
        print('1. Convert state to abbreviation')
        print('2. Convert abbreviation to state')
        print('3. Quit')
        choice = input('Enter choice : ')

        if choice == '1':
            convert_state_to_abbreviation(state_dict)
        elif choice == '2':
            convert_abbreviation_to_state(state_abbr)
        elif choice == '3':
            break
        else:
            print('try again')


def convert_state_to_abbreviation(dictionary):
    """Function to get state name and give abbreviation"""
    user_input = input('Enter state name: ').capitalize()
    result = dictionary.get(user_input)
    if result is None:
        print('State not found')
    else:
        print('The abbreviation for ' + user_input+' is ' + result)


def convert_abbreviation_to_state(dictionary):
    """Function to take abbreviaton name and return a state name"""
    user_input = input('Enter abbreviation name: ').upper()
    result = dictionary.get(user_input)

    if result is None:
        print('Abbreviation not found.')
    else:
        print('The state with the abbreviation ' + user_input + ' is ' + result)


if __name__ == '__main__':
    main()
