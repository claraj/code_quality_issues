import json  # import json for json processing



def main():
    with open("states.json","r") as file:
        states = file.read()
        abrvs_to_states = json.loads(states) # dictionary of state codes with corresponding state names

    states_to_abrvs = {}  # dictionary of states with corresponding state codes
  
    for key, value in abrvs_to_states.items() :
        states_to_abrvs[value] =  key


    while True:
        print("1. Convert state to abbreviation")
        print("2. Convery abbreviation to state")
        print("3. Quit")

        choice =   input("Enter the integer value of your choice: ")

        if choice == "1":

            convert_state_to_abvr(states_to_abrvs)

        elif  choice == "2":

            convert_abvr_to_state(abrvs_to_states)
        
        elif choice==  "3":

            print("Good Bye.")
            break

        else:

            print('Invalid entry.')


def convert_state_to_abvr(states):
    userInput   = input("Enter state name").  capitalize()
    result = states.get(userInput  )
    if result == None:
        print(' state not found')
    else:
        print ( "The abbreviation for " +  userInput+" is " + result)


def convert_abvr_to_state(state_abvrs):
    abvr_name   = input("Enter abbreviation name: ").upper()
    state = state_abvrs.get(abvr_name)
    if state:
        print(f"The state with the abbreviation  {abvr_name} is {state}")
    else:
        print('Abbreviation not found.')
        


if __name__ == "__main__":

    main()