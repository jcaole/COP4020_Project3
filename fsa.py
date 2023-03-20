import tkinter as tk

from fsa_window import FSAWindow


class FSA:
    def __init__(self, states, alphabet, initial, finals, transitions):
        self.states = states
        self.alphabet = alphabet
        self.initial = initial
        self.finals = finals
        self.transitions = transitions

    def accepts(self, string):
        current_state = self.initial
        for char in string:
            # print(f"Processing character '{char}' at state {current_state}")
            if char not in self.alphabet:
                # print(f"Invalid character '{char}'")
                return False
            try:
                current_state = self.transitions[current_state][char]
            except KeyError:
                # print(f"No transition from state {current_state} with input '{char}'")
                return False
        if current_state in self.finals:
            # print(f"Reached final state {current_state}")
            return True
        else:
            # print(f"Ended at non-final state {current_state}")
            return False


def read_fsa_file(filename):
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
        if symbol not in alphabet:
            raise ValueError(f"Invalid symbol '{symbol}' in transition from state {src_state} to state {dest_state}")
        transitions.setdefault(src_state, {})[symbol] = dest_state
    initial_state = int(fsa_parts[3])  # Get the initial state
    final_states = [int(x) for x in fsa_parts[4].split(',')]  # Get the final states

    # Create an FSA object and return it
    return FSA(range(num_states), sorted(list(alphabet)), initial_state, final_states, transitions)



# def show_tokens(tokens):
#     for token in tokens[:-1]:
#         print('token - ' + token)


def check_file(fsa_filename, error_filename):
    # Read in the FSA file and create the FSA object
    fsa = read_fsa_file(fsa_filename)

    # Read in the error strings from the error file
    with open(error_filename, 'r') as f:
        error_strings = f.readlines()

    # Remove any whitespace characters from each error string
    error_strings = [error_string.strip() for error_string in error_strings]

    # Check if the FSA accepts each error string
    for error_string in error_strings:
        if fsa.accepts(error_string):
            print(f'{error_string} is a legal string')
        else:
            print(f'{error_string} is an illegal string')


if __name__ == '__main__':
    import sys

    fsa_filename = sys.argv[1]
    filename = sys.argv[2]

    # testing output
    # print("fsa_filename: " + fsa_filename)
    # print("filename: " + filename + "\n")

    # fsa = read_fsa_file(fsa_filename)
    fsa = read_fsa_file(fsa_filename)
    # tokens = fsa.to_tokens()
    check_file(fsa_filename, filename)

    window = tk.Tk()
    window.title('FSA processor')
    canvas = FSAWindow(fsa, master=window, width=600, height=400)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Start the GUI event loop
    window.mainloop()
    print("\n")
