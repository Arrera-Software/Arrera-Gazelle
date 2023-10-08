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
        listTheme = ["default","light","black"]
        listMoteur = ["Duckduckgo","google","bing","brave","ecosia","qwant"]
        self.varParametre = StringVar(windows)
        #widget
        #Cadre
        self.cadreMenu = Frame(windows,width=150,height=600,bg=self.colorSecondaire)
        self.cadreAcceuil = Frame(windows,width=350,height=600,bg=self.colorPrimaire)
        #cadre interne a l'acceuil
        cadresPresentations = [
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid")]
        #Label
        labelTitreMenu = Label(self.cadreMenu,text="Menu",font=("arial","20"),bg=self.colorSecondaire,fg=self.textColorSecondaire)
        labelcadresPresentations = [
            Label(cadresPresentations[0],text="Gestion utilisateur",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[1],text="Gestion theme",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[2],text="Gestion recherche",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[3],text="Gestion meteo",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[4],text="Gestion GPS",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[5],text="Gestion software",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)]
        #cadresPresentations
        #0
        buttonManageUser = Button(cadresPresentations[0],text="Utilisateur\nmanageur",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        #1
        menuTheme1 = OptionMenu(cadresPresentations[1],self.varParametre,*listTheme)
        btnValiderTheme1 = Button(cadresPresentations[1],text="Valider",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        #2
        menuRecherche1 = OptionMenu(cadresPresentations[2],self.varParametre,*listMoteur)
        btnValiderMoteur1 = Button(cadresPresentations[2],text="Valider",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        #3
        btnMeteo1 = Button(cadresPresentations[3],text="Ajouter\nune ville",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        #4
        btnGPSHome = Button(cadresPresentations[4],text="Adresse\nde domicile",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        btnGPSWork = Button(cadresPresentations[4],text="Adresse\nde travail",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        #5
        btnSoftware1 = Button(cadresPresentations[5],text="Ajouter\nun logiciel",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        #bouton
        #cadre menu
        boutonAcceuil = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Acceuil")
        boutonUser = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Utilisateur")
        boutonTheme = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Theme")
        boutonMeteo = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Meteo")
        boutonGPS = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="GPS")
        boutonRecherche = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Recherche")
        boutonSoftware = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Software")
        boutonInternet = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Internet")
        boutonQuitter = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Quitter")
        #formatage de la fenetre
        windows.maxsize(500,600)
        windows.minsize(500,600)
        windows.title(self.nameAssistant+": Parametre")
        if self.icon == True :
            windows.iconphoto(False,PhotoImage(file=self.fileIcon))
        #Calcule position
        xlabel2 = int(self.cadreMenu.winfo_width()/2)
        xBoutonMenu = xlabel2 + 5
        yBTNQuitter = int(self.cadreMenu.winfo_reqheight()-boutonQuitter.winfo_reqheight())
        #Cadre acceuil
        cadresPresentations[0].place(x=0,y=0)
        cadresPresentations[1].place(x=180,y=0)
        cadresPresentations[2].place(x=0,y=200)
        cadresPresentations[3].place(x=180,y=200)
        cadresPresentations[4].place(x=0,y=400)
        cadresPresentations[5].place(x=180,y=400)
        #Affichage des cadre composant du cadre acceuil
        labelcadresPresentations[0].place(x=0,y=0)
        labelcadresPresentations[1].place(x=0,y=0)
        labelcadresPresentations[2].place(x=0,y=0)
        labelcadresPresentations[3].place(x=0,y=0)
        labelcadresPresentations[4].place(x=0,y=0)
        labelcadresPresentations[5].place(x=0,y=0)
        buttonManageUser.place(relx=0.5, rely=0.5, anchor="center")
        menuTheme1.place(relx=0.5,y=(labelcadresPresentations[1].winfo_reqheight()+45), anchor="center")
        btnValiderTheme1.place(relx=0.5, rely=1.0, anchor="s")
        menuRecherche1.place(relx=0.5,y=(labelcadresPresentations[1].winfo_reqheight()+45), anchor="center")
        btnValiderMoteur1.place(relx=0.5, rely=1.0, anchor="s")
        btnMeteo1.place(relx=0.5, rely=0.5, anchor="center")
        btnGPSHome.place(relx=0.5, rely=1.0, anchor="s")
        btnGPSWork.place(relx=0.5,y=(labelcadresPresentations[1].winfo_reqheight()+45), anchor="center")
        btnSoftware1.place(relx=0.5, rely=0.5, anchor="center")
        #Affichage cadre menu 
        labelTitreMenu.place(x=xBoutonMenu,y=0)
        boutonAcceuil.place(x=xBoutonMenu,y=50)
        boutonUser.place(x=xBoutonMenu,y=100)
        boutonTheme.place(x=xBoutonMenu,y=150)
        boutonMeteo.place(x=xBoutonMenu,y=200)
        boutonGPS.place(x=xBoutonMenu,y=250)
        boutonRecherche.place(x=xBoutonMenu,y=300)
        boutonSoftware.place(x=xBoutonMenu,y=350)
        boutonInternet.place(x=xBoutonMenu,y=400)
        boutonQuitter.place(x=xBoutonMenu,y=yBTNQuitter)
        #Affichage cadre principal
        self.cadreMenu.pack(side="left")
        return True
       
        
        
    def mainView(self)->bool  :
        self.cadreAcceuil.pack(side="left")
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
        