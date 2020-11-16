# Modules used to create this Notepad
import tkinter as tk
import tkinter.messagebox as timb
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

class Notepad:
    # Geometry, Title and icon constructor
    def __init__(self,master):
        self.master = master
        master.geometry("600x600")
        master.title("Notepad by Mayuresh Koli")
        master.wm_iconbitmap("notepad icon.ico")

        # Setting up mainmenu for notepad
        self.mainmenu = tk.Menu(master)
        master.config(menu=self.mainmenu)  

        # Setting up scrollbar and text area for notepad
        self.scroll_bar = tk.Scrollbar(master)
        self.scroll_bar.pack(side="right", fill="y") 
        
        self.text_area = tk.Text(master,yscrollcommand=self.scroll_bar.set,font="lucida 14")
        self.text_area.pack(expand=True, fill="both") 

        self.scroll_bar.config(command = self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)   
    
    # Setting up a function which creates a new file
    def newfile(self):
        global file
        self.master.title("Untitled - Notepad")
        file = None
        self.text_area.delete(1.0,"end")


    # This function will help to save file in our computer
    def savefile(self):
        global file
        if file == None:
            file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                                        filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            if file == "":
                file = None

            else:
                # Save as a new file
                f = open(file,"w")
                f.write(self.text_area.get(1.0,"end"))
                f.close()
                self.master.title(os.path.basename(file) + " - Notepad") 

        else:
            # Save the file
            f = open(file,"w") 
            f.write(self.text_area.get(1.0,"end"))
            f.close()          


    # This function will help to open any other text file
    def openfile(self):
        global file
        file = askopenfilename(defaultextension=".txt",
                                filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        
        if file == "":
            file = None
        
        else:
            self.master.title(os.path.basename(file) + " - Notepad")
            self.text_area.delete(1.0,"end")
            f = open(file,"r")
            self.text_area.insert(1.0, f.read())
            f.close()

    # The following three fucntions are for cut, copy, and paste
    def cut(self):
        self.text_area.event_generate(("<<Cut>>"))

    def copy(self):
        self.text_area.event_generate(("<<Copy>>"))
    
    def paste(self):
        self.text_area.event_generate(("<<Paste>>"))

    # This will give a message box when the user click on about
    def about(self):
        timb.showinfo("Notepad","Notepad by Mayuresh Koli")

    # Setting up some events in the menu bar
    def menu_bar_1(self):
        menu_1 = tk.Menu(self.mainmenu,tearoff=0)
        menu_1.add_command(label="New",command=self.newfile)
        menu_1.add_command(label="Open",command=self.openfile)
        menu_1.add_command(label="Save",command=self.savefile)
        menu_1.add_separator()
        menu_1.add_command(label="Exit",command=quit)
        self.mainmenu.add_cascade(label="File",menu=menu_1)

    def menu_bar_2(self):
        menu_2 = tk.Menu(self.mainmenu,tearoff=0)
        menu_2.add_command(label="Cut",command=self.cut)
        menu_2.add_command(label="Copy",command=self.copy)
        menu_2.add_command(label="Paste",command=self.paste)
        self.mainmenu.add_cascade(label="Edit",menu=menu_2) 

    def menu_bar_3(self):
        menu_3 = tk.Menu(self.mainmenu,tearoff=0)
        menu_3.add_command(label="About Notepad",command=self.about)
        self.mainmenu.add_cascade(label="Help",menu=menu_3) 

if __name__ == "__main__":
    # Calling all classes and functions
    root = tk.Tk()
    app = Notepad(root)
    file = None
    app.menu_bar_1()
    app.menu_bar_2()
    app.menu_bar_3()
    root.mainloop()         