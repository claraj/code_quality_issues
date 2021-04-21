import json  # import json for json processing


def main():
    with open('data.json','r') as file:
        state_data = file.read()
        state_data = json.loads(state_data)
    
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    state_abbr_dict = state_data    # dictionary of state abbreviation keys and state name values 
    state_name_dict = {} # dictionary of state name keys and state abbreviation values
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for statekey, statevalue in state_abbr_dict.items() :
        state_name_dict[statevalue] =  statekey

    # This is the main menu
    while True:
        print('1. Convert state to abbreviation ')
        print('2. Convert abbreviasion to state ')
        print('3. Quit ')

        choice = input('Enter choice: ')

        if choice == '1':
            convert_state_to_abbreviation(state_name_dict)

        elif  choice == '2':
            convert_abbreviation_to_state(state_abbr_dict)
         
        elif choice ==  '3':
            break

        else:
            print('try again')


#   Convert state to abbreviation takes the user input, finds the name in state_data and outputs the abbreviation
def convert_state_to_abbreviation(dictionary):
    user_input   = input('Enter state name ').capitalize()   #User inputs state name
    result = dictionary.get(user_input)
    if result is None:
        print('State not found')

    else:
        print ('The abbreviation for ' +  user_input + ' is ' + result)


#   Convert abbreviation to state takes the user input and finds the state name.
def convert_abbreviation_to_state(dictionary):
    user_input = input('Enter abbreviation name').upper() #   User inputs abbreviation
    result = dictionary.get(user_input)
    if result is None:
        print('Abbreviation not found')

    else:
        print('The state with the abbreviation ' + user_input + ' is ' + result)

if __name__ == '__main__':

    main()