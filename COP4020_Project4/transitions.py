# File Name:    fsa.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  FSA class, parses, checks and main method
class Transitions:
    def __init__(self, startState, nextState, transitionChar):
        self.startState = int(startState)
        self.nextState = int(nextState)
        self.transitionChar = transitionChar

    def isTransitionValid(self, currentState, char):
        if (currentState == self.startState) and (char == self.transitionChar):
            return True
        else:
            return False

    def isStateValid(self, numOfStates):
        if ((self.startState < 0) or (self.startState >= numOfStates)) or (
                (self.nextState < 0) or (self.nextState >= numOfStates)):
            return False
        else:
            return True

    def getStartState(self):
        return self.startState

    def getNextState(self):
        return self.nextState

    def getTransitionChar(self):
        return self.transitionChar