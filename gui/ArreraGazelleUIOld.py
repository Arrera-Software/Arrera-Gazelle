from tkinter import*
from objet.arreraGazelle import*
from typing import Union

class CArreraGazelleUI :
    def __init__(self,windows:Union[Tk,Toplevel],emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,emplacementJsonAssistant:str,emplacementConfigSetting:str):
        # Ouverture de l'objet
        self.__gazelle = CArreraGazelle(emplacementJsonUser,emplacementJsonNeuronNetwork,emplacementJsonAssistant)
        jsonSetting = jsonWork(emplacementConfigSetting)
        # Recuperation des variable pour les couleur
        self.__fristColor = [jsonSetting.lectureJSON("colorLight1"),jsonSetting.lectureJSON("colorDark1")]
        self.__secondColor = [jsonSetting.lectureJSON("colorLight2"),jsonSetting.lectureJSON("colorDark2")]
        self.__fristColorTexte = [jsonSetting.lectureJSON("textColorLight1"),jsonSetting.lectureJSON("textColorDark1")]
        self.__secondColorTexte = [jsonSetting.lectureJSON("textColorLight2"),jsonSetting.lectureJSON("textColorDark2")]
        # Mise de la fenetre dans un atribut
        self.__windows = windows
        # Varriable
        self.__varRecherche = StringVar(self.__windows)
        self.__varTheme = StringVar(self.__windows)
        self.__listTheme = jsonSetting.lectureJSONList("listeTheme")
        listMoteur = ["Duckduckgo","google","bing","brave","ecosia","qwant"]
        # Creation des Frame
        self.__cadreMenu = Frame(self.__windows,width=150,height=600)
        self.__cadreAcceuil = Frame(self.__windows,width=350,height=600)
        self.__cadreUser = Frame(self.__windows,width=350,height=600)
        self.__cadreMeteo = Frame(self.__windows,width=350,height=600)
        self.__cadreGPS = Frame(self.__windows,width=350,height=600)
        self.__cadreRecherche = Frame(self.__windows,width=350,height=600)
        self.__cadreSoft = Frame(self.__windows,width=350,height=600)
        self.__cadreInternet = Frame(self.__windows,width=350,height=600)
        self.__cadreTheme = Frame(self.__windows,width=350,height=600)
        self.__cadreMicro = Frame(self.__windows,width=350,height=600)

        #cadre interne a l'acceuil
        self.__cadresPresentations = [
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,borderwidth=1, relief="solid")]
        #Widget
        self.__labelTitreMenu = Label(self.__cadreMenu,text="Menu",font=("arial","20"))
        self.__labelcadresPresentations = [
            Label(self.__cadresPresentations[0],text="Gestion recherche",font=("arial","13")),
            Label(self.__cadresPresentations[1],text="Gestion meteo",font=("arial","13")),
            Label(self.__cadresPresentations[2],text="Gestion GPS",font=("arial","13")),
            Label(self.__cadresPresentations[3],text="Gestion software",font=("arial","13")),
            Label(self.__cadresPresentations[4],text="Gestion Site internet",font=("arial","13")),
            Label(self.__cadresPresentations[5],text="Gestion theme",font=("arial","13"))]
        
        self.__boutonMenu = [Button(self.__cadreMenu,font=("arial","15"),text="Acceuil",command=self.__backAcceuil),
                        Button(self.__cadreMenu,font=("arial","15"),text="Utilisateur",command=self.__showUserFrame),
                        Button(self.__cadreMenu,font=("arial","15"),text="Meteo",command=self.__showMeteoFrame),
                        Button(self.__cadreMenu,font=("arial","15"),text="GPS",command=self.__showGPSFrame),
                        Button(self.__cadreMenu,font=("arial","15"),text="Recherche",command=self.__showRechercheFrame),
                        Button(self.__cadreMenu,font=("arial","15"),text="Software",command=self.__showSoftFrame),
                        Button(self.__cadreMenu,font=("arial","15"),text="Internet",command=self.__showInternetFrame),
                        Button(self.__cadreMenu,font=("arial","15"),text="Theme",command=self.__showThemeFrame),
                        Button(self.__cadreMenu,font=("arial","15"),text="Micro",command=self.__showMicroFrame),
                        Button(self.__cadreMenu,font=("arial","15"),text="Quitter")]
        
        #cadresPresentations
        #0
        self.__menuRecherche1 = OptionMenu(self.__cadresPresentations[0],self.__varRecherche,*listMoteur)
        self.__btnValiderMoteur1 = Button(self.__cadresPresentations[0],text="Valider",font=("arial","13"))
        #1
        self.__btnMeteo1 = Button(self.__cadresPresentations[1],text="Ajouter\nune ville",font=("arial","13"))
        #2
        self.__btnGPSHome = Button(self.__cadresPresentations[2],text="Adresse\nde domicile",font=("arial","13"))
        self.__btnGPSWork = Button(self.__cadresPresentations[2],text="Adresse\nde travail",font=("arial","13"))
        #3
        self.__btnSoftware1 = Button(self.__cadresPresentations[3],text="Ajouter\nun logiciel",font=("arial","13"))
        #4
        self.__buttonAddSite = Button(self.__cadresPresentations[4],text="Ajouter",font=("arial","13"))
        self.__buttonSupprSite = Button(self.__cadresPresentations[4],text="Supprimer",font=("arial","13"))
        #5
        self.__menuTheme1 = OptionMenu(self.__cadresPresentations[5],self.__varTheme,*self.__listTheme)
        self.__btnValiderTheme1 = Button(self.__cadresPresentations[5],text="Valider",font=("arial","13"))

        # Placement widget 
        #Cadre acceuil
        self.__cadresPresentations[0].place(x=0,y=0)
        self.__cadresPresentations[1].place(x=180,y=0)
        self.__cadresPresentations[2].place(x=0,y=200)
        self.__cadresPresentations[3].place(x=180,y=200)
        self.__cadresPresentations[4].place(x=0,y=400)
        self.__cadresPresentations[5].place(x=180,y=400)
        

        self.__labelTitreMenu.place(relx=0.5, rely=0.0, anchor="n")
        for i in range(0,5):
            self.__labelcadresPresentations[i].place(relx=0.5, rely=0.0, anchor="n")
        
        self.__boutonMenu[0].place(relx=0.2,y=50)
        self.__boutonMenu[1].place(relx=0.2,y=100)
        self.__boutonMenu[2].place(relx=0.2,y=150)
        self.__boutonMenu[3].place(relx=0.2,y=200)
        self.__boutonMenu[4].place(relx=0.2,y=250)
        self.__boutonMenu[5].place(relx=0.2,y=300)
        self.__boutonMenu[6].place(relx=0.2,y=350)
        self.__boutonMenu[7].place(relx=0.2,y=400)
        self.__boutonMenu[8].place(relx=0.2,y=450)
        self.__boutonMenu[9].place(relx=0.2,y=500)

        self.__labelcadresPresentations[0].place(relx=0.5, rely=0.0, anchor="n")
        self.__labelcadresPresentations[1].place(relx=0.5, rely=0.0, anchor="n")
        self.__labelcadresPresentations[2].place(relx=0.5, rely=0.0, anchor="n")
        self.__labelcadresPresentations[3].place(relx=0.5, rely=0.0, anchor="n")
        self.__labelcadresPresentations[4].place(relx=0.5, rely=0.0, anchor="n")
        self.__labelcadresPresentations[5].place(relx=0.5, rely=0.0, anchor="n")
        
        self.__menuRecherche1.place(relx=0.5, rely=0.5, anchor="center")
        self.__btnValiderMoteur1.place(relx=0.5, rely=1.0, anchor="s")
        self.__btnMeteo1.place(relx=0.5, rely=0.5, anchor="center")
        self.__btnGPSHome.place(relx=0.5, rely=1.0, anchor="s")
        self.__btnGPSWork.place(relx=0.5,y=(self.__labelcadresPresentations[2].winfo_reqheight()+45), anchor="center")
        self.__btnSoftware1.place(relx=0.5, rely=0.5, anchor="center")
        self.__buttonSupprSite.place(relx=0.5, rely=0.5, anchor="center")
        self.__buttonAddSite.place(relx=0.5,y=(self.__labelcadresPresentations[4].winfo_reqheight()+45), anchor="s")
        self.__menuTheme1.place(relx=0.5,y=(self.__labelcadresPresentations[1].winfo_reqheight()+45), anchor="center")
        self.__btnValiderTheme1.place(relx=0.5, rely=1.0, anchor="s")
        # Mise en place des valeur sur les menu 
        self.__varRecherche.set(listMoteur[0])
        self.__varTheme.set(self.__listTheme[0])
            
        
    def active(self,darkMode:bool):
        if (darkMode == True) :
            nb = 1
        else : 
            nb = 0 
        self.__cadreMenu.configure(bg=self.__secondColor[nb])
        self.__cadreAcceuil.configure(bg=self.__fristColor[nb])
        self.__cadreUser.configure(bg=self.__fristColor[nb])
        self.__cadreMeteo.configure(bg=self.__fristColor[nb])
        self.__cadreGPS.configure(bg=self.__fristColor[nb])
        self.__cadreRecherche.configure(bg=self.__fristColor[nb])
        self.__cadreSoft.configure(bg=self.__fristColor[nb])
        self.__cadreInternet.configure(bg=self.__fristColor[nb])
        self.__cadreTheme.configure(bg=self.__fristColor[nb])
        self.__cadreMicro.configure(bg=self.__fristColor[nb])
        for i in range(0,6):
            self.__labelcadresPresentations[i].configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
            self.__cadresPresentations[i].configure(bg=self.__fristColor[nb])
        
        for i in range(0,10):
            self.__boutonMenu[i].configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])

        self.__labelTitreMenu.configure(bg=self.__secondColor[nb],fg=self.__secondColorTexte[nb])

        self.__btnValiderMoteur1.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnMeteo1.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnGPSHome.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnGPSWork.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnSoftware1.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__buttonSupprSite.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__buttonAddSite.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnValiderTheme1.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
            
        self.__cadreAcceuil.pack(side="right")
        self.__cadreMenu.pack(side="left")
    
    def __backAcceuil(self):
        self.__cadreAcceuil.pack(side="right")
        self.__cadreUser.pack_forget()
        self.__cadreMeteo.pack_forget()
        self.__cadreGPS.pack_forget()
        self.__cadreRecherche.pack_forget()
        self.__cadreSoft.pack_forget()
        self.__cadreInternet.pack_forget()
        self.__cadreTheme.pack_forget()
        self.__cadreMicro.pack_forget()
    
    def __disableAllFrame(self):
        self.__cadreAcceuil.pack_forget()
        self.__cadreUser.pack_forget()
        self.__cadreMeteo.pack_forget()
        self.__cadreGPS.pack_forget()
        self.__cadreRecherche.pack_forget()
        self.__cadreSoft.pack_forget()
        self.__cadreInternet.pack_forget()
        self.__cadreTheme.pack_forget()
        self.__cadreMicro.pack_forget()
    
    def __showUserFrame(self):
        self.__disableAllFrame()
        self.__cadreUser.pack(side="right")
    
    def __showMeteoFrame(self):
        self.__disableAllFrame()
        self.__cadreMeteo.pack(side="right")
    
    def __showGPSFrame(self):
        self.__disableAllFrame()
        self.__cadreGPS.pack(side="right")

    def __showRechercheFrame(self):
        self.__disableAllFrame()
        self.__cadreRecherche.pack(side="right")
    
    def __showSoftFrame(self):
        self.__disableAllFrame()
        self.__cadreSoft.pack(side="right")
    
    def __showInternetFrame(self):
        self.__disableAllFrame()
        self.__cadreInternet.pack(side="right")
    
    def __showThemeFrame(self):
        self.__disableAllFrame()
        self.__cadreTheme.pack(side="right")
    
    def __showMicroFrame(self):
        self.__disableAllFrame()
        self.__cadreMicro.pack(side="right")