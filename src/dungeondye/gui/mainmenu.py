import tkinter as tk
from dungeondye.gui import titleframe, diceframe, bottomframe
from PIL import Image, ImageTk


class MainMenu(tk.Tk):
    #private attributes
    _background_canvas:tk.Canvas = None
    _main_frame:tk.Frame = None
    _title:titleframe.Title = None
    _dice_setup:diceframe.DiceFrame = None
    _bottom_buttons:bottomframe.BottomButtons = None 
    _background_image:tk.Label = None
    _actual_image: tk.PhotoImage = None
    _resized_image = None
    _unformmated_image = None


    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("540x340")
        self.title("Dungeon Dice")
        self.resizable(False,False)
        self._background_canvas = tk.Canvas(self)
        self._background_canvas.pack(expand = True, fill = tk.BOTH)

        self._format_logo()


        self._main_frame = tk.Frame(self._background_canvas, bg = "")
        self._background_canvas.create_window(0, 0, anchor= "nw", window = self._main_frame, width= 540, height = 340)
        #self._main_frame.config(bg = "brown")
        # self._main_frame.grid_rowconfigure(0, weight=1)  # Title frame row
        # self._main_frame.grid_columnconfigure(0, weight=1) 
        # self._main_frame.place(x=0, y=0, relwidth=1, relheight=1)
        
        self._create_frames()

    def _format_logo(self) -> None:
        self._unformatted_image = Image.open(r'C:\Users\ssper\OneDrive\Projects\Table-Top-Dice-Roller\src\resources\images\DungeonDyeLogo.png')
        self._resized_image = self._unformatted_image.resize((540, 340))
        self._acutal_image = ImageTk.PhotoImage(self._resized_image)

        self._background_canvas.create_image(0, 0, anchor= "nw", image = self._acutal_image)

    #function that instantiates all frames
    def _create_frames(self) -> None:
        self._title = titleframe.Title(self._main_frame)
        self._dice_setup = diceframe.DiceFrame(self._main_frame)
        self._bottom_buttons = bottomframe.BottomButtons(self._main_frame)








