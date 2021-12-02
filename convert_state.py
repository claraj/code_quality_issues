


import json  # use an import statement to import json for json processing

# no docstring
def main(): # make a main function
    with open('data.json','r') as file:
        data = file.read()
        data = json.loads(data)
# should be no whitespace
    print(data)
    
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 

    # stateAbbr should be {} and different names should be used for the stateAbbr dictionaries
    # should be state_abbr
    stateAbbr = data #dictionary of state abbreviations keys and state name values 
    stateAbbr2 = {}# dictionary of state name keys and state abbreviation values
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for statekey, statevalue in stateAbbr.items() :
        stateAbbr2[statevalue] =  statekey



    #loop
    while True:
        # should only use ' ' or " "
        print('1. Convert state to abbreviation')  # print a choice

        # abbreviation is spelled wrong

        print("2. Convery abreviasion to state")   # print a choice
        print(' 3. quit')  # print a choice
        choice =   input("Enter choice : ")
    # should be no whitespace
        if choice=="1":

            convertStateToAbbreviation(stateAbbr2)
        elif  choice == "2":
            convert_abbreviation_to_state(stateAbbr)
        
        
        elif choice==  "3":
            break
        else:
            print('try again')
# shouldn't use dictionary for an argument
def convertStateToAbbreviation(dictionary ):

    # should be user_input
    # should be no space between . and capitalize
    userInput   = input("Enter state name").  capitalize()
    # should end in (userInput) no space
    result = dictionary.get(userInput  )
    # should be if result is None
    if result == None:
        print(' state not found')
    else:

        #should be a space after +
        print ( "The abbreviation for " +  userInput+" is " + result)

# should be a different argument name
def convert_abbreviation_to_state(dictionary):
    #should use a _ and no capitol between user and input
    userInput   = input("Enter abbrviation name").upper()
    result = dictionary.get(userInput)
    # should be if result is None
    if result == None:
        print('error')
    else:
        print("the state with the abbreviation   " + userInput + " is " + result)





if __name__ == "__main__":

    main()
