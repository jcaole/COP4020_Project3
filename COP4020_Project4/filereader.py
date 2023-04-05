# File Name:    filereader.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  reads file and tokenizes the content of the file

class FileReader:
    fsa_name = ''

    def __init__(self, fsa_name):
        self.fsa_name = fsa_name
        self.tokens = []

    def read(self):
        with open(self.fsa_name) as f:
            file_to_read = f.readline()
        #     check file output
        print('Reading FSA: ' + file_to_read)
        self.tokens = file_to_read.split(';')
        f.close()

    def showTokens(self):
        for i in range(0, len(self.tokens) - 1):
            print('token - ' + self.tokens[i])

    def setStrings(self):
        self.state_num_string = self.tokens[0]
        self.alphabet_string = self.tokens[1]
        self.transition_string = self.tokens[2]
        self.start_state = self.tokens[3]
        self.accept_state = self.tokens[4]

    def tokenizeString(self):
        self.tokenizeAlphabet()
        self.tokenizeTransition()
        self.tokenizeAcceptState()

    def tokenizeTransition(self):
        self.transition_string = self.transition_string.replace('(', '')
        self.transition_string = self.transition_string.replace(')', '')
        self.transition_tokens = self.transition_string.split(',')

    def tokenizeAlphabet(self):
        self.alphabetTokens = self.alphabet_string.split(',')

        for i in range(0, len(self.alphabetTokens)):
            self.alphabetTokens[i] = self.alphabetTokens[i].strip()

    def tokenizeAcceptState(self):
        self.acceptTokens = self.accept_state.split(',')

    def getStateNum(self):
        return int(self.state_num_string)

    def getAlphabet(self):
        return self.alphabetTokens

    def getTransitionStates(self):
        return self.transition_tokens

    def getStartState(self):
        return self.start_state

    def getAcceptStates(self):
        return self.acceptTokens

    def run(self):
        self.read()
        self.setStrings()
        self.tokenizeString()
