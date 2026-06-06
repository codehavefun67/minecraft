import tkinter as tk
from tkinter.filedialog import SaveAs
import os as o
from subprocess import Popen
from os.path import exists
from typing import Any
class fishstrap:
    def __init__(self,
                main: Any,
                dirfile:str,
                width:int,
                height:int,
                name:str,
                config_func:function,

        ) -> None:
        self.main = main
        self.dirfile = dirfile
        self.width = width
        self.height=height
        self.name=name
        self.config_func=config_func
        self.config_ui()
        self.main.configure(f"{self.width}x{self.height}")
    def load(self):
        # check if minecraft.py exists
        path="minecraft.py"
        try:
            if exists(path):
                Popen(f"python {path}")
            else:
                raise FileNotFoundError("Main Game does not exist")
        except:
            pass
    def config(self):
        pass
    def config_ui(self):
        self.ui = tk.Button(main, width=600, height=300)

if __name__ == "__main__":
    main = tk.Tk()
    dirfile = ""
    
    app = fishstrap(main, dirfile, 600, 300, "Loader", )
    
    main.mainloop()
