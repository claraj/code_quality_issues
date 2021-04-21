


import json  # import json for json processing
def main():
    with open('data.json','r') as file:
        state_Names = file.read()
        state_Names = json.loads(data)
    # Create a dictionary of states -> abbreviations, and a dictionary of abbreviations -> states 
    state_Abbr = state_Names # dictionary of state abbreviations keys and state name values 
    state_Abbr2 = {} # dictionary of state name keys and state abbreviation values
    # state key is the key in the state dictionary. state value is the value in the dictionary 
    for state_key, state_value in state_Abbr.items() :
        state_Abbr2[state_value] = state_key



    #loop
    while True:
        print('1. Convert state to abbreviation')
        print('2. Convert abreviasion to state')
        print('3. quit')
        choice = input('Enter choice : ')
        if choice == '1':
            convert_State_To_Abbreviation(state_Abbr2)
        elif choice == '2':
            convert_Abbreviation_To_State(state_Abbr)
        elif choice == '3':
            break
        else:
            print('try again')
def convert_State_To_Abbreviation(dictionary ):
    user_Input = input('Enter state name').  capitalize()
    result = dictionary.get(userInput)
    if result == None:
        print('state not found')
    else:
        print ('The abbreviation for ' +  user_Input+ ' is ' + result)
def convert_Abbreviation_To_State(dictionary):
    user_Input   = input('Enter abbrviation name').upper()
    result = dictionary.get(user_Input)
    if result == None:
        print('abreviation not found')
    else:
        print('the state with the abbreviation ' + user_Input + ' is ' + result)

if __name__ == "__main__":

    main()