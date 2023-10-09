from tkinter import *
from travailJSON import *

class ArreraSettingAssistant :
    def __init__(self,configSettingFile:str,configFile:str,configAssistant:str,fichierConfigUser:str):
        self.multiUser = bool
        self.changeColor = bool 
        self.icon = bool 
        self.fileIcon = str
        self.fnc = None
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
            Label(cadresPresentations[0],text="Gestion recherche",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[1],text="Gestion meteo",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[2],text="Gestion GPS",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[3],text="Gestion software",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[4],text="Gestion utilisateur",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[5],text="Gestion theme",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)]
        if self.multiUser == False :
            labelcadresPresentations[4].configure(text="Cette fonction\nn'est pas\ndisponible sur\ncette assistant")
        if self.changeColor == False :
            labelcadresPresentations[5].configure(text="Cette fonction\nn'est pas\ndisponible sur\ncette assistant")
        #cadresPresentations
         #0
        menuRecherche1 = OptionMenu(cadresPresentations[0],self.varParametre,*listMoteur)
        btnValiderMoteur1 = Button(cadresPresentations[0],text="Valider",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        #1
        btnMeteo1 = Button(cadresPresentations[1],text="Ajouter\nune ville",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        #2
        btnGPSHome = Button(cadresPresentations[2],text="Adresse\nde domicile",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        btnGPSWork = Button(cadresPresentations[2],text="Adresse\nde travail",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        #3
        btnSoftware1 = Button(cadresPresentations[3],text="Ajouter\nun logiciel",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        #4
        if self.multiUser == True :
            buttonManageUser = Button(cadresPresentations[4],text="Utilisateur\nmanageur",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
        #5
        if self.changeColor == True:
            menuTheme1 = OptionMenu(cadresPresentations[5],self.varParametre,*listTheme)
            btnValiderTheme1 = Button(cadresPresentations[5],text="Valider",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)
       
        #bouton
        #cadre menu
        boutonMenu = [
            Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Acceuil",command=self.mainView),
            Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Meteo",command=self.meteoView),
            Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="GPS",command=self.gpsView),
            Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Recherche",command=self.rechercheView),
            Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Software",command=self.softwareView),
            Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Internet",command=self.internetView),
            Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Utilisateur",command=self.userView),
            Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Theme",command=self.themeView)]
        boutonQuitter = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Quitter",command=self.quittePara)
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
        menuRecherche1.place(relx=0.5,y=(labelcadresPresentations[0].winfo_reqheight()+45), anchor="center")
        btnValiderMoteur1.place(relx=0.5, rely=1.0, anchor="s")
        labelcadresPresentations[1].place(x=0,y=0)
        btnMeteo1.place(relx=0.5, rely=0.5, anchor="center")
        labelcadresPresentations[2].place(x=0,y=0)
        btnGPSHome.place(relx=0.5, rely=1.0, anchor="s")
        btnGPSWork.place(relx=0.5,y=(labelcadresPresentations[2].winfo_reqheight()+45), anchor="center")
        labelcadresPresentations[3].place(x=0,y=0)
        btnSoftware1.place(relx=0.5, rely=0.5, anchor="center")
        if self.multiUser == True :
            labelcadresPresentations[4].place(x=0,y=0)
            buttonManageUser.place(relx=0.5, rely=0.5, anchor="center")
        else :
            labelcadresPresentations[4].place(relx=0.5, rely=0.5, anchor="center")
        if self.changeColor == True :   
            labelcadresPresentations[5].place(x=0,y=0)
            menuTheme1.place(relx=0.5,y=(labelcadresPresentations[1].winfo_reqheight()+45), anchor="center")
            btnValiderTheme1.place(relx=0.5, rely=1.0, anchor="s")
        else :
            labelcadresPresentations[5].place(relx=0.5, rely=0.5, anchor="center")
        #Affichage cadre menu 
        labelTitreMenu.place(x=xBoutonMenu,y=0)
        boutonMenu[0].place(x=xBoutonMenu,y=50)
        boutonMenu[1].place(x=xBoutonMenu,y=100)
        boutonMenu[2].place(x=xBoutonMenu,y=150)
        boutonMenu[3].place(x=xBoutonMenu,y=200)
        boutonMenu[4].place(x=xBoutonMenu,y=250)
        boutonMenu[5].place(x=xBoutonMenu,y=300)
        if self.multiUser == True :
            boutonMenu[6].place(x=xBoutonMenu,y=350)
        if self.changeColor == True :
            if self.multiUser == True :
                boutonMenu[7].place(x=xBoutonMenu,y=400)
            else :
                boutonMenu[7].place(x=xBoutonMenu,y=350)

        
        boutonQuitter.place(x=xBoutonMenu,y=yBTNQuitter)
        #Affichage cadre principal
        self.cadreMenu.pack(side="left")
        return True
       
        
        
    def mainView(self)->bool  :
        self.cadreAcceuil.pack(side="left")
        return True 
    
    def gpsView(self)->bool:
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
    
    def internetView(self)->bool :
        return True
    
    def passageFonctionQuitter(self,fonctionQuitter):
        self.fnc = fonctionQuitter
    
    def quittePara(self)->bool :
        self.cadreAcceuil.destroy()
        self.cadreMenu.destroy()
        self.fnc()
        
            
        return True 
        