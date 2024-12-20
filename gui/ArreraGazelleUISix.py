from librairy.arrera_tk import *
from objet.arreraGazelle import*
from typing import Union

class CArreraGazelleUISix :
    def __init__(self,arrTK:CArreraTK,windows:Union[ctk.CTk,ctk.CTkToplevel],emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,emplacementJsonAssistant:str,emplacementConfigSetting:str):
        # Ouverture de l'objet
        self.__gazelle = CArreraGazelle(emplacementJsonUser,emplacementJsonNeuronNetwork,emplacementJsonAssistant)
        jsonSetting = jsonWork(emplacementConfigSetting)

        # Mise de la fenetre dans un atribut
        self.__windows = windows
        self.__arrtk = arrTK
        # Declaration des cardre
        self.__mainCadre = self.__arrtk.createFrame(self.__windows,width=500,height=400)

        self.__userFrame = self.__arrtk.createFrame(self.__windows,width=500,height=330)
        self.__userAcceuil = self.__arrtk.createFrame(self.__userFrame,width=500,height=330)
        self.__userName = self.__arrtk.createFrame(self.__userFrame,width=500,height=330)
        self.__userGenre = self.__arrtk.createFrame(self.__userFrame,width=500,height=330)

        self.__meteoFrame = self.__arrtk.createFrame(self.__windows,width=500,height=330)
        self.__meteoAcceuil = self.__arrtk.createFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoDomicile = self.__arrtk.createFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoTravail = self.__arrtk.createFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoVille = self.__arrtk.createFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoSuppr = self.__arrtk.createFrame(self.__meteoFrame,width=500,height=330)

        self.__gpsFrame = self.__arrtk.createFrame(self.__windows,width=500,height=330)
        self.__gpsAcceuil = self.__arrtk.createFrame(self.__gpsFrame,width=500,height=330)
        self.__gpsDomicile = self.__arrtk.createFrame(self.__gpsFrame,width=500,height=330)
        self.__gpsTravail = self.__arrtk.createFrame(self.__gpsFrame,width=500,height=330)
        self.__gpsSuppr = self.__arrtk.createFrame(self.__gpsFrame,width=500,height=330)

        self.__rechercheFrame = self.__arrtk.createFrame(self.__windows,width=500,height=330)

        self.__softFrame = self.__arrtk.createFrame(self.__windows,width=500,height=330)
        self.__softAcceuil = self.__arrtk.createFrame(self.__softFrame,width=500,height=330)
        self.__softAdd = self.__arrtk.createFrame(self.__softFrame,width=500,height=330)
        self.__softSuppr = self.__arrtk.createFrame(self.__softFrame,width=500,height=330)
        self.__softType = self.__arrtk.createFrame(self.__softFrame,width=500,height=330)
        self.__softListe = self.__arrtk.createFrame(self.__softFrame,width=500,height=330)

        self.__backFrame = self.__arrtk.createFrame(self.__windows,width=500,height=70)

        # Variable
        # Taille Police
        taillePolice = 20
        # Liste
        listGenre = jsonSetting.lectureJSONList("listGenre")
        listMoteurRecherche = jsonSetting.lectureJSONList("listMoteurRecherche")
        # Icon Assistant
        iconAssistant = self.__arrtk.createImage(jsonSetting.lectureJSON("iconSoft"),tailleX=95,tailleY=95)
        # String var
        self.__varNameUser = StringVar(self.__windows)
        self.__varSupprMeteo = StringVar(self.__windows)
        self.__varSupprGPS = StringVar(self.__windows)
        self.__varMoteurRecherche = StringVar(self.__windows)
        # Widget 
        # Main frame
        btnIcon = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,image=iconAssistant)
        btnAcceuilUser = self.__arrtk.createButton(self.__mainCadre, width=100, height=100, text="Utilisateur"
                                                   , ppolice="Arial", ptaille=taillePolice-2, pstyle="bold", command= lambda  : self.__viewUserAcceuil())
        btnAcceuilMeteo = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Meteo"
                                                    ,ppolice="Arial",ptaille=taillePolice,pstyle="bold",command=lambda:self.__viewMeteoAcceuil())
        btnAcceuilGPS = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="GPS"
                                                  ,ppolice="Arial",ptaille=taillePolice,pstyle="bold",command=lambda : self.__viewGPSAcceuil())
        btnAcceuilRecherche = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Recherche"
                                                        ,ppolice="Arial",ptaille=taillePolice-2,pstyle="bold",command=lambda:self.__viewRecherche())
        btnAcceuilLogiciel = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Logiciel"
                                                       ,ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilInternet = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Internet"
                                                       ,ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilTheme = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Theme"
                                                    ,ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilArreraWork = self.__arrtk.createButton(self.__mainCadre,width=100,height=100
                                                         ,text="Arrera\nWork",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilDownload = self.__arrtk.createButton(self.__mainCadre,width=100,height=100
                                                       ,text="Arrera\nDownload",ppolice="Arial",ptaille=taillePolice-2,pstyle="bold")
        btnAcceuilMicro = self.__arrtk.createButton(self.__mainCadre,width=100,height=100
                                                    ,text="Micro",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        self.__btnRetourAssistant = self.__arrtk.createButton(self.__mainCadre,width=100,
                                                              height=100,text="Retour",ppolice="Arial",ptaille=taillePolice,pstyle="bold")

        # backFrame
        retourAcceuilBTN = self.__arrtk.createButton(self.__backFrame,text="Retour Acceuil"
                                                     ,ppolice="Arial",ptaille=taillePolice,command=lambda:self.__backAcceuil())


        # userFrame
        # Label
        labelTitleUser = [self.__arrtk.createLabel(self.__userAcceuil,text="Gestion utilisateur"
                                                  ,ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                          self.__arrtk.createLabel(self.__userName,text="Nom de l'utilisateur",
                                                   ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                          self.__arrtk.createLabel(self.__userGenre,text="Genre de l'utilisateur"
                                                   ,ppolice="Arial",ptaille=taillePolice,pstyle="bold")]
        # Button
        btnUserName = self.__arrtk.createButton(self.__userAcceuil,text="Nom\nde\nl'utilisateur",ppolice="Arial",
                                                ptaille=taillePolice,pstyle="bold",command=lambda:self.__viewUserName())
        btnUserGenre = self.__arrtk.createButton(self.__userAcceuil,text="Genre\nde\nl'utilisateur",ppolice="Arial",
                                                 ptaille=taillePolice,pstyle="bold",command=lambda:self.__viewUserGenre())
        btnValiderUserName = self.__arrtk.createButton(self.__userName,text="Valider",ppolice="Arial",
                                                       ptaille=taillePolice,pstyle="normal",command=lambda:self.__saveUserName())
        btnValiderUserGenre = self.__arrtk.createButton(self.__userGenre,text="Valider",ppolice="Arial",
                                                        ptaille=taillePolice,pstyle="normal",command=lambda:self.__saveUserGenre())
        btnRetourUserName = self.__arrtk.createButton(self.__userName, text="Retour", ppolice="Arial",
                                                      ptaille=taillePolice, pstyle="normal",command=lambda:self.__viewUserAcceuil())
        btnRetourUserGenre = self.__arrtk.createButton(self.__userGenre, text="Retour", ppolice="Arial",
                                                       ptaille=taillePolice, pstyle="normal",command=lambda:self.__viewUserAcceuil())
        # entry
        self.__entryNameUser = self.__arrtk.createEntry(self.__userName, police="Arial", taille=taillePolice, width=200)
        # option menu
        menuUserGenre = self.__arrtk.createOptionMenu(self.__userGenre,value = listGenre,var = self.__varNameUser)

        # meteoFrame
        # Label
        labelTitleMeteo = [self.__arrtk.createLabel(self.__meteoAcceuil,text="Gestion de meteo",
                                                    ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                           self.__arrtk.createLabel(self.__meteoDomicile,text="Lieu Domicile",
                                                    ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                           self.__arrtk.createLabel(self.__meteoTravail,text="Lieu Travail",
                                                    ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                           self.__arrtk.createLabel(self.__meteoVille,text="Autre Ville",
                                                    ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                           self.__arrtk.createLabel(self.__meteoSuppr,text="Supprimer Lieu",
                                                    ppolice="Arial",ptaille=taillePolice,pstyle="bold")]
        # Button
        btnAcceuilMeteoDomicile = self.__arrtk.createButton(self.__meteoAcceuil,text="Lieu\nDomicile",
                                                       ppolice="Arial",ptaille=taillePolice,pstyle="bold",
                                                       command=lambda:self.__viewMeteoDomicile())
        btnAcceuilMeteoTravail = self.__arrtk.createButton(self.__meteoAcceuil,text="Lieu\nTravail",
                                                      ppolice="Arial",ptaille=taillePolice,pstyle="bold",
                                                      command=lambda:self.__viewMeteoTravail())
        btnAcceuiMeteolVille = self.__arrtk.createButton(self.__meteoAcceuil,text="Autre\nVille",
                                                    ppolice="Arial",ptaille=taillePolice,pstyle="bold",
                                                    command=lambda:self.__viewMeteoVille())
        btnAcceuilMeteoSuppr = self.__arrtk.createButton(self.__meteoAcceuil,text="Supprimer un lieu",
                                                    ppolice="Arial",ptaille=taillePolice,pstyle="bold",
                                                    command=lambda:self.__viewMeteoSuppr())

        btnValiderMeteoDomicile = self.__arrtk.createButton(self.__meteoDomicile,text="Valider",
                                                            ppolice="Arial",ptaille=taillePolice,pstyle="normal",
                                                            command=lambda:self.__saveMeteoDomicile())
        btnValiderMeteoTravail = self.__arrtk.createButton(self.__meteoTravail,text="Valider",
                                                           ppolice="Arial",ptaille=taillePolice,pstyle="normal",
                                                           command=lambda:self.__saveMeteoTravail())
        btnValiderMeteoVille = self.__arrtk.createButton(self.__meteoVille,text="Valider",
                                                         ppolice="Arial",ptaille=taillePolice,pstyle="normal",
                                                         command=lambda:self.__saveMeteoVille())
        btnValiderMeteoSuppr = self.__arrtk.createButton(self.__meteoSuppr,text="Supprimer",
                                                         ppolice="Arial",ptaille=taillePolice,pstyle="normal",
                                                         command=lambda:self.__supprMeteoVille())

        btnRetourMeteoDomicile = self.__arrtk.createButton(self.__meteoDomicile,text="Retour",
                                                           ppolice="Arial",ptaille=taillePolice,pstyle="normal",
                                                           command=lambda:self.__viewMeteoAcceuil())
        btnRetourMeteoTravail = self.__arrtk.createButton(self.__meteoTravail,text="Retour",
                                                          ppolice="Arial",ptaille=taillePolice,pstyle="normal",
                                                          command=lambda:self.__viewMeteoAcceuil())
        btnRetourMeteoVille = self.__arrtk.createButton(self.__meteoVille,text="Retour",
                                                        ppolice="Arial",ptaille=taillePolice,pstyle="normal",
                                                        command=lambda:self.__viewMeteoAcceuil())
        btnRetourMeteoSuppr = self.__arrtk.createButton(self.__meteoSuppr,text="Retour",
                                                        ppolice="Arial",ptaille=taillePolice,pstyle="normal",
                                                        command=lambda:self.__viewMeteoAcceuil())
        # entry
        self.__entryMeteoDomicile = self.__arrtk.createEntry(self.__meteoDomicile,police="Arial",taille=taillePolice,width=300)
        self.__entryMeteoTravail = self.__arrtk.createEntry(self.__meteoTravail,police="Arial",taille=taillePolice,width=300)
        self.__entryMeteoVille = self.__arrtk.createEntry(self.__meteoVille,police="Arial",taille=taillePolice,width=300)
        #option menu
        self.__menuMeteoSuppr = self.__arrtk.createOptionMenu(self.__meteoSuppr, value = ["", ""], var = self.__varSupprMeteo)

        # GPS Frame
        # Label
        labelTitleGPS = [self.__arrtk.createLabel(self.__gpsAcceuil,text="Gestion GPS",
                                                  ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                         self.__arrtk.createLabel(self.__gpsDomicile,text="Lieu Domicile",
                                                  ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                         self.__arrtk.createLabel(self.__gpsTravail,text="Lieu Travail",
                                                  ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                         self.__arrtk.createLabel(self.__gpsSuppr,text="Supprimer Lieu",
                                                  ppolice="Arial",ptaille=taillePolice,pstyle="bold")]
        # Button
        btnAcceuilGPSDomicile = self.__arrtk.createButton(self.__gpsAcceuil,text="Lieu\nDomicile",
                                                          ppolice="Arial", ptaille=taillePolice, pstyle="bold",
                                                          command=lambda:self.__viewGPSDomicile())
        btnAcceuilGPSTravail = self.__arrtk.createButton(self.__gpsAcceuil,text="Lieu\nTravail",
                                                         ppolice="Arial", ptaille=taillePolice, pstyle="bold",
                                                         command=lambda:self.__viewGPSTravail())
        btnAcceuilGPSSuppr = self.__arrtk.createButton(self.__gpsAcceuil,text="Supprimer\nun lieu",
                                                       ppolice="Arial", ptaille=taillePolice, pstyle="bold",
                                                       command=lambda:self.__viewGPSSuppr())

        btnValiderGPSDomicile = self.__arrtk.createButton(self.__gpsDomicile,text="Valider",ppolice="Arial",
                                                          ptaille=taillePolice, pstyle="bold",
                                                          command=lambda:self.__saveGPSDomicile())
        btnValiderGPSTravail = self.__arrtk.createButton(self.__gpsTravail,text="Valider",ppolice="Arial",
                                                         ptaille=taillePolice, pstyle="bold",
                                                         command=lambda:self.__saveGPSTravail())
        btnValiderGPSSuppr = self.__arrtk.createButton(self.__gpsSuppr,text="Supprimer",ppolice="Arial",
                                                       ptaille=taillePolice, pstyle="bold",
                                                       command=lambda:self.__supprGPSAdresse())

        btnRetourGPSDomicile = self.__arrtk.createButton(self.__gpsDomicile,text="Retour",ppolice="Arial",
                                                         ptaille=taillePolice, pstyle="bold",
                                                         command=lambda:self.__viewGPSAcceuil())
        btnRetourGPSTravail = self.__arrtk.createButton(self.__gpsTravail,text="Retour",ppolice="Arial",
                                                        ptaille=taillePolice, pstyle="bold",
                                                        command=lambda:self.__viewGPSAcceuil())
        btnRetourGPSSuppr = self.__arrtk.createButton(self.__gpsSuppr,text="Retour",ppolice="Arial",
                                                      ptaille=taillePolice, pstyle="bold",
                                                      command=lambda:self.__viewGPSAcceuil())

        # entry
        self.__entryGPSDomicile = self.__arrtk.createEntry(self.__gpsDomicile,police="Arial",taille=taillePolice,width=300)
        self.__entryGPSTravail = self.__arrtk.createEntry(self.__gpsTravail,police="Arial",taille=taillePolice,width=300)
        #option menu
        self.__menuGPSSuppr = self.__arrtk.createOptionMenu(self.__gpsSuppr, value = ["", ""], var = self.__varSupprGPS)

        # Recherche Frame
        # Label
        labelTitleRecherche = self.__arrtk.createLabel(self.__rechercheFrame,text="Gestion du moteur de recherche",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        # Button
        btnValiderRecherche = self.__arrtk.createButton(self.__rechercheFrame,text="Valider",ppolice="Arial",ptaille=taillePolice,pstyle="bold",command=lambda:self.__saveRecherche())
        # Option Menu
        menuMoteurRecherche = self.__arrtk.createOptionMenu(self.__rechercheFrame,value = listMoteurRecherche,var = self.__varMoteurRecherche)

        # Soft Frame
        # Label
        labelTitleSoft = [self.__arrtk.createLabel(self.__softAcceuil,text="Gestion des logiciels",ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                          self.__arrtk.createLabel(self.__softAdd,text="Ajout de logiciel",ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                          self.__arrtk.createLabel(self.__softSuppr,text="Suppression logiciel",ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                          self.__arrtk.createLabel(self.__softType,text="Type du logicel ",ppolice="Arial",ptaille=taillePolice,pstyle="bold"),
                          self.__arrtk.createLabel(self.__softListe,text="Gestion des logiciels",ppolice="Arial",ptaille=taillePolice,pstyle="bold")]

        # Button
        btnAcceuilSoftAdd = self.__arrtk.createButton(self.__softAcceuil,text="Ajout\nlogiciel",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilSoftSuppr = self.__arrtk.createButton(self.__softAcceuil,text="Suppression\nlogiciel",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilSoftList = self.__arrtk.createButton(self.__softAcceuil,text="Liste\nlogiciel",ppolice="Arial",ptaille=taillePolice,pstyle="bold")

        btnAddSoftValider = self.__arrtk.createButton(self.__softAdd,text="Valider",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAddSoftRetour = self.__arrtk.createButton(self.__softAdd,text="Retour",ppolice="Arial",ptaille=taillePolice,pstyle="bold")

        btnSupprSoftValider = self.__arrtk.createButton(self.__softSuppr,text="Valider",ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnSupprSoftRetour = self.__arrtk.createButton(self.__softSuppr,text="Retour",ppolice="Arial",ptaille=taillePolice,pstyle="bold")



        # Affichage 
        btnIcon.place(x=20,y=20)
        btnAcceuilUser.place(x=140,y=20)
        btnAcceuilMeteo.place(x=260,y=20)
        btnAcceuilGPS.place(x=380,y=20)
        btnAcceuilRecherche.place(x=20,y=140)
        btnAcceuilLogiciel.place(x=140,y=140)
        btnAcceuilInternet.place(x=260,y=140)
        btnAcceuilTheme.place(x=380,y=140)
        btnAcceuilArreraWork.place(x=20,y=260)
        btnAcceuilDownload.place(x=140,y=260)
        btnAcceuilMicro.place(x=260,y=260)
        self.__btnRetourAssistant.place(x=380,y=260)
        # backFrame
        self.__arrtk.placeCenterRight(retourAcceuilBTN)
        # userFrame
        for i in (range(0,len(labelTitleUser))):
            self.__arrtk.placeTopCenter(labelTitleUser[i])

        self.__arrtk.placeRightCenter(btnUserName)
        self.__arrtk.placeLeftCenter(btnUserGenre)

        self.__arrtk.placeBottomLeft(btnValiderUserName)
        self.__arrtk.placeBottomLeft(btnValiderUserGenre)
        self.__arrtk.placeBottomRight(btnRetourUserName)
        self.__arrtk.placeBottomRight(btnRetourUserGenre)

        self.__arrtk.placeCenter(self.__entryNameUser)
        self.__arrtk.placeCenter(menuUserGenre)

        # meteoFrame
        for i in (range(0,len(labelTitleMeteo))):
            self.__arrtk.placeTopCenter(labelTitleMeteo[i])

        self.__arrtk.placeRightCenter(btnAcceuilMeteoDomicile)
        self.__arrtk.placeLeftCenter(btnAcceuilMeteoTravail)
        self.__arrtk.placeCenter(btnAcceuiMeteolVille)
        self.__arrtk.placeBottomCenter(btnAcceuilMeteoSuppr)

        self.__arrtk.placeBottomLeft(btnValiderMeteoDomicile)
        self.__arrtk.placeBottomRight(btnRetourMeteoDomicile)

        self.__arrtk.placeBottomLeft(btnValiderMeteoVille)
        self.__arrtk.placeBottomRight(btnRetourMeteoVille)

        self.__arrtk.placeBottomLeft(btnValiderMeteoTravail)
        self.__arrtk.placeBottomRight(btnRetourMeteoTravail)

        self.__arrtk.placeBottomLeft(btnValiderMeteoSuppr)
        self.__arrtk.placeBottomRight(btnRetourMeteoSuppr)

        self.__arrtk.placeCenter(self.__entryMeteoDomicile)
        self.__arrtk.placeCenter(self.__entryMeteoTravail)
        self.__arrtk.placeCenter(self.__entryMeteoVille)

        for i in range(0,len(labelTitleGPS)):
            self.__arrtk.placeTopCenter(labelTitleGPS[i])

        self.__arrtk.placeRightCenter(btnAcceuilGPSDomicile)
        self.__arrtk.placeLeftCenter(btnAcceuilGPSTravail)
        self.__arrtk.placeCenter(btnAcceuilGPSSuppr)

        self.__arrtk.placeBottomLeft(btnValiderGPSDomicile)
        self.__arrtk.placeBottomRight(btnRetourGPSDomicile)

        self.__arrtk.placeBottomLeft(btnValiderGPSTravail)
        self.__arrtk.placeBottomRight(btnRetourGPSTravail)

        self.__arrtk.placeBottomLeft(btnValiderGPSSuppr)
        self.__arrtk.placeBottomRight(btnRetourGPSSuppr)

        self.__arrtk.placeCenter(self.__entryGPSTravail)
        self.__arrtk.placeCenter(self.__entryGPSDomicile)

        self.__arrtk.placeTopCenter(labelTitleRecherche)
        self.__arrtk.placeCenter(menuMoteurRecherche)
        self.__arrtk.placeBottomCenter(btnValiderRecherche)

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

    def __backAcceuil(self):
        self.__clearAll()
        self.__mainCadre.pack()

    # Methode pour la partie User
    def __viewUserAcceuil(self):
        self.__clearAll()
        self.__userName.pack_forget()
        self.__userGenre.pack_forget()
        self.__userAcceuil.pack()
        self.__userFrame.pack()
        self.__backFrame.pack()

    def __viewUserName(self):
        self.__userName.pack()
        self.__userGenre.pack_forget()
        self.__userAcceuil.pack_forget()

    def __viewUserGenre(self):
        self.__userName.pack_forget()
        self.__userGenre.pack()
        self.__userAcceuil.pack_forget()

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

    def __viewMeteoDomicile(self):
        self.__entryMeteoDomicile.delete(0,END)
        self.__meteoDomicile.pack()
        self.__meteoTravail.pack_forget()
        self.__meteoVille.pack_forget()
        self.__meteoAcceuil.pack_forget()
        self.__meteoSuppr.pack_forget()

    def __viewMeteoTravail(self):
        self.__entryMeteoTravail.delete(0, END)
        self.__meteoDomicile.pack_forget()
        self.__meteoTravail.pack()
        self.__meteoVille.pack_forget()
        self.__meteoAcceuil.pack_forget()
        self.__meteoSuppr.pack_forget()

    def __viewMeteoVille(self):
        self.__entryMeteoVille.delete(0, END)
        self.__meteoDomicile.pack_forget()
        self.__meteoTravail.pack_forget()
        self.__meteoVille.pack()
        self.__meteoAcceuil.pack_forget()
        self.__meteoSuppr.pack_forget()

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
        self.__menuMeteoSuppr = self.__arrtk.createOptionMenu(self.__meteoSuppr,value = listVille,var = self.__varSupprMeteo)
        self.__arrtk.placeCenter(self.__menuMeteoSuppr)

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

    def __viewGPSDomicile(self):
        self.__entryGPSDomicile.delete(0,END)
        self.__gpsDomicile.pack()
        self.__gpsTravail.pack_forget()
        self.__gpsSuppr.pack_forget()
        self.__gpsAcceuil.pack_forget()

    def __viewGPSTravail(self):
        self.__entryGPSTravail.delete(0,END)
        self.__gpsDomicile.pack_forget()
        self.__gpsTravail.pack()
        self.__gpsSuppr.pack_forget()
        self.__gpsAcceuil.pack_forget()

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
        self.__menuGPSSuppr = self.__arrtk.createOptionMenu(self.__gpsSuppr,value = listVille,var = self.__varSupprGPS)
        self.__arrtk.placeCenter(self.__menuGPSSuppr)

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

    def __saveRecherche(self):
        moteur = self.__varMoteurRecherche.get()
        self.__gazelle.changeMoteur(moteur)
        messagebox.showinfo("Parametre","Le moteur de recherche a bien été enregistré")
        self.__backAcceuil()
