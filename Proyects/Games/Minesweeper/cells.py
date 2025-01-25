from tkinter import Button

class Cell:
    def __init__(self, is_mine = False):
        self.is_mine = is_mine
        self.cell_button_object = None

            
    def create_button_object(self, location):
        btn = Button(
            location,
            text = "Text",
        )
        btn.bind("<Button-1>", self._left_click_actions)
        btn.bind("<Button-3>", self._right_click_actions)
        self.cell_button_object = btn
        
    def _left_click_actions(self, event):
        print(event)
        print("Left Button Clicked")

        
        
    def _right_click_actions(self, event):
        print(event)
        print("Right Button Clicked")