# File Name:    file_reader.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  reads file and tokenizes the content of the file

class FileReader:
    def __init__(self, file):
        self.acceptTokens = None
        self.alphabetTokens = None
        self.transition_tokens = None
        self.start_state = None
        self.accept_state = None
        self.transition_string = None
        self.alphabet_string = None
        self.state_num_string = None
        self.fsa_file = file
        self.tokens = []

    def read(self):
        with open(self.fsa_file) as f:
            file_to_read = f.read()
            # TEST: checking the file
            # print(fsa_file)
            # TEST: checking the contents of the file
            # print(file_to_read)
            print("Reading FSA")
        # Split the file contents by semicolons to get tokens
        self.tokens = file_to_read.split(';')
        # Close the file
        f.close()

    # Show the tokens from theString.txt
    def showTokens(self):
        for i in range(0, len(self.tokens) - 1):
            print('token - ' + self.tokens[i])

    # Tokenize strings the variables
    def tokenizer(self):
        self.tokenizeAlphabet()
        self.tokenizeTransition()
        self.tokenizeAccept()

    # Split the transition list into tokens
    def tokenizeTransition(self):
        self.transition_string = self.transition_string.replace('(', '')
        self.transition_string = self.transition_string.replace(')', '')
        self.transition_tokens = self.transition_string.split(',')

    # Split the alphabet string into tokens
    def tokenizeAlphabet(self):
        self.alphabetTokens = self.alphabet_string.split(',')

        for i in range(0, len(self.alphabetTokens)):
            self.alphabetTokens[i] = self.alphabetTokens[i].strip()

    # Split the accept state string tokens
    def tokenizeAccept(self):
        self.acceptTokens = self.accept_state.split(',')

    # Split the tokens into separate strings for each variable
    def setStrings(self):
        self.state_num_string = self.tokens[0]
        self.alphabet_string = self.tokens[1]
        self.transition_string = self.tokens[2]
        self.start_state = self.tokens[3]
        self.accept_state = self.tokens[4]

    # -----------Getters------------
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

    #  run method, runs the methods of the class.
    def run(self):
        self.read()
        self.setStrings()
        self.tokenizer()
