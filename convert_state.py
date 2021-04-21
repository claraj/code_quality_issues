


import json  # import json for json processing
def main():
    with open('data.json','r') as file:
        state_data = file.read()
        state_data = json.loads(state_data)

    print(state_data)
    
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    state_abbr_dict = state_data    # dictionary of state abbreviation keys and state name values 
    state_name_dict = {} # dictionary of state name keys and state abbreviation values
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for statekey, statevalue in state_abbr_dict.items() :
        state_name_dict[statevalue] =  statekey



    # loop
    while True:
        print('1. Convert state to abbreviation')
        print('2. Convery abreviasion to state')
        print(' 3. quit')
        choice =   input('Enter choice : ')

        if choice=='1':

            convertStateToAbbreviation(state_name_dict)
        elif  choice == '2':
            convert_abbreviation_to_state(state_abbr_dict)
        
        
        elif choice==  '3':
            break
        else:
            print('try again')

def convert_state_to_abbreviation(dictionary):
    userInput   = input('Enter state name').  capitalize()
    result = dictionary.get(userInput  )
    if result == None:
        print('State not found')
    else:
        print ( 'The abbreviation for ' +  userInput+' is ' + result)

def convert_abbreviation_to_state(dictionary):
    userInput   = input('Enter abbrviation name').upper()
    result = dictionary.get(userInput)
    if result == None:
        print(' abreviation not found')
    else:
        print('the state with the abbreviation   ' + userInput + ' is ' + result)





if __name__ == '__main__':

    main()