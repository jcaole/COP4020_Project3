# File Name:    lisp_fsa_gen.py
# Course:       COP4020
# Project:      4
# Author:       Jeremy Caole
# Description:  Lisp FSA generator class creates part2.lsp file from fileReader

from file_reader import FileReader
from fsa import FSA


# write demo method
def writeDemo(fp):
    fp.write('(DEFUN demo()\n')
    fp.write('\t(setq fp (open "theString.txt" :direction :input))\n')
    fp.write('\t(setq l (read fp "done"))\n')
    fp.write('\t(princ "processing ")\n')
    fp.write('\t(princ l)\n')
    fp.write('\t(fsa l)\n')
    fp.write(')\n\n')


class LispFSAGenerator:
    def __init__(self, stateNum, alphabet, stateTransitions, transitionArray, startState, acceptStates):
        print("")
        self.state_num = stateNum
        self.alphabet = alphabet
        self.state_transitions = stateTransitions
        self.transition_array = transitionArray
        self.start_state = startState
        self.accept_states = acceptStates

    # write the lisp program to part2.lsp
    def writeFile(self):
        with open('part2.lsp', 'w') as fp:
            writeDemo(fp)
            self.writeFSA(fp)
            self.writeStates(fp)

    # write the lisp code for the fsa
    def writeFSA(self, fp):
        fp.write('(DEFUN fsa(l)\n')
        fp.write('\t(cond \n')
        fp.write('\t\t((null l) "illegal")\n')
        fp.write(f'\t\t(t(state{self.start_state} l))\n')
        fp.write('\t)\n')
        fp.write(')\n\n')

    # write states to lisp program
    def writeStates(self, fp):
        # write lisp code for each state
        self.writeRecursiveState(0, fp)

    # attempt on recursion, write lisp code for each state
    def writeRecursiveState(self, i, fp):
        # once all code is written, return
        if i == self.state_num:
            return

        # write lisp code for current state
        fp.write(f'(DEFUN state{i}(l)\n')
        fp.write('\t(cond \n')
        if self.checkAcceptState(i) == 1:
            fp.write(f'\t\t((null l) "legal")\n')
        else:
            fp.write(f'\t\t((null l) "illegal character in state {i}")\n')

        # write lisp code for state transitions
        self.writeTransitionCode(i, fp)

        fp.write('\t)\n')
        fp.write(')\n\n')

        # attempt on recursion, next state
        self.writeRecursiveState(i + 1, fp)

    # check to see if state is in an accept state
    def checkAcceptState(self, i):
        for acceptState in self.accept_states:
            if str(i) == acceptState:
                return 1
        return 0

    # write lisp code for state transistions
    def writeTransitionCode(self, i, fp):
        for transitions in self.transition_array:
            if i == transitions.getStartState():
                fp.write(
                    f'\t\t((equal \'{transitions.getTransitionCharacter()} (car l)) (state{transitions.getNextState()}(cdr l)))\n')
        fp.write(f'\t\t(t "illegal character in state {i}")\n')


if __name__ == "__main__":
    import sys  # needed to implement inputs arguments

    # theString.txt
    file_reader = FileReader(sys.argv[1])
    file_reader.run()

    # fsa.txt
    fsa = FSA(file_reader.getStateNum(), file_reader.getAlphabet(), file_reader.getTransitionStates(),
              file_reader.getStartState(),
              file_reader.getAcceptStates())

    print("\nGenerating Program")
    fsa.makeTransitions()

    # instance of lispFSAGenerator
    lisp_gen = LispFSAGenerator(fsa.number_of_states, fsa.alphabet, fsa.state_transitions, fsa.transition_array,
                                fsa.start_state,
                                fsa.accept_states)
    # generate lisp program file
    lisp_gen.writeFile()
