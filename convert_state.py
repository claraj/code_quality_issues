"""
This code converts written state names to the 2 letter abbreviations, or the reverse
"""
import json

def main():
    """
    Reads in the data from state_data json file
    """
    with open('state_data.json','r') as file:
        state_data = file.read()
        state_abbr_json = json.loads(state_data)

    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    state_abbr_to_longform = state_abbr_json  
    state_longform_to_abbr = {} 
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for state_key, state_value in state_abbr_to_longform.items() :
        state_longform_to_abbr[state_value] = state_key

    while True:
        print('1. Convert state to abbreviation ')
        print('2. Convert abbreviation to state ')
        print('3. Quit ')
        choice = input('Enter choice: ')

        if choice == '1':
            convert_state_to_abbreviation(state_longform_to_abbr)

        elif  choice == '2':
            convert_abbreviation_to_state(state_abbr_to_longform)
        
        elif choice == '3':
            break

        else:
            print('try again ')
            
def convert_state_to_abbreviation(dictionary):
    """
    Function converts full written state to abbreviation, e.g. 'Minnesota' to 'MN'
    """
    user_input = input('Enter state name ').capitalize()
    result = dictionary.get(user_input)

    if result is None:
        print('state not found ')
    else:
        print ('The abbreviation for ' +  user_input + ' is ' + result)

def convert_abbreviation_to_state(dictionary):
    """
    Converts state abbreviation to full name, e.g. 'WI' to 'Wisconsin'
    """
    user_input = input('Enter abbrviation name ').upper()
    result = dictionary.get(user_input)

    if result is None:
        print('abreviation not found')
    else:
        print('the state with the abbreviation ' + user_input + ' is ' + result)


if __name__ == "__main__":

    main()
