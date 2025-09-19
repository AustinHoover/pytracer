
import tkinter
from collections.abc import Callable
from typing import Final

# Size of the window
window_size: Final[int] = 400

# Scaling applied to the pixels
pixel_scaling: Final[int] = 10

# Ray
ray_dimension: Final[int] = int(window_size / pixel_scaling)

# The main window for the app
class Window:

    # TKinter object backing the window
    window: tkinter.Tk

    # Canvas for rendering
    canvas: tkinter.Canvas

    # Inits the window
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, width=window_size, height=window_size)
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
            # Clear canvas
            canvas.delete()
            # Draw each ray
            for x_raw in range(ray_dimension):
                for y_raw in range(ray_dimension):
                    x_real = x_raw * pixel_scaling
                    y_real = y_raw * pixel_scaling
                    color = "#000fff000"
                    canvas.create_rectangle(
                        x_real,
                        y_real,
                        pixel_scaling,
                        pixel_scaling,
                        fill = color
                    )
        # Return the curried func
        return repaint


