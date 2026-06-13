import tkinter as tk
import os as o
import subprocess as sp

class OriginalMinecraft(tk.Button):
    def __init__(self, master, text, anchor, bg, fg, **kwargs):
        super().__init__(
            master=master,
            text=text,
            anchor=anchor,
            command=self.load,
            bg=bg,
            fg=fg
            )
    def load(self):
        script_dir = o.path.dirname(o.path.abspath(__file__))
        file_path = o.path.join(script_dir, "Minecraft", "minecraft.py")
        if o.path.exists(file_path):
            sp.Popen(["python", file_path])
            sp.run("cls", shell=True)
        else:
            print(-1)
class ModMinecraft(tk.Button):
    def __init__(self, master, text, anchor, bg, fg, **kwargs):
        super().__init__(
            master=master,
            text=text,
            anchor=anchor,
            command=self.load,
            bg=bg,
            fg=fg
            )
    def load(self):
        script_dir = o.path.dirname(o.path.abspath(__file__))
        file_path = o.path.join(script_dir, "Minecraft_FFlags", "main.py")
        if o.path.exists(file_path):
            sp.Popen(["python", file_path])
            sp.run("cls", shell=True)
        else:
            print(-2)
class Loader(tk.Tk):
    def __init__(self, name):
        super().__init__()
        self.title(name)
        self.geometry("950x450")
        self.configure(bg="#1e1e1e")
        self.original=OriginalMinecraft(
            self,
            "-> Launch Game",
            "w",
            "#FFFFFF",
            "#1e1e1e",
        )
        self.original.pack(ipady=20, ipadx=15, pady=(0, 10), fill="x")
        self.mod = ModMinecraft(
            self,
            "-> Launch Modified Game",
            "w",
            "#FFFFFF",
            "#1E1E1E"
        )
        self.mod.pack(ipady=20, ipadx=15, pady=(0, 10), fill="x")
    def run(self):
        self.mainloop()
if __name__ == "__main__":
    loader=Loader("TLauncher")
    loader.run()