from lib.arrera_tk import *
from tkinter import messagebox
from typing import Union
import threading as th
from lib.travailJSON import *
from gestionnaire.gestUserSetting import gestUserSetting

class CArreraGazelleUISix :
    def __init__(self,windows:Union[aTk,aTopLevel],gestUser:gestUserSetting):
        # Ouverture de l'objet
        self.__gazelle = None
        # Var qui contient les thead
        self.__threadSaveVoicePrint = th.Thread()

        # Mise de la fenetre dans un atribut
        self.__windows = windows
        # Declaration des cardre
        self.__mainCadre = aFrame(self.__windows,width=500,height=400)

        self.__userFrame = aFrame(self.__windows,width=500,height=330)
        self.__userAcceuil = aFrame(self.__userFrame,width=500,height=330)
        self.__userName = aFrame(self.__userFrame,width=500,height=330)
        self.__userGenre = aFrame(self.__userFrame,width=500,height=330)

        self.__meteoGPSFrame = aFrame(self.__windows,width=500,height=330)

        self.__meteoFrame = aFrame(self.__windows,width=500,height=330)
        self.__meteoAcceuil = aFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoDomicile = aFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoTravail = aFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoVille = aFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoSuppr = aFrame(self.__meteoFrame,width=500,height=330)

        self.__gpsFrame = aFrame(self.__windows,width=500,height=330)
        self.__gpsAcceuil = aFrame(self.__gpsFrame,width=500,height=330)
        self.__gpsDomicile = aFrame(self.__gpsFrame,width=500,height=330)
        self.__gpsTravail = aFrame(self.__gpsFrame,width=500,height=330)
        self.__gpsSuppr = aFrame(self.__gpsFrame,width=500,height=330)

        self.__rechercheFrame = aFrame(self.__windows,width=500,height=330)

        self.__softFrame = aFrame(self.__windows,width=500,height=330)
        self.__softAcceuil = aFrame(self.__softFrame,width=500,height=330)
        self.__softAdd = aFrame(self.__softFrame,width=500,height=330)
        self.__softSuppr = aFrame(self.__softFrame,width=500,height=330)
        self.__softListe = aFrame(self.__softFrame,width=500,height=330)

        self.__internetFrame = aFrame(self.__windows,width=500,height=330)
        self.__internetAcceuil = aFrame(self.__internetFrame,width=500,height=330)
        self.__internetSiteWeb = aFrame(self.__internetFrame,width=500,height=330)
        self.__internetSupprSite = aFrame(self.__internetFrame,width=500,height=330)
        self.__internetListeSite = aFrame(self.__internetFrame,width=500,height=330)

        self.__themeFrame = aFrame(self.__windows,width=500,height=330)

        self.__microFrame = aFrame(self.__windows,width=500,height=330)
        self.__microAcceuil = aFrame(self.__microFrame,width=500,height=330)
        self.__microSound = aFrame(self.__microFrame,width=500,height=330)
        self.__microTigerWord = aFrame(self.__microFrame,width=500,height=330)
        self.__microVoicePrint = aFrame(self.__microFrame,width=500,height=330)
        self.__microDuringSave = aFrame(self.__microFrame,width=500,height=330)
        self.__microViewSave = aFrame(self.__microFrame,width=500,height=330)
        self.__microViewWordSave = aFrame(self.__microFrame,width=500,height=330)

        self.__arreraWorkFrame = aFrame(self.__windows,width=500,height=330)

        self.__arreraDownloadFrame = aFrame(self.__windows, width=500, height=330)

        self.__backFrame = aFrame(self.__windows,width=500,height=70)

        # Variable
        # Taille Police
        taillePolice = 20
        # Liste
        listGenre = ["",""]#jsonSetting.lectureJSONList("listGenre")
        listMoteurRecherche = ["",""]#jsonSetting.lectureJSONList("listMoteurRecherche")
        self.__listTheme = ["",""]#jsonSetting.lectureJSONList("listeTheme")
        # Icon Assistant
        iconAssistant = aImage(path_light="asset/logo-six.png",width=95,height=95)
        # String var
        self.__varNameUser = StringVar(self.__windows)
        self.__varSupprMeteo = StringVar(self.__windows)
        self.__varSupprGPS = StringVar(self.__windows)
        self.__varMoteurRecherche = StringVar(self.__windows)
        self.__varSupprSoft = StringVar(self.__windows)
        self.__varSupprWeb = StringVar(self.__windows)
        # Widget
        # Main frame
        self.__btnIcon = aButton(self.__mainCadre,image=iconAssistant,text="",corner_radius=8,width=95,height=95)
        btnAcceuilUser = aButton(self.__mainCadre, width=100, height=100, text="Utilisateur"
                                                   ,command= lambda  : self.__viewUserAcceuil())
        btnAcceuilMeteoAndGPS = aButton(self.__mainCadre,width=100,height=100,text="Meteo"
                                                    ,command=lambda:self.__viewGPSMeteo())
        btnAcceuilIA = aButton(self.__mainCadre,width=100,height=100,text="IA"
                                                  ,command=lambda : self.__viewGPSAcceuil())
        btnAcceuilRecherche = aButton(self.__mainCadre,width=100,height=100,text="Recherche"
                                                        ,command=lambda:self.__viewRecherche())
        btnAcceuilLogiciel = aButton(self.__mainCadre,width=100,height=100,text="Logiciel"
                                                       ,command=lambda:self.__viewSoftAcceuil())
        btnAcceuilInternet = aButton(self.__mainCadre,width=100,height=100,text="Internet"
                                                       ,command=lambda:self.__viewInternetAcceuil())
        btnAcceuilGps = aButton(self.__mainCadre,width=100,height=100,text="GPS"
                                                    ,command=lambda:self.__viewTheme())
        btnAcceuilArreraWork = aButton(self.__mainCadre,width=100,height=100
                                                         ,text="Arrera\nWork",
                                       command=lambda:self.__viewArreraWork())
        btnAcceuilDownload = aButton(self.__mainCadre,width=100,height=100
                                                       ,text="Arrera\nDownload",
                                                       command=lambda:self.__viewArreraDownload())
        btnAcceuilMicro = aButton(self.__mainCadre,width=100,height=100
                                                    ,text="Micro",
                                                    command=lambda:self.__viewMicroAcceuil())
        self.__btnRetourAssistant = aButton(self.__mainCadre,width=100,
                                                              height=100,text="Retour")

        # backFrame
        retourAcceuilBTN = aButton(self.__backFrame,text="Retour Acceuil"
                                                     ,command=lambda:self.__backAcceuil())


        # userFrame
        # Label
        labelTitleUser = [aLabel(self.__userAcceuil,text="Gestion utilisateur"),
                          aLabel(self.__userName,text="Nom de l'utilisateur"),
                          aLabel(self.__userGenre,text="Genre de l'utilisateur")]
        # Button
        btnUserName = aButton(self.__userAcceuil,text="Nom\nde\nl'utilisateur",
                                                command=lambda:self.__viewUserName())
        btnUserGenre = aButton(self.__userAcceuil,text="Genre\nde\nl'utilisateur",
                                                 command=lambda:self.__viewUserGenre())
        btnValiderUserName = aButton(self.__userName,text="Valider",
                                                       command=lambda:self.__saveUserName())
        btnValiderUserGenre = aButton(self.__userGenre,text="Valider",
                                                        command=lambda:self.__saveUserGenre())
        btnRetourUserName = aButton(self.__userName, text="Retour",
                                                      command=lambda:self.__viewUserAcceuil())
        btnRetourUserGenre = aButton(self.__userGenre, text="Retour",
                                                       command=lambda:self.__viewUserAcceuil())
        # entry
        self.__entryNameUser = aEntry(self.__userName, width=200)
        # option menu
        menuUserGenre = aOptionMenu(self.__userGenre,value = listGenre)

        # Meteo GPS Frame

        lTitleGPSAndMeteo = aLabel(self.__meteoGPSFrame,text="Meteo & GPS")

        btnViewMeteo = aButton(self.__meteoGPSFrame,text="Meteo",width=100,height=100,
                                                    command=lambda:self.__viewMeteoAcceuil())
        btnViewGPS = aButton(self.__meteoGPSFrame,text="GPS",width=100,height=100,
                                                    command=lambda:self.__viewGPSAcceuil())

        # meteoFrame
        # Label
        labelTitleMeteo = [aLabel(self.__meteoAcceuil,text="Gestion de meteo"),
                           aLabel(self.__meteoDomicile,text="Lieu Domicile"),
                           aLabel(self.__meteoTravail,text="Lieu Travail"),
                           aLabel(self.__meteoVille,text="Autre Ville"),
                           aLabel(self.__meteoSuppr,text="Supprimer Lieu")]
        # Button
        btnAcceuilMeteoDomicile = aButton(self.__meteoAcceuil,text="Lieu\nDomicile",
                                                       command=lambda:self.__viewMeteoDomicile())
        btnAcceuilMeteoTravail = aButton(self.__meteoAcceuil,text="Lieu\nTravail",
                                                      command=lambda:self.__viewMeteoTravail())
        btnAcceuiMeteolVille = aButton(self.__meteoAcceuil,text="Autre\nVille",
                                                    command=lambda:self.__viewMeteoVille())
        btnAcceuilMeteoSuppr = aButton(self.__meteoAcceuil,text="Supprimer un lieu",
                                                    command=lambda:self.__viewMeteoSuppr())

        btnValiderMeteoDomicile = aButton(self.__meteoDomicile,text="Valider",
                                                            command=lambda:self.__saveMeteoDomicile())
        btnValiderMeteoTravail = aButton(self.__meteoTravail,text="Valider",
                                                           command=lambda:self.__saveMeteoTravail())
        btnValiderMeteoVille = aButton(self.__meteoVille,text="Valider",
                                                         command=lambda:self.__saveMeteoVille())
        btnValiderMeteoSuppr = aButton(self.__meteoSuppr,text="Supprimer",
                                                         command=lambda:self.__supprMeteoVille())

        btnRetourMeteoDomicile = aButton(self.__meteoDomicile,text="Retour",
                                                           command=lambda:self.__viewMeteoAcceuil())
        btnRetourMeteoTravail = aButton(self.__meteoTravail,text="Retour",
                                                          command=lambda:self.__viewMeteoAcceuil())
        btnRetourMeteoVille = aButton(self.__meteoVille,text="Retour",
                                                        command=lambda:self.__viewMeteoAcceuil())
        btnRetourMeteoSuppr = aButton(self.__meteoSuppr,text="Retour",
                                                        command=lambda:self.__viewMeteoAcceuil())
        # entry
        self.__entryMeteoDomicile = aEntry(self.__meteoDomicile, width=300)
        self.__entryMeteoTravail = aEntry(self.__meteoTravail, width=300)
        self.__entryMeteoVille = aEntry(self.__meteoVille, width=300)
        #option menu
        self.__menuMeteoSuppr = aOptionMenu(self.__meteoSuppr, value = ["", ""])

        # GPS Frame
        # Label
        labelTitleGPS = [aLabel(self.__gpsAcceuil,text="Gestion GPS"),
                         aLabel(self.__gpsDomicile,text="Lieu Domicile"),
                         aLabel(self.__gpsTravail,text="Lieu Travail"),
                         aLabel(self.__gpsSuppr,text="Supprimer Lieu")]
        # Button
        btnAcceuilGPSDomicile = aButton(self.__gpsAcceuil,text="Lieu\nDomicile",
                                                          command=lambda:self.__viewGPSDomicile())
        btnAcceuilGPSTravail = aButton(self.__gpsAcceuil,text="Lieu\nTravail",
                                                         command=lambda:self.__viewGPSTravail())
        btnAcceuilGPSSuppr = aButton(self.__gpsAcceuil,text="Supprimer\nun lieu",
                                                       command=lambda:self.__viewGPSSuppr())

        btnValiderGPSDomicile = aButton(self.__gpsDomicile,text="Valider",
                                                          command=lambda:self.__saveGPSDomicile())
        btnValiderGPSTravail = aButton(self.__gpsTravail,text="Valider",
                                                         command=lambda:self.__saveGPSTravail())
        btnValiderGPSSuppr = aButton(self.__gpsSuppr,text="Supprimer",
                                                       command=lambda:self.__supprGPSAdresse())

        btnRetourGPSDomicile = aButton(self.__gpsDomicile,text="Retour",
                                                         command=lambda:self.__viewGPSAcceuil())
        btnRetourGPSTravail = aButton(self.__gpsTravail,text="Retour",
                                                        command=lambda:self.__viewGPSAcceuil())
        btnRetourGPSSuppr = aButton(self.__gpsSuppr,text="Retour",
                                                      command=lambda:self.__viewGPSAcceuil())

        # entry
        self.__entryGPSDomicile = aEntry(self.__gpsDomicile, width=300)
        self.__entryGPSTravail = aEntry(self.__gpsTravail, width=300)
        #option menu
        self.__menuGPSSuppr = aOptionMenu(self.__gpsSuppr, value = ["", ""])

        # Recherche Frame
        # Label
        labelTitleRecherche = aLabel(self.__rechercheFrame,text="Gestion du moteur de recherche")
        # Button
        btnValiderRecherche = aButton(self.__rechercheFrame,text="Valider",
                                                        command=lambda:self.__saveRecherche())
        # Option Menu
        menuMoteurRecherche = aOptionMenu(self.__rechercheFrame,value = listMoteurRecherche)

        # Soft Frame
        # Label
        labelTitleSoft = [aLabel(self.__softAcceuil,text="Gestion des logiciels"),
                          aLabel(self.__softAdd,text="Nom du logiciel ajouter"),
                          aLabel(self.__softSuppr,text="Suppression logiciel"),
                          aLabel(self.__softListe,text="Liste de logiciel enregistrée")]

        self.__listSoftware = aText(self.__softListe, width=450, height=250,
                                             wrap="word", state="normal")

        # Button
        btnAcceuilSoftAdd = aButton(self.__softAcceuil,text="Ajout\nlogiciel"
                                                      ,command=lambda:self.__viewSoftAdd())
        btnAcceuilSoftSuppr = aButton(self.__softAcceuil,text="Suppression\nlogiciel"
                                                        ,command=lambda:self.__viewSoftSuppr())
        btnAcceuilSoftList = aButton(self.__softAcceuil,text="Liste\nlogiciel"
                                                       ,command=lambda:self.__viewSoftList())

        btnAddSoftValider = aButton(self.__softAdd, text="Valider"
                                                      , command=lambda : self.__addSoft())
        btnAddSoftRetour = aButton(self.__softAdd,text="Retour"
                                                     ,command=lambda:self.__viewSoftAcceuil())

        btnSupprSoftValider = aButton(self.__softSuppr,text="Valider",
                                                        command=lambda:self.__supprSoft())
        btnSupprSoftRetour = aButton(self.__softSuppr,text="Retour",
                                                       command=lambda:self.__viewSoftAcceuil())
        btnSoftListRetour = aButton(self.__softListe,text="Retour",
                                                      command=lambda:self.__viewSoftAcceuil())

        # Entry
        self.__entryAddSoft = aEntry(self.__softAdd, width=300)

        # Option Menu
        self.__menuSoftSuppr = aOptionMenu(self.__softSuppr,value = ["",""])

        # Internet Frame
        # Label
        labelTitleInternet = [aLabel(self.__internetAcceuil,text="Gestion d'internet"),
                                aLabel(self.__internetSiteWeb,text="Ajouter un site web"),
                                aLabel(self.__internetSupprSite,text="Supprimer un site"),
                                aLabel(self.__internetListeSite, text="Liste site enregistrer")]

        # Bouton
        btnAcceuilInternetSiteWeb = aButton(self.__internetAcceuil,text="Ajouter un \nSite Web",
                                                                command=lambda:self.__viewInternetSiteWeb())
        btnAcceuilInternetCloudLink = aButton(self.__internetAcceuil,text="Lien \nde cloud"
                                                                ,command=lambda:self.__viewInternetCloudLink())
        btnAcceuilInternetSupprSite = aButton(self.__internetAcceuil,text="Supprimer\nun site",
                                                                command=lambda:self.__viewInternetSupprSite())
        btnAcceuilInternetListeSite = aButton(self.__internetAcceuil,text="Liste des sites enregistrer",
                                                                command=lambda:self.__viewInternetListeSite())

        btnValiderSiteWeb = aButton(self.__internetSiteWeb, text="Valider",
                                                      command=lambda:self.__saveSiteWeb(1))
        btnRetourSiteWeb = aButton(self.__internetSiteWeb, text="Retour"
                                                     ,command=lambda:self.__viewInternetAcceuil())

        btnInternetValiderSuppr = aButton(self.__internetSupprSite,text="Valider"
                                                            ,command=lambda:self.__supprSiteWeb())
        btnInternetRetourSuppr = aButton(self.__internetSupprSite,text="Retour"
                                                           ,command=lambda:self.__viewInternetAcceuil())

        btnRetourInternetListe = aButton(self.__internetListeSite,text="Retour"
                                                              ,command=lambda:self.__viewInternetAcceuil())

        self.__listSite = aText(self.__internetListeSite, width=450, height=250,
                                             wrap="word", state="normal")

        # Entry
        self.__entryNameSiteWeb = aEntry(self.__internetSiteWeb, width=300)
        self.__entrySiteWeb = aEntry(self.__internetSiteWeb, width=300)


        # option menu
        self.__menuSiteWeb = aOptionMenu(self.__internetSupprSite,value = ["",""])

        # Theme Frame
        # Label
        labelTitleTheme = aLabel(self.__themeFrame,text="Gestion du theme")

        self.__btnChangeTheme = aButton(self.__themeFrame,text="",
                                                          command=lambda:self.__saveNewTheme())

        # Micro Frame
        # Label
        labelTitleMicro = [aLabel(self.__microAcceuil,text="Gestion des paramètres micro"),
                            aLabel(self.__microSound,text="Son émis au déclenchement du micro"),
                            aLabel(self.__microTigerWord,text="Définition du mot de déclenchement du micro")
                            ,aLabel(self.__microViewSave,text="Enregistrement de l'empreinte vocale"),
                            aLabel(self.__microViewWordSave,text="Mots enregistrer"),]
        self.__labelVoicePrint = aLabel(self.__microVoicePrint,text="Empreinte vocale")
        self.__labelWordVoicePrint = aLabel(self.__microViewSave,text="")
        self.__labelWordViewSave = aLabel(self.__microViewWordSave,text="")
        labelDuringSave = aLabel(self.__microDuringSave,text="Dites le mots de décellement que vous voulez")

        # Button
        btnAcceuilMicroSound = aButton(self.__microAcceuil,text="Son\némis",
                                                         command=lambda:self.__viewMicroSound())
        btnAcceuilMicroTigerWord = aButton(self.__microAcceuil,text="Empreinte\nvocale",
                                                             command=lambda:self.__viewMicroTigerWord())

        self.__btnMicroSoundChangeEtat = aButton(self.__microSound,text="",
                                                                   command=lambda:self.__changeMicroSound())

        btnMicroSoundRetour = aButton(self.__microSound, text="Retour",
                                                        command=lambda:self.__viewMicroAcceuil())
        btnMicroTigerWordRetour = aButton(self.__microTigerWord, text="Retour",
                                                            command=lambda:self.__viewMicroAcceuil())

        self.__btnTrigerWordVoicePrint1 = aButton(self.__microTigerWord,text="Empreinte\nvocale 1"
                                                                    ,command=lambda : self.__viewVoicePrint(1))
        self.__btnTrigerWordVoicePrint2 = aButton(self.__microTigerWord, text="Empreinte\nvocale 2"
                                                  ,command=lambda : self.__viewVoicePrint(2))
        self.__btnTrigerWordVoicePrint3 = aButton(self.__microTigerWord, text="Empreinte\nvocale 3"
                                                                    ,command=lambda : self.__viewVoicePrint(3))
        btnSauvegarderVoicePrint = aButton(self.__microViewSave,text="Sauvegarder",
                                                             command=lambda : self.__saveTigerWord() )

        btnRetourVoicePrint = aButton(self.__microVoicePrint, text="Retour",
                                                        command=lambda:self.__viewMicroTigerWord())
        btnRetourWordVoicePrint = aButton(self.__microViewSave, text="Annuler",
                                                            command=lambda:self.__viewMicroAcceuil())
        btnRetourViewWord = aButton(self.__microViewWordSave, text="Retour",
                                                        command=lambda:self.__viewMicroTigerWord())

        self.__btnSaveVoicePrint = aButton(self.__microVoicePrint,text="Enregister",
                                                             command=lambda :self.__saveVoicePrint())

        self.__btnSupprVoicePrint = aButton(self.__microVoicePrint,text="Supprimer")

        self.__btnViewVoicePrint = aButton(self.__microVoicePrint, text="Voir le mot")


        # Frame Arrera Work
        labelTitleArreraWork = aLabel(self.__arreraWorkFrame,text="Paramètre Arrera Work")

        btnChooseFolderArreraWork = aButton(self.__arreraWorkFrame,text="Choisir un dossier"
                                                                ,command=lambda:self.__chooseFolderArreraWork())

        # Frame Arrera Download
        labelTitleArreraDownload = aLabel(self.__arreraDownloadFrame,text="Paramètre Arrera Download")
        btnChooseFolderArreraDownload = aButton(self.__arreraDownloadFrame,text="Choisir un dossier\nd'Arrera Download",
                                                                    command=lambda:self.__chooseFolderArreraDownload())

        # Affichage

        btnAcceuilUser.place(x=140,y=20)
        btnAcceuilMeteoAndGPS.place(x=260,y=20)
        btnAcceuilIA.place(x=380,y=20)
        btnAcceuilRecherche.place(x=20,y=140)
        btnAcceuilLogiciel.place(x=140,y=140)
        btnAcceuilInternet.place(x=260,y=140)
        btnAcceuilGps.place(x=380,y=140)
        btnAcceuilArreraWork.place(x=20,y=260)
        btnAcceuilDownload.place(x=140,y=260)
        btnAcceuilMicro.place(x=260,y=260)

        # backFrame
        retourAcceuilBTN.placeCenterRight()
        # userFrame
        for i in (range(0,len(labelTitleUser))):
            labelTitleUser[i].placeTopCenter()

        btnUserName.placeRightCenter()
        btnUserGenre.placeLeftCenter()

        btnValiderUserName.placeBottomLeft()
        btnValiderUserGenre.placeBottomLeft()
        btnRetourUserName.placeBottomRight()
        btnRetourUserGenre.placeBottomRight()

        self.__entryNameUser.placeCenter()
        menuUserGenre.placeCenter()

        # meteoFrame
        for i in (range(0,len(labelTitleMeteo))):
            labelTitleMeteo[i].placeTopCenter()

        btnAcceuilMeteoDomicile.placeRightCenter()
        btnAcceuilMeteoTravail.placeLeftCenter()
        btnAcceuiMeteolVille.placeCenter()
        btnAcceuilMeteoSuppr.placeBottomCenter()

        btnValiderMeteoDomicile.placeBottomLeft()
        btnRetourMeteoDomicile.placeBottomRight()

        btnValiderMeteoVille.placeBottomLeft()
        btnRetourMeteoVille.placeBottomRight()

        btnValiderMeteoTravail.placeBottomLeft()
        btnRetourMeteoTravail.placeBottomRight()

        btnValiderMeteoSuppr.placeBottomLeft()
        btnRetourMeteoSuppr.placeBottomRight()

        self.__entryMeteoDomicile.placeCenter()
        self.__entryMeteoTravail.placeCenter()
        self.__entryMeteoVille.placeCenter()

        for i in range(0,len(labelTitleGPS)):
            labelTitleGPS[i].placeTopCenter()

        btnAcceuilGPSDomicile.placeRightCenter()
        btnAcceuilGPSTravail.placeLeftCenter()
        btnAcceuilGPSSuppr.placeCenter()

        btnValiderGPSDomicile.placeBottomLeft()
        btnRetourGPSDomicile.placeBottomRight()

        btnValiderGPSTravail.placeBottomLeft()
        btnRetourGPSTravail.placeBottomRight()

        btnValiderGPSSuppr.placeBottomLeft()
        btnRetourGPSSuppr.placeBottomRight()

        self.__entryGPSTravail.placeCenter()
        self.__entryGPSDomicile.placeCenter()

        labelTitleRecherche.placeTopCenter()
        menuMoteurRecherche.placeCenter()
        btnValiderRecherche.placeBottomCenter()

        for i in range(0,len(labelTitleSoft)):
            labelTitleSoft[i].placeTopCenter()

        btnAcceuilSoftAdd.placeRightCenter()
        btnAcceuilSoftSuppr.placeLeftCenter()
        btnAcceuilSoftList.placeCenter()

        self.__entryAddSoft.placeCenter()
        btnAddSoftValider.placeBottomLeft()
        btnAddSoftRetour.placeBottomRight()

        btnSupprSoftValider.placeBottomLeft()
        btnSupprSoftRetour.placeBottomRight()

        btnSoftListRetour.placeBottomLeft()
        self.__listSite.placeCenter()
        self.__listSoftware.placeCenter()

        for i in range(0,len(labelTitleInternet)):
            labelTitleInternet[i].placeTopCenter()

        btnAcceuilInternetSiteWeb.placeRightCenter()
        btnAcceuilInternetSupprSite.placeLeftCenter()
        btnAcceuilInternetListeSite.placeBottomCenter()

        btnRetourSiteWeb.placeBottomLeft()
        btnValiderSiteWeb.placeBottomRight()

        btnInternetValiderSuppr.placeBottomLeft()
        self.__menuSiteWeb.placeCenter()
        btnInternetRetourSuppr.placeBottomRight()

        self.__entryNameSiteWeb.placeCenterOnWidth(y=100)
        self.__entrySiteWeb.placeCenterOnWidth(y=150)

        btnRetourInternetListe.placeBottomCenter()

        labelTitleTheme.placeTopCenter()
        self.__btnChangeTheme.placeCenter()

        for i in range(0,len(labelTitleMicro)):
            labelTitleMicro[i].placeTopCenter()

        self.__labelVoicePrint.placeTopCenter()
        btnRetourVoicePrint.placeBottomRight()
        self.__labelWordVoicePrint.placeCenter()
        btnRetourWordVoicePrint.placeBottomRight()
        btnSauvegarderVoicePrint.placeBottomLeft()
        btnRetourViewWord.placeBottomRight()
        self.__labelWordViewSave.placeCenter()
        labelDuringSave.placeCenter()

        #self.__arrtk.placeCenter(btnAcceuilMicroSound)

        btnAcceuilMicroSound.placeRightCenter()
        btnAcceuilMicroTigerWord.placeLeftCenter()

        self.__btnMicroSoundChangeEtat.placeCenter()

        btnMicroSoundRetour.placeBottomCenter()
        btnMicroTigerWordRetour.placeBottomCenter()

        labelTitleArreraWork.placeTopCenter()
        btnChooseFolderArreraWork.placeCenter()

        labelTitleArreraDownload.placeTopCenter()
        btnChooseFolderArreraDownload.placeCenter()

        btnViewMeteo.placeCenterLeft()
        btnViewGPS.placeCenterRight()
        lTitleGPSAndMeteo.placeTopCenter()

    # Methode generale
    def active(self):
        self.__mainCadre.pack()

    def __clearAll(self):
        self.__mainCadre.pack_forget()
        self.__userFrame.pack_forget()
        self.__backFrame.pack_forget()
        self.__meteoFrame.pack_forget()
        self.__gpsFrame.pack_forget()
        self.__rechercheFrame.pack_forget()
        self.__softFrame.pack_forget()
        self.__internetFrame.pack_forget()
        self.__themeFrame.pack_forget()
        self.__microFrame.pack_forget()
        self.__arreraWorkFrame.pack_forget()
        self.__arreraDownloadFrame.pack_forget()
        self.__meteoGPSFrame.pack_forget()
        self.__windows.update()

    def __backAcceuil(self):
        self.__clearAll()
        self.__mainCadre.pack()

    def passFNCQuit(self,fnc):
        self.__btnRetourAssistant.configure(command=fnc)
        self.__btnRetourAssistant.place(x=380, y=260)

    def passFNCBTNIcon(self,fnc):
        self.__btnIcon.configure(command=fnc)
        self.__btnIcon.place(x=20, y=20)

    def clearAllFrame(self):
        self.__clearAll()

    # Methode pour la partie User
    def __viewUserAcceuil(self):
        self.__clearAll()
        self.__userName.pack_forget()
        self.__userGenre.pack_forget()
        self.__userAcceuil.pack()
        self.__userFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __viewUserName(self):
        self.__userName.pack()
        self.__userGenre.pack_forget()
        self.__userAcceuil.pack_forget()
        self.__windows.update()

    def __viewUserGenre(self):
        self.__userName.pack_forget()
        self.__userGenre.pack()
        self.__userAcceuil.pack_forget()
        self.__windows.update()

    def __saveUserName(self):
        name = self.__entryNameUser.get()
        if name == "":
            messagebox.showerror("Parametre","Le nom de l'utilisateur ne peut pas etre vide")
            return
        else :
            self.__gazelle.changeUserName(name)
            messagebox.showinfo("Parametre","Le nom de l'utilisateur a bien été enregistré")
            self.__entryNameUser.delete(0,END)
            self.__viewUserAcceuil()

    def __saveUserGenre(self):
        genre = self.__varNameUser.get()
        self.__gazelle.changeUserGenre(genre)
        messagebox.showinfo("Parametre","Le genre de l'utilisateur a bien été enregistré")
        self.__viewUserAcceuil()


    # Methode pour la partie GPS et Meteo

    def __viewGPSMeteo(self):
        self.__clearAll()
        self.__meteoGPSFrame.pack()
        self.__backFrame.pack()

    # Methode partie Meteo

    def __viewMeteoAcceuil(self):
        self.__clearAll()
        self.__meteoVille.pack_forget()
        self.__meteoTravail.pack_forget()
        self.__meteoDomicile.pack_forget()
        self.__meteoSuppr.pack_forget()
        self.__meteoAcceuil.pack()
        self.__meteoFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __viewMeteoDomicile(self):
        self.__entryMeteoDomicile.delete(0,END)
        self.__meteoDomicile.pack()
        self.__meteoTravail.pack_forget()
        self.__meteoVille.pack_forget()
        self.__meteoAcceuil.pack_forget()
        self.__meteoSuppr.pack_forget()
        self.__windows.update()

    def __viewMeteoTravail(self):
        self.__entryMeteoTravail.delete(0, END)
        self.__meteoDomicile.pack_forget()
        self.__meteoTravail.pack()
        self.__meteoVille.pack_forget()
        self.__meteoAcceuil.pack_forget()
        self.__meteoSuppr.pack_forget()
        self.__windows.update()

    def __viewMeteoVille(self):
        self.__entryMeteoVille.delete(0, END)
        self.__meteoDomicile.pack_forget()
        self.__meteoTravail.pack_forget()
        self.__meteoVille.pack()
        self.__meteoAcceuil.pack_forget()
        self.__meteoSuppr.pack_forget()
        self.__windows.update()

    def __viewMeteoSuppr(self):
        listVille = self.__gazelle.getMeteoSave()
        if len(listVille) == 0:
            messagebox.showerror("Erreur", "Aucune ville n'a été enregistré")
            return
        self.__meteoDomicile.pack_forget()
        self.__meteoTravail.pack_forget()
        self.__meteoVille.pack_forget()
        self.__meteoAcceuil.pack_forget()
        self.__meteoSuppr.pack()
        del self.__menuMeteoSuppr
        self.__menuMeteoSuppr = aOptionMenu(self.__meteoSuppr,value = listVille)
        self.__menuMeteoSuppr.placeCenter()

    def __saveMeteoDomicile(self):
        domicile = self.__entryMeteoDomicile.get()
        if domicile == "":
            messagebox.showerror("Parametre","Le lieu domicile ne peut pas etre vide")
            return
        else :
            self.__gazelle.ajoutVilleMeteo(1,domicile)
            messagebox.showinfo("Parametre","Le lieu domicile a bien été enregistré")
            self.__entryMeteoDomicile.delete(0,END)
            self.__viewMeteoAcceuil()

    def __saveMeteoTravail(self):
        travail = self.__entryMeteoTravail.get()
        if travail == "":
            messagebox.showerror("Parametre","Le lieu travail ne peut pas etre vide")
            return
        else :
            self.__gazelle.ajoutVilleMeteo(2,travail)
            messagebox.showinfo("Parametre","Le lieu travail a bien été enregistré")
            self.__entryMeteoTravail.delete(0,END)
            self.__viewMeteoAcceuil()

    def __saveMeteoVille(self):
        ville = self.__entryMeteoVille.get()
        if ville == "":
            messagebox.showerror("Parametre","Le lieu ville ne peut pas etre vide")
            return
        else :
            self.__gazelle.ajoutVilleMeteo(3,ville)
            messagebox.showinfo("Parametre","Le lieu ville a bien été enregistré")
            self.__entryMeteoVille.delete(0,END)
            self.__viewMeteoAcceuil()

    def __supprMeteoVille(self):
        ville = self.__varSupprMeteo.get()
        if ville == "":
            messagebox.showerror("Erreur","Aucune ville n'a été selectionné")
            return
        else :
            self.__gazelle.supprVilleMeteo(3,ville)
            messagebox.showinfo("Parametre","Le lieu a bien été supprimé")
            self.__viewMeteoAcceuil()

    # Methode partie GPS

    def __viewGPSAcceuil(self):
        self.__clearAll()
        self.__gpsDomicile.pack_forget()
        self.__gpsTravail.pack_forget()
        self.__gpsSuppr.pack_forget()
        self.__gpsAcceuil.pack()
        self.__gpsFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __viewGPSDomicile(self):
        self.__entryGPSDomicile.delete(0,END)
        self.__gpsDomicile.pack()
        self.__gpsTravail.pack_forget()
        self.__gpsSuppr.pack_forget()
        self.__gpsAcceuil.pack_forget()
        self.__windows.update()

    def __viewGPSTravail(self):
        self.__entryGPSTravail.delete(0,END)
        self.__gpsDomicile.pack_forget()
        self.__gpsTravail.pack()
        self.__gpsSuppr.pack_forget()
        self.__gpsAcceuil.pack_forget()
        self.__windows.update()

    def __viewGPSSuppr(self):
        travailSet = self.__gazelle.getGPSAdresseIsSet(2)
        domicileSet = self.__gazelle.getGPSAdresseIsSet(1)
        listVille = []

        if domicileSet:
            listVille.append("Lieu de Domicile")

        if travailSet:
            listVille.append("Lieu de Travail")

        if len(listVille) == 0:
            messagebox.showerror("Erreur", "Aucune ville n'a été enregistré")
            return
        self.__gpsDomicile.pack_forget()
        self.__gpsTravail.pack_forget()
        self.__gpsSuppr.pack()
        self.__gpsAcceuil.pack_forget()
        del self.__menuGPSSuppr
        self.__menuGPSSuppr = aOptionMenu(self.__gpsSuppr,value = listVille)
        self.__menuGPSSuppr.placeCenter()

    def __saveGPSDomicile(self):
        domicile = self.__entryGPSDomicile.get()
        if domicile == "":
            messagebox.showerror("Parametre","Le lieu domicile ne peut pas etre vide")
            return
        else :
            self.__gazelle.ajoutGPSAdresse(1,domicile)
            messagebox.showinfo("Parametre","Le lieu domicile a bien été enregistré")
            self.__entryGPSDomicile.delete(0,END)
            self.__viewGPSAcceuil()

    def __saveGPSTravail(self):
        travail = self.__entryGPSTravail.get()
        if travail == "":
            messagebox.showerror("Parametre","Le lieu travail ne peut pas etre vide")
            return
        else :
            self.__gazelle.ajoutGPSAdresse(2,travail)
            messagebox.showinfo("Parametre","Le lieu travail a bien été enregistré")
            self.__entryGPSTravail.delete(0,END)
            self.__viewGPSAcceuil()

    def __supprGPSAdresse(self):
        adresse = self.__varSupprGPS.get()
        if adresse == "":
            messagebox.showerror("Erreur","Aucune adresse n'a été selectionné")
            return
        else :
            if adresse == "Lieu de Domicile":
                self.__gazelle.supprGPSAdresse(1)
            else :
                self.__gazelle.supprGPSAdresse(2)
            messagebox.showinfo("Parametre","Le lieu a bien été supprimé")
            self.__viewGPSAcceuil()


    # Methode recherche

    def __viewRecherche(self):
        self.__clearAll()
        self.__rechercheFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __saveRecherche(self):
        moteur = self.__varMoteurRecherche.get()
        self.__gazelle.changeMoteur(moteur)
        messagebox.showinfo("Parametre","Le moteur de recherche a bien été enregistré")
        self.__backAcceuil()
        self.__windows.update()

    # Methode soft

    def __viewSoftAcceuil(self):
        self.__clearAll()
        self.__softFrame.pack()
        self.__backFrame.pack()
        self.__softAcceuil.pack()
        self.__softAdd.pack_forget()
        self.__softSuppr.pack_forget()
        self.__softListe.pack_forget()
        self.__windows.update()

    def __viewSoftAdd(self):
        self.__softAcceuil.pack_forget()
        self.__softAdd.pack_forget()
        self.__softSuppr.pack_forget()
        self.__softAdd.pack()
        self.__windows.update()

    def __viewSoftSuppr(self):
        listSoft = self.__gazelle.getListSoft()
        if (len(listSoft) == 0):
            messagebox.showerror("Erreur", "Aucun logiciel n'a été enregistré")
            return
        self.__softAcceuil.pack_forget()
        self.__softAdd.pack_forget()
        self.__softSuppr.pack()
        del self.__menuSoftSuppr
        self.__menuSoftSuppr = aOptionMenu(self.__softSuppr,value = listSoft)
        self.__menuSoftSuppr.placeCenter()

    def __viewSoftList(self):
        self.__listSoftware.configure(state="normal")
        self.__listSoftware.delete(1.0, END)
        listSoft = self.__gazelle.getListSoft()
        if len(listSoft) == 0:
            messagebox.showerror("Erreur", "Aucun logiciel n'a été enregistré")
            return
        for i in range(0,len(listSoft)):
            self.__listSoftware.insert(END, listSoft[i] + "\n")
        self.__listSoftware.configure(state="disabled")
        self.__softAcceuil.pack_forget()
        self.__softSuppr.pack_forget()
        self.__softAdd.pack_forget()
        self.__softListe.pack()
        self.__windows.update()

    def __viewSoftSoft(self):
        self.__softAcceuil.pack_forget()
        self.__softAdd.pack()
        self.__softSuppr.pack_forget()
        self.__entryAddSoft.delete(0,END)

    def __addSoft(self):
        soft = self.__entryAddSoft.get()
        if soft == "":
            messagebox.showerror("Erreur","Le nom du logiciel ne peut pas etre vide")
            return
        else :
            self.__gazelle.addSoft(soft)
            messagebox.showinfo("Parametre","Le logiciel a bien été ajouté")
            self.__entryAddSoft.delete(0,END)
            self.__viewSoftAcceuil()

    def __supprSoft(self):
        soft = self.__varSupprSoft.get()
        if not self.__gazelle.supprSoft(soft):
            messagebox.showinfo("Parametre", "Le logiciel n'a pas pu être supprimé.")
        else :
            messagebox.showinfo("Parametre", "Le logiciel a bien été supprimé")
        self.__viewSoftAcceuil()

    # Methode internet

    def __viewInternetAcceuil(self):
        self.__clearAll()
        self.__internetSiteWeb.pack_forget()
        self.__internetSupprSite.pack_forget()
        self.__internetListeSite.pack_forget()
        self.__internetAcceuil.pack()
        self.__internetFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __viewInternetSiteWeb(self):
        self.__entryNameSiteWeb.delete(0,END)
        self.__entrySiteWeb.delete(0,END)
        self.__internetSiteWeb.pack()
        self.__internetSupprSite.pack_forget()
        self.__internetAcceuil.pack_forget()
        self.__internetListeSite.pack_forget()
        self.__windows.update()

    def __viewInternetCloudLink(self):
        self.__internetSiteWeb.pack_forget()
        self.__internetSupprSite.pack_forget()
        self.__internetAcceuil.pack_forget()
        self.__internetListeSite.pack_forget()
        self.__windows.update()

    def __viewInternetSupprSite(self):
        listSite = self.__gazelle.getListSite()
        if len(listSite) == 0:
            messagebox.showerror("Erreur", "Aucun site web n'a été enregistré")
            return
        self.__internetSiteWeb.pack_forget()
        self.__internetSupprSite.pack()
        self.__internetAcceuil.pack_forget()
        del self.__menuSiteWeb
        self.__menuSiteWeb = aOptionMenu(self.__internetSupprSite,value = listSite)
        self.__menuSiteWeb.placeCenter()

    def __viewInternetListeSite(self):
        listSite = self.__gazelle.getListSite()
        if len(listSite) == 0:
            messagebox.showerror("Erreur", "Aucun site web n'a été enregistré")
            return
        self.__internetSiteWeb.pack_forget()
        self.__internetSupprSite.pack_forget()
        self.__internetAcceuil.pack_forget()
        self.__listSite.configure(state="normal")
        self.__listSite.delete(1.0, END)
        for i in range(0,len(listSite)):
            self.__listSite.insert(END, listSite[i] + "\n")
        self.__listSite.configure(state="disabled")
        self.__internetListeSite.pack()

    def __saveSiteWeb(self, mode:int):
        """
        :param mode: 1. Site web 2. Cloud Link
        :return:
        """
        match mode :
            case 1 :
                name = self.__entryNameSiteWeb.get()
                link = self.__entrySiteWeb.get()
                if name == "" or link == "":
                    messagebox.showerror("Erreur","Le nom ou le lien ne peut pas etre vide")
                    return
                else :
                    self.__gazelle.addSite(1,name,link)
                    messagebox.showinfo("Parametre","Le site web a bien été ajouté")
                    self.__entryNameSiteWeb.delete(0,END)
                    self.__entrySiteWeb.delete(0,END)
                    self.__viewInternetAcceuil()
            case 2 :
                return

    def __supprSiteWeb(self):
        site = self.__varSupprWeb.get()
        if site == "Cloud":
            self.__gazelle.supprSite(2, site)
        else :
            self.__gazelle.supprSite(1,site)
        messagebox.showinfo("Parametre", "Le site a bien été supprimé")
        self.__viewInternetAcceuil()

    # Methode Theme

    def __viewTheme(self):
        self.__clearAll()
        self.__themeFrame.pack()
        self.__backFrame.pack()
        theme = self.__gazelle.getTheme()
        if theme == self.__listTheme[0]:
            self.__btnChangeTheme.configure(text="Passer au mode "+self.__listTheme[1])
        else :
            self.__btnChangeTheme.configure(text="Passer au mode "+self.__listTheme[0])
        self.__windows.update()

    def __saveNewTheme(self):
        theme = self.__gazelle.getTheme()
        if theme == self.__listTheme[0]:
            self.__gazelle.changeTheme(self.__listTheme[1])
        else :
            self.__gazelle.changeTheme(self.__listTheme[0])
        self.__backAcceuil()

    # Methode Micro

    def __viewMicroAcceuil(self):
        self.__clearAll()
        self.__microFrame.pack()
        self.__backFrame.pack()
        self.__microAcceuil.pack()
        self.__microSound.pack_forget()
        self.__microTigerWord.pack_forget()
        self.__microVoicePrint.pack_forget()
        self.__microViewSave.pack_forget()
        self.__microViewWordSave.pack_forget()
        self.__windows.update()

    def __viewMicroSound(self):
        self.__microAcceuil.pack_forget()
        self.__microSound.pack()
        self.__microTigerWord.pack_forget()
        microEnable = self.__gazelle.getSoundMicroAsEnable()
        if microEnable:
            self.__btnMicroSoundChangeEtat.configure(text="Désactiver le son")
        else :
            self.__btnMicroSoundChangeEtat.configure(text="Activer le son")

    def __viewMicroTigerWord(self):
        self.__microAcceuil.pack_forget()
        self.__microSound.pack_forget()
        self.__microVoicePrint.pack_forget()
        self.__microViewSave.pack_forget()
        self.__microViewWordSave.pack_forget()

        self.__microTigerWord.pack()

        nbTriger = self.__gazelle.getNbTrigerWord()

        self.__btnTrigerWordVoicePrint1.place_forget()
        self.__btnTrigerWordVoicePrint2.place_forget()
        self.__btnTrigerWordVoicePrint3.place_forget()

        if nbTriger == 0:
            self.__arrtk.placeCenter(self.__btnTrigerWordVoicePrint1)
        elif nbTriger == 1:
            self.__arrtk.placeCenterLeft(self.__btnTrigerWordVoicePrint1)
            self.__arrtk.placeRightCenter(self.__btnTrigerWordVoicePrint2)
        else :
            self.__arrtk.placeCenterLeft(self.__btnTrigerWordVoicePrint1)
            self.__arrtk.placeCenter(self.__btnTrigerWordVoicePrint2)
            self.__arrtk.placeRightCenter(self.__btnTrigerWordVoicePrint3)
        self.__windows.update()


    def __viewVoicePrint(self,mode:int):
        self.__microTigerWord.pack_forget()
        self.__microVoicePrint.pack()
        listWord = self.__gazelle.getTrigerWord()
        nb = len(listWord)
        self.__btnSaveVoicePrint.place_forget()
        self.__btnSupprVoicePrint.place_forget()
        self.__btnViewVoicePrint.place_forget()
        match mode :
            case 1 :
                self.__labelVoicePrint.configure(text="Gestion empreinte vocale 1")
                if (nb == 0):
                    self.__btnSaveVoicePrint.placeCenter()
                else :
                    self.__btnSupprVoicePrint.placeLeftCenter()
                    self.__btnViewVoicePrint.placeRightCenter()
                    self.__btnViewVoicePrint.configure(command=lambda : self.__viewSaveWord(1))
                    self.__btnSupprVoicePrint.configure(command=lambda :self.__supprTrigerWord(1))
            case 2 :
                self.__labelVoicePrint.configure(text="Gestion empreinte vocale 2")
                if (nb == 1):
                    self.__btnSaveVoicePrint.placeCenter()
                else :
                    self.__btnSupprVoicePrint.placeLeftCenter()
                    self.__btnViewVoicePrint.placeRightCenter()
                    self.__btnViewVoicePrint.configure(command=lambda: self.__viewSaveWord(2))
                    self.__btnSupprVoicePrint.configure(command=lambda: self.__supprTrigerWord(2))
            case 3 :
                self.__labelVoicePrint.configure(text="Gestion empreinte vocale 3")
                if (nb == 2):
                    self.__btnSaveVoicePrint.placeCenter()
                else :
                    self.__btnSupprVoicePrint.placeLeftCenter()
                    self.__btnViewVoicePrint.placeRightCenter()
                    self.__btnViewVoicePrint.configure(command=lambda: self.__viewSaveWord(3))
                    self.__btnSupprVoicePrint.configure(command=lambda: self.__supprTrigerWord(3))

    def __saveVoicePrint(self):
        self.__threadSaveVoicePrint = th.Thread(target=self.__gazelle.recordTrigerWord)
        self.__threadSaveVoicePrint.start()
        self.__microTigerWord.pack_forget()
        self.__microVoicePrint.pack_forget()
        self.__microDuringSave.pack_forget()
        self.__microDuringSave.pack()
        self.__windows.update()
        self.__windows.after(100, self.__duringSaveVoicePrint)

    def __duringSaveVoicePrint(self):
        if self.__threadSaveVoicePrint.is_alive():
            self.__windows.after(100, self.__duringSaveVoicePrint)
            self.__windows.update()
        else:
            sortie = self.__gazelle.getStateRecordTigerWord()
            if sortie:
                self.__microTigerWord.pack_forget()
                self.__microVoicePrint.pack_forget()
                self.__microDuringSave.pack_forget()
                self.__microViewSave.pack()
                self.__labelWordVoicePrint.configure(text="Mots enregistrer : " + self.__gazelle.getRecordTrigerWord())
            else:
                self.__microVoicePrint.pack()

    def __saveTigerWord(self):
        self.__viewMicroAcceuil()
        self.__gazelle.saveRecordTrigerWord()
        messagebox.showinfo("Parametre","Le mot déclencheur ont bien été enregistrés.")

    def __viewSaveWord(self,mode:int):
        self.__microAcceuil.pack_forget()
        self.__microSound.pack_forget()
        self.__microTigerWord.pack_forget()
        self.__microVoicePrint.pack_forget()
        self.__microViewSave.pack_forget()
        self.__microViewWordSave.pack()
        self.__windows.update()

        word = self.__gazelle.getTrigerWord()[mode-1]
        self.__labelWordViewSave.configure(text="Le mots enregister est : "+word)

    def __supprTrigerWord(self,mode:int):
        self.__viewMicroAcceuil()

        word = self.__gazelle.getTrigerWord()[mode-1]

        self.__gazelle.supprTrigerWord(word)

    def __changeMicroSound(self):
        microEnable = self.__gazelle.getSoundMicroAsEnable()
        if microEnable:
            self.__gazelle.changeSoundMicro(False)
        else :
            self.__gazelle.changeSoundMicro(True)
        self.__viewMicroAcceuil()

    def gettigerWordSet(self):
        nb = self.__gazelle.getNbTrigerWord()
        if (nb == 0):
            return False
        else :
            return True

    # Methode Arrera Work

    def __viewArreraWork(self):
        self.__clearAll()
        self.__arreraWorkFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __chooseFolderArreraWork(self):
        sortie = self.__gazelle.setWorkFolder()
        if sortie:
            messagebox.showinfo("Parametre","Le dossier de travail a bien été enregistré")
        else :
            messagebox.showerror("Erreur","Le dossier de travail n'a pas été enregistré")
        self.__backAcceuil()

    # Methode Arrera Download

    def __viewArreraDownload(self):
        self.__clearAll()
        self.__arreraDownloadFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __chooseFolderArreraDownload(self):
        sortie = self.__gazelle.setVideoDownloadFolder()
        if sortie:
            messagebox.showinfo("Parametre","Le dossier de téléchargement a bien été enregistré")
        else :
            messagebox.showerror("Erreur","Le dossier de téléchargement n'a pas été enregistré")
        self.__backAcceuil()