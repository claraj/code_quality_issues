module.string
import json  # import json for json processing


def main():
    """ This command Converts states to abbreviations and vice versa 
    """ 
    with open('data.json','r') as file:
        state_json= file.read()
        abbr_to_names = json.loads(state_json)

    
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    state_abbr = abbr_to_names #dictionary of state abbreviations keys and state name values 
    state_dictionary = {}# dictionary of state name keys and state abbreviation values
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    
    for statekey, statevalue in state_abbr.items() :
        state_dictionary[statevalue] =  statekey

    #loop
    while True:
        print('1. Convert state to abbreviation')
        print('2. Convert abbreviation to state')
        print('3. Quit')
        choice= input('Enter choice:')

        if choice=='1':
            convert_state_to_abbreviation(state_dictionary)
        elif  choice == '2':
            convert_abbreviation_to_state(state_abbr)
        elif choice=='3':
            

            break
        else:
            print('try again')




def convert_state_to_abbreviation(dictionary ):
    user_input = input('Enter state name').  capitalize()
    result = dictionary.get(user_input)
    if result == None:
        print('State not found')
    else:
        print ('The abbreviation for' + user_input + 'is' + result)


def convert_abbreviation_to_state(dictionary):
    user_input = input('Enter abbreviation name').upper()
    result = dictionary.get(user_input)
    if result == None:
        print('Abbreviation not found')
    else:
        print('The state with the abbreviation' + user_input + 'is' + result)


if __name__ == '__main__':
    main()
