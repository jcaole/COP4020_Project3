import math
import tkinter as tk


class FSAWindow(tk.Canvas):
    def __init__(self, fsa, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.fsa = fsa
        self.draw()

    def draw(self):
        state_radius = 30
        state_distance = 200  # increase state distance
        margin = 50  # add margin
        state_coords = {}
        for i, state in enumerate(self.fsa.states):
            x = state_distance * (i % 3) + state_radius * 2 + margin
            y = state_distance * (i // 3) + state_radius * 2 + margin
            state_coords[state] = (x, y)
            fill = "white"
            if state == self.fsa.initial:
                fill = "light green"
            elif state in self.fsa.finals:
                self.create_oval(x - state_radius * 1.5, y - state_radius * 1.5, x + state_radius * 1.5, y + state_radius * 1.5, width=2)
                fill = "white"
            self.create_oval(x - state_radius, y - state_radius, x + state_radius, y + state_radius, fill=fill)
            self.create_text(x, y, text=str(state))

        for src_state, trans in self.fsa.transitions.items():
            for symbol, dest_state in trans.items():
                src_x, src_y = state_coords[src_state]
                dest_x, dest_y = state_coords[dest_state]
                angle = math.atan2(dest_y - src_y, dest_x - src_x)
                dx = state_radius * math.cos(angle)
                dy = state_radius * math.sin(angle)
                x1, y1 = src_x + dx, src_y + dy
                x2, y2 = dest_x - dx, dest_y - dy
                self.create_line(x1, y1, x2, y2, arrow=tk.LAST)
                text_x, text_y = (x1 + x2) / 2, (y1 + y2) / 2
                if abs(x2 - x1) < abs(y2 - y1):
                    text_x += state_radius / 2 * math.copysign(1, math.cos(angle))
                else:
                    text_y += state_radius / 2 * math.copysign(1, math.sin(angle))
                self.create_text(text_x, text_y, text=symbol)