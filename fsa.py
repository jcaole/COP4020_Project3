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
            if char not in self.alphabet:
                return False
            try:
                current_state = self.transitions[current_state][char]
            except KeyError:
                return False
        return current_state in self.finals


# def read_fsa_file(filename):
#     with open(filename, 'r') as fsa_file:
#         fsa_string = fsa_file.read().strip()
#
#     fsa_parts = fsa_string.split(';')
#     num_states = int(fsa_parts[0])
#     alphabet = fsa_parts[1].split(',')
#     transitions = {}
#     states = set()
#     for trans in fsa_parts[2].split(','):
#         parts = trans[1:-1].split(':')
#         src_state = int(parts[0])
#         dest_state = int(parts[1])
#         symbol = parts[2]
#         states.add(src_state)
#         states.add(dest_state)
#         if src_state not in transitions:
#             transitions[src_state] = {}
#         transitions[src_state][symbol] = dest_state
#     initial_state = int(fsa_parts[3])
#     final_states = [int(x) for x in fsa_parts[4].split(',')]
#
#     return FSA(states, alphabet, initial_state, final_states, transitions)

def read_fsa_file(filename):
    # Open the FSA file and read its contents
    with open(filename, 'r') as fsa_file:
        fsa_string = fsa_file.read().strip()

    # Split the FSA string into its parts
    fsa_parts = fsa_string.split(';')
    num_states = int(fsa_parts[0])  # Get the number of states
    alphabet = fsa_parts[1].split(',')  # Get the alphabet
    transitions = {}
    for trans in fsa_parts[2].split(','):  # Get the transition table
        parts = trans[1:-1].split(':')
        src_state = int(parts[0])
        dest_state = int(parts[1])
        symbol = parts[2]
        if src_state not in transitions:
            transitions[src_state] = {}
        transitions[src_state][symbol] = dest_state
    initial_state = int(fsa_parts[3])  # Get the initial state
    final_states = [int(x) for x in fsa_parts[4].split(',')]  # Get the final states

    # Create an FSA object and return it
    return FSA(range(num_states), alphabet, initial_state, final_states, transitions)


def check_file(fsa_filename, error_filename):
    # Read in the FSA file and extract its components
    with open(fsa_filename, 'r') as fsa_file:
        fsa_string = fsa_file.read().strip()

    fsa_parts = fsa_string.split(';')
    num_states = int(fsa_parts[0])
    alphabet = fsa_parts[1].split(',')
    transitions = {}
    for trans in fsa_parts[2].split(','):
        parts = trans[1:-1].split(':')
        src_state = int(parts[0])
        dest_state = int(parts[1])
        symbol = parts[2]
        # Create a nested dictionary for the transition function
        if src_state not in transitions:
            transitions[src_state] = {}
        transitions[src_state][symbol] = dest_state
    initial_state = int(fsa_parts[3])
    final_states = [int(x) for x in fsa_parts[4].split(',')]
    # Create the FSA object
    fsa = FSA(range(num_states), alphabet, initial_state, final_states, transitions)

    # Read in the error string from the error file
    with open(error_filename, 'r') as f:
        string = f.read().strip()

    # Check if the FSA accepts the error string
    if fsa.accepts(string):
        print(f'{string} is a legal string')
        return True
    else:
        print(f'{string} is an illegal string')
        return False



if __name__ == '__main__':
    import sys

    fsa_filename = sys.argv[1]
    filename = sys.argv[2]

    # testing output
    # print(fsa_filename)
    # print(filename)
    fsa = read_fsa_file(fsa_filename)
    check_file(fsa_filename, filename)

    window = tk.Tk()
    window.title('FSA processor')
    canvas = FSAWindow(fsa, master=window, width=600, height=400)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Start the GUI event loop
    window.mainloop()