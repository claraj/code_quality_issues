import json


def main():
    with open('code_quality_issues/data.json','r') as file:
        data = file.read()
        data = json.loads(data)
    print(data)

    stateAbbr = data # Create a dictionary of abbreviations -> states
    stateAbbr2 = {} # Initiate a new dictionary to hold states -> abbreviations
    # Populate stateAbbr2 with states -> abbreviations
    for statekey, statevalue in stateAbbr.items() :
        stateAbbr2[statevalue] =  statekey

    while True:
        print('1. Convert state to abbreviation')
        print('2. Convery abreviasion to state')
        print('3. Quit')
        choice = input('Enter choice: ')

        if choice == '1':
            convertStateToAbbreviation(stateAbbr2)
        elif choice == '2':
            convert_abbreviation_to_state(stateAbbr)
        elif choice == '3':
            break
        else:
            print('Try again')


def convertStateToAbbreviation(dictionary ):
    userInput = input('Enter state name: ').  capitalize()
    result = dictionary.get(userInput  )
    if result == None:
        print('State not found')
    else:
        print('The abbreviation for ' +  userInput+' is ' + result)


def convert_abbreviation_to_state(dictionary):
    userInput = input('Enter abbrviation name: ').upper()
    result = dictionary.get(userInput)
    if result == None:
        print('Error')
    else:
        print('The state with the abbreviation ' + userInput + ' is ' + result)


if __name__ == '__main__':
    main()
