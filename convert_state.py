import json  # import json to access data.json


def main():
    with open('data.json', 'r') as file:
        data = file.read()
        data = json.loads(data)
    
    state_abbr = data  # dictionary of state abbreviations keys and state name values 
    state_abbr_2 = {}  # state_abbr dictionary with reversed keys & values

    for statekey, statevalue in state_abbr.items():
        state_abbr_2[statevalue] =  statekey

    while True:
        print('1. Convert state to abbreviation')
        print('2. Convert abbreviation to state')
        print('3. Quit')
        choice = input('Enter choice: ')

        if choice== '1':
            convert_state_to_abbreviation(state_abbr_2)
        elif  choice == '2':
            convert_abbreviation_to_state(state_abbr)
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
