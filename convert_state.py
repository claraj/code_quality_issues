'''
This program converts between US state names, and abbreviations. 
For example, converting "MN" to "Minnesota" or converting "California" to "CA".
'''
import json


def main():
    with open('data.json','r') as file:
        states = file.read()
        states = json.loads(states)
    print(states)

    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    stateAbbr = states    #dictionary of state abbreviations keys and state name values 
    state = {}     # dictionary of state name keys and state abbreviation values
    
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for statekey, statevalue in stateAbbr.items():
        state[statevalue] = statekey

    while True:
        print('1. Convert state to abbreviation')
        print('2. Convery abbreviation to state')
        print('3. quit')

        choice = input("Enter choice : ")

        if choice=='1':
            convert_state_to_abbreviation(state)

        elif  choice=='2':
            convert_abbreviation_to_state(stateAbbr)
         
        elif choice=='3':
            break

        else:
            print('try again')


def convert_state_to_abbreviation(dictionary):
    user_input=input("Enter state name: ").capitalize()
    result = dictionary.get(user_input)

    if result==None:
        print('state not found')

    else:
        print ('The abbreviation for ' + user_input + ' is ' + result)


def convert_abbreviation_to_state(dictionary):
    user_input = input("Enter abbrviation name: ").upper()
    result = dictionary.get(user_input)

    if result==None:
        print('abbreviation not found')

    else:
        print('the state with the abbreviation ' + user_input + ' is ' + result)


if __name__ == "__main__":

    main()