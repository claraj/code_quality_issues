"""
Application to convert state names to their state codes
and state codes to their corresponding state names
"""
import json 


def main():
    """ 
    Allows the user to choose whether they'd like
    to convert a state to state code, state code to state,
    or quit.
    """
    states_file = "states.json"

    # dictionary of state codes with corresponding state names
    abbreviation_to_states = read_file(states_file)

    # dictionary of states with corresponding state codes
    states_to_abbreviation = reverse_dict(abbreviation_to_states)  

    while True:

        choice = show_menu_get_choice()

        if choice == "1":

            convert_state_to_abbreviation(states_to_abbreviation)

        elif  choice == "2":

            convert_abbreviation_to_state(abbreviation_to_states)
        
        elif choice ==  "3":

            print("Good Bye.")
            break

        else:

            print('Invalid entry.')
  

def convert_state_to_abbreviation(states):
    """
    Takes a state name and converts it to a state code

    """
    state = input("Enter state name: ").capitalize()
    abbreviation_name = states.get(state)
    if abbreviation_name:
        print (f"The abbreviation for {state} is {abbreviation_name}")
    else:
        print("State not found.")


def convert_abbreviation_to_state(state_abbreviations):
    """
    Takes a state code and converts it to a state name

    """
    abbreviation_name   = input("Enter abbreviation name: ").upper()
    state = state_abbreviations.get(abbreviation_name)
    if state:
        print(f"The state with the abbreviation {abbreviation_name} is {state}")
    else:
        print('Abbreviation not found.')
        

def read_file(states_file):
    """
    Reads a json file a returns a python dictionary

    """
    with open(states_file,"r") as file:
        states = file.read()
        abbreviation_to_states = json.loads(states) 
    return abbreviation_to_states


def reverse_dict(initial_dict):
    """
    Takes a dictionary and switches the key and value positions

    """
    reversed_dict = {}

    for key, value in initial_dict.items() :
        reversed_dict[value] =  key
    
    return reversed_dict


def show_menu_get_choice():
    """
    Displays the menu options and returns the user's choice

    """
    print("1. Convert state to abbreviation")
    print("2. Convery abbreviation to state")
    print("3. Quit")

    choice = input("Enter the integer value of your choice: ")

    return choice

        
if __name__ == "__main__":
    main()
