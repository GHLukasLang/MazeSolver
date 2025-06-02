from tkinter import Tk, BOTH, Canvas
from objects import Line, Point

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(master=self.root, bg="white")
        self.canvas.pack()
        self.running = False
    
    def redraw(self):
        
        self.canvas.update_idletasks()
        self.canvas.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

