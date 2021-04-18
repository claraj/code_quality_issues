import json  # import json for json processing

def main():
    with open('data.json', 'r') as file:
        json_states = file.read()
        abbreviations_to_names = json.loads(data)
    
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    
    names_to_abbreviations = {}
    
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for abbreviation, name in abbreviations_to_names.items() :
        names_to_abbreviations[name] =  abbreviation

    while True:
        print('1. Convert state to abbreviation')
        print('2. Convert abbreviation to state')
        print('3. Quit')
        choice = input("Enter choice : ")

        if choice == '1':
            convert_state_to_abbreviation(names_to_abbreviations)
        elif choice == '2':
            convert_abbreviation_to_state(abbreviations_to_names) 
        elif choice==  "3":
            break
        else:
            print('Invalid choice - please try again')
            
            
def convertStateToAbbreviation(dictionary):
    userInput = input("Enter state name").capitalize()
    result = dictionary.get(userInput  )
    if result is None:
        print('State not found')
    else:
        print("The abbreviation for " + userInput + " is " + result)
        
        
def convert_abbreviation_to_state(dictionary):
    userInput = input("Enter abbreviation name").upper()
    result = dictionary.get(userInput)
    if result is None:
        print('Abreviation not found')
    else:
        print("the state with the abbreviation " + userInput + " is " + result)


if __name__ == "__main__":
    main()
