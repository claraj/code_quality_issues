"""
This python program converts states in abbreviations and abbreviations into states 
"""
import json  # import json for processing

def main():
    """ Main method """
    with open('data.json','r') as file:
        json_data = file.read()
        json_data = json.loads(json_data)
    print(json_data)
 
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    state_name_keys = json_data # dictionary of state abbreviations keys and state name values 
    state_dictionary = {} # dictionary of state name keys and state abbreviation values
    for state_key, state_value in state_name_keys.items():
        state_dictionary[state_value] =  state_key

    while True:
        print('1: Convert a state to an abbreviation')
        print('2: Convert an abbreviation to a state')
        print('3: Press 3 to quit')
        choice = input('Enter choice: ')

        if choice == '1':
            convert_state_to_abbreviation(state_dictionary)
        elif choice == '2':
            convert_abbreviation_to_state(state_name_keys)
        elif choice == '3':
            break
        else:
            print('try again')

def convert_state_to_abbreviation(state_dictionary):
    """
    Takes states and converts to abbreviation
    """
    user_input = input('Enter state name: ').title()
    result = state_dictionary.get(user_input)
    if result is None:
        print('State not found')
    else:
        print(f'The abbreviation for {user_input} is {result}')

def convert_abbreviation_to_state(dictionary):
    """
    Take state abbreviation to a state
    """
    user_input = input('Enter abbrviation name: ').upper()
    result = dictionary.get(user_input)
    if result is None:
        print('Abbreviation not found')
    else:
        print(f'The state with the abbreviation {user_input} is {result}')

if __name__ == '__main__':
    main()