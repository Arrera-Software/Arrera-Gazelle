from tkinter import *
from travailJSON import *

class ArreraSettingAssistant :
    def __init__(self,configSettingFile:str,configFile:str,configAssistant:str,fichierConfigUser:str):
        self.multiUser = bool
        self.changeColor = bool 
        self.icon = bool 
        self.fileIcon = str
        #overture des fichier
        settingFile = jsonWork(configSettingFile)
        self.fileConfig = jsonWork(configFile)
        self.assistantFile = jsonWork(configAssistant)
        self.fileUser = jsonWork(fichierConfigUser)
        #Recuperarton donner
        #fichier settingFile
        self.colorPrimaire = settingFile.lectureJSON("color1")
        self.colorSecondaire = settingFile.lectureJSON("color2")
        self.textColorPrimaire = settingFile.lectureJSON("textColor1")
        self.textColorSecondaire = settingFile.lectureJSON("textColor2")
        if settingFile.lectureJSON("multiUser") == "1" :
            self.multiUser = True
            self.nbUser = int(settingFile.lectureJSON("nbUser"))
        else :
            self.multiUser = False
            
        if settingFile.lectureJSON("colorInterface") == "1" :
            self.changeColor =  True 
        else :
            self.changeColor = False
        if settingFile.lectureJSON("setIcon") == "1" : 
            self.icon = True
        else :
            self.icon = False 
        #fichier fileconfig 
        self.icon = self.fileConfig.lectureJSON("iconAssistant")
        self.nameAssistant = self.fileConfig.lectureJSON("name")
        if self.icon == True :
            self.fileIcon = self.fileConfig.lectureJSON("iconAssistant")
         
       
            
    def windows(self,windows:Tk) -> bool :
        #variable
        xLabel1 = int
        xlabel2 = int 
        yBTNQuitter = int 
        #widget
        #Cadre
        self.cadreMenu = Frame(windows,width=150,height=600,bg=self.colorSecondaire)
        self.cadreAcceuil = Frame(windows,width=350,height=600,bg=self.colorPrimaire)
        #Label
        self.labelTitreAcceuil = Label(self.cadreAcceuil,text="Parametre",font=("arial","20"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        self.labelTitreMenu = Label(self.cadreMenu,text="Menu",font=("arial","20"),bg=self.colorSecondaire,fg=self.textColorSecondaire)
        #bouton
        self.boutonAcceuil = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Acceuil")
        self.boutonUser = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Utilisateur")
        self.boutonTheme = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Theme")
        self.boutonMeteo = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Meteo")
        self.boutonGPS = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="GPS")
        self.boutonRecherche = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Recherche")
        self.boutonSoftware = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Software")
        self.boutonInternet = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Internet")
        self.boutonQuitter = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Quitter")
        #menu 
        #formatage de la fenetre
        windows.maxsize(500,600)
        windows.minsize(500,600)
        windows.title(self.nameAssistant+": Parametre")
        if self.icon == True :
            windows.iconphoto(False,PhotoImage(file=self.fileIcon))
        #Calcule position
        xLabel1 = int((self.cadreAcceuil.winfo_reqwidth()/2)-self.labelTitreAcceuil.winfo_reqwidth() )
        xlabel2 = int(self.cadreMenu.winfo_width()/2)
        yBTNQuitter = int(self.cadreMenu.winfo_reqheight()-self.boutonQuitter.winfo_reqheight())
        #Affichage  
        self.labelTitreAcceuil.place(x=xLabel1+5,y=0)
        self.labelTitreMenu.place(x=xlabel2+5,y=0)
        self.boutonAcceuil.place(x=xlabel2+5,y=50)
        self.boutonUser.place(x=xlabel2+5,y=100)
        self.boutonTheme.place(x=xlabel2+5,y=150)
        self.boutonMeteo.place(x=xlabel2+5,y=200)
        self.boutonGPS.place(x=xlabel2+5,y=250)
        self.boutonRecherche.place(x=xlabel2+5,y=300)
        self.boutonSoftware.place(x=xlabel2+5,y=350)
        self.boutonInternet.place(x=xlabel2+5,y=400)
        self.boutonQuitter.place(x=xlabel2+5,y=yBTNQuitter)
        self.cadreMenu.pack(side="left")
        self.cadreAcceuil.pack(side="right")
        return True
       
        
        
    def mainView(self)->bool  :
        
       
        
        return True 
    
    def userView(self)->bool  :
        return True 
    
    def themeView(self)->bool  :
        return True 
    
    def meteoView(self)->bool  :
        return True 
    
    def rechercheView(self)->bool  :
        return True 
    
    def softwareView(self)->bool  :
        return True 
        