import json  # import json for json processing


def main():
    with open('data.json','r') as file:
        data = file.read()
        data = json.loads(data)

    print(data)
    
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    stateAbbr = data #dictionary of state abbreviations keys and state name values 
    stateAbbr2 = {}# dictionary of state name keys and state abbreviation values
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for statekey, statevalue in stateAbbr.items() :
        stateAbbr2[statevalue] =  statekey

    #loop
    while True:
        print('1. Convert state to abbreviation')
        print("2. Convery abreviasion to state")
        print(' 3. quit')
        choice =   input("Enter choice : ")

        if choice=="1":

            convertStateToAbbreviation(stateAbbr2)
        elif  choice == "2":
            convert_abbreviation_to_state(stateAbbr)
        
        
        elif choice==  "3":
            break
        else:
            print('try again')
def convertStateToAbbreviation(dictionary ):
    userInput   = input("Enter state name").  capitalize()
    result = dictionary.get(userInput  )
    if result == None:
        print(' state not found')
    else:
        print ( "The abbreviation for " +  userInput+" is " + result)
def convert_abbreviation_to_state(dictionary):
    userInput   = input("Enter abbrviation name").upper()
    result = dictionary.get(userInput)
    if result == None:
        print(' abreviation not found')
    else:
        print("the state with the abbreviation   " + userInput + " is " + result)





if __name__ == "__main__":

    main()