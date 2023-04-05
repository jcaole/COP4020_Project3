# File Name:    lisp_fsa_gen.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  Lisp FSA generator class.

def writeDemo(fp):
    fp.write('(DEFUN demo()\n')
    fp.write('\t(setq fp (open "theString.txt" :direction :input))\n')
    fp.write('\t(setq list (read fp "done"))\n')
    fp.write('\t(princ "processing ")\n')
    fp.write('\t(princ list)\n')
    fp.write('\t(fsa list)\n')
    fp.write(')\n\n')


class LispFSAGenerator:

    def __init__(self):
        print("")

    def __init__(self, stateNum, alphabet, stateTransitons, transitionArray, startState, acceptStates):
        print("")
        self.stateNum = stateNum
        self.alphabet = alphabet
        self.stateTransitons = stateTransitons
        self.transitionArray = transitionArray
        self.startState = startState
        self.acceptStates = acceptStates

    def writeFile(self):
        with open('part2.lsp', 'w') as fp:
            writeDemo(fp)
            self.writeFSA(fp)
            self.writeStates(fp)

    def writeFSA(self, fp):
        fp.write('(DEFUN fsa(list)\n')
        fp.write('\t(cond \n')
        fp.write('\t\t((null list) "illegal")\n')
        fp.write(f'\t\t(t(state{self.startState} list))\n')
        fp.write('\t)\n')
        fp.write(')\n\n')

    def writeStates(self, fp):
        for i in range(0, self.stateNum):
            fp.write(f'(DEFUN state{i}(list)\n')
            fp.write('\t(cond \n')
            if self.checkAcceptState(i) == 1:
                fp.write(f'\t\t((null list) "legal")\n')
            else:
                fp.write(f'\t\t((null list) "illegal character in state {i}")\n')

            self.writeTransitionCode(i, fp)

            fp.write('\t)\n')
            fp.write(')\n\n')

    def checkAcceptState(self, i):
        for acceptState in self.acceptStates:
            if str(i) == acceptState:
                return 1
        return 0

    def writeTransitionCode(self, i, fp):
        for transitions in self.transitionArray:
            if i == transitions.getStartState():
                fp.write(
                    f'\t\t((equal \'{transitions.getTransitionCharacter()} (car list)) (state{transitions.getNextState()}(cdr list)))\n')
        fp.write(f'\t\t(t "illegal character in state {i}")\n')
