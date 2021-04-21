""" Program to convert state names to abbreviation and vice versa """
import json

def main():
    with open('data.json','r') as file:
        data = file.read()
        data = json.loads(data)

    # print(data)
    
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    state_Abbr = data # dictionary of state abbreviations keys and state name values 
    state_Abbr2 = {} # dictionary of state name keys and state abbreviation values
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for statekey, statevalue in state_Abbr.items() :
        state_Abbr2[statevalue] =  statekey

    while True:
        print('1. Convert state to abbreviation')
        print('2. Convery abbreviation to state')
        print('3. quit')
        choice = input('Enter choice: ')

        if choice=='1':
            convert_state_to_abbreviation(state_Abbr2)
        elif  choice == '2':
            convert_abbreviation_to_state(state_Abbr)
        elif choice==  '3':
            break
        else:
            print('try again')

def convert_state_to_abbreviation(dictionary):
    """ Allow user to get conversion from dictionary """
    user_input = input('Enter state name').capitalize()
    result = dictionary.get(user_input)
    if result is None:
        print('State not found')
    else:
        print ('The abbreviation for' +  user_input + ' is ' + result)

def convert_abbreviation_to_state(dictionary):
    """ Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states """
    user_input = input('Enter abbreviation name').upper()
    result = dictionary.get(user_input)
    if result is None:
        print('Abreviation not found')
    else:
        print('The state with the abbreviation ' + user_input + ' is ' + result)

if __name__ == "__main__":
    main()
