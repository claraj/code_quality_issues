


import json  # import json for json processing
def main():
    with open('data.json','r') as file:
        state_names = file.read()
        state_names_data = json.loads(data)
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    state_abbr = state_names_data # dictionary of state abbreviations keys and state name values 
    state_abbr2 = {} # dictionary of state name keys and state abbreviation values
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for state_key, state_value in state_abbr.items() :
        state_abbr2[state_value] = state_key

    #loop
    while True:
        print('1. Convert state to abbreviation')
        print('2. Convert abreviasion to state')
        print('3. quit')
        choice = input('Enter choice : ')
        if choice == '1':
            convert_state_to_abbreviation(state_abbr2)
        elif choice == '2':
            convert_abbreviation_to_state(state_abbr)
        elif choice == '3':
            break
        else:
            print('try again')

def convert_state_to_abbreviation(dictionary ):
    user_input = input('Enter state name').  capitalize()
    result = dictionary.get(userInput)
    if result is None:
        print('state not found')
    else:
        print ('The abbreviation for ' +  user_input+ ' is ' + result)
def convert_abbreviation_to_state(dictionary):
    user_input   = input('Enter abbrviation name').upper()
    result = dictionary.get(user_input)
    if result is None:
        print('abreviation not found')
    else:
        print('the state with the abbreviation ' + user_input + ' is ' + result)

if __name__ == "__main__":

    main()