import json

def main():
    with open('state_data.json','r') as file:
        state_data = file.read()
        state_abbr_json = json.loads(state_data)

    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    # dictionary of state abbreviations keys and state name values
    state_abbr_to_longform = state_abbr_json  
    state_longform_to_abbr = {} # dictionary of state name keys and state abbreviation values
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for statekey, statevalue in state_abbr_to_longform.items() :
        state_longform_to_abbr[statevalue] = statekey

    while True:
        print('1. Convert state to abbreviation ')
        print('2. Convery abreviasion to state ')
        print('3. Quit ')
        choice =   input('Enter choice: ')

        if choice == '1':
            convertStateToAbbreviation(state_longform_to_abbr)

        elif  choice == '2':
            convert_abbreviation_to_state(state_abbr_to_longform)
        
        elif choice == '3':
            break

        else:
            print('try again ')
            
def convertStateToAbbreviation(dictionary):
    user_input = input('Enter state name ').capitalize()
    result = dictionary.get(user_input)

    if result == None:
        print('state not found ')
    else:
        print ('The abbreviation for ' +  user_input + ' is ' + result)

def convert_abbreviation_to_state(dictionary):
    user_input = input('Enter abbrviation name ').upper()
    result = dictionary.get(user_input)
    
    if result is None:
        print('abreviation not found')
    else:
        print("the state with the abbreviation " + user_input + " is " + result)


if __name__ == "__main__":

    main()