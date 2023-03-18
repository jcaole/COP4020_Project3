import tkinter as tk

from fsa import read_fsa_file, check_file
from fsa_window import FSAWindow


def main():
    # Read the FSA from a file
    fsa = read_fsa_file('fsa.txt')
    # fsa = read_fsa_file('fsa.txt')

    # Create a window to display the FSA
    window = tk.Tk()
    window.title('FSA processor')
    canvas = FSAWindow(fsa, master=window, width=600, height=400)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Start the GUI event loop
    window.mainloop()


    # fsa_filename = 'fsa.txt'
    legal_filename = 'legal.txt'
    illegal_filename = 'illegal.txt'

    print('Checking legal file...')
    check_file(fsa, legal_filename)

    print('\nChecking illegal file...')
    check_file(fsa, illegal_filename)


if __name__ == '__main__':
    main()
