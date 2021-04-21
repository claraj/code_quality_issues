import json

"""
Command line program to convert state names to abbreviations or convert abbreviations to names
"""

def main():
    with open('data.json', 'r') as file:
        state_names = file.read()
        state_names = json.loads(state_names)
    print(state_names)

    # create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states
    state_abbr_to_names_dict = state_names
    state_names_to_abbr = {}

    # state key is the key in the state dictionary. State value is the value in the dictionary
    for state_key, state_value in state_abbr_to_names_dict.items():
        state_names_to_abbr[state_value] = state_key

    while True:
        print('1. Convert state to abbreviation')
        print('2. Convert abbreviation to state')
        print('3. Quit')
        choice = input('Enter choice: ')

        if choice == '1':
            convert_state_to_abbreviation(state_names_to_abbr)
        elif choice == '2':
            convert_abbreviation_to_state(state_abbr_to_names_dict)
        elif choice == '3':
            break
        else:
            print('Try again.')


def convert_state_to_abbreviation(state_names_to_abbr):
    user_input = input('Enter state name: ').title()
    result = state_names_to_abbr.get(user_input)
    if result is None:
        print('State not found.')
    else:
        print(f'The abbreviation for {user_input} is {result}.')


def convert_abbreviation_to_state(state_abbr_to_names_dict):
    user_input = input('Enter abbreviation name: ').upper()
    result = state_abbr_to_names_dict.get(user_input)
    if result is None:
        print('Abbreviation not found.')
    else:
        print(f'The state with the abbreviation {user_input} is {result}.')


if __name__ == '__main__':
    main()
