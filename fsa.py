import tkinter as tk

from fsa_window import FSAWindow


class FSA:
    # initialize variables
    def __init__(self, states, alphabet, transitions, initial, finals):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial = initial
        self.finals = finals

    def accepts(self, string):
        current_state = self.initial
        for char in string:
            # testing character transitions to states
            # note: f'' allows formatting in string literal
            # print(f"checking character '{char}' at state {current_state}")
            if char not in self.alphabet:
                # testing character not in alphabet for fsa.txt
                # print(f"Invalid character '{char}'")
                return False
            try:
                current_state = self.transitions[current_state][char]
            except KeyError:
                # print(f"No transition from state {current_state} with input '{char}'")
                return False
        # checks to see if the string ended in a final state
        if current_state in self.finals:
            # print(f"Reached final state | state {current_state}")
            return True
        else:
            # print(f"Did not end in a final state | state: {current_state}")       # format string literal
            return False


# parses FSA file
def parseFSAFile(filename):
    # Open the FSA file and read its contents
    with open(filename, 'r') as fsa_file:
        fsa_string = fsa_file.read().strip()

    # Split the FSA string into its parts
    fsa_parts = fsa_string.split(';')
    num_states = int(fsa_parts[0])  # Get the number of states
    alphabet = set(fsa_parts[1])  # Get the alphabet
    transitions = {}
    for trans in fsa_parts[2].split(','):  # Get the transition table
        parts = trans[1:-1].split(':')
        src_state = int(parts[0])
        dest_state = int(parts[1])
        symbol = parts[2]
        # if a symbol is not in dictionary
        if symbol not in alphabet:
            raise ValueError(f"Invalid symbol '{symbol}' in transition from state {src_state} to state {dest_state}")
        transitions.setdefault(src_state, {})[symbol] = dest_state
    initial_state = int(fsa_parts[3])  # Get the initial state
    final_states = [int(x) for x in fsa_parts[4].split(',')]  # Get the final states

    # Create an FSA object and return it
    return FSA(range(num_states), sorted(list(alphabet)), transitions, initial_state, final_states)


# def show_tokens(tokens):
#     for token in tokens[:-1]:
#         print('token - ' + token)

# method checks to see if input file is legal/illegal
def checkFile(fsaFile, inputFile):
    # Read in the FSA file and create the FSA object
    fsa = parseFSAFile(fsaFile)

    # Read in the strings from the input file
    with open(inputFile, 'r') as f:
        inputStrings = f.readlines()

    # Remove whitespace characters from each error string
    inputStrings = [checkingString for checkingString in inputStrings]

    # Checks to see if the FSA accepts input string
    for checkingString in inputStrings:
        if fsa.accepts(checkingString):
            print(f'{checkingString} is a legal string')  # format string literal
        else:
            print(f'{checkingString} is an illegal string')  # format string literal


if __name__ == '__main__':
    import sys

    fsa_filename = sys.argv[1]
    input_filename = sys.argv[2]

    # testing output
    # print("fsa_filename: " + fsa_filename)
    # print("filename: " + filename + "\n")

    # fsa = read_fsa_file(fsa_filename)
    fsa = parseFSAFile(fsa_filename)
    # tokens = fsa.to_tokens()
    checkFile(fsa_filename, input_filename)

    window = tk.Tk()
    window.title('FSA processor')
    canvas = FSAWindow(fsa, master=window, width=600, height=600)
    canvas.pack(fill=tk.BOTH, expand=True)

    # starting GUI event loop
    window.mainloop()
    print("\n")
