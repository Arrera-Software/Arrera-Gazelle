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

        self.__backFrame = self.__arrtk.createFrame(self.__windows,width=500,height=70)

        # Variable
        # Taille Police
        taillePolice = 20
        # Liste
        listGenre = jsonSetting.lectureJSONList("listGenre")
        # Icon Assistant
        iconAssistant = self.__arrtk.createImage(jsonSetting.lectureJSON("iconSoft"),tailleX=95,tailleY=95)
        # String var
        self.__varNameUser = StringVar(self.__windows)
        self.__varSupprMeteo = StringVar(self.__windows)
        # Widget 
        # Main frame
        btnIcon = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,image=iconAssistant)
        btnAcceuilUser = self.__arrtk.createButton(self.__mainCadre, width=100, height=100, text="Utilisateur"
                                                   , ppolice="Arial", ptaille=taillePolice-2, pstyle="bold", command= lambda  : self.__viewUserAcceuil())
        btnAcceuilMeteo = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Meteo"
                                                    ,ppolice="Arial",ptaille=taillePolice,pstyle="bold",command=lambda:self.__viewMeteoAcceuil())
        btnAcceuilGPS = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="GPS"
                                                  ,ppolice="Arial",ptaille=taillePolice,pstyle="bold")
        btnAcceuilRecherche = self.__arrtk.createButton(self.__mainCadre,width=100,height=100,text="Recherche"
                                                        ,ppolice="Arial",ptaille=taillePolice-2,pstyle="bold")
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

    # Methode generale
    def active(self):
        self.__mainCadre.pack()

    def __clearAll(self):
        self.__mainCadre.pack_forget()
        self.__userFrame.pack_forget()
        self.__backFrame.pack_forget()
        self.__meteoFrame.pack_forget()
        self.__gpsFrame.pack_forget()

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