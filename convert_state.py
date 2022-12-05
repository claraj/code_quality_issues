import json  # import json to access data.json


def main():
    with open('data.json', 'r') as file:
        data = file.read()
        data = json.loads(data)
    
    abbr_to_state = data  # dictionary - key: state abbreviations, value: state name 
    state_to_abbr = {}  # key: state name, value: abbreviation

    for statekey, statevalue in abbr_to_state.items():
        state_to_abbr[statevalue] =  statekey

    while True:
        print('1. Convert state to abbreviation')
        print('2. Convert abbreviation to state')
        print('3. Quit')
        choice = input('Enter choice: ')

        if choice== '1':
            convert_state_to_abbreviation(state_to_abbr)
        elif  choice == '2':
            convert_abbreviation_to_state(abbr_to_state)
        elif choice ==  '3':
            break
        else:
            print('Try again')


def convert_state_to_abbreviation(dictionary):
    user_input = input('Enter state name: ').capitalize()
    result = dictionary.get(user_input)
    if result == None:
        print('State not found')
    else:
        print(f'The abbreviation for {user_input} is {result}')


def convert_abbreviation_to_state(dictionary):
    user_input   = input('Enter abbrviation name: ').upper()
    result = dictionary.get(user_input)
    if result == None:
        print('error')
    else:
        print(f'The state with the abbreviation {user_input} is {result}')


if __name__ == '__main__':

    main()
