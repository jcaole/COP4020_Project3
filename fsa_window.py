# File Name:    fsa_window.py
# Course:       COP4020
# Project:      3
# Author:       Jeremy Caole
# Description:  FSAWindow class,

import tkinter as tk


# update the Y-axis value
def update_y_axis(y):
    return y * 100 + 100


class FSAWindow:
    up = 0

    def __init__(self, id, start, accept):
        self.map = {}       #
        self.id = id
        self.start = start
        self.accept = accept
        self.y = update_y_axis

    # draw the states of the FSA
    def drawState(self, canvas):
        x = 200             # margin x-axis
        diameter = 30       # diameter of states
        resize_oval = 1.25  # variable to adjust inner oval for accept states
        # initial state
        if self.start:
            canvas.create_line(
                x, self.y(self.id) - 50,  # start line length
                x, self.y(self.id) - diameter,
                arrow=tk.LAST
            )
            canvas.create_text(x + diameter, self.y(self.id) - (2 * diameter), text="initial")
        self.drawLines(canvas, x, diameter)
        # accept state
        if self.accept:
            canvas.create_oval(x - diameter, self.y(self.id) - diameter, x + diameter, self.y(self.id) + diameter,
                               fill="white", outline="black", width=2)
            canvas.create_oval(x - diameter / resize_oval, self.y(self.id) - diameter / resize_oval, x + diameter / resize_oval,
                               self.y(self.id) + diameter / resize_oval,
                               fill="white", outline="black", width=2)
        else:
            canvas.create_oval(x - diameter, self.y(self.id) - diameter, x + diameter, self.y(self.id) + diameter,
                               fill="white", width=2)
        canvas.create_text(x, self.y(self.id), text=str(self.id))

    # set the transition to a state
    def setTransition(self, input, output):
        self.map[input] = int(output)

    # get the next state
    def getNext(self, c):
        return self.map.get(c, None)

    # draw the lines for the FSA
    def drawLines(self, canvas, x, diameter):
        ARROW_LENGTH = diameter * 1.5
        ARROW_WIDTH = diameter * 2.85
        TEXT_OFFSET_SAME_STATE = 50
        UP_ARROW_OFFSET = diameter * 2
        SIDE_ARROW_OFFSET = diameter
        TEXT_OFFSET = diameter - 5
        UP_ARROW_INCREMENT = 25
        # same_state_transition_points =

        for i, j in self.map.items():
            # arrow pointing to the same state
            if abs(self.id - j) == 0:
                canvas.create_line(
                    x + diameter, self.y(self.id) + diameter / 2, x + ARROW_LENGTH,
                    self.y(self.id) - 2 * diameter, x + ARROW_WIDTH, self.y(j) + UP_ARROW_OFFSET,
                    x + diameter, self.y(j), smooth=1, arrow=tk.LAST
                )
                canvas.create_text(x + TEXT_OFFSET_SAME_STATE, self.y(self.id), text=i)
            # arrow pointing down
            if abs(self.id - j) == 1:
                canvas.create_line(
                    x,
                    self.y(self.id) - diameter,
                    x,
                    self.y(self.id) + 100 - diameter,
                    arrow=tk.LAST
                )
                canvas.create_text(x + TEXT_OFFSET, self.y(self.id) + (2 * diameter), text=i)
            # arrow pointing up
            if abs(self.id - j) > 1:
                # global up
                # up = 0
                temp = self.up
                canvas.create_line(
                    x,
                    self.y(self.id),
                    x + self.up - UP_ARROW_OFFSET,
                    self.y(self.id),
                    x + self.up - UP_ARROW_OFFSET,
                    self.y(j),
                    x - SIDE_ARROW_OFFSET,
                    self.y(j),
                    arrow=tk.LAST
                )
                canvas.create_text(x + self.up - (diameter * 4), ((self.y(j) - self.y(self.id)) / 2) + self.y(self.id),
                                   text=i)
                self.up = temp + UP_ARROW_INCREMENT