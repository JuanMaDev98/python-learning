from tkinter import *

import settings as st
import utils
from cells import Cell

# Create the main window and apply properties
root = Tk()
root.title("MineSweeper")
root.geometry(f"{st.WIDTH}x{st.HEIGHT}")
root.resizable(False, False)
root.configure(bg="black")


# Top frame config
top_frame = Frame(
    root, 
    bg = "black",
    width = utils.width_prct(100),
    height= utils.height_prct(25)
)
top_frame.place(x=0,y=0)

# Left Frame config
left_frame = Frame(
    root, 
    bg = "black",
    width = utils.width_prct(25),
    height= utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

# Center frame config (main frame)
center_frame = Frame(
    root,
    bg = "black",
    width = utils.width_prct(75),
    height= utils.height_prct(75)    
)
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

for x in range(st.GRID_HEIGHT):
    for y in range(st.GRID_WIDTH):
        c = Cell()
        c.create_button_object(center_frame)
        c.cell_button_object.grid(column=y, row =x)





# Run main window
root.mainloop()
