# File Name:    fsa.py
# Course:       COP4020
# Project:      3
# Author:       Jeremy Caole
# Description:  FSA class, parses, checks and main method

import tkinter as tk
from fsa_window import FSAWindow


def readFile(fileName):
    with open(fileName) as f:
        return f.read().replace(" ", "")


class FSA:
    state_list = []

    def __init__(self, fsa_file, input_string):
        self.fsa_file = fsa_file
        self.input_string = input_string

    # Read the contents of a file and remove all spaces

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

    # issue with position of params
    # def checkFSA(self, numberOfStates, alphabet, stateTransitions, startState, acceptState):
    #     # Create all the nodes/states in the FSA and add them to state_list
    #     for i in range(numberOfStates):
    #         self.state_list.append(FSAWindow(i, i == startState, i in acceptState))
    #
    #     # Set the state transitions for each node based on the input stateTransitions list
    #     for t in stateTransitions:
    #         if t[2] in alphabet:
    #             # Check if the state ID is valid
    #             if int(t[0]) >= numberOfStates or int(t[1]) >= numberOfStates:
    #                 print("State does not exist")
    #                 return
    #             # Set the transition for the node at index t[0]
    #             self.state_list[int(t[0])].setTransition(t[2], t[1])
    #         else:
    #             print("Character is not valid:", t[2])
    #             return
    #
    #     # Check if the input string is accepted by the FSA
    #     input_string = readFile(self.input_string)
    #     if self.accept(startState, input_string):
    #         print(input_string + " is a Legal String")
    #     else:
    #         print(input_string + " is an Illegal String")
    # Check if the FSA is valid and traverse the graph to check if the input string is accepted or not
    def checkFSA(self, numberOfStates, acceptState, startState, stateTransitions, alphabet):
        # Create all the nodes/states in the FSA and add them to state_list
        for i in range(numberOfStates):
            self.state_list.append(FSAWindow(i, i == startState, i in acceptState))

        # Set the state transitions for each node based on the input stateTransitions list
        for t in stateTransitions:
            if t[2] in alphabet:
                # Check if the state ID is valid
                if int(t[0]) >= numberOfStates or int(t[1]) >= numberOfStates:
                    print("State does not exist")
                    return
                # Set the transition for the node at index t[0]
                self.state_list[int(t[0])].setTransition(t[2], t[1])
            else:
                print("Character is not valid:", t[2])
                return

        # Check if the input string is accepted by the FSA
        input_string = readFile(self.input_string)
        if self.accept(startState, input_string):
            print(input_string + " is a Legal String")
        else:
            print(input_string + " is an Illegal String")

    # Display the FSA graph using tkinter
    def displayGUI(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=600, height=600, bg="white")
        for s in self.state_list:
            s.drawState(canvas)
        canvas.pack()
        root.mainloop()


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
    import sys

    fsa_file = sys.argv[1]
    input_file = sys.argv[2]
    check_this_fsa = FSA(fsa_file, input_file)

    # Parse the FSA file contents
    num_states, alphabet, transitions, start_state, accept_states = parseFSAFile(check_this_fsa.fsa_file)

    # Check the FSA and display the GUI
    check_this_fsa.checkFSA(num_states, accept_states, start_state, transitions, alphabet)
    check_this_fsa.displayGUI()
