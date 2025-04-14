from librairy.arrera_tk import *
from objet.arreraGazelle import*
from tkinter.messagebox import*
from typing import Union

class CArreraGazelleUIRyleyCopilote :
    def __init__(self,atk:CArreraTK,windows:Union[ctk.CTk,ctk.CTkToplevel],
                 emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,
                 emplacementJsonAssistant:str,emplacementConfigSetting:str):
        # Ouverture de l'objet

        self.__gazelle = CArreraGazelle(emplacementJsonUser,emplacementJsonNeuronNetwork,emplacementJsonAssistant)
        jsonSetting = jsonWork(emplacementConfigSetting)

        # Mise de la fenetre dans un atribut

        self.__windows = windows
        self.__arrTK = atk

        # Varriable
        tailleTitle = 27
        tailleMain = 23
        self.__varMoteurRecherce = StringVar(self.__windows)
        self.__varTheme = StringVar(self.__windows)
        self.__varGenre = StringVar(self.__windows)
        self.__varChoixLieu = StringVar(self.__windows)
        self.__varSupprLieu = StringVar(self.__windows)
        self.__varSupprSoft = StringVar(self.__windows)
        self.__varChoixSite =  StringVar(self.__windows)
        self.__varSupprSite =  StringVar(self.__windows)
        self.__varChoixTheme  =  StringVar(self.__windows)
        self.__varChoixMicro =  StringVar(self.__windows)
        self.__varChoixSupprMeteo = StringVar(self.__windows)
        startX = 60    # Position X de départ
        startY = 25 # Position Y de départ
        spacingHorizontal = 150 # Espacement horizontal entre les colonnes
        spacingVertical = 150  # Espacement vertical entre les lignes

        # Image
        imgSoft = self.__arrTK.createImage(jsonSetting.lectureJSON("iconSoft"),
                                           tailleX=90,tailleY=90)

        # Liste
        listeTheme = jsonSetting.lectureJSONList("listeTheme")
        self.__listMoteur = jsonSetting.lectureJSONList("listMoteurRecherche")
        self.__listGenre = jsonSetting.lectureJSONList("listGenre")
        listChoixLieu = ["Simple","Domicile","Travail"]
        listChoixSite = ["Autre","Cloud"]

        self.__listChoixMicro = ["ON","OFF"]

        # Creation des Frame
        # Acceuil
        self.__mainFrame = self.__arrTK.createFrame(self.__windows,width=500,height=630)
        self.__cadreMenu = self.__arrTK.createFrame(self.__windows,width=150,height=630)

        # User
        self.__cadreUser = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__userAcceuil = self.__arrTK.createFrame(self.__cadreUser,width=325,height=630)
        self.__userName = self.__arrTK.createFrame(self.__cadreUser,width=325,height=630)
        self.__userGenre = self.__arrTK.createFrame(self.__cadreUser,width=325,height=630)
        # Meteo
        self.__cadreMeteo = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__meteoAcceuil = self.__arrTK.createFrame(self.__cadreMeteo,width=325,height=630)
        self.__meteoDomicile = self.__arrTK.createFrame(self.__cadreMeteo,width=325,height=630)
        self.__meteoWork = self.__arrTK.createFrame(self.__cadreMeteo,width=325,height=630)
        self.__meteoVille = self.__arrTK.createFrame(self.__cadreMeteo,width=325,height=630)
        self.__meteoSuppr = self.__arrTK.createFrame(self.__cadreMeteo,width=325,height=630)

        # GPS
        self.__cadreGPS = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        # Recherche
        self.__cadreRecherche = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        # Logiciel
        self.__cadreSoft = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        # Internet
        self.__cadreInternet = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        # Theme
        self.__cadreTheme = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        # Micro
        self.__cadreMicro = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        # Arrera Work
        self.__cadreArreraWork = self.__arrTK.createFrame(self.__windows, width=350, height=630)
        # Download
        self.__cadreVideoDownload = self.__arrTK.createFrame(self.__windows, width=350, height=630)


        #Widget
        labelTitreMenu = self.__arrTK.createLabel(self.__cadreMenu, text="Menu", ppolice="arial", ptaille=tailleTitle)
        
        boutonMenu = [
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Acceuil",command=self.__backAcceuil,width=20),#0
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Utilisateur",command=self.__showUserFrame,width=20),#1
                        self.__arrTK.createButton(self.__cadreMenu, ppolice="arial", ptaille=23,
                                                  text="Meteo", command=lambda : self.__viewMeteo(), width=20),#2
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="GPS",command=lambda : self.__showGPSFrame(1),width=20),#3
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Recherche",command=self.__showRechercheFrame,width=20),#4
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Logiciel",command=lambda : self.__showSoftFrame(1),width=20),#5
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Site Web",command=lambda :self.__showInternetFrame(1),width=20),#6
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Theme",command=self.__showThemeFrame,width=20),#7
                        self.__arrTK.createButton(self.__cadreMenu, ppolice="arial",ptaille=23,
                                                text="Arrera Work", command=self.__showArreraWorkFolder, width=20),#8
                        self.__arrTK.createButton(self.__cadreMenu, ppolice="arial",ptaille=23,
                                      text="Downloader",command=self.__showArreraDownloadFolder, width=20),  # 9
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Micro",command=self.__showMicroFrame,width=20),#10
        ]

        #mainFrame

        self.__boutonMenuMain = [
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="",image=imgSoft),#0
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nde\nl'utilisateur",command=self.__showUserFrame),#1
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nmeteo",command = lambda : self.__viewMeteo()),#2
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nGPS",command=lambda : self.__showGPSFrame(1)),#3
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nde\nrecherche",command=self.__showRechercheFrame),#4
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\ndes\nlogiciels",command=lambda : self.__showSoftFrame(1)),#5
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\ndes sites\ninternet",command=lambda :self.__showInternetFrame(1)),#6
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\ndu\ntheme",command=self.__showThemeFrame),#7
            self.__arrTK.createButton(self.__mainFrame, ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nArrera\nWork",command=self.__showArreraWorkFolder),#8
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nArrera\nDownload",command=self.__showArreraDownloadFolder),#10
            self.__arrTK.createButton(self.__mainFrame, ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\ndu\nmicro",command=self.__showMicroFrame),  # 9
        ]

        self.__btnQuitMainFrame = self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=200,
                                  text="Quitter")

        # Cadre User
        labelTitleUserAcceuil = self.__arrTK.createLabel(self.__userAcceuil,text="Gestion de l'utilisateur",
                                                         ppolice="Arial", ptaille=tailleTitle)
        btnName = self.__arrTK.createButton(self.__userAcceuil,ppolice = "arial" , ptaille = tailleMain
                                            ,text="Nom de\nl'utilisateur",command=self.__viewUserName)
        btnGenre = self.__arrTK.createButton(self.__userAcceuil,ppolice = "arial" , ptaille = tailleMain
                                             ,text="genre de\nl'utilisateur",command=self.__viewUserGenre)

        labelTitleUserGenre = self.__arrTK.createLabel(self.__userGenre,text="Genre de l'utilisateur",
                                                         ppolice="Arial", ptaille=tailleTitle)
        menuSelectGenreUser = self.__arrTK.createOptionMenu(self.__userGenre,var=self.__varGenre,value=self.__listGenre)
        btnValidateGenreUser = self.__arrTK.createButton(self.__userGenre,text="Valider",
                                                            ppolice = "arial" , ptaille = tailleMain,command=self.__validerUserGenre)
        btnCancelGenreUser = self.__arrTK.createButton(self.__userGenre,text="Annuler",
                                                         ppolice = "arial" , ptaille = tailleMain,command=self.__viewUser)

        labelTitleUserName = self.__arrTK.createLabel(self.__userName,text="Nom de l'utilisateur",
                                                       ppolice="Arial", ptaille=tailleTitle)
        self.__entryNameUser = self.__arrTK.createEntry(self.__userName,ppolice="Arial",ptaille=tailleMain,width=250)
        btnValidateNameUser = self.__arrTK.createButton(self.__userName,text="Valider",
                                                         ppolice = "arial" , ptaille = tailleMain,command=self.__validerUserName)
        btnCancelNameUser = self.__arrTK.createButton(self.__userName,text="Annuler",
                                                       ppolice = "arial" , ptaille = tailleMain,command=self.__viewUser)

        # Cadre Meteo
        labelTitleMainMeteo = self.__arrTK.createLabel(self.__meteoAcceuil, text="Gestion de la meteo"
                                                       ,ppolice="Arial", ptaille=tailleTitle)
        btnAddMeteoHome = self.__arrTK.createButton(self.__meteoAcceuil,text="Lieu\nTravail",
                                                    ppolice = "arial" , ptaille = tailleMain,command=self.__viewMeteoAddWork)
        btnAddMeteoWork = self.__arrTK.createButton(self.__meteoAcceuil,text="Lieu\nDomicile",
                                                    ppolice = "arial" , ptaille = tailleMain,command=self.__viewMeteoAddDomicile)
        btnAddMeteoTown = self.__arrTK.createButton(self.__meteoAcceuil,text="Autre\nVille",
                                                    ppolice = "arial" , ptaille = tailleMain,command=self.__viewMeteoAddVille)
        btnSupprMeteo = self.__arrTK.createButton(self.__meteoAcceuil,text="Supprimer\nlieu",
                                                  ppolice = "arial" , ptaille = tailleMain,command=self.__viewMeteoSuppr)

        labelTitleAddWordMeteo = self.__arrTK.createLabel(self.__meteoWork, text="Ajouter le lieu travail"
                                                          ,ppolice="Arial", ptaille=tailleTitle)
        self.__entryMeteoWork = self.__arrTK.createEntry(self.__meteoWork,ppolice="Arial",ptaille=tailleMain,width=220)
        btnAddValideMeteoWork = self.__arrTK.createButton(self.__meteoWork,text="Ajouter",
                                                        ppolice="Arial",ptaille=tailleMain,command=self.__addMeteoWork)
        btnCancelMeteoWork = self.__arrTK.createButton(self.__meteoWork,text="Annuler",
                                                       ppolice="Arial",ptaille=tailleMain,
                                                       command=lambda : self.__viewMeteo())

        labelTitleAddHomeMeteo = self.__arrTK.createLabel(self.__meteoDomicile, text="Ajouter le lieu domicile"
                                                          ,ppolice="Arial", ptaille=tailleTitle)
        self.__entryMeteoDomicile = self.__arrTK.createEntry(self.__meteoDomicile,ppolice="Arial",ptaille=tailleMain,width=220)
        btnAddMeteoDomicile = self.__arrTK.createButton(self.__meteoDomicile,text="Ajouter",
                                                        ppolice="Arial",ptaille=tailleMain,command=self.__addMeteoHome)
        btnCancelMeteoDomicile = self.__arrTK.createButton(self.__meteoDomicile,text="Annuler",
                                                           ppolice="Arial",ptaille=tailleMain,
                                                           command=lambda : self.__viewMeteo())

        labelTitleAddTwonMeteo = self.__arrTK.createLabel(self.__meteoVille, text="Ajouter une\nville pour la meteo"
                                                          ,ppolice="Arial", ptaille=tailleTitle)
        self.__entryMeteoTwon = self.__arrTK.createEntry(self.__meteoVille,ppolice="Arial",ptaille=tailleMain,width=220)
        btnAddMeteoTwon = self.__arrTK.createButton(self.__meteoVille,text="Ajouter",
                                                    ppolice="Arial",ptaille=tailleMain,command=self.__addMeteoVille)
        btnCancelMeteoTwon = self.__arrTK.createButton(self.__meteoVille,text="Annuler",
                                                       ppolice="Arial",ptaille=tailleMain,
                                                       command=lambda : self.__viewMeteo())

        labelTitleSupprMeteo = self.__arrTK.createLabel(self.__meteoSuppr, text="Supprimer un lieu\nde meteo"
                                                        ,ppolice="Arial", ptaille=tailleTitle)
        self.__menuSupprMeteo = None
        self.__labelNoMeteo = self.__arrTK.createLabel(self.__meteoSuppr, text="Aucun lieu de meteo\najouté",
                                                       ppolice="Arial",ptaille=tailleMain)
        btnValidateSupprMeteo = self.__arrTK.createButton(self.__meteoSuppr,text="Supprimer",
                                                          ppolice="Arial",ptaille=tailleMain,command=self.__supprMeteo)
        btnCancelSupprMeteo = self.__arrTK.createButton(self.__meteoSuppr,text="Annuler",
                                                          ppolice="Arial",ptaille=tailleMain,command=self.__viewMeteo)

        # Cadre GPS 
        self.__labelTitreGPS = self.__arrTK.createLabel(self.__cadreGPS, ppolice="Arial", ptaille=tailleTitle)
        self.__btnAdresseDomicile = self.__arrTK.createButton(self.__cadreGPS,text="Adresse du domicile"
                                                              ,ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreGPS(2))
        self.__btnAdresseWork = self.__arrTK.createButton(self.__cadreGPS,text="Adresse du lieu de travail"
                                                          ,ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreGPS(3))
        self.__btnvaliderGPS = self.__arrTK.createButton(self.__cadreGPS,text="Valider",ppolice = "arial" , ptaille = tailleMain)
        self.__btnretourGPS = self.__arrTK.createButton(self.__cadreGPS,text="Retour",ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreGPS(1))
        self.__btnSupprGPSDomicile = self.__arrTK.createButton(self.__cadreGPS,text="Supprimer l'adresse du domicile"
                                                               ,ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__validerGPS(2,1))
        self.__btnSupprGPSWork = self.__arrTK.createButton(self.__cadreGPS,text="Supprimer l'adresse du travail"
                                                           ,ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__validerGPS(2,2))
        self.__btnsupprGPS = self.__arrTK.createButton(self.__cadreGPS,text="Supprimer une adresse"
                                                       ,ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreGPS(4))
        self.__btnentryGPS = self.__arrTK.createEntry(self.__cadreGPS,ppolice="Arial",ptaille=tailleMain)
        # Cadre Rechecrhe
        labelTitreRecherche = self.__arrTK.createLabel(self.__cadreRecherche, text="Choisissez votre moteur\nde recherche"
                                                       , ppolice="Arial", ptaille=tailleTitle)
        menuMoteurRecherche = self.__arrTK.createOptionMenu(self.__cadreRecherche,
                                                            var = self.__varMoteurRecherce,value = self.__listMoteur)
        btnvaliderMoteur = self.__arrTK.createButton(self.__cadreRecherche,text="Valider"
                                                            ,ppolice = "arial" , ptaille = tailleMain,command=self.__validerMoteur)
        # Cadre Software 
        self.__labelTitreSoftware = self.__arrTK.createLabel(self.__cadreSoft, ppolice="Arial", ptaille=tailleTitle)
        self.__btnAnnulerSoft = self.__arrTK.createButton(self.__cadreSoft,text="Annuler",
                                                          ppolice = "arial" , ptaille = tailleMain,command=lambda:self.__affichageCadreSoft(1))

        self.__btnValiderSoftAdd = self.__arrTK.createButton(self.__cadreSoft, text="Valider",
                                                             ppolice = "arial", ptaille = tailleMain,
                                                             command=lambda : self.__addSoftware(1))

        self.__btnValiderSoftSuppr = self.__arrTK.createButton(self.__cadreSoft, text="Valider",
                                                             ppolice="arial", ptaille=tailleMain,
                                                               command=lambda : self.__supprSoft())

        self.__btnAddSoft = self.__arrTK.createButton(self.__cadreSoft,text="Ajouter un logiciel",
                                                      ppolice = "arial" , ptaille = tailleMain,command=lambda:self.__affichageCadreSoft(4))

        self.__btnSupprSoft= self.__arrTK.createButton(self.__cadreSoft,text="Supprimer un logiciel",
                                                       ppolice = "arial" , ptaille = tailleMain,command=lambda:self.__affichageCadreSoft(3))

        self.__btnListSoft = self.__arrTK.createButton(self.__cadreSoft,text="Liste des logiciels",
                                                         ppolice = "arial" , ptaille = tailleMain,command=lambda:self.__affichageCadreSoft(5))

        self.__menuSupprSoft = self.__arrTK.createOptionMenu(self.__cadreSoft,var = self.__varSupprSoft,value = ["",""])

        self.__entryNameSoft = self.__arrTK.createEntry(self.__cadreSoft,ppolice="Arial",ptaille=15)

        self.__btnTypeSoftNormal = self.__arrTK.createButton(self.__cadreSoft,text="Normal",ppolice="arial",ptaille=tailleMain,
                                                             command=lambda : self.__affichageCadreSoft(2))
        self.__btnTypeSoftPresentation = self.__arrTK.createButton(self.__cadreSoft, text="Presentation", ppolice="arial", ptaille=tailleMain,
                                                                   command=lambda : self.__addSoftware(2))
        self.__btnTypeSoftNavigateur = self.__arrTK.createButton(self.__cadreSoft, text="Navigateur Internet", ppolice="arial", ptaille=tailleMain,
                                                                 command=lambda : self.__addSoftware(3))
        self.__btnTypeSoftNote = self.__arrTK.createButton(self.__cadreSoft, text="Note", ppolice="arial", ptaille=tailleMain,
                                                           command=lambda : self.__addSoftware(4))
        self.__btnTypeSoftMusique = self.__arrTK.createButton(self.__cadreSoft, text="Musique", ppolice="arial", ptaille=tailleMain,
                                                              command=lambda : self.__addSoftware(5))
        self.__btnRetourTypeSoft = self.__arrTK.createButton(self.__cadreSoft,text="Retour",ppolice="arial",ptaille=tailleMain,
                                                             command=lambda:self.__affichageCadreSoft(1))

        self.__textListSoft = ctk.CTkTextbox(self.__cadreSoft, width=300, height=550,wrap="word",
                                             state="normal", font=("Arial", 14))
        self.__btnRetourListeSoft = self.__arrTK.createButton(self.__cadreSoft,text="Retour",ppolice="arial",ptaille=tailleMain
                                                              ,command=lambda:self.__affichageCadreSoft(1))

        # Cadre Internet
        self.__labelTitreInternet = self.__arrTK.createLabel(self.__cadreInternet, ppolice="Arial", ptaille=tailleTitle)
        self.__btnAddSite = self.__arrTK.createButton(self.__cadreInternet,text="Enregister un site",
                                                      ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreSite(2))
        self.__btnSupprSite = self.__arrTK.createButton(self.__cadreInternet,text="Supprimer un site",
                                                        ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreSite(3))
        self.__btnAnnulerInternet = self.__arrTK.createButton(self.__cadreInternet,text="Annuler",
                                                              ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreSite(1))
        self.__btnValiderInternet = self.__arrTK.createButton(self.__cadreInternet,text="Valider",
                                                              ppolice = "arial" , ptaille = tailleMain)
        self.__entryNameSite = self.__arrTK.createEntry(self.__cadreInternet,ppolice="Arial",ptaille=tailleMain)
        self.__entryLinkSite = self.__arrTK.createEntry(self.__cadreInternet,ppolice="Arial",ptaille=tailleMain)
        self.__menuChoixSite =  self.__arrTK.createOptionMenu(self.__cadreInternet,var = self.__varChoixSite,value = listChoixSite)
        self.__menuSupprSite =  self.__arrTK.createOptionMenu(self.__cadreInternet,var = self.__varSupprSite,value=listChoixSite)
        # Cardre theme 
        labelTitreTheme = self.__arrTK.createLabel(self.__cadreTheme, text="Choix du thème\nde l'interface"
                                                   , ppolice="Arial", ptaille=tailleTitle)
        menuChoixTheme = self.__arrTK.createOptionMenu(self.__cadreTheme,var = self.__varChoixTheme,value=listeTheme)
        btnValiderTheme = self.__arrTK.createButton (self.__cadreTheme,text="Valider",
                                                            ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__validerTheme(1))
        # Cadre Micro
        labelTitreMicro = self.__arrTK.createLabel(self.__cadreMicro, text="Sons au déclenchement\ndu micro",
                                                   ppolice="Arial", ptaille=tailleTitle)
        menuChoixMicro = self.__arrTK.createOptionMenu(self.__cadreMicro,
                                                              var = self.__varChoixMicro,value=self.__listChoixMicro)
        btnValiderMicro = self.__arrTK.createButton (self.__cadreMicro,text="Valider"
                                                            ,ppolice = "arial" , ptaille = tailleMain,command=self.__validerMicro)


        # Cader Work folder
        self.__labelTitreArreraWork = self.__arrTK.createLabel(self.__cadreArreraWork,
                                                               text="Choisir le dossier\npour Arrera Work",
                                                               ppolice="Arial", ptaille=tailleTitle)
        self.__btnFolderArreraWork = self.__arrTK.createButton(self.__cadreArreraWork, text="Choisir le dossier",
                                                               ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__validerFolderWork(1))
        self.__btnSupprArreraWork = self.__arrTK.createButton(self.__cadreArreraWork, text="Supprimer le dossier",
                                                              ppolice = "arial" , ptaille = tailleMain,command = lambda : self.__validerFolderWork(2))
        # Cadre Download folder
        self.__labelTitreDownload = self.__arrTK.createLabel(self.__cadreVideoDownload,
                                                             text="Choisir le dossier pour\nArrera video download",
                                                             ppolice="Arial", ptaille=tailleTitle)
        self.__btnFolderDownload = self.__arrTK.createButton(self.__cadreVideoDownload, text="Choisir le dossier",
                                                             ppolice = "arial" , ptaille = tailleMain,command = lambda : self.__validerFolderDownload(1))
        self.__btnSupprDownload = self.__arrTK.createButton(self.__cadreVideoDownload, text="Supprimer le dossier",
                                                            ppolice = "arial" , ptaille = tailleMain,command = lambda : self.__validerFolderDownload(2))
        # Placement widget
        self.__arrTK.placeTopCenter(labelTitreMenu)
        
        boutonMenu[0].place(relx=0.0,y=50)
        boutonMenu[1].place(relx=0.0,y=100)
        boutonMenu[2].place(relx=0.0,y=150)
        boutonMenu[3].place(relx=0.0,y=200)
        boutonMenu[4].place(relx=0.0,y=250)
        boutonMenu[5].place(relx=0.0,y=300)
        boutonMenu[6].place(relx=0.0,y=350)
        boutonMenu[7].place(relx=0.0,y=400)
        boutonMenu[8].place(relx=0.0,y=450)
        boutonMenu[9].place(relx=0.0,y=500)

        self.__arrTK.placeTopCenter(self.__labelTitreGPS)

        self.__arrTK.placeTopCenter(labelTitreRecherche)
        self.__arrTK.placeCenter(menuMoteurRecherche)
        self.__arrTK.placeBottomCenter(btnvaliderMoteur)

        self.__arrTK.placeTopCenter(self.__labelTitreSoftware)

        self.__arrTK.placeTopCenter(self.__labelTitreInternet)

        self.__arrTK.placeTopCenter(labelTitreTheme)
        self.__arrTK.placeCenter(menuChoixTheme)
        self.__arrTK.placeBottomCenter(btnValiderTheme)

        self.__arrTK.placeTopCenter(labelTitreMicro)
        self.__arrTK.placeCenter(menuChoixMicro)
        self.__arrTK.placeBottomCenter(btnValiderMicro)

        self.__arrTK.placeTopCenter(self.__labelTitreDownload)
        self.__arrTK.placeTopCenter(self.__labelTitreArreraWork)


        for index, bouton in enumerate(self.__boutonMenuMain):
            x = startX + (index % 3) * spacingHorizontal  # Calculer la position X (colonne pour 3 boutons par ligne)
            y = startY + (index // 3) * spacingVertical # Calculer la position Y (ligne)
            bouton.place(x=x, y=y)

        if (jsonSetting.lectureJSON("gestionMicro")=="1"):
            boutonMenu[10].place(relx=0.0,y=550)
        else :
            self.__boutonMenuMain[10].place_forget()

        # Cadre Meteo
        self.__arrTK.placeTopCenter(labelTitleMainMeteo)
        self.__arrTK.placeCenterOnWidth(btnAddMeteoHome,100)
        self.__arrTK.placeCenterOnWidth(btnAddMeteoWork,200)
        self.__arrTK.placeCenterOnWidth(btnAddMeteoTown,300)
        self.__arrTK.placeCenterOnWidth(btnSupprMeteo,400)

        self.__arrTK.placeTopCenter(labelTitleAddHomeMeteo)
        self.__arrTK.placeCenter(self.__entryMeteoDomicile)
        self.__arrTK.placeLeftBottom(btnCancelMeteoDomicile)
        self.__arrTK.placeRightBottom(btnAddMeteoDomicile)

        self.__arrTK.placeTopCenter(labelTitleAddWordMeteo)
        self.__arrTK.placeCenter(self.__entryMeteoWork)
        self.__arrTK.placeLeftBottom(btnCancelMeteoWork)
        self.__arrTK.placeRightBottom(btnAddValideMeteoWork)

        self.__arrTK.placeTopCenter(labelTitleAddTwonMeteo)
        self.__arrTK.placeCenter(self.__entryMeteoTwon)
        self.__arrTK.placeLeftBottom(btnCancelMeteoTwon)
        self.__arrTK.placeRightBottom(btnAddMeteoTwon)

        self.__arrTK.placeTopCenter(labelTitleSupprMeteo)
        self.__arrTK.placeLeftBottom(btnCancelSupprMeteo)
        self.__arrTK.placeRightBottom(btnValidateSupprMeteo)

        self.__arrTK.placeTopCenter(labelTitleUserAcceuil)
        self.__arrTK.placeCenterOnWidth(btnName,100)
        self.__arrTK.placeCenterOnWidth(btnGenre,200)

        self.__arrTK.placeTopCenter(labelTitleUserGenre)
        self.__arrTK.placeCenter(menuSelectGenreUser)
        self.__arrTK.placeLeftBottom(btnCancelGenreUser)
        self.__arrTK.placeRightBottom(btnValidateGenreUser)

        self.__arrTK.placeTopCenter(labelTitleUserName)
        self.__arrTK.placeCenter(self.__entryNameUser)
        self.__arrTK.placeLeftBottom(btnCancelNameUser)
        self.__arrTK.placeRightBottom(btnValidateNameUser)

    def active(self):
        self.__arrTK.setResizable(False)
        self.__arrTK.setGeometry(500,630)
        self.__mainFrame.pack()

    def passQUITFNC(self,quitFNC):
        self.__btnQuitMainFrame.configure(command=lambda : self.__fncQuit(quitFNC))
        self.__arrTK.placeBottomCenter(self.__btnQuitMainFrame)

    def __fncQuit(self,quitFnc):
        self.__disableAllFrame()
        self.__cadreMenu.pack_forget()
        quitFnc()

    def __backAcceuil(self):
        self.__mainFrame.pack()
        self.__cadreMenu.pack_forget()
        self.__cadreUser.pack_forget()
        self.__cadreMeteo.pack_forget()
        self.__cadreGPS.pack_forget()
        self.__cadreRecherche.pack_forget()
        self.__cadreSoft.pack_forget()
        self.__cadreInternet.pack_forget()
        self.__cadreTheme.pack_forget()
        self.__cadreMicro.pack_forget()
        self.__cadreArreraWork.pack_forget()
        self.__cadreVideoDownload.pack_forget()
    
    def __disableAllFrame(self):
        self.__mainFrame.pack_forget()
        self.__cadreUser.pack_forget()
        self.__cadreMeteo.pack_forget()
        self.__cadreGPS.pack_forget()
        self.__cadreRecherche.pack_forget()
        self.__cadreSoft.pack_forget()
        self.__cadreInternet.pack_forget()
        self.__cadreTheme.pack_forget()
        self.__cadreMicro.pack_forget()
        self.__cadreArreraWork.pack_forget()
        self.__cadreVideoDownload.pack_forget()
        self.__cadreMenu.pack(side="left")
    
    def __showUserFrame(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreUser)
        self.__viewUser()
    
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
       

    def __viewUser(self):
        self.__arrTK.placeCenter(self.__userAcceuil)
        self.__userName.place_forget()
        self.__userGenre.place_forget()

    def __viewUserName(self):
        self.__entryNameUser.delete(0,END)
        self.__arrTK.placeCenter(self.__userName)
        self.__userAcceuil.place_forget()
        self.__userGenre.place_forget()

    def __viewUserGenre(self):
        self.__varGenre.set(self.__listGenre[0])
        self.__arrTK.placeCenter(self.__userGenre)
        self.__userAcceuil.place_forget()
        self.__userName.place_forget()
    
    def __validerUserName(self):
        name = self.__entryNameUser.get()
        self.__entryNameUser.delete(0,END)
        if (name == ""):
            showerror("Parametre","Impossible d'enregistrer un nom vide")
        else :
            self.__gazelle.changeUserName(name)
            showinfo("Parametre","Nom enregistré")
        self.__viewUser()

    def __validerUserGenre(self):
        genre = self.__varGenre.get()
        self.__gazelle.changeUserGenre(genre)
        showinfo("Parametre","Nom enregistré")
        self.__viewUser()


    def __viewMeteo(self):
        self.__disableAllFrame()
        self.__meteoDomicile.place_forget()
        self.__meteoWork.place_forget()
        self.__meteoVille.place_forget()
        self.__meteoSuppr.place_forget()
        self.__arrTK.packRight(self.__cadreMeteo)
        self.__arrTK.placeTopCenter(self.__meteoAcceuil)

    def __viewMeteoAddDomicile(self):
        self.__meteoAcceuil.place_forget()
        self.__arrTK.placeCenter(self.__meteoDomicile)

    def __viewMeteoAddWork(self):
        self.__meteoAcceuil.place_forget()
        self.__arrTK.placeCenter(self.__meteoWork)

    def __viewMeteoAddVille(self):
        self.__meteoAcceuil.place_forget()
        self.__arrTK.placeCenter(self.__meteoVille)

    def __viewMeteoSuppr(self):
        self.__meteoAcceuil.place_forget()
        self.__arrTK.placeCenter(self.__meteoSuppr)
        listVille = self.__gazelle.getMeteoSave()
        self.__labelNoMeteo.place_forget()
        self.__menuSupprMeteo = None
        if len(listVille) == 0:
            self.__arrTK.placeCenter(self.__labelNoMeteo)
        else :
            self.__menuSupprMeteo = self.__arrTK.createOptionMenu(self.__meteoSuppr,
                                                                  var = self.__varChoixSupprMeteo,
                                                                  value = listVille)
            self.__arrTK.placeCenter(self.__menuSupprMeteo)
    
    def __addMeteoHome(self):
        home = self.__entryMeteoDomicile.get()
        if (home==""):
            showerror("Parametre","Impossible d'enregistrer une ville vide")
        else :
            self.__entryMeteoDomicile.delete(0,END)
            if (self.__gazelle.ajoutVilleMeteo(1,home) == False):
                showerror("Parametre","Impossible d'enregistrer cette ville")
            else :
                showinfo("Parametre","Ville enregistré")
                self.__viewMeteo()

    def __addMeteoWork(self):
        work = self.__entryMeteoWork.get()
        if (work== ""):
            showerror("Parametre","Impossible d'enregistrer une ville vide")
        else :
            self.__entryMeteoWork.delete(0,END)
            if (self.__gazelle.ajoutVilleMeteo(2, work) == False):
                showerror("Parametre","Impossible d'enregistrer cette ville")
            else :
                showinfo("Parametre","Ville enregistré")
                self.__viewMeteo()

    def __addMeteoVille(self):
        twon = self.__entryMeteoTwon.get()
        if (twon== ""):
            showerror("Parametre","Impossible d'enregistrer une ville vide")
        else :
            self.__entryMeteoTwon.delete(0,END)
            if (self.__gazelle.ajoutVilleMeteo(3, twon) == False):
                showerror("Parametre","Impossible d'enregistrer cette ville")
            else :
                showinfo("Parametre","Ville enregistré")
                self.__viewMeteo()

    def __supprMeteo(self):
        ville = self.__varChoixSupprMeteo.get()
        if (ville == ""):
            showerror("Parametre","Impossible de supprimer une ville vide")
        else :
            if (self.__gazelle.supprVilleMeteo(3,ville) == False):
                showerror("Parametre","Impossible de supprimer cette ville")
            else :
                showinfo("Parametre","Ville supprimé")

        self.__menuSupprMeteo.place_forget()
        self.__menuSupprMeteo = None
        self.__viewMeteo()
    
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
                    messagebox.showerror("Parametre","Il n'a aucune adresse enregistrée")
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
                    showerror("Parametre","Entrer une adresse pour l'enregistrer")
                else :
                    self.__gazelle.ajoutGPSAdresse(type,adresse)
                    self.__btnentryGPS.delete(0,END)
                self.__affichageCadreGPS(1)
            case 2 : 
                self.__gazelle.supprGPSAdresse(type)
                self.__affichageCadreGPS(1)
    
    def __validerMoteur(self):
        moteur = self.__varMoteurRecherce.get()
        if (self.__gazelle.changeMoteur(moteur)):
            showinfo("Parametre","Moteur enregistré")
        else :
            showerror("Parametre","Impossible d'enregistrer le moteur")
        self.__backAcceuil()

    def __affichageCadreSoft(self,mode:int):
        """
        1 : Acceuil 
        2 : Add
        3 : Suppr
        """
        self.__btnTypeSoftNormal.place_forget()
        self.__btnTypeSoftPresentation.place_forget()
        self.__btnTypeSoftNavigateur.place_forget()
        self.__btnTypeSoftNote.place_forget()
        self.__btnTypeSoftMusique.place_forget()
        self.__btnRetourTypeSoft.place_forget()
        self.__menuSupprSoft.place_forget()
        self.__entryNameSoft.place_forget()
        self.__btnAddSoft.place_forget()
        self.__btnSupprSoft.place_forget()
        self.__menuSupprSoft.place_forget()
        self.__btnAddSoft.place_forget()
        self.__btnSupprSoft.place_forget()
        self.__entryNameSoft.place_forget()
        self.__btnValiderSoftAdd.place_forget()
        self.__btnValiderSoftSuppr.place_forget()
        self.__textListSoft.place_forget()
        self.__btnRetourListeSoft.place_forget()
        self.__btnListSoft.place_forget()
        match mode : 
            case 1 :
                self.__labelTitreSoftware.configure(text="Gestion des logiciels")
                self.__btnAnnulerSoft.place_forget()
                self.__btnAddSoft.place(relx=0.5, y=200, anchor="n")
                self.__btnSupprSoft.place(relx=0.5, y=275, anchor="n")
                self.__btnListSoft.place(relx=0.5, y=350, anchor="n")

            case 2 :
                self.__labelTitreSoftware.configure(text="Ajout de logiciels")
                self.__btnAnnulerSoft.place(relx=0, rely=1, anchor='sw')
                self.__btnValiderSoftAdd.place(relx=1, rely=1, anchor='se')
                self.__entryNameSoft.place(relx=0.5, rely=0.5, anchor="center")

            case 3 :

                listSoft = self.__gazelle.getListSoft()
                if (len(listSoft)==0):
                    showerror("Parametre","Impossible de supprimer des logiciels avant d'en ajoute")
                    return
                del self.__menuSupprSoft
                self.__menuSupprSoft = self.__arrTK.createOptionMenu(self.__cadreSoft,var=self.__varSupprSoft,value=listSoft)
                self.__labelTitreSoftware.configure(text="Suppression de logiciel")
                self.__btnAnnulerSoft.place(relx=0, rely=1, anchor='sw')
                self.__btnValiderSoftSuppr.place(relx=1, rely=1, anchor='se')
                self.__menuSupprSoft.place(relx=0.5, rely=0.5, anchor="center")

            case 4 :
                self.__labelTitreSoftware.configure(text="Type du logiciel ajouter")
                self.__btnTypeSoftNormal.place(relx=0.5, y=100, anchor="n")
                self.__btnTypeSoftPresentation.place(relx=0.5, y=150, anchor="n")
                self.__btnTypeSoftNavigateur.place(relx=0.5, y=200, anchor="n")
                self.__btnTypeSoftNote.place(relx=0.5, y=250, anchor="n")
                self.__btnTypeSoftMusique.place(relx=0.5, y=300, anchor="n")
                self.__arrTK.placeBottomCenter(self.__btnRetourTypeSoft)

            case 5 :
                self.__labelTitreSoftware.configure(text="Liste des logiciels")
                listSoft = self.__gazelle.getListSoft()
                if (len(listSoft)==0):
                    messagebox.showerror("Parametre","Aucun logiciel enregistré")
                else :
                    self.__textListSoft.delete(1.0,END)
                    self.__textListSoft.configure(state="normal")
                    for i in range(0, len(listSoft)):
                        self.__textListSoft.insert(END, listSoft[i] + "\n")
                    self.__textListSoft.configure(state="disabled")

                self.__arrTK.placeCenter(self.__textListSoft)
                self.__arrTK.placeBottomCenter(self.__btnRetourListeSoft)


    def __addSoftware(self, mode:int):
        """
        1 : normal
        2 : Presentation
        3 : Navigateur
        4 : Note
        5 : Musique
        """
        match mode:
            case 1 :
                soft = self.__entryNameSoft.get()
                if (soft==""):
                    showerror("Parametre","Impossible d'ajouter un logiciel sans nom")
                else :
                    self.__gazelle.addSoft(1,soft)
                    showinfo("Parametre","Logiciel ajouté")
                    self.__entryNameSoft.delete(0,END)
            case 2:
                self.__gazelle.addSoft(2, "presentation")
            case 3:
                self.__gazelle.addSoft(3, "navigateur")
            case 4:
                self.__gazelle.addSoft(4, "musique")
            case 5:
                self.__gazelle.addSoft(5, "note")
        self.__affichageCadreSoft(1)

    def __supprSoft(self):
        soft = self.__varSupprSoft.get()
        if (soft == "Presentation"):
            self.__gazelle.supprSoft(2, "")
        else:
            if (soft == "Navigateur internet"):
                self.__gazelle.supprSoft(3, "")
            else:
                if (soft == "Note"):
                    self.__gazelle.supprSoft(5, "")
                else:
                    if (soft == "Musique"):
                        self.__gazelle.supprSoft(4, "")
                    else:
                        self.__gazelle.supprSoft(1, soft)
        self.__affichageCadreSoft(1)

    
    def __affichageCadreSite(self,mode:int):
        """
        1 : Acceuil
        2 : Add
        3 : Suppr
        """
        match mode :
            case 1 :
                self.__labelTitreInternet.configure(text="Gestion des sites\nInternet")
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
                    showerror("Parametre","Aucun site enregistré")
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
                            showerror("Parametre","Impossible d'enregistrer un site sans nom")
                        else :
                            self.__gazelle.addSite(1,name,link)
                            showinfo("Parametre","Site enregistré")
                            self.__affichageCadreSite(1)
                else :
                    showerror("Parametre","Impossible d'enregistrer un site sans URL")
                
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
            case other :
                return
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

    def __showArreraWorkFolder(self):
        folderExist = self.__gazelle.workFolderExist()
        self.__disableAllFrame()
        self.__btnSupprArreraWork.place_forget()
        self.__btnFolderArreraWork.place_forget()
        self.__arrTK.packRight(self.__cadreArreraWork)
        if folderExist :
            self.__arrTK.placeCenter(self.__btnSupprArreraWork)
        else :
            self.__arrTK.placeCenter(self.__btnFolderArreraWork)

    def __showArreraDownloadFolder(self):
        print("test")
        folderExist = self.__gazelle.downloadFolderExist()
        self.__disableAllFrame()
        self.__btnSupprDownload.place_forget()
        self.__btnFolderDownload.place_forget()
        self.__arrTK.packRight(self.__cadreVideoDownload)
        if folderExist :
            self.__arrTK.placeCenter(self.__btnSupprDownload)
        else :
            self.__arrTK.placeCenter(self.__btnFolderDownload)

    def __validerFolderWork(self,mode : int ):
        """
        1 : add
        2 : suppr
        """
        self.__backAcceuil()

        match mode :
            case 1 :
                self.__gazelle.setWorkFolder()
            case 2 :
                self.__gazelle.supprWorkFolder()

    def __validerFolderDownload(self,mode : int ):
        """
        1 : add
        2 : suppr
        """
        self.__backAcceuil()

        match mode :
            case 1 :
                self.__gazelle.setVideoDownloadFolder()
            case 2 :
                self.__gazelle.supprVideoDownloadFolder()

    def passApropos(self,aproposFNC):
        self.__boutonMenuMain[0].configure(command=aproposFNC)