import math
import tkinter as tk


class FSAWindow(tk.Canvas):
    def __init__(self, fsa, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.fsa = fsa
        self.draw()

    def draw(self):
        state_radius = 25  # radius of each state circle
        state_distance = 100  # distance between each state
        margin = 50  # add margin to the left and top of the canvas
        state_coords = {}  # dictionary to store the coordinates of each state
        for i, state in enumerate(self.fsa.states):
            x = state_radius * 2 + margin  # set column number to 0 and add margin to the left
            y = state_distance * i + state_radius * 2 + margin  # use i as the row number and add margin to the top
            state_coords[state] = (x, y)
            fill = "white"
            # color initial state
            if state == self.fsa.initial:
                fill = "light green"
            elif state in self.fsa.finals:
                # if the state is a final state, draw an oval around it
                self.create_oval(x - state_radius * 1.5, y - state_radius * 1.5, x + state_radius * 1.5,
                                 y + state_radius * 1.5, width=2)
                fill = "white"
            # draw the state circle
            self.create_oval(x - state_radius, y - state_radius, x + state_radius, y + state_radius, fill=fill)
            # draw the state label
            self.create_text(x, y, text=str(state))

        for src_state, trans in self.fsa.transitions.items():
            for symbol, dest_state in trans.items():
                # calculate the angle between the source state and the destination state
                src_x, src_y = state_coords[src_state]
                dest_x, dest_y = state_coords[dest_state]
                angle = math.atan2(dest_y - src_y, dest_x - src_x)
                # calculate the offset from the center of the state circle to the intersection of the transition line
                dx = state_radius * math.cos(angle)
                dy = state_radius * math.sin(angle)
                # calculate the start and end points of the transition line
                x1, y1 = src_x + dx, src_y + dy
                x2, y2 = dest_x - dx, dest_y - dy

                if dest_state == src_state:
                    # draw a loopback arrow
                    self.create_arc(x1 - state_radius, y1 - state_radius, x1 + state_radius, y1 + state_radius,
                                    start=0, extent=260, style=tk.ARC, width=2, outline="black")
                    # calculate the position of the transition label
                    text_x, text_y = x1 - state_radius / 2, y1 - state_radius / 2
                else:
                    # draw the transition line with an arrow at the end
                    self.create_line(x1, y1, x2, y2, arrow=tk.LAST)
                    # calculate the position of the transition label
                    text_x, text_y = (x1 + x2) / 2, (y1 + y2) / 2
                    if abs(x2 - x1) < abs(y2 - y1):
                        # if the transition is vertical, move the label to the right
                        text_x += state_radius / 2 * math.copysign(1, math.cos(angle))
                    else:
                        # if the transition is horizontal, move the label up
                        text_y += state_radius / 2 * math.copysign(1, math.sin(angle))

                # draw the transition label
                self.create_text(text_x, text_y, text=symbol)