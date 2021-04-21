import json

def main():

    with open('data.json','r') as file:
        data = file.read()
        data = json.loads(data)
    
    state_abbreviations = data #dictionary of state abbreviations keys and state name values 
    state_names = {} # dictionary of state name keys and state abbreviation values

    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for state_key, state_value in state_abbreviations.items():
        state_names[state_value] = state_key

    while True:
        print('1. Convert state to abbreviation')
        print('2. Convert abbreviation to state')
        print('3. Quit')
        choice = input('Enter choice: ')

        if choice =='1':
            convert_state_to_abbreviation(state_names)
        elif choice == '2':
            convert_abbreviation_to_state(state_abbreviations)
        elif choice ==  '3':
            break
        else:
            print('try again.')


def convert_state_to_abbreviation(dictionary):
    user_input = input('Enter state name: ').capitalize()
    result = dictionary.get(user_input)
    if result == None:
        print('state not found.')
    else:
        print ( 'The abbreviation for ' +  user_input + 'is' + result)


def convert_abbreviation_to_state(dictionary):
    user_input = input('Enter abbreviation name: ').upper()
    result = dictionary.get(user_input)
    if result == None:
        print('abbreviation not found.')
    else:
        print('The state with the abbreviation ' + user_input + 'is' + result)


if __name__ == '__main__':

    main()