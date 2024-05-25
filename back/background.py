import tkinter as tk

class Background:
    def __init__(self, canvas, width=800, height=800, interval=50):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.interval = interval
        self.grid_visible = True
        self.setup_bindings()

    def setup_bindings(self):
        self.canvas.bind_all("<Control-u>", self.toggle_grid)
        self.canvas.bind_all("<Command-u>", self.toggle_grid)

    def toggle_grid(self, event=None):
        self.grid_visible = not self.grid_visible
        self.draw_background()

    def draw_background(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white", outline="white")
        if self.grid_visible:
            for i in range(0, self.width, self.interval):
                self.canvas.create_line([(i, 0), (i, self.height)], tag='grid_line', fill='gray')
            for i in range(0, self.height, self.interval):
                self.canvas.create_line([(0, i), (self.width, i)], tag='grid_line', fill='gray')