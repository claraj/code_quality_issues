import json  # import json for json processing
def main():
    with open('data.json','r') as file:
        data = file.read()
        stateData = json.loads(data)

    print(stateData)
    
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    stateKeyandName = stateData 
    stateKeyandAbbrev = {}

    for statekey, statevalue in stateKeyandName.items() :
        stateKeyandAbbrev[statevalue] =  statekey

    while True:
        print('1. Convert state to abbreviation')
        print("2. Convert abbreviation to state")
        print('3. Quit')
        choice =   input("Enter choice : ")

        if choice=="1":
            convert_state_to_abbreviation(stateKeyandAbbrev)
        elif  choice=="2":
            convert_abbreviation_to_state(stateKeyandName)
        elif choice=="3":
            break
        else:
            print('Try Again')

def convert_state_to_abbreviation(dictionary ):
    userInput = input("Enter state name").capitalize()
    result = dictionary.get(userInput  )

    if result == None:
        print('State Not found')
    else:
        print ( "The abbreviation for " + userInput + " is " + result + ".")

def convert_abbreviation_to_state(dictionary):

    userInput = input("Enter abbrviation name.").upper()
    result = dictionary.get(userInput)
    if result == None:
        print('Abreviation not found.')
    else:
        print("The state with the abbreviation." + userInput + " is " + result)





if __name__ == "__main__":

    main()