
import tkinter
from collections.abc import Callable

class Window:

    # TKinter object backing the window
    window: tkinter.Tk

    # Canvas for rendering
    canvas: tkinter.Canvas

    # Inits the window
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, width=400, height=400)
        self.canvas.pack()

        # Setup repaint function
        repaint_func = self.curry_repaint()
        self.canvas.bind("<Motion>", repaint_func)


    # Runs the window
    def start(self) -> None:
        self.window.mainloop()

    # Curries a repaint function to attach the specific self reference
    def curry_repaint(self) -> Callable:
        canvas: tkinter.Canvas = self.canvas
        # Main repaint function
        def repaint(event: None) -> None:
            color = "#000fff000"
            canvas.create_rectangle(0,0,50,50,fill = color)
        # Return the curried func
        return repaint


