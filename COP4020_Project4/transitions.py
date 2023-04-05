# File Name:    fsa.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  FSA class, parses, checks and main method

class Transitions:
    def __init__(self, startState, nextState, transitionCharacter):
        self.start_state = int(startState)
        self.next_state = int(nextState)
        self.transition_character = transitionCharacter

    def validateTransition(self, currentState, char):
        if (currentState == self.startState) and (char == self.transition_character):
            return True
        else:
            return False

    def validateState(self, numOfStates):
        if ((self.start_state < 0) or (self.start_state >= numOfStates)) or (
                (self.next_state < 0) or (self.next_state >= numOfStates)):
            return False
        else:
            return True

    def getStartState(self):
        return self.start_state

    def getNextState(self):
        return self.next_state

    def getTransitionCharacter(self):
        return self.transition_character
