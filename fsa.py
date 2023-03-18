import tkinter as tk

# from fsa import read_fsa_file
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


def read_fsa_file(filename):
    with open(filename, 'r') as fsa_file:
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
        if src_state not in transitions:
            transitions[src_state] = {}
        transitions[src_state][symbol] = dest_state
    initial_state = int(fsa_parts[3])
    final_states = [int(x) for x in fsa_parts[4].split(',')]

    return FSA(range(num_states), alphabet, initial_state, final_states, transitions)


def check_file(fsa_filename, filename):
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
        if src_state not in transitions:
            transitions[src_state] = {}
        transitions[src_state][symbol] = dest_state
    initial_state = int(fsa_parts[3])
    final_states = [int(x) for x in fsa_parts[4].split(',')]
    fsa = FSA(range(num_states), alphabet, initial_state, final_states, transitions)

    with open(filename, 'r') as f:
        string = f.read().strip()

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

    # fsa_filename = 'fsa.txt'
    # filename = 'legal1.txt'

    check_file(fsa_filename, filename)

    read_fsa_file(filename)
    window = tk.Tk()
    window.title('FSA processor')
    canvas = FSAWindow(FSA, master=window, width=600, height=400)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Start the GUI event loop
    window.mainloop()

# # import math
# # import tkinter as tk
#
#
# class FSA:
#     def __init__(self, states, alphabet, initial, finals, transitions):
#         self.states = states
#         self.alphabet = alphabet
#         self.initial = initial
#         self.finals = finals
#         self.transitions = transitions
#
#     def accepts(self, string):
#         current_state = self.initial
#         for char in string:
#             if char not in self.alphabet:
#                 return False
#             try:
#                 current_state = self.transitions[current_state][char]
#             except KeyError:
#                 return False
#         return current_state in self.finals
#
#
# def read_fsa_file(filename):
#     with open(filename, 'r') as fsa_file:
#         fsa_string = fsa_file.read().strip()
#
#     fsa_parts = fsa_string.split(';')
#     num_states = int(fsa_parts[0])
#     alphabet = fsa_parts[1].split(',')
#     transitions = {}
#     for trans in fsa_parts[2].split(','):
#         parts = trans[1:-1].split(':')
#         src_state = int(parts[0])
#         dest_state = int(parts[1])
#         symbol = parts[2]
#         if src_state not in transitions:
#             transitions[src_state] = {}
#         transitions[src_state][symbol] = dest_state
#     initial_state = int(fsa_parts[3])
#     final_states = [int(x) for x in fsa_parts[4].split(',')]
#
#     return FSA(range(num_states), alphabet, initial_state, final_states, transitions)
#
#
# def check_file(filename):
#     fsa = read_fsa_file('fsa.txt')
#     with open(filename, 'r') as f:
#         string = f.read().strip()
#     if fsa.accepts(string):
#         print(f'{string} is a legal string')
#     else:
#         print(f'{string} is an illegal string')
