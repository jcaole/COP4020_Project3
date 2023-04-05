# File Name:    fsa.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  FSA class, parses, checks and main method

from filereader import FileReader
from transitions import Transitions
from lisp_fsa_gen import LispFSAGenerator


# Read the contents of a file
def readFile(self, fileName):
    with open(fileName) as f:
        content = f.read()
    self.input = content
    f.close()


class FSA:
    state_list = []

    def __init__(self, stateNum, alphabet, stateTransitions, startState, acceptStates):
        self.currentState = None
        self.input = None
        self.state_num = stateNum
        self.alphabet = alphabet
        self.state_transitions = stateTransitions
        self.start_state = startState
        self.accept_states = acceptStates
        self.current_state = int(self.start_state)
        self.transition_array = []
        self.valid_transition = True

    # Traverse the FSA graph recursively and check if a given string is accepted or not
    def makeTransitions(self):
        for transition in self.state_transitions:
            transition_param = transition.split(':')

            if (((int(transition_param[0]) < 0) or (int(transition_param[0]) >= self.state_num)) or (
                    (int(transition_param[1]) < 0) or (int(transition_param[1]) >= self.state_num))):
                self.valid_transition = False

            self.transition_array.append(
                Transitions(transition_param[0], transition_param[1], transition_param[2]))

    def showStateTransitions(self):
        for i in range(0, len(self.state_transitions)):
            print('State transition - ' + self.state_transitions[i])

    def checkInAlpha(self, letter):
        for i in range(0, len(self.alphabet)):
            if letter == self.alphabet[i]:
                return True
        return False

    def runFSA(self):
        self.makeTransitions()
        round_num = 0

        for letter in self.input:
            round_num = round_num + 1
            if not self.checkInAlpha(letter):
                print("Invalid character. Input String %s is Illegal!" % self.getFileInput())
                return

            for i in range(0, len(self.transition_array)):
                if not self.checkState(self.transition_array[i]):
                    return
                if self.checkTransition(self.transition_array[i], letter):
                    break

        self.checkForAcceptState()

    def runLispFSAGenerator(self):
        lisp_gen = LispFSAGenerator(self.state_num, self.alphabet, self.state_transitions, self.transition_array,
                                    self.start_state,
                                    self.accept_states)
        lisp_gen.writeFile()

    def checkForAcceptState(self):

        if not self.valid_transition:
            print("Invalid State or Transition, input %s is not accepted!" % self.getFileInput())
            return

        for state in self.getAcceptStates():
            if self.currentState == int(state):
                print("legal!" % self.getFileInput())
                return True
            else:
                pass
        print("illegal!" % self.getFileInput())
        return False

    def checkState(self, transition):
        if not transition.isStateValid(self.state_num):
            return False
        return True

    def checkTransition(self, transition, letter):
        if transition.isTransitionValid(self.current_state, letter):
            self.currentState = transition.getNextState()
            return True
        else:
            return False

    def getStateNum(self):
        return self.state_num

    def getAlphabet(self):
        return self.alphabet

    def getStateTransitions(self):
        return self.state_transitions

    def getTransitionArray(self):
        return self.transition_array

    def getStartState(self):
        return self.start_state

    def getAcceptStates(self):
        return self.accept_states

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

    fsa.runLispFSAGenerator()
