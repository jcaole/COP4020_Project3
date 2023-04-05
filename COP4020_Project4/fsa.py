# File Name:    fsa.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  FSA class, parses, checks and main method


# Read the contents of a file and remove all spaces
def readFile(fileName):
    with open(fileName) as f:
        return f.read().replace(" ", "")


class FSA:
    state_list = []

    def __init__(self, fsa_file, input_string):
        self.fsa_file = fsa_file
        self.input_string = input_string

    # NOTE: this is already recursive method
    # Traverse the FSA graph recursively and check if a given string is accepted or not
    def accept(self, node, remainder):
        if node is not None and len(self.state_list) > node > -1:
            if len(remainder) == 0:
                return self.state_list[node].accept
            next_node = self.state_list[node].getNext(remainder[0])
            if next_node is None:
                return False
            return self.accept(next_node, remainder[1:])
        else:
            print("Error")
            return False

    def checkFSA(self, numberOfStates, acceptState, startState, stateTransitions, alphabet):
        # Create a dictionary to represent the state transitions
        transitions = {}
        for t in stateTransitions:
            if t[2] in alphabet:
                # Check if the state ID is valid
                if int(t[0]) >= numberOfStates or int(t[1]) >= numberOfStates:
                    print("State does not exist")
                    return
                # Set the transition for the current state and input symbol
                transitions[(int(t[0]), t[2])] = int(t[1])
            else:
                print("Character is not valid:", t[2])
                return

        # Store the accept states in a set
        accept_states = set(acceptState)

        # Check if the input string is accepted by the FSA
        input_string = readFile(self.input_string)
        current_state = startState
        for symbol in input_string:
            if (current_state, symbol) in transitions:
                current_state = transitions[(current_state, symbol)]
            else:
                # test to check if method finds the correct invalid symbol
                print("Invalid symbol:", symbol)
                print(input_string + " is an Illegal String")
                return
        if current_state in accept_states:
            print(input_string + " is a Legal String")


# parse method, follows fsa.txt format
def parseFSAFile(fsa_file):
    fsa_contents = readFile(fsa_file).split(';')[:-1]
    num_states = int(fsa_contents[0])
    alphabet = fsa_contents[1].strip().split(',')
    transitions = [t[1:-1].split(':') for t in fsa_contents[2].split(',')]
    start_state = int(fsa_contents[3])
    accept_states = [int(i) for i in fsa_contents[4].split(',')]
    return num_states, alphabet, transitions, start_state, accept_states


# Main function
if __name__ == "__main__":
    import sys  # needed to implement inputs arguments

    fsa_file = sys.argv[1]
    input_file = sys.argv[2]
    check_this_fsa = FSA(fsa_file, input_file)

    # Parse the FSA file contents
    num_states, alphabet, transitions, start_state, accept_states = parseFSAFile(check_this_fsa.fsa_file)

    # Check the FSA
    check_this_fsa.checkFSA(num_states, accept_states, start_state, transitions, alphabet)
