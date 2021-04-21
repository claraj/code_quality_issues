import json  # import json for processing



def main():
    with open('data.json','r') as file:
        jsondata = file.read()
        loaded_data = json.loads(jsondata)
 
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    state_name_keys = loaded_data # dictionary of state abbreviations keys and state name values 
    state_dictionary = {} # dictionary of state name keys and state abbreviation values
    for state_key, state_value in state_name_keys.items():
        state_dictionary[state_value] =  state_key

    while True:
        print('1: Convert a state to an abbreviation')
        print('2: Convert an abbreviation to a state')
        print('Press any other number to quit')
        choice = input('Enter choice: ')

        if choice == '1':
            convertStateToAbbreviation(state_dictionary)
        elif choice == '2':
            convert_abbreviation_to_state(state_name_keys)
        else:
            break

def convertStateToAbbreviation(dictionary):
    user_input = input('Enter state name: ').capitalize()
    result = dictionary.get(user_input)
    if result == None:
        print('State not found')
    else:
        print(f'The abbreviation for {user_input} is {result}')

def convert_abbreviation_to_state(dictionary):
    user_input = input('Enter abbrviation name: ').upper()
    result = dictionary.get(user_input)
    if result is None:
        print('Abbreviation not found')
    else:
        print(f'The state with the abbreviation {user_input} is {result}')

if __name__ == '__main__':
    main()