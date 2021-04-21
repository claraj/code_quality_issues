import json  # import json for json processing
"""Convert between state name and abbreviation"""

def main():

    """ Main function creates dictionary of states and runs menu """

    with open('data.json','r') as file:
        data = file.read()
        state_data = json.loads(data)

    state_key_and_name = state_data 
    state_key_and_abbrev = {}

    for statekey, statevalue in state_key_and_name.items() :
        state_key_and_abbrev[statevalue] = statekey

    while True:
        print('1. Convert state to abbreviation')
        print("2. Convert abbreviation to state")
        print('3. Quit')
        choice = input("Enter choice:")

        if choice=="1":
            convert_state_to_abbreviation(state_key_and_abbrev)
        elif  choice=="2":
            convert_abbreviation_to_state(state_key_and_name)
        elif choice=="3":
            break
        else:
            print('Try Again')

def convert_state_to_abbreviation(dictionary ):

    """ Take state name and convert to abbreviation"""

    user_input = input("Enter state name:").capitalize()
    result = dictionary.get(user_input)

    if result is None:
        print('State Not found')
    else:
        print ( "The abbreviation for " + user_input + " is " + result + ".")

def convert_abbreviation_to_state(dictionary):

    """ Take abbreviation to state name"""

    user_input = input("Enter abbrviation name:").upper()
    result = dictionary.get(user_input)
    if result is None:
        print('Abreviation not found.')
    else:
        print("The state with the abbreviation." + user_input + " is " + result)

if __name__ == "__main__":
    """Calls main funciton"""
    main()