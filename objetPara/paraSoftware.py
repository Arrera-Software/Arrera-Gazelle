from tkinter import*
from Librairy.dectectionOS import*
from Librairy.gestionSoftWindows import*
from travailJSON import*
from tkinter import messagebox

class SettingSoftware :
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,settingConfig:jsonWork,neuronFile:jsonWork,textColor:str,color:str):
        #varriable
        self.config = config
        self.assistantFile = neuronFile
        self.varType = StringVar(windows)
        self.varSuppr = StringVar(windows)
        self.listTypeSoft = [
            "Autre",
            "Traitement de texte",
            "Tableur",
            "Presentation",
            "Navigateur Internet",
            "Note",
            "Musique"
        ]
        #declaration cadre
        self.mainFrame = cadre
        self.acceuilFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.addFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.addLinuxFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.supprFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        #objet detction 
        self.dectOS = OS()
        #widget
        labelTitre = [
            Label(self.acceuilFrame,text="Gestion logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addFrame,text="Ajouter un logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.supprFrame,text="Supprimer un logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addLinuxFrame,text="Entrer la commande\npour lancer le logiciel",bg=color,fg=textColor,font=("arial","20")),
            ]
        btnRetour = [
            Button(self.addFrame,text="Supprimer",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.supprFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.addLinuxFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"))
        ]
        #acceuilFrame
        btnAjout=Button(self.acceuilFrame,text="Ajouter un logiciel",bg=color,fg=textColor,font=("arial","15"),command=self.addView) 
        btnSuppr=Button(self.acceuilFrame,text="Supprimer un logiciel",bg=color,fg=textColor,font=("arial","15"),command=self.supprSoft)
        btnSetEmplacement = Button(self.acceuilFrame,text="Definir emplacement",bg=color,fg=textColor,font=("arial","15"),command=self.setEmplacementWindows)
        #supprFrame
        btnValiderSuppr = Button(self.supprFrame,text="Supprimer",bg=color,fg=textColor,font=("arial","15"),command=self.supprSoft) 
        #addFrame
        self.entryNameSoft = Entry(self.addFrame,font=("arial","15"),borderwidth=2,relief="solid")
        menuTypeSoft = OptionMenu(self.addFrame,self.varType,*self.listTypeSoft)
        self.varType.set(self.listTypeSoft[0])
        btnValiderAdd = Button(self.addFrame,text="Ajouter",bg=color,fg=textColor,font=("arial","15")) 
        #addLinuxFram
        self.entryCommandSoft = Entry(self.addLinuxFrame,font=("arial","15"),borderwidth=2,relief="solid")
        btnSaveLinux = Button(self.addLinuxFrame,text="Enregistrer",bg=color,fg=textColor,font=("arial","15")) 
        if (self.dectOS.osLinux()==True):
            btnValiderAdd.configure(command=self.addSoftLinux)
        else :
            if (self.dectOS.osWindows() == True) :
                btnValiderAdd.configure(command=self.addSoftWindows)
                btnValiderSuppr.configure(command=self.supprSoftWindows)

                self.softWin  = gestionSoftWindows(settingConfig.lectureJSON("emplacementSoftWindows"))
        #calcule affichage
        largeurFrame=self.acceuilFrame.winfo_reqwidth()
        hauteurFrame=self.acceuilFrame.winfo_reqheight()
        #Affichage
        #acceuilFrame
        labelTitre[0].place(x=((largeurFrame-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnAjout.place(x=((largeurFrame-btnAjout.winfo_reqwidth())//2),y=200)
        btnSuppr.place(x=((largeurFrame-btnSuppr.winfo_reqwidth())//2),y=275)
        if (self.dectOS.osWindows()==True):
            btnSetEmplacement.place(x=((largeurFrame-btnSetEmplacement.winfo_reqwidth())//2),y=350)
        #addFrame
        labelTitre[1].place(x=((largeurFrame-labelTitre[1].winfo_reqwidth())//2),y=0)
        menuTypeSoft.place(x=10,y=((labelTitre[1].winfo_reqheight()+menuTypeSoft.winfo_reqheight())+5))
        self.entryNameSoft.place(relx=0.5,rely=0.5,anchor="center")
        btnValiderAdd.place(x=0,y=(hauteurFrame-btnValiderAdd.winfo_reqheight()))
        btnRetour[0].place(x=(largeurFrame-btnRetour[0].winfo_reqwidth()),y=(hauteurFrame-btnRetour[0].winfo_reqheight()))
        #suppr Frame
        labelTitre[2].place(x=((largeurFrame-labelTitre[2].winfo_reqwidth())//2),y=0)
        btnValiderSuppr.place(x=0,y=(hauteurFrame-btnValiderSuppr.winfo_reqheight()))
        btnRetour[1].place(x=(largeurFrame-btnRetour[1].winfo_reqwidth()),y=(hauteurFrame-btnRetour[1].winfo_reqheight()))
        #addLinuxFrame
        labelTitre[3].place(x=((largeurFrame-labelTitre[3].winfo_reqwidth())//2),y=0)
        self.entryCommandSoft.place(relx=0.5,rely=0.5,anchor="center")
        btnSaveLinux.place(x=0,y=(hauteurFrame-btnSaveLinux.winfo_reqheight()))
        btnRetour[2].place(x=(largeurFrame-btnRetour[2].winfo_reqwidth()),y=(hauteurFrame-btnRetour[2].winfo_reqheight()))
    
    def view(self)->bool:
        self.mainFrame.pack(side="left")
        self._backAcceuil()
        return True
    
    def _backAcceuil(self):
        self.addFrame.place_forget()
        self.supprFrame.place_forget()
        self.acceuilFrame.place(x=0,y=0)
    
    def addView(self)->bool:
        self.entryNameSoft.delete(0,END)
        self.varType.set(self.listTypeSoft[0])
        self.acceuilFrame.place_forget()
        self.addFrame.place(x=0,y=0)
        return True
    def addSoftLinux(self):
        name = self.entryNameSoft.get()
        self.addFrame.place_forget()
        self.addLinuxFrame.place(x=0,y=0)
    
    def _saveSoftWindows(self,name:str,flag:str,dict:bool):
        if name:
            self.softWin.setName(name)
            sortie = self.softWin.saveSoftware()
            if sortie == True :
                if dict == True :
                    self.config.EcritureJSONDictionnaire(flag,name,self.softWin.getName())
                else :
                    self.config.EcritureJSON(flag,self.softWin.getName())
                messagebox.showinfo("Logiciel sauvegarder","Le logiciel a bien etais enregister")
            else :
                messagebox.showerror("Erreur emplacement","Une erreur c'est produit lors de la selection de l'emplacement")
        else :
            messagebox.showerror("Erreur nom","Vous pouver pas enregister un logiciel sans nom")
    
    def setEmplacementWindows(self):
        sortie = self.softWin.setEmplacementSoft()
        self.assistantFile.EcritureJSON("emplacementSoftWindows",sortie)
    
    def addSoftWindows(self):
        typeSoft = self.varType.get()
        if typeSoft == self.listTypeSoft[0]:
            self._saveSoftWindows(self.entryNameSoft.get(),"dictSoftWindows",True)
        else :
            if typeSoft == self.listTypeSoft[1]:
                self.softWin.setName()
                self._saveSoftWindows("TTexte","wordWindows",False)
            else :
                if typeSoft == self.listTypeSoft[2]:
                    self._saveSoftWindows("tableur","exelWindows",False)
                else :
                    if typeSoft == self.listTypeSoft[3]:
                        self._saveSoftWindows("presentation",)
                    else :
                        if typeSoft == self.listTypeSoft[4]:
                            self._saveSoftWindows("internet","diapoWindows",False)
                        else :
                            if typeSoft == self.listTypeSoft[5]:
                                self._saveSoftWindows("note","noteWindows",False)
                            else :
                                if typeSoft == self.listTypeSoft[6]:
                                    self._saveSoftWindows("musique","musicWindows",False)
        self.entryNameSoft.delete(0,END)
        self._backAcceuil() 
        
    def supprSoft(self):
        if (self.dectOS.osWindows()==True):
            listSoft= list(self.config.lectureJSONDict("dictSoftWindows").keys())
        else :
            listSoft= list(self.config.lectureJSONDict("dictSoftLinux").keys())
        if not listSoft :
            messagebox.showerror("Erreur","Aucun logiciel n'est enregistrer")
        else :
            self.acceuilFrame.place_forget()
            self.supprFrame.place(x=0,y=0)
            self.menuSuppr = OptionMenu(self.supprFrame,self.varSuppr,*listSoft)
            self.menuSuppr.place(relx=0.5,rely=0.5,anchor="center")
            
    def supprSoftWindows(self):
        self._backAcceuil()
        self.config.supprJSONList("dictSoftWindows",self.varSuppr.get())
        self.menuSuppr.destroy() 