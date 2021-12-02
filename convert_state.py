import json


def main():
    with open('data.json','r') as file:
        state_data = file.read()
        json_state_data = json.loads(state_data)
    state_abbreviation = json_state_data # Create a dictionary of abbreviations -> states
    state_state_abbreviation_2 = {} # Initiate a new dictionary to hold states -> abbreviations

    # Populate stateAbbr2 with states -> abbreviations
    for state_key, state_value in state_abbreviation.items():
        state_state_abbreviation_2[state_value] =  state_key
    # Display choice menu to user
    while True:
        print('1. Convert state to abbreviation')
        print('2. Convery abbreviation to state')
        print('3. Quit')
        choice = input('Enter choice: ')
        if choice == '1':
            convert_state_to_abbreviation(state_state_abbreviation_2)
        elif choice == '2':
            convert_abbreviation_to_state(state_abbreviation)
        elif choice == '3':
            break
        else:
            print('Try again')
            print('\n')


def convert_state_to_abbreviation(dictionary):
    user_input = input('Enter state name: ').capitalize()
    result = dictionary.get(user_input)
    if result == None:
        print('State not found')
        print('\n')
    else:
        print('The abbreviation for ' + user_input + ' is ' + result + '\n')


def convert_abbreviation_to_state(dictionary):
    user_input = input('Enter abbreviation name: ').upper()
    result = dictionary.get(user_input)
    if result == None:
        print('Error')
        print('\n')
    else:
        print('The state with the abbreviation ' + user_input + ' is ' + result + '\n')


if __name__ == '__main__':
    main()
