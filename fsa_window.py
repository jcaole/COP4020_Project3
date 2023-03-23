import tkinter as tk


# update the Y-axis value
def update_y_axis(y):
    return y * 100 + 100


class FSAWindow:
    def __init__(self, id, start, accept):
        self.map = {}
        self.id = id
        self.start = start
        self.accept = accept
        self.y = update_y_axis

    # set the transition to a state
    def setTransition(self, input, output):
        self.map[input] = int(output)

    # get the next state
    def getNext(self, c):
        return self.map.get(c, None)

    # draw the lines for the FSA
    def drawLines(self, canvas, x, diameter):
        for i, j in self.map.items():
            # arrow pointing to the same state
            if abs(self.id - j) == 0:
                canvas.create_line(
                    x + diameter, self.y(self.id) + diameter / 4, x + (diameter * 2),
                    self.y(self.id) - 2 * diameter, x + (diameter * 2), self.y(j) + diameter * 2,
                    x + diameter, self.y(j), smooth=1, arrow=tk.LAST
                )
                canvas.create_text(x + 50, self.y(self.id), text=i)
            # arrow pointing down
            if abs(self.id - j) == 1:
                canvas.create_line(
                    x,
                    self.y(self.id) - diameter,
                    x,
                    self.y(self.id) + 100 - diameter,
                    arrow=tk.LAST
                )
                canvas.create_text(x + diameter - 5, self.y(self.id) + (2 * diameter), text=i)
            # arrow pointing up
            if abs(self.id - j) > 1:
                global up
                up = 0
                temp = up
                canvas.create_line(
                    x,
                    self.y(self.id),
                    x + up - (diameter * 3),
                    self.y(self.id),
                    x + up - (diameter * 3),
                    self.y(j),
                    x - diameter,
                    self.y(j),
                    arrow=tk.LAST
                )
                canvas.create_text(x + up - (diameter * 4), ((self.y(j) - self.y(self.id)) / 2) + self.y(self.id),
                                   text=i)
                up = temp + 25

    # draw the states of the FSA
    def drawState(self, canvas):
        x = 110
        diameter = 30  # diameter
        if self.start:
            canvas.create_line(
                x, self.y(self.id) - 100,
                x, self.y(self.id) - diameter,
                arrow=tk.LAST
            )
            canvas.create_text(x + diameter, self.y(self.id) - (2 * diameter), text="start")
        self.drawLines(canvas, x, diameter)
        if self.accept:
            canvas.create_oval(x - diameter, self.y(self.id) - diameter, x + diameter, self.y(self.id) + diameter,
                               fill="white", outline="green", width=2)
        else:
            canvas.create_oval(x - diameter, self.y(self.id) - diameter, x + diameter, self.y(self.id) + diameter,
                               fill="white")
        canvas.create_text(x, self.y(self.id), text=str(self.id))
