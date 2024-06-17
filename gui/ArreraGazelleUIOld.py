from tkinter import*
from objet.arreraGazelle import*
from tkinter.messagebox import*
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
        self.__varMoteurRecherce = StringVar(self.__windows)
        self.__varTheme = StringVar(self.__windows)
        self.__varGenre = StringVar(self.__windows)
        self.__varChoixLieu = StringVar(self.__windows)
        self.__varSupprLieu = StringVar(self.__windows)
        self.__listTheme = jsonSetting.lectureJSONList("listeTheme")
        listMoteur = ["Duckduckgo","google","bing","brave","ecosia","qwant"]
        listGenre = jsonSetting.lectureJSONList("listGenre")
        listChoixLieu = ["Simple","Domicile","Travail"]
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

        # Cadre User 
        self.__labelTitreUser = Label(self.__cadreUser,font=("arial","20"))
        self.__btnPrenom = Button(self.__cadreUser,font=("arial","15"),text="Nom de l'utilisateur",command=lambda : self.__affichageCadreUser(2))
        self.__btnGenre = Button(self.__cadreUser,font=("arial","15"),text="genre de l'utilisateur",command=lambda : self.__affichageCadreUser(3))
        self.__menuGenre = OptionMenu(self.__cadreUser,self.__varGenre,*listGenre)
        self.__entryName = Entry(self.__cadreUser,font=("arial","15"),borderwidth=2,relief="solid")
        self.__btnvaliderUser = Button(self.__cadreUser,font=("arial","15"),text="Valider")
        self.__btnAnulerUser = Button(self.__cadreUser,font=("arial","15"),text="Annuler",command=lambda : self.__affichageCadreUser(1))

        # Cadre Meteo 
        self.__labelTitreMeteo = Label(self.__cadreMeteo,font=("arial","20"))
        self.__btnListMeteo =  Button(self.__cadreMeteo,text="      Liste meteo      ",font=("arial","15"),command= lambda : self.__affichageCadreMeteo(2))
        self.__btnAddVille =   Button(self.__cadreMeteo,text="   Ajouter une ville   ",font=("arial","15"),command= lambda : self.__affichageCadreMeteo(3))
        self.__btnSupprVille = Button(self.__cadreMeteo,text="   Supprimer une ville ",font=("arial","15"),command= lambda : self.__affichageCadreMeteo(4))
        self.__labelListeMeteo = Label(self.__cadreMeteo,font=("arial","15"))
        self.__menuChoixLieu = OptionMenu(self.__cadreMeteo,self.__varChoixLieu,*listChoixLieu)
        self.__menuSupprLieu = OptionMenu(self.__cadreMeteo,self.__varSupprLieu,*listChoixLieu)
        self.__entryVille = Entry(self.__cadreMeteo,font=("arial","15"),borderwidth=2,relief="solid")
        self.__btnvaliderMeteo = Button(self.__cadreMeteo,text="Valider",font=("arial","15"))
        self.__btnannulerMeteo = Button(self.__cadreMeteo,font=("arial","15"),command= lambda : self.__affichageCadreMeteo(1))
        # Placement widget 
        #Cadre acceuil
        self.__cadresPresentations[0].place(x=0,y=0)
        self.__cadresPresentations[1].place(x=180,y=0)
        self.__cadresPresentations[2].place(x=0,y=200)
        self.__cadresPresentations[3].place(x=180,y=200)
        self.__cadresPresentations[4].place(x=0,y=400)
        self.__cadresPresentations[5].place(x=180,y=400)
        # Cadre GPS 
        self.__labelTitreGPS = Label(self.__cadreGPS,font=("arial","20"))
        self.__btnAdresseDomicile = Button(self.__cadreGPS,text="Adresse du domicile",font=("arial","15"),command=lambda : self.__affichageCadreGPS(2))
        self.__btnAdresseWork = Button(self.__cadreGPS,text="Adresse du lieu de travail",font=("arial","15"),command=lambda : self.__affichageCadreGPS(3))
        self.__btnvaliderGPS = Button(self.__cadreGPS,text="Valider",font=("arial","15"))
        self.__btnretourGPS = Button(self.__cadreGPS,text="Retour",font=("arial","15"),command=lambda : self.__affichageCadreGPS(1))
        self.__btnsupprGPS = Button(self.__cadreGPS,text="Supprimer",font=("arial","15"))
        self.__btnentryGPS = Entry(self.__cadreGPS,font=("arial","15"),borderwidth=2,relief="solid")
        # Cadre Rechecrhe
        self.__labelTitreRecherche = Label(self.__cadreRecherche,text="Chosissez votre moteur\nde recherche",font=("arial","20"))
        self.__menuMoteurRecherche = OptionMenu(self.__cadreRecherche,self.__varMoteurRecherce,*listMoteur)
        self.__btnvaliderMoteur = Button(self.__cadreRecherche,text="Valider",font=("arial","15"),command=self.__validerMoteur)
        

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

        self.__labelTitreUser.place(relx=0.5, rely=0.0, anchor="n")

        self.__labelTitreMeteo.place(relx=0.5, rely=0.0, anchor="n")

        self.__labelTitreGPS.place(relx=0.5, rely=0.0, anchor="n")

        self.__labelTitreRecherche.place(relx=0.5, rely=0.0, anchor="n")
        self.__menuMoteurRecherche.place(relx=0.5, rely=0.5, anchor="center")
        self.__btnvaliderMoteur.place(relx=0.5, rely=1.0, anchor="s")  
        
        # Mise en place des valeur sur les menu 
        self.__varRecherche.set(listMoteur[0])
        self.__varTheme.set(self.__listTheme[0])
        self.__varGenre.set(listGenre[0])
        self.__varChoixLieu.set(listChoixLieu[0])
        self.__varMoteurRecherce.set(listMoteur[0])
            
        
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

        self.__labelTitreUser.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnPrenom.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnGenre.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnvaliderUser.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnAnulerUser.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])

        self.__labelTitreMeteo.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnListMeteo.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnAddVille.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnSupprVille.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__labelListeMeteo.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnvaliderMeteo.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnannulerMeteo.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])

        self.__labelTitreGPS.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnAdresseDomicile .configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnAdresseWork .configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnvaliderGPS.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnretourGPS.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnsupprGPS.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
        self.__btnentryGPS.configure(bg=self.__fristColor[nb],fg=self.__fristColorTexte[nb])
            
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
        self.__affichageCadreUser(1)
    
    def __showMeteoFrame(self):
        self.__disableAllFrame()
        self.__cadreMeteo.pack(side="right")
        self.__affichageCadreMeteo(1)
    
    def __showGPSFrame(self):
        self.__disableAllFrame()
        self.__cadreGPS.pack(side="right")
        self.__affichageCadreGPS(1)

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
    
    def __affichageCadreUser(self,mode:int):
        """
        1 : Acceuil
        2 : Prenom 
        3 : Genre 
        """
        match mode :
            case 1 :
                self.__labelTitreUser.configure(text="Parametre Utilisateur")
                self.__btnPrenom.place(relx=0.5, y=200, anchor="n")
                self.__btnGenre.place(relx=0.5, y=275, anchor="n")
                self.__menuGenre.place_forget()
                self.__entryName.place_forget()
                self.__btnvaliderUser.place_forget()
                self.__btnAnulerUser.place_forget()
            case 2 :
                self.__labelTitreUser.configure(text="Prenom de l'utilisateur")
                self.__btnPrenom.place_forget()
                self.__btnGenre.place_forget()
                self.__menuGenre.place_forget()
                self.__entryName.place(relx=0.5, rely=0.5, anchor="center")
                self.__btnvaliderUser.place(relx=1, rely=1, anchor='se')  
                self.__btnAnulerUser.place(relx=0, rely=1, anchor='sw')
                self.__btnvaliderUser.configure(command=lambda : self.__validerUser(1))
            case 3 :
                self.__labelTitreUser.configure(text="Genre de l'utilisateur")
                self.__btnPrenom.place_forget()
                self.__btnGenre.place_forget()
                self.__menuGenre.place(relx=0.5, rely=0.5, anchor="center")
                self.__entryName.place_forget()
                self.__btnvaliderUser.place(relx=1, rely=1, anchor='se')
                self.__btnAnulerUser.place(relx=0, rely=1, anchor='sw')
                self.__btnvaliderUser.configure(command=lambda : self.__validerUser(2))
    
    def __validerUser(self,mode:int):
        """
        1 : User 
        2 : Genre
        """
        match mode :
            case 1 :
                name = self.__entryName.get()
                if (name==""):
                    showerror("Parametre","Vous avez pas entrer votre prenom")
                else :
                    self.__entryName.delete(0,END)
                    self.__gazelle.changeUserName(name)
                    showinfo("Parametre","Prenom enregistrer")
                    self.__affichageCadreUser(1)
            case 2 :
                genre = self.__varGenre.get()
                self.__gazelle.changeUserGenre(genre)
                showinfo("Parametre","genre enregistrer")
                self.__affichageCadreUser(1)

    def __affichageCadreMeteo(self,mode:int):
        """
        1 : Acceuil 
        2 : Liste 
        3 : Ajout 
        4 : Suppr
        """
        match mode :
            case 1 :
                self.__labelTitreMeteo.configure(text="Parametre Meteo")
                self.__btnListMeteo.place(relx=0.2,y=200)
                self.__btnAddVille.place(relx=0.2,y=275)
                self.__btnSupprVille.place(relx=0.2,y=350)
                self.__btnvaliderMeteo.place_forget()
                self.__btnannulerMeteo.place_forget()
                self.__entryVille.place_forget()
                self.__labelListeMeteo.place_forget()
                self.__menuChoixLieu.place_forget()
                self.__menuSupprLieu.place_forget()
            case 2 : 
                self.__labelTitreMeteo.configure(text="Liste des lieu enregistrer")
                self.__btnListMeteo.place_forget()
                self.__btnAddVille.place_forget()
                self.__btnSupprVille.place_forget()
                # Recuperation de la liste des ville 
                self.__btnannulerMeteo.configure(text="Retour")
                self.__btnannulerMeteo.place(relx=0.5, rely=1.0, anchor="s")
                listeVille = self.__gazelle.getMeteoSave()
                self.__labelListeMeteo.configure(text="")
                nbVille = len(listeVille)
                if (nbVille == 0 ) :
                    self.__labelListeMeteo.configure(text="Aucun lieu enregistrer")
                else :
                    for i in range(0,nbVille):
                        texte = self.__labelListeMeteo.cget("text")
                        self.__labelListeMeteo.configure(text=texte+"\n"+listeVille[i])
    
                self.__labelListeMeteo.place(x=0,y=100)
            case 3 :
                self.__labelTitreMeteo.configure(text="Ajouter un lieu")
                self.__btnListMeteo.place_forget()
                self.__btnAddVille.place_forget()
                self.__btnSupprVille.place_forget()
                self.__menuChoixLieu.place(x=0,y=100)
                self.__btnannulerMeteo.configure(text="Annuler")
                self.__btnvaliderMeteo.place(relx=1, rely=1, anchor='se')
                self.__btnannulerMeteo.place(relx=0, rely=1, anchor='sw')
                self.__entryVille.place(relx=0.5, rely=0.5, anchor="center")
                self.__btnvaliderMeteo.configure(command=lambda : self.__validerMeteo(1))
            case 4 : 
                listeVille = self.__gazelle.getMeteoSave()
                self.__labelListeMeteo.configure(text="")
                nbVille = len(listeVille)
                if (nbVille == 0 ) :
                    showerror("Parametre","Aucun lieu enregister")
                else :
                    self.__menuSupprLieu = OptionMenu(self.__cadreMeteo,self.__varSupprLieu,*listeVille)
                    self.__labelTitreMeteo.configure(text="Supprimer un lieu")
                    self.__btnListMeteo.place_forget()
                    self.__btnAddVille.place_forget()
                    self.__btnSupprVille.place_forget()
                    self.__menuChoixLieu.place_forget()
                    self.__btnannulerMeteo.configure(text="Annuler")
                    self.__btnvaliderMeteo.place(relx=1, rely=1, anchor='se')
                    self.__btnannulerMeteo.place(relx=0, rely=1, anchor='sw')
                    self.__menuSupprLieu.place(relx=0.5, rely=0.5, anchor="center")
                    self.__entryVille.place_forget()
                    self.__btnvaliderMeteo.configure(command=lambda : self.__validerMeteo(2))
    
    def __validerMeteo(self,mode:int):
        """
        1 : add 
        2 : suppr
        """
        match mode :
            case 1 :
                lieu = self.__entryVille.get()
                if (lieu==""):
                    showerror("Parametre","Impossible d'ajouter un lieu sans nom")
                else :
                    choix = self.__varChoixLieu.get()
                    if (choix == "Simple"):
                        self.__gazelle.ajoutVilleMeteo(3,lieu)
                    else :
                        if (choix=="Domicile"):
                            self.__gazelle.ajoutVilleMeteo(1,lieu)
                        else :
                            if (choix=="Travail") :
                                self.__gazelle.ajoutVilleMeteo(2,lieu) 
                
                self.__entryVille.delete(0,END)    
                self.__affichageCadreMeteo(1)
            case 2 :
                choixSuppr = self.__varSupprLieu.get()
                if (choixSuppr == ""):
                    showerror("Parametre","Selectionner le lieu a supprimer")
                else :
                    if (choixSuppr=="Lieu d'habitation enregister") :
                        self.__gazelle.supprVilleMeteo(1,"")
                    else :
                        if (choixSuppr=="Lieu de travail enregister") :
                            self.__gazelle.supprVilleMeteo(2,"")
                        else :
                            self.__gazelle.supprVilleMeteo(3,choixSuppr)
                self.__affichageCadreMeteo(1)
    
    def __affichageCadreGPS(self,mode:int):
        """
        1 : Acceuil
        2 : Domicile
        3 : Travail
        """
        match mode :
            case 1 :
                self.__labelTitreGPS.configure(text="Parametre GPS")
                self.__btnAdresseDomicile.place(relx=0.2,y=200)
                self.__btnAdresseWork.place(relx=0.2,y=275)
                self.__btnvaliderGPS.place_forget()
                self.__btnretourGPS.place_forget()
                self.__btnsupprGPS.place_forget()
                self.__btnentryGPS.place_forget()
            case 2 :
                self.__labelTitreGPS.configure(text="Adresse du domicile")
                self.__btnAdresseDomicile.place_forget()
                self.__btnAdresseWork.place_forget()
                self.__btnvaliderGPS.place(relx=1, rely=1, anchor='se')
                self.__btnretourGPS.place(relx=0, rely=1, anchor='sw')
                self.__btnsupprGPS.place(relx=0.5, rely=1.0, anchor="s")  
                self.__btnentryGPS.place(relx=0.5, rely=0.5, anchor="center") 
                self.__btnvaliderGPS.configure(command=lambda:self.__validerGPS(1,1))
                self.__btnsupprGPS.configure(command=lambda:self.__validerGPS(2,1))
            case 3 : 
                self.__labelTitreGPS.configure(text="Adresse du lieu de travail")
                self.__btnAdresseDomicile.place_forget()
                self.__btnAdresseWork.place_forget()
                self.__btnvaliderGPS.place(relx=1, rely=1, anchor='se')
                self.__btnretourGPS.place(relx=0, rely=1, anchor='sw')
                self.__btnsupprGPS.place(relx=0.5, rely=1.0, anchor="s")  
                self.__btnentryGPS.place(relx=0.5, rely=0.5, anchor="center") 
                self.__btnvaliderGPS.configure(command=lambda:self.__validerGPS(1,2))
                self.__btnsupprGPS.configure(command=lambda:self.__validerGPS(2,2))
    
    def __validerGPS(self,mode:int,type:int):
        """
        Mode : 
        1 : Add 
        2 : Suppr \n 
        Type : 
        1 : Domicile 
        2 : Travail
        """
        
        match mode :
            case 1 :
                adresse = self.__btnentryGPS.get()
                if (adresse==""):
                    showerror("Parametre","Entrer une adresse pour l'enregister")
                else :
                    self.__gazelle.ajoutGPSAdresse(type,adresse)
                    self.__btnentryGPS.delete(0,END)
                self.__affichageCadreGPS(1)
            case 2 : 
                self.__gazelle.supprGPSAdresse(type)
                self.__affichageCadreGPS(1)
    
    def __validerMoteur(self):
        moteur = self.__varMoteurRecherce.get()
        self.__gazelle.changeMoteur(moteur)
        showinfo("Parametre","Moteur enregistrer")
        self.__backAcceuil()


