class FileReader:
    fsaname = ''

    def __init__(self, fsaname):
        self.fsaname = fsaname

    def read(self):
        with open(self.fsaname) as f:
            content = f.readline()
        print('the FSA: ' + content)
        global tokens
        self.tokens = content.split(';')
        f.close()

    def showTokens(self):
        for i in range(0, len(self.tokens) - 1):
            print('token - ' + self.tokens[i])

    def setStrings(self):
        self.stateNumString = self.tokens[0]
        self.alphabetString = self.tokens[1]
        self.transitionString = self.tokens[2]
        self.startStateString = self.tokens[3]
        self.acceptStateString = self.tokens[4]

    def tokenizeString(self):
        self.tokenizeAlphabet()
        self.tokenizeTransition()
        self.tokenizeAcceptState()

    def tokenizeTransition(self):
        self.transitionString = self.transitionString.replace('(', '')
        self.transitionString = self.transitionString.replace(')', '')
        self.transitionTokens = self.transitionString.split(',')

    def tokenizeAlphabet(self):
        self.alphabetTokens = self.alphabetString.split(',')

        for i in range(0, len(self.alphabetTokens)):
            self.alphabetTokens[i] = self.alphabetTokens[i].strip()

    def tokenizeAcceptState(self):
        self.acceptTokens = self.acceptStateString.split(',')

    def getStateNum(self):
        return int(self.stateNumString)

    def getAlphabet(self):
        return self.alphabetTokens

    def getTransitionStates(self):
        return self.transitionTokens

    def getStartState(self):
        return self.startStateString

    def getAcceptStates(self):
        return self.acceptTokens

    def run(self):
        self.read()
        self.setStrings()
        self.tokenizeString()