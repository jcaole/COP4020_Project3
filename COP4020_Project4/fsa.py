# File Name:    fsa.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  FSA class, parses, checks and main method

from filereader import FileReader
from transitions import Transitions
from lispmaker import LispMaker


# Read the contents of a file and remove all spaces
def readFile(self, fileName):
    with open(fileName) as f:
        content = f.readline()
    self.input = content
    f.close()


class FSA:
    state_list = []

    def __init__(self, stateNum, alphabet, stateTransitons, startState, acceptStates):
        self.stateNum = stateNum
        self.alphabet = alphabet
        self.stateTransitons = stateTransitons
        self.startState = startState
        self.acceptStates = acceptStates
        self.currentState = int(self.startState)
        self.transitionArray = []
        self.transitionsValid = True

    # Traverse the FSA graph recursively and check if a given string is accepted or not
    def makeTransitions(self):
        for transition in self.stateTransitons:
            transition_param = transition.split(':')

            if (((int(transition_param[0]) < 0) or (int(transition_param[0]) >= self.stateNum)) or (
                    (int(transition_param[1]) < 0) or (int(transition_param[1]) >= self.stateNum))):
                self.transitionsValid = False

            self.transitionArray.append(
                Transitions(transition_param[0], transition_param[1], transition_param[2]))

    def showStateTransitions(self):
        for i in range(0, len(self.stateTransitons)):
            print('State transition - ' + self.stateTransitons[i])

    def checkInAlpha(self, letter):
        for i in range(0, len(self.alphabet)):
            if letter == self.alphabet[i]:
                return True
        return False

    def runFSA(self):
        self.makeTransitions()
        roundNum = 0

        for letter in self.input:
            roundNum = roundNum + 1
            if not self.checkInAlpha(letter):
                print("Invalid letter. Input String %s is not accepted!" % self.getFileInput())
                return

            for i in range(0, len(self.transitionArray)):
                if not self.checkState(self.transitionArray[i]):
                    return
                if self.checkTransition(self.transitionArray[i], letter):
                    break

        self.checkForAcceptState()

    def runLispMaker(self):
        lispMaker = LispMaker(self.stateNum, self.alphabet, self.stateTransitons, self.transitionArray, self.startState,
                              self.acceptStates)
        lispMaker.writeFile()

    def checkForAcceptState(self):

        if not self.transitionsValid:
            print("Invalid State or Transition, input %s is not accepted!" % self.getFileInput())
            return

        for state in self.getAcceptStates():
            if self.currentState == int(state):
                print("Input String %s accepted!" % self.getFileInput())
                return True
            else:
                pass
        print("Input String %s not accepted!" % self.getFileInput())
        return False

    def checkState(self, transition):
        if not transition.isStateValid(self.stateNum):
            return False
        return True

    def checkTransition(self, transition, letter):
        if transition.isTransitionValid(self.currentState, letter):
            self.currentState = transition.getNextState()
            return True
        else:
            return False

    def getStateNum(self):
        return self.stateNum

    def getAlphabet(self):
        return self.alphabet

    def getStateTransitions(self):
        return self.stateTransitons

    def getTransitionArray(self):
        return self.transitionArray

    def getStartState(self):
        return self.startState

    def getAcceptStates(self):
        return self.acceptStates

    def getFileInput(self):
        return self.input


# Main function
if __name__ == "__main__":
    import sys  # needed to implement inputs arguments

    reader = FileReader(sys.argv[1])
    reader.run()

    fsa = FSA(reader.getStateNum(), reader.getAlphabet(), reader.getTransitionStates(), reader.getStartState(),
              reader.getAcceptStates())

    fsa.makeTransitions()

    fsa.runLispMaker()
