import json


def main():
    with open('code_quality_issues/data.json','r') as file:
        data = file.read()
        data = json.loads(data)
    print(data)

    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    stateAbbr = data
    stateAbbr2 = {}

    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for statekey, statevalue in stateAbbr.items() :
        stateAbbr2[statevalue] =  statekey
    while True:
        print('1. Convert state to abbreviation')
        print('2. Convery abreviasion to state')
        print(' 3. quit')
        choice =   input('Enter choice : ')

        if choice=='1':
            convertStateToAbbreviation(stateAbbr2)
        elif  choice == '2':
            convert_abbreviation_to_state(stateAbbr)
        elif choice==  '3':
            break
        else:
            print('try again')


def convertStateToAbbreviation(dictionary ):
    userInput   = input('Enter state name').  capitalize()
    result = dictionary.get(userInput  )
    if result == None:
        print(' state not found')
    else:
        print ( 'The abbreviation for ' +  userInput+' is ' + result)


def convert_abbreviation_to_state(dictionary):
    userInput   = input('Enter abbrviation name').upper()
    result = dictionary.get(userInput)
    if result == None:
        print('error')
    else:
        print('the state with the abbreviation   ' + userInput + ' is ' + result)


if __name__ == '__main__':
    main()
