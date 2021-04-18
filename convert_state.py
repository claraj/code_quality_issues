"""
Command-line program for converting between US state names and abbreviations, and vice-versa.
"""

import json  # import json for json processing

def main():
    """ Loads JSON data and prepares dictionaries, loop for  """
    
    abbreviations_to_names, names_to_abbreviations = load_state_data('data.json')
 
    while True:
        print('1. Convert state to abbreviation')
        print("2. Convert abbreviation to state")
        print('3. Quit')
        choice = input('Enter choice : ')

        if choice=='1':
            convert_state_to_abbreviation(names_to_abbreviations)
        elif choice == '2':
            convert_abbreviation_to_state(abbreviations_to_names)
        elif choice == "3":
            break
        else:
            print('Invalid choice - please try again')
            

def load_state_data(filename):
    """ Read state names and abbreviations from JSON data file """
    with open(filename, 'r') as file:
        json_states = file.read()
        abbreviations_to_names = json.loads(json_states)
        
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states
    
    names_to_abbreviations = {}
    
    # state key is the key in the state dictionary. state value is the value in the dictionary
    for abbreviation, name in abbreviations_to_names.items():
        names_to_abbreviations[name] =  abbreviation
        
    return abbreviations_to_names, names_to_abbreviations

def convert_state_to_abbreviation(dictionary):
    """ Convert state to 2-letter abbreviation.
    Prints 'not found' message if state not found """
    name = input("Enter state name").capitalize()
    abbreviation = dictionary.get(name)
    if abbreviation== None:
        print('State not found')
    else:
        print('The abbreviation for ' + name + ' is ' + abbreviation)
        
        
def convert_abbreviation_to_state(dictionary):
    """ Convert abbreviation to full state name. 
    Prints 'not found' message if abbreviation not found """
    abbreviation = input("Enter abbreviation name").upper()
    name = dictionary.get(abbreviation)
    if name is None:
        print('Abreviation not found')
    else:
        print('the state with the abbreviation ' + abbreviation + ' is ' + name)


if __name__ == "__main__":
    main()
