# File Name:    transitions.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  represents the state transition for fsa. gets start, next,
# and transition variables

class Transitions:
    def __init__(self, currState, nextState, transition):
        # Initialize variables
        self.curr_state = int(currState)
        self.next_state = int(nextState)
        self.transition = transition

    # getters
    def getCurrent(self):
        # Return the start state
        return self.curr_state

    def getNext(self):
        # Return the next state
        return self.next_state

    def getTransition(self):
        # Return the transition
        return self.transition
