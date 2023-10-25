import shutil
import subprocess
import os
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter import messagebox

class gestionSoftWindows :
    def __init__(self,emplacement:str):
        self.emplacement = emplacement
    
    def setEmplacementSoft(self):
        messagebox.showinfo("Information","Choisir un le dossier ou enregistrer les logiciel")
        self.emplacement = filedialog.askdirectory()
        return self.emplacement 

    def setName(self,name:str):
        self.name = name
    
    def saveSoftware(self)->bool:
        self.racourcieSoft =os.path.abspath(self.emplacement+"/"+self.name+".lnk")
        emplacement = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk")])
        if emplacement:
            shutil.copyfile(emplacement,self.racourcieSoft)
            return True
        else :
            return False
        
    def getName(self):
        return str(self.name)  