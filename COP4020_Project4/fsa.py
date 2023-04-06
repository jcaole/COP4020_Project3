# File Name:    fsa.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  project 3 FSA class, modified for project 4

from transitions import Transitions


# # Read the contents of a file and remove all spaces
# def readFile(fileName):
#     with open(fileName) as f:
#         return f.read().replace(" ", "")

class FSA:
    state_list = []

    def __init__(self, numberOfStates, alphabet, stateTransitions, startState, acceptStates):
        self.number_of_states = numberOfStates
        self.alphabet = alphabet
        self.state_transitions = stateTransitions
        self.start_state = startState
        self.accept_states = acceptStates
        self.current_state = int(self.start_state)
        self.transition_array = []
        self.valid_transition = True

    def makeTransitions(self):
        self.valid_transition = True
        self.transition_array = []
        self.makeTransitionsHelper(self.state_transitions)

    # helper function
    def makeTransitionsHelper(self, transition_list):
        # if there are no more transitions left, return
        if not transition_list:
            return
        # get the first transition in the list
        transition = transition_list[0]
        # split the transition string
        transition_param = transition.split(':')

        # check if the curr state of transition is out of bounds
        if int(transition_param[0]) < 0 or int(transition_param[0]) >= self.number_of_states:
            self.valid_transition = False

        # check if the destination state of the transition is out of bounds
        if int(transition_param[1]) < 0 or int(transition_param[1]) >= self.number_of_states:
            self.valid_transition = False

        # add the transition to transition array
        self.transition_array.append(
            Transitions(transition_param[0], transition_param[1], transition_param[2]))

        # recursion
        self.makeTransitionsHelper(transition_list[1:])
