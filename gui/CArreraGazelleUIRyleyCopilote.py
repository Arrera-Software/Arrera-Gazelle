from librairy.arrera_tk import *
from objet.arreraGazelle import*
from tkinter.messagebox import*
from typing import Union

class CArreraGazelleUIRyleyCopilote :
    def __init__(self,atk:CArreraTK,windows:Union[ctk.CTk,ctk.CTkToplevel],emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,emplacementJsonAssistant:str,emplacementConfigSetting:str):
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
        self.__arrTK = atk
        # Varriable

        # Varriable police taille

        police = "Arial"
        tailleTitle = 27
        tailleMain = 23

        # Varriable pour les widget
        self.__varRecherche = StringVar(self.__windows)
        self.__varMoteurRecherce = StringVar(self.__windows)
        self.__varTheme = StringVar(self.__windows)
        self.__varGenre = StringVar(self.__windows)
        self.__varChoixLieu = StringVar(self.__windows)
        self.__varSupprLieu = StringVar(self.__windows)
        self.__varSupprSoft = StringVar(self.__windows)
        self.__varChoixSoft = StringVar(self.__windows)
        self.__varChoixSite =  StringVar(self.__windows)
        self.__varSupprSite =  StringVar(self.__windows)
        self.__varChoixTheme  =  StringVar(self.__windows)
        self.__varChoixMicro =  StringVar(self.__windows)
        # Liste
        listeTheme = jsonSetting.lectureJSONList("listeTheme")
        listMoteur = ["Duckduckgo",
                      "google",
                      "bing",
                      "brave",
                      "ecosia",
                      "qwant"]
        listGenre = jsonSetting.lectureJSONList("listGenre")
        listChoixLieu = ["Simple","Domicile","Travail"]
        listTypeSoft = ["Autre","Traitement de texte",
                        "Tableur","Presentation",
                        "Navigateur Internet",
                        "Note","Musique"]
        listChoixSite = ["Autre","Cloud"]
        self.__listChoixMicro = ["ON","OFF"]

        # Creation des Frame
        self.__cadreMenu = self.__arrTK.createFrame(self.__windows,width=150,height=600)
        self.__cadreAcceuil = self.__arrTK.createFrame(self.__windows,width=350,height=600)
        self.__cadreUser = self.__arrTK.createFrame(self.__windows,width=350,height=600)
        self.__cadreMeteo = self.__arrTK.createFrame(self.__windows,width=350,height=600)
        self.__cadreGPS = self.__arrTK.createFrame(self.__windows,width=350,height=600)
        self.__cadreRecherche = self.__arrTK.createFrame(self.__windows,width=350,height=600)
        self.__cadreSoft = self.__arrTK.createFrame(self.__windows,width=350,height=600)
        self.__cadreInternet = self.__arrTK.createFrame(self.__windows,width=350,height=600)
        self.__cadreTheme = self.__arrTK.createFrame(self.__windows,width=350,height=600)
        self.__cadreMicro = self.__arrTK.createFrame(self.__windows,width=350,height=600)

        #cadre interne a l'acceuil
        self.__cadresPresentations = [
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=200,wightBoder=1),
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=200,wightBoder=1),
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=200,wightBoder=1),
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=200,wightBoder=1),
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=200,wightBoder=1),
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=200,wightBoder=1)]
        #Widget
        self.__labelTitreMenu = self.__arrTK.createLabel(self.__cadreMenu,text="Menu",police="arial",taille=tailleTitle)
        self.__labelcadresPresentations = [
            self.__arrTK.createLabel(self.__cadresPresentations[0],text="Gestion recherche",police="Arial",taille=17),
            self.__arrTK.createLabel(self.__cadresPresentations[1],text="Gestion meteo",police="Arial",taille=17),
            self.__arrTK.createLabel(self.__cadresPresentations[2],text="Gestion GPS",police="Arial",taille=17),
            self.__arrTK.createLabel(self.__cadresPresentations[3],text="Gestion software",police="Arial",taille=17),
            self.__arrTK.createLabel(self.__cadresPresentations[4],text="Gestion Site internet",police="Arial",taille=17),
            self.__arrTK.createLabel(self.__cadresPresentations[5],text="Gestion theme",police="Arial",taille=17)]
        
        self.__boutonMenu = [
                        self.__arrTK.createButton(self.__cadreMenu,police="arial",taille=23,
                                                  text="Acceuil",command=self.__backAcceuil,width=20),#0
                        self.__arrTK.createButton(self.__cadreMenu,police="arial",taille=23,
                                                  text="Utilisateur",command=self.__showUserFrame,width=20),#1
                        self.__arrTK.createButton(self.__cadreMenu,police="arial",taille=23,
                                                  text="Meteo",command=lambda : self.__showMeteoFrame(1),width=20),#2
                        self.__arrTK.createButton(self.__cadreMenu,police="arial",taille=23,
                                                  text="GPS",command=lambda : self.__showGPSFrame(1),width=20),#3
                        self.__arrTK.createButton(self.__cadreMenu,police="arial",taille=23,
                                                  text="Recherche",command=self.__showRechercheFrame,width=20),#4
                        self.__arrTK.createButton(self.__cadreMenu,police="arial",taille=23,
                                                  text="Software",command=lambda : self.__showSoftFrame(1),width=20),#5
                        self.__arrTK.createButton(self.__cadreMenu,police="arial",taille=23,
                                                  text="Site Web",command=lambda :self.__showInternetFrame(1),width=20),#6
                        self.__arrTK.createButton(self.__cadreMenu,police="arial",taille=23,
                                                  text="Theme",command=self.__showThemeFrame,width=20),#7
                        self.__arrTK.createButton(self.__cadreMenu, police="arial", taille=23,
                                                text="Arrera Work", command=self.__showMicroFrame, width=20),#8
                        self.__arrTK.createButton(self.__cadreMenu, police="arial", taille=23,
                                                text="Video Download", command=self.__showMicroFrame, width=20),#9
                        self.__arrTK.createButton(self.__cadreMenu,police="arial",taille=23,
                                                  text="Micro",command=self.__showMicroFrame,width=20),#10
                        self.__arrTK.createButton(self.__cadreMenu,police="arial",taille=23,
                                                  text="Quitter",width=20)#11
        ]
        
        #cadresPresentations
        #0
        self.__menuRecherche1 = self.__arrTK.createOptionMenu(self.__cadresPresentations[0],var=self.__varRecherche,value=listMoteur)
        self.__btnValiderMoteur1 = self.__arrTK.createButton(self.__cadresPresentations[0],text="Valider"
                                                             ,width=20,police = "arial" , taille = tailleMain ,command=lambda : self.__validerMoteur(2))
        #1
        self.__btnMeteo1 = self.__arrTK.createButton(self.__cadresPresentations[1],text="Ajouter\nune ville"
                                                     ,width=20,police = "arial" , taille = tailleMain  ,command = lambda : self.__showMeteoFrame(2))
        #2
        self.__btnGPSHome = self.__arrTK.createButton(self.__cadresPresentations[2],text="Adresse\nde domicile"
                                                      ,width=20,police = "arial" , taille = tailleMain ,command=lambda : self.__showGPSFrame(2))
        self.__btnGPSWork = self.__arrTK.createButton(self.__cadresPresentations[2],text="Adresse\nde travail"
                                                      ,width=20,police = "arial" , taille = tailleMain ,command=lambda : self.__showGPSFrame(3))
        #3
        self.__btnSoftware1 = self.__arrTK.createButton(self.__cadresPresentations[3],text="Ajouter\nun logiciel"
                                                        ,width=20,police = "arial" , taille = tailleMain ,command=lambda : self.__showSoftFrame(2))
        #4
        self.__buttonAddSite = self.__arrTK.createButton(self.__cadresPresentations[4],text="Ajouter"
                                                         ,width=20,police = "arial" , taille = tailleMain ,command=lambda :self.__showInternetFrame(2))
        self.__buttonSupprSite = self.__arrTK.createButton(self.__cadresPresentations[4],text="Supprimer"
                                                           ,width=20,police = "arial" , taille = tailleMain ,command=lambda :self.__showInternetFrame(3))
        #5
        self.__menuTheme1 = self.__arrTK.createOptionMenu(self.__cadresPresentations[5],var=self.__varTheme,value=listeTheme)
        self.__btnValiderTheme1 = self.__arrTK.createButton(self.__cadresPresentations[5],text="Valider"
                                                            ,width=20,police = "arial" , taille = tailleMain ,command=lambda : self.__validerTheme(2))

        # Cadre User 
        self.__labelTitreUser = self.__arrTK.createLabel(self.__cadreUser,police="Arial",taille=tailleTitle)
        self.__btnPrenom = self.__arrTK.createButton(self.__cadreUser,police="Arial",taille=tailleMain
                                                     ,text="Nom de l'utilisateur",command=lambda : self.__affichageCadreUser(2))
        self.__btnGenre = self.__arrTK.createButton(self.__cadreUser,police="Arial",taille=tailleMain
                                                    ,text="genre de l'utilisateur",command=lambda : self.__affichageCadreUser(3))
        self.__menuGenre = self.__arrTK.createOptionMenu(self.__cadreUser,var=self.__varGenre,value=listGenre)
        self.__entryNameUser = self.__arrTK.createEntry(self.__cadreUser,police="Arial",taille=tailleMain,width=250)
        self.__btnvaliderUser = self.__arrTK.createButton(self.__cadreUser,police="Arial",taille=tailleMain,
                                                          text="Valider",width=20)
        self.__btnAnulerUser = self.__arrTK.createButton(self.__cadreUser,police="Arial",taille=tailleMain,
                                                         text="Annuler",command=lambda : self.__affichageCadreUser(1),width=20)

        # Cadre Meteo 
        self.__labelTitreMeteo = self.__arrTK.createLabel(self.__cadreMeteo,police="Arial",taille=tailleTitle)
        self.__btnListMeteo =  self.__arrTK.createButton(self.__cadreMeteo,text="Liste meteo"
                                                         ,police="Arial",taille=tailleMain,command= lambda : self.__affichageCadreMeteo(2))
        self.__btnAddVille =   self.__arrTK.createButton(self.__cadreMeteo,text="Ajouter une ville"
                                                         ,police="Arial",taille=tailleMain,command= lambda : self.__affichageCadreMeteo(3))
        self.__btnSupprVille = self.__arrTK.createButton(self.__cadreMeteo,text="Supprimer une ville"
                                                         ,police="Arial",taille=tailleMain,command= lambda : self.__affichageCadreMeteo(4))
        self.__labelListeMeteo = self.__arrTK.createLabel(self.__cadreMeteo,police="Arial",taille=tailleTitle)
        self.__menuChoixLieu = self.__arrTK.createOptionMenu(self.__cadreMeteo,var=self.__varChoixLieu,value=listChoixLieu)
        self.__menuSupprLieu = self.__arrTK.createOptionMenu(self.__cadreMeteo,var=self.__varSupprLieu,value=listChoixLieu)
        self.__entryVille = self.__arrTK.createEntry(self.__cadreMeteo,police="Arial",taille=tailleMain)
        self.__btnvaliderMeteo = self.__arrTK.createButton(self.__cadreMeteo,text="Valider"
                                                           ,police="Arial",taille=tailleMain)
        self.__btnannulerMeteo = self.__arrTK.createButton(self.__cadreMeteo,police="Arial"
                                                           ,taille=tailleMain,command= lambda : self.__affichageCadreMeteo(1))
        # Cadre GPS 
        self.__labelTitreGPS = self.__arrTK.createLabel(self.__cadreGPS,police="Arial",taille=tailleTitle)
        self.__btnAdresseDomicile = self.__arrTK.createButton(self.__cadreGPS,text="Adresse du domicile"
                                                              ,police="Arial",taille=tailleMain,command=lambda : self.__affichageCadreGPS(2))
        self.__btnAdresseWork = self.__arrTK.createButton(self.__cadreGPS,text="Adresse du lieu de travail"
                                                          ,police="Arial",taille=tailleMain,command=lambda : self.__affichageCadreGPS(3))
        self.__btnvaliderGPS = self.__arrTK.createButton(self.__cadreGPS,text="Valider",police="Arial",taille=tailleMain)
        self.__btnretourGPS = self.__arrTK.createButton(self.__cadreGPS,text="Retour",police="Arial",taille=tailleMain,command=lambda : self.__affichageCadreGPS(1))
        self.__btnSupprGPSDomicile = self.__arrTK.createButton(self.__cadreGPS,text="Supprimer l'adresse du domicile"
                                                               ,police="Arial",taille=tailleMain,command=lambda : self.__validerGPS(2,1))
        self.__btnSupprGPSWork = self.__arrTK.createButton(self.__cadreGPS,text="Supprimer l'adresse du travail"
                                                           ,police="Arial",taille=tailleMain,command=lambda : self.__validerGPS(2,2))
        self.__btnsupprGPS = self.__arrTK.createButton(self.__cadreGPS,text="Supprimer une adresse"
                                                       ,police="Arial",taille=tailleMain,command=lambda : self.__affichageCadreGPS(4))
        self.__btnentryGPS = self.__arrTK.createEntry(self.__cadreGPS,police="Arial",taille=tailleMain)
        # Cadre Rechecrhe
        self.__labelTitreRecherche = self.__arrTK.createLabel(self.__cadreRecherche,text="Chosissez votre moteur\nde recherche"
                                                              ,police="Arial",taille=tailleTitle)
        self.__menuMoteurRecherche = self.__arrTK.createOptionMenu(self.__cadreRecherche,var = self.__varMoteurRecherce,value = listMoteur)
        self.__btnvaliderMoteur = self.__arrTK.createButton(self.__cadreRecherche,text="Valider"
                                                            ,police="Arial",taille=tailleMain,command=lambda : self.__validerMoteur(1))
        # Cadre Software 
        self.__labelTitreSoftware = self.__arrTK.createLabel(self.__cadreSoft,police="Arial",taille=tailleTitle)
        self.__btnAnnulerSoft = self.__arrTK.createButton(self.__cadreSoft,text="Annuler",
                                                          police="Arial",taille=tailleMain,command=lambda:self.__affichageCadreSoft(1))
        self.__btnValiderSoft = self.__arrTK.createButton(self.__cadreSoft,text="Valider",
                                                          police="Arial",taille=tailleMain)
        self.__btnAddSoft = self.__arrTK.createButton(self.__cadreSoft,text="Ajouter un logiciel",
                                                      police="Arial",taille=tailleMain,command=lambda:self.__affichageCadreSoft(2))
        self.__btnSupprSoft= self.__arrTK.createButton(self.__cadreSoft,text="Supprimer un logiciel",
                                                       police="Arial",taille=tailleMain,command=lambda:self.__affichageCadreSoft(3))
        self.__menuSupprSoft = self.__arrTK.createOptionMenu(self.__cadreSoft,var = self.__varSupprSoft,value = listTypeSoft)
        self.__menuChoixSoft  = self.__arrTK.createOptionMenu(self.__cadreSoft,var = self.__varChoixSoft,value = listTypeSoft)
        self.__entryNameSoft = self.__arrTK.createEntry(self.__cadreSoft,police="Arial",taille=15)
        # Cadre Internet
        self.__labelTitreInternet = self.__arrTK.createLabel(self.__cadreInternet,police="Arial",taille=tailleTitle)
        self.__btnAddSite = self.__arrTK.createButton(self.__cadreInternet,text="Enregister un site",
                                                      police="Arial",taille=tailleMain,command=lambda : self.__affichageCadreSite(2))
        self.__btnSupprSite = self.__arrTK.createButton(self.__cadreInternet,text="Supprimer un site",
                                                        police="Arial",taille=tailleMain,command=lambda : self.__affichageCadreSite(3))
        self.__btnAnnulerInternet = self.__arrTK.createButton(self.__cadreInternet,text="Annuler",
                                                              police="Arial",taille=tailleMain,command=lambda : self.__affichageCadreSite(1))
        self.__btnValiderInternet = self.__arrTK.createButton(self.__cadreInternet,text="Valider",
                                                              police="Arial",taille=tailleMain)
        self.__entryNameSite = self.__arrTK.createEntry(self.__cadreInternet,police="Arial",taille=tailleMain)
        self.__entryLinkSite = self.__arrTK.createEntry(self.__cadreInternet,police="Arial",taille=tailleMain)
        self.__menuChoixSite =  self.__arrTK.createOptionMenu(self.__cadreInternet,var = self.__varChoixSite,value = listChoixSite)
        self.__menuSupprSite =  self.__arrTK.createOptionMenu(self.__cadreInternet,var = self.__varSupprSite,value=listChoixSite)
        # Cardre theme 
        self.__labelTitreTheme = self.__arrTK.createLabel(self.__cadreTheme,text="Choix du theme\nde l'interface"
                                                          ,police="Arial",taille=tailleTitle)
        self.__menuChoixTheme = self.__arrTK.createOptionMenu(self.__cadreTheme,var = self.__varChoixTheme,value=listeTheme)
        self.__btnValiderTheme = self.__arrTK.createButton (self.__cadreTheme,text="Valider",
                                                            police="Arial",taille=tailleMain,command=lambda : self.__validerTheme(1))
        # Cadre Micro
        self.__labelTitreMicro = self.__arrTK.createLabel(self.__cadreMicro,text="Sons au declanchement\ndu micro",police="Arial",taille=tailleTitle)
        self.__menuChoixMicro = self.__arrTK.createOptionMenu(self.__cadreMicro,
                                                              var = self.__varChoixMicro,value=self.__listChoixMicro)
        self.__btnValiderMicro = self.__arrTK.createButton (self.__cadreMicro,text="Valider"
                                                            ,police="Arial",taille=tailleMain,command=self.__validerMicro)

        self.__arrTK.placeTopCenter(self.__labelTitreMenu)

        # Placement widget
        # Cadre acceuil
        self.__cadresPresentations[0].place(x=0, y=0)
        self.__cadresPresentations[1].place(x=180, y=0)
        self.__cadresPresentations[2].place(x=0, y=200)
        self.__cadresPresentations[3].place(x=180, y=200)
        self.__cadresPresentations[4].place(x=0, y=400)
        self.__cadresPresentations[5].place(x=180, y=400)

        for i in range(0,5):
            self.__arrTK.placeTopCenter(self.__labelcadresPresentations[i])
        
        self.__boutonMenu[0].place(relx=0.1,y=50)
        self.__boutonMenu[1].place(relx=0.1,y=100)
        self.__boutonMenu[2].place(relx=0.1,y=150)
        self.__boutonMenu[3].place(relx=0.1,y=200)
        self.__boutonMenu[4].place(relx=0.1,y=250)
        self.__boutonMenu[5].place(relx=0.1,y=300)
        self.__boutonMenu[6].place(relx=0.1,y=350)
        self.__boutonMenu[7].place(relx=0.1,y=400)
        self.__boutonMenu[8].place(relx=0.1,y=450)
        self.__boutonMenu[9].place(relx=0.1,y=500)
        if (jsonSetting.lectureJSON("gestionMicro")=="1"):
            self.__boutonMenu[10].place(relx=0.1,y=550)

        self.__arrTK.placeTopCenter(self.__labelcadresPresentations[0])
        self.__arrTK.placeTopCenter(self.__labelcadresPresentations[1])
        self.__arrTK.placeTopCenter(self.__labelcadresPresentations[2])
        self.__arrTK.placeTopCenter(self.__labelcadresPresentations[3])
        self.__arrTK.placeTopCenter(self.__labelcadresPresentations[4])
        self.__arrTK.placeTopCenter(self.__labelcadresPresentations[5])


        self.__arrTK.placeCenter(self.__menuRecherche1)
        self.__arrTK.placeBottomCenter(self.__btnValiderMoteur1)
        self.__arrTK.placeCenter(self.__btnMeteo1)
        self.__arrTK.placeCenter(self.__btnGPSHome)
        self.__arrTK.placeBottomCenter(self.__btnGPSWork)
        self.__arrTK.placeCenter(self.__btnSoftware1)
        self.__arrTK.placeCenter(self.__buttonAddSite)
        self.__arrTK.placeBottomCenter(self.__buttonSupprSite)
        self.__arrTK.placeCenter(self.__menuTheme1)
        self.__arrTK.placeBottomCenter(self.__btnValiderTheme1)

        self.__arrTK.placeTopCenter(self.__labelTitreUser)

        self.__arrTK.placeTopCenter(self.__labelTitreMeteo)

        self.__arrTK.placeTopCenter(self.__labelTitreGPS)

        self.__arrTK.placeTopCenter(self.__labelTitreRecherche)
        self.__arrTK.placeCenter(self.__menuMoteurRecherche)
        self.__arrTK.placeBottomCenter(self.__btnvaliderMoteur)

        self.__arrTK.placeTopCenter(self.__labelTitreSoftware)

        self.__arrTK.placeTopCenter(self.__labelTitreInternet)

        self.__arrTK.placeTopCenter(self.__labelTitreTheme)
        self.__arrTK.placeCenter(self.__menuChoixTheme)
        self.__arrTK.placeBottomCenter(self.__btnValiderTheme)

        self.__arrTK.placeTopCenter(self.__labelTitreMicro)
        self.__arrTK.placeCenter(self.__menuChoixMicro)
        self.__arrTK.placeBottomCenter(self.__btnValiderMicro)

            
        
    def active(self):
        self.__arrTK.setResizable(False)
        self.__arrTK.setGeometry(500,600)
        self.__cadreAcceuil.pack(side="right")
        self.__cadreMenu.pack(side="left")
    
    def passQuitFnc(self,quitFNC):
        self.__boutonMenu[9].configure(command=lambda : self.__fncQuit(quitFNC) )
        self.__arrTK.placeBottomCenter(self.__boutonMenu[11])
    
    def __fncQuit(self,quitFnc):
        self.__disableAllFrame()
        self.__cadreMenu.pack_forget()
        quitFnc()

    def __backAcceuil(self):
        self.__arrTK.packRight(self.__cadreAcceuil)
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
        self.__arrTK.packRight(self.__cadreUser)
        self.__affichageCadreUser(1)
    
    def __showMeteoFrame(self,mode:int):
        """
        1 : Normal
        2 : add direct
        """
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreMeteo)
        match mode :
            case 1 :
                self.__affichageCadreMeteo(1)
            case 2 :
                self.__affichageCadreMeteo(3)
    
    def __showGPSFrame(self,mode:int):
        """
        1 : Normal
        2 : Domicile direct
        3 : Work direct
        """
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreGPS)
        match mode :
            case 1 :
                self.__affichageCadreGPS(1)
            case 2 :
                self.__affichageCadreGPS(2)
            case 3 :
                self.__affichageCadreGPS(3)

    def __showRechercheFrame(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreRecherche)
    
    def __showSoftFrame(self,mode:int):
        """
        1 : Normal
        2 : Add direct
        """
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreSoft)
        match mode :
            case 1 :
                self.__affichageCadreSoft(1)
            case 2 :
                self.__affichageCadreSoft(2)
    
    def __showInternetFrame(self,mode:int):
        """
        1 : Normal
        2 : Add direct
        3 : Suppr direct
        """
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreInternet)
        match mode :
            case 1 :
                self.__affichageCadreSite(1)
            case 2 :
                self.__affichageCadreSite(2)
            case 3 : 
                self.__affichageCadreSite(3)
    
    def __showThemeFrame(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreTheme)
    
    def __showMicroFrame(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreMicro)
        etatMicro = self.__gazelle.getSoundMicroAsEnable()
        if (etatMicro==True):
            self.__varChoixMicro.set(self.__listChoixMicro[0])
        else :
            self.__varChoixMicro.set(self.__listChoixMicro[1])
       

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
                self.__entryNameUser.place_forget()
                self.__btnvaliderUser.place_forget()
                self.__btnAnulerUser.place_forget()
            case 2 :
                self.__labelTitreUser.configure(text="Prenom de l'utilisateur")
                self.__btnPrenom.place_forget()
                self.__btnGenre.place_forget()
                self.__menuGenre.place_forget()
                self.__entryNameUser.place(relx=0.5, rely=0.5, anchor="center")
                self.__btnvaliderUser.place(relx=1, rely=1, anchor='se')  
                self.__btnAnulerUser.place(relx=0, rely=1, anchor='sw')
                self.__btnvaliderUser.configure(command=lambda : self.__validerUser(1))
            case 3 :
                self.__labelTitreUser.configure(text="Genre de l'utilisateur")
                self.__btnPrenom.place_forget()
                self.__btnGenre.place_forget()
                self.__menuGenre.place(relx=0.5, rely=0.5, anchor="center")
                self.__entryNameUser.place_forget()
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
                name = self.__entryNameUser.get()
                if (name==""):
                    showerror("Parametre","Vous avez pas entrer votre prenom")
                else :
                    self.__entryNameUser.delete(0,END)
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
                #place(relx=0.2,y=200)
                self.__arrTK.placeCenterOnWidth(self.__btnListMeteo,y=150)
                self.__arrTK.placeCenterOnWidth(self.__btnAddVille,y=250)
                self.__arrTK.placeCenterOnWidth(self.__btnSupprVille,y=350)
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
                self.__arrTK.placeBottomCenter(self.__btnannulerMeteo)
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
                self.__arrTK.placeBottomRight(self.__btnvaliderMeteo)
                self.__arrTK.placeBottomLeft(self.__btnannulerMeteo)
                self.__arrTK.placeCenter(self.__entryVille)
                self.__btnvaliderMeteo.configure(command=lambda : self.__validerMeteo(1))
            case 4 : 
                listeVille = self.__gazelle.getMeteoSave()
                self.__labelListeMeteo.configure(text="")
                nbVille = len(listeVille)
                if (nbVille == 0 ) :
                    showerror("Parametre","Aucun lieu enregister")
                else :
                    self.__menuSupprLieu = self.__arrTK.createOptionMenu(self.__cadreMeteo,var = self.__varSupprLieu,value=listeVille)
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
                self.__arrTK.placeCenterOnWidth(self.__btnAdresseDomicile,y=200)
                self.__arrTK.placeCenterOnWidth(self.__btnAdresseWork,y=275)
                self.__arrTK.placeCenterOnWidth(self.__btnsupprGPS,y=350)
                self.__btnvaliderGPS.place_forget()
                self.__btnretourGPS.place_forget()
                self.__btnentryGPS.place_forget()
                self.__btnSupprGPSDomicile.place_forget()
                self.__btnSupprGPSWork.place_forget()
            case 2 :
                self.__labelTitreGPS.configure(text="Adresse du domicile")
                self.__btnAdresseDomicile.place_forget()
                self.__btnAdresseWork.place_forget()
                self.__btnsupprGPS.place_forget()
                self.__arrTK.placeBottomRight(self.__btnvaliderGPS)
                self.__arrTK.placeBottomLeft(self.__btnretourGPS)

                self.__btnentryGPS.place(relx=0.5, rely=0.5, anchor="center") 
                self.__btnvaliderGPS.configure(command=lambda:self.__validerGPS(1,1))

            case 3 : 
                self.__labelTitreGPS.configure(text="Adresse du lieu de travail")
                self.__btnAdresseDomicile.place_forget()
                self.__btnAdresseWork.place_forget()
                self.__btnsupprGPS.place_forget()
                self.__btnvaliderGPS.place(relx=1, rely=1, anchor='se')
                self.__btnretourGPS.place(relx=0, rely=1, anchor='sw')
                self.__btnentryGPS.place(relx=0.5, rely=0.5, anchor="center") 
                self.__btnvaliderGPS.configure(command=lambda:self.__validerGPS(1,2))

            case 4 :
                if (self.__gazelle.getGPSAdresseIsSet(1) == False) and (self.__gazelle.getGPSAdresseIsSet(2) == False):
                    messagebox.showerror("Parametre","Il a aucune adresse enregistrer")
                else :
                    self.__labelTitreGPS.configure(text="Suppression d'adresse")
                    self.__btnAdresseDomicile.place_forget()
                    self.__btnAdresseWork.place_forget()
                    self.__btnsupprGPS.place_forget()
                    self.__arrTK.placeBottomLeft(self.__btnretourGPS)

                    if (self.__gazelle.getGPSAdresseIsSet(1)==True and self.__gazelle.getGPSAdresseIsSet(2) == True):
                        self.__arrTK.placeCenterOnWidth(self.__btnSupprGPSDomicile,y=200)
                        self.__arrTK.placeCenterOnWidth(self.__btnSupprGPSWork, y=275)
                    else :
                        if (self.__gazelle.getGPSAdresseIsSet(1)==True and self.__gazelle.getGPSAdresseIsSet(2) == False):
                            self.__arrTK.placeCenterOnWidth(self.__btnSupprGPSDomicile, y=200)
                        else :
                            if (self.__gazelle.getGPSAdresseIsSet(1) == False and self.__gazelle.getGPSAdresseIsSet(2) == True):
                                self.__arrTK.placeCenterOnWidth(self.__btnSupprGPSWork, y=200)
    
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
    
    def __validerMoteur(self,mode:int):
        """
        1 : page
        2 : acceuil
        """
        match mode : 
            case 1 :
                moteur = self.__varMoteurRecherce.get()
            case 2 : 
                moteur = self.__varRecherche.get()
            case other :
                return
        self.__gazelle.changeMoteur(moteur)
        showinfo("Parametre","Moteur enregistrer")
        self.__backAcceuil()

    def __affichageCadreSoft(self,mode:int):
        """
        1 : Acceuil 
        2 : Add
        3 : Suppr
        """
        match mode : 
            case 1 :
                self.__labelTitreSoftware.configure(text="Gestion des logiciel")
                self.__btnAnnulerSoft.place_forget()
                self.__btnValiderSoft.place_forget()
                self.__btnAddSoft.place(relx=0.5, y=200, anchor="n")
                self.__btnSupprSoft.place(relx=0.5, y=275, anchor="n")
                self.__menuSupprSoft.place_forget()
                self.__menuChoixSoft.place_forget()
                self.__entryNameSoft.place_forget()
            case 2 :
                self.__labelTitreSoftware.configure(text="Ajout de logiciel")
                self.__btnAnnulerSoft.place(relx=0, rely=1, anchor='sw')
                self.__btnValiderSoft.place(relx=1, rely=1, anchor='se')
                self.__btnAddSoft.place_forget()
                self.__btnSupprSoft.place_forget()
                self.__menuSupprSoft.place_forget()
                self.__menuChoixSoft.place(x=0,y=100)
                self.__entryNameSoft.place(relx=0.5, rely=0.5, anchor="center")
                self.__btnValiderSoft.configure(command=lambda : self.__validerSoft(1))
            case 3 :
                listSoft = self.__gazelle.getListSoft()
                if (len(listSoft)==0):
                    showerror("Parametre","Impossible de supprimer des logiciel avant d'en ajouter")
                else :
                    self.__menuSupprSoft = self.__arrTK.createOptionMenu(self.__cadreSoft,var=self.__varSupprSoft,value=listSoft)
                    self.__varSupprSoft.set(listSoft[0])

                    self.__labelTitreSoftware.configure(text="Suppression de logiciel")
                    self.__btnAnnulerSoft.place(relx=0, rely=1, anchor='sw')
                    self.__btnValiderSoft.place(relx=1, rely=1, anchor='se')
                    self.__btnAddSoft.place_forget()
                    self.__btnSupprSoft.place_forget()
                    self.__menuSupprSoft.place(relx=0.5, rely=0.5, anchor="center")
                    self.__menuChoixSoft.place_forget()
                    self.__entryNameSoft.place_forget()
                    self.__btnValiderSoft.configure(command=lambda : self.__validerSoft(2))
    
    def __validerSoft(self,mode:int):
        """
        1 : add 
        2 : suppr
        """
        os = self.__gazelle.getOS()
        match mode :
            case 1 :
                type = self.__varChoixSoft.get()
                if( type == "Autre") :
                    nameSoft = self.__entryNameSoft.get()
                    if (os=="windows"):
                        self.__gazelle.addSoft(1,nameSoft,"")
                    else :
                        if (os=="linux") :
                            self.addSoftLinux(1,nameSoft)
                        else :
                            showerror("Parametre","Systeme d'exploitation non reconnu")
                else : 
                    if (type=="Traitement de texte"):
                        if (os=="windows"):
                            self.__gazelle.addSoft(2,"","")
                        else :
                            if (os=="linux") :
                                self.addSoftLinux(2,"")
                            else :
                                showerror("Parametre","Systeme d'exploitation non reconnu")
                    else :
                        if (type=="Tableur"):
                            if (os=="windows"):
                                self.__gazelle.addSoft(3,"","")
                            else :
                                if (os=="linux") :
                                    self.addSoftLinux(3,"")
                                else :
                                    showerror("Parametre","Systeme d'exploitation non reconnu")
                        else :
                            if (type=="Presentation"):
                                if (os=="windows"):
                                    self.__gazelle.addSoft(4,"","")
                                else :
                                    if (os=="linux") :
                                        self.addSoftLinux(4,"")
                                    else :
                                        showerror("Parametre","Systeme d'exploitation non reconnu")
                            else : 
                                if (type=="Navigateur Internet"):
                                    if (os=="windows"):
                                        self.__gazelle.addSoft(5,"","")
                                    else :
                                        if (os=="linux") :
                                            self.addSoftLinux(5,"")
                                        else :
                                            showerror("Parametre","Systeme d'exploitation non reconnu")
                                else :
                                    if (type=="Note"):
                                        if (os=="windows"):
                                            self.__gazelle.addSoft(7,"","")
                                        else :
                                            if (os=="linux") :
                                                self.addSoftLinux(7,"")
                                            else :
                                                showerror("Parametre","Systeme d'exploitation non reconnu")
                                    else :
                                        if (type=="Musique"):
                                            if (os=="windows"):
                                                self.__gazelle.addSoft(6,"","")
                                            else :
                                                if (os=="linux") :
                                                    self.addSoftLinux(6,"")
                                                else :
                                                    showerror("Parametre","Systeme d'exploitation non reconnu")
                self.__entryNameSoft.delete(0,END)
                self.__affichageCadreSoft(1)
            case 2 :
                soft = self.__varSupprSoft.get()
                if (soft=="Traitement de texte"):
                    self.__gazelle.supprSoft(2,"")
                else :
                    if (soft=="Tableur"):
                        self.__gazelle.supprSoft(3,"")
                    else :
                        if (soft=="Presentation"):
                            self.__gazelle.supprSoft(4,"")
                        else :
                            if (soft=="Navigateur internet"):
                                self.__gazelle.supprSoft(5,"")
                            else :
                                if (soft=="Note"):
                                    self.__gazelle.supprSoft(7,"")
                                else :
                                    if (soft=="Musique"):
                                        self.__gazelle.supprSoft(6,"")
                                    else :
                                        self.__gazelle.supprSoft(1,soft)
                self.__affichageCadreSoft(1)
    
    
    def addSoftLinux(self,mode:int,name:str):
        """
        1 : normal
        2 : Traitement de texte
        3 : Tableur
        4 : Presentation
        5 : Navigateur internet
        6 : Musique
        7 : Note
        """
        popUP = Toplevel()
        popUP.title("Parametre")
        popUP.minsize(300,110)
        popUP.minsize(300,110)
        Label(popUP,text="Entrer la commande du logiciel",font=("arial","15")).pack()
        entryCommand = Entry(popUP,font=("arial","15"),borderwidth=2,relief="solid")
        entryCommand.place(relx=0.5,rely=0.5,anchor="center")
        if mode == 1 : 
            Button(popUP,text="Valider",font=("arial","15"),command=lambda : self.__gazelle.addSoft(1,name,entryCommand.get()) and popUP.destroy()).pack(side="bottom")
        else :
            Button(popUP,text="Valider",font=("arial","15"),command=lambda : self.__gazelle.addSoft(mode,"",entryCommand.get()) and popUP.destroy()).pack(side="bottom")
    
    def __affichageCadreSite(self,mode:int):
        """
        1 : Acceuil
        2 : Add
        3 : Suppr
        """
        match mode :
            case 1 :
                self.__labelTitreInternet.configure(text="Gestion des sites\ninternet")
                self.__btnAddSite.place(relx=0.2,y=200)
                self.__btnSupprSite.place(relx=0.2,y=275)
                self.__btnAnnulerInternet.place_forget()
                self.__btnValiderInternet.place_forget()
                self.__entryNameSite.place_forget()
                self.__entryLinkSite.place_forget()
                self.__menuChoixSite.place_forget()
                self.__menuSupprSite.place_forget()
            case 2 : 
                self.__labelTitreInternet.configure(text="Enregistrement d'un site")
                self.__btnAddSite.place_forget()
                self.__btnSupprSite.place_forget()
                self.__btnAnnulerInternet.place(relx=0, rely=1, anchor='sw')
                self.__btnValiderInternet.place(relx=1, rely=1, anchor='se')
                self.__entryNameSite.place(relx=0.2,y=200)
                self.__entryLinkSite.place(relx=0.2,y=275)
                self.__menuChoixSite.place(x=0,y=100)
                self.__menuSupprSite.place_forget()
                self.__btnValiderInternet.configure(command=lambda:self.__validerSite(1))
            case 3 : 
                listSite = self.__gazelle.getListSite()
                if (len(listSite)==0):
                    showerror("Parametre","Aucun site enregistrer")
                else :
                    self.__menuSupprSite =  self.__arrTK.createOptionMenu(self.__cadreInternet,var=self.__varSupprSite,value=listSite)
                    self.__labelTitreInternet.configure(text="Enregistrement d'un site")
                    self.__btnAddSite.place_forget()
                    self.__btnSupprSite.place_forget()
                    self.__btnAnnulerInternet.place(relx=0, rely=1, anchor='sw')
                    self.__btnValiderInternet.place(relx=1, rely=1, anchor='se')
                    self.__entryNameSite.place_forget()
                    self.__entryLinkSite.place_forget()
                    self.__menuChoixSite.place_forget()
                    self.__menuSupprSite.place(relx=0.5,rely=0.5,anchor="center")
                    self.__btnValiderInternet.configure(command=lambda:self.__validerSite(2))
                    self.__varSupprSite.set(listSite[0])
                    

    
    def __validerSite(self,mode:int):
        """
        1 : add
        2 : suppr
        """
        match mode :
            case 1 :
                link = self.__entryLinkSite.get()
                if (link!="") :
                    type = self.__varChoixSite.get()
                    if (type == "Cloud"):
                        self.__gazelle.addSite(2,"",link)
                    else :
                        name = self.__entryNameSite.get()
                        if(name=="") :
                            showerror("Parametre","Impossible d'enregister un site sans nom")
                        else :
                            self.__gazelle.addSite(1,name,link)
                            showinfo("Parametre","Site enregister")
                            self.__affichageCadreSite(1)
                else :
                    showerror("Parametre","Impossible d'enregister un site sans url")
                
                self.__entryLinkSite.delete(0,END)
                self.__entryNameSite.delete(0,END)
            case 2 : 
                site = self.__varSupprSite.get()
                if (site == "Cloud") :
                    self.__gazelle.supprSite(2,"")
                else :
                    self.__gazelle.supprSite(1,site)
                showinfo("Parametre","Site supprimer")
                self.__affichageCadreSite(1)  
    
    def __validerTheme(self,mode:int):
        """
        1 : Page 
        2 : Acceuil
        """
        match mode :
            case 1 :
                theme = self.__varChoixTheme.get()
            case 2 :
                theme = self.__varTheme.get()
        self.__gazelle.changeTheme(theme)
        showinfo("Parametre","Theme changer")
        self.__backAcceuil()
    
    def __validerMicro(self):
        sortie = self.__varChoixMicro.get()
        if (sortie=="ON"):
            self.__gazelle.changeSoundMicro(True)
        else :
            self.__gazelle.changeSoundMicro(False)
        self.__backAcceuil()