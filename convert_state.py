import json 



def main():
    states_file = "states.json"

    # dictionary of state codes with corresponding state names
    abrvs_to_states = read_file(states_file)

    # dictionary of states with corresponding state codes
    states_to_abrvs = reverse_dict(abrvs_to_states)  

    while True:

        choice = show_menu_get_choice()

        if choice == "1":

            convert_state_to_abvr(states_to_abrvs)
            continue

        elif  choice == "2":

            convert_abvr_to_state(abrvs_to_states)
            continue
        
        elif choice==  "3":

            print("Good Bye.")
            break

        else:

            print('Invalid entry.')
  

def convert_state_to_abvr(states):
    state = input("Enter state name: ").capitalize()
    abrv_name = states.get(state)
    if abrv_name:
        print (f"The abbreviation for {state} is {abrv_name}")
    else:
        print("State not found.")


def convert_abvr_to_state(state_abvrs):
    abvr_name   = input("Enter abbreviation name: ").upper()
    state = state_abvrs.get(abvr_name)
    if state:
        print(f"The state with the abbreviation  {abvr_name} is {state}")
    else:
        print('Abbreviation not found.')
        

def read_file(states_file):
    with open(states_file,"r") as file:
        states = file.read()
        abrvs_to_states = json.loads(states) 
    return abrvs_to_states


def reverse_dict(initial_dict):
    reversed_dict = {}

    for key, value in initial_dict.items() :
        reversed_dict[value] =  key
    
    return reversed_dict


def show_menu_get_choice():
    print("1. Convert state to abbreviation")
    print("2. Convery abbreviation to state")
    print("3. Quit")

    choice =   input("Enter the integer value of your choice: ")

    return choice


        
if __name__ == "__main__":

    main()
