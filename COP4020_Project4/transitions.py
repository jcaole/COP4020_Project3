# File Name:    transitions.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  represents the state transition for fsa. checks transition, gets start, next,
# and transition character (alphabet)

class Transitions:
    def __init__(self, startState, nextState, transitionCharacter):
        # Initialize variables
        self.start_state = int(startState)
        self.next_state = int(nextState)
        self.transition_character = transitionCharacter

    def checkState(self, numStates):
        # check start and next state
        if self.start_state < 0 or self.start_state >= numStates or self.next_state < 0 or self.next_state >= numStates:
            return False
        else:
            return True

    def getStartState(self):
        # Return the start state
        return self.start_state

    def getNextState(self):
        # Return the next state
        return self.next_state

    def getTransitionCharacter(self):
        # Return the transition character
        return self.transition_character


# Attempt to utilize recursion to validate transitions
def checkTransitionsHelper(transitions, current_state, char):
    # If there are no more transitions to validate, return False
    if not transitions:
        return False
    # If the current transition is valid, return True
    elif transitions[0].validateTransition(current_state, char):
        return True
    # Otherwise, recurse with the remaining transitions
    else:
        return checkTransitionsHelper(transitions[1:], current_state, char)


def cheTransitions(transitions, current_state, char):
    # Call the helper function to validate transitions
    return checkTransitionsHelper(transitions, current_state, char)

