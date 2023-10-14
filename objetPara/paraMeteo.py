
from tkinter import*
from travailJSON import*

class SettingMeteo :
    def __init__(self,varFenetre:StringVar,cadre:Frame,config:jsonWork,textColor:str,color:str):
        #varriable
        varChoix = varFenetre
        self.configFile = config
        listVille = [str]
        centrageLargeur = int
        #declaration cadre
        self.mainFrame = cadre
        self.listFrame = Frame(self.mainFrame,bg=color,width=150,height=600)
        self.addVilleFrame = Frame(self.mainFrame,bg=color,width=150,height=600)
        self.supprVilleFrame = Frame(self.mainFrame,bg=color,width=150,height=600)
        self.addFrame = Frame(self.mainFrame,bg=color,width=150,height=600)
        self.supprFrame = Frame(self.mainFrame,bg=color,width=150,height=600)
        labelTitre = [
            Label(self.mainFrame,text="Parametre Meteo",bg=color,fg=textColor,font=("arial","20")),
            Label(self.listFrame,text="Parametre Meteo",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addVilleFrame,text="Ajouter un lieu",bg=color,fg=textColor,font=("arial","20")),
            Label(self.supprVilleFrame,text="Supprimer un lieu",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addFrame,text="Ecrivez la ville que vous voulez rajouter",bg=color,fg=textColor,font=("arial","20")),
            Label(self.supprFrame,text="Selectionner la ville que vous voulez supprimer",bg=color,fg=textColor,font=("arial","20"))
        ]
        btnRetour = [
            Button(self.listFrame,text="Retour",bg=color,fg=textColor),
            Button(self.addVilleFrame,text="Retour",bg=color,fg=textColor),
            Button(self.supprVilleFrame,text="Retour",bg=color,fg=textColor),
            Button(self.addFrame,text="Annuler",bg=color,fg=textColor),
            Button(self.supprFrame,text="Annuler",bg=color,fg=textColor)
        ]
        #Frame mainFrame
        btnListMeteo =  Button(self.mainFrame,text="      Liste meteo      ",bg=color,fg=textColor,font=("arial","15"))
        btnAddVille =   Button(self.mainFrame,text="   Ajouter une ville   ",bg=color,fg=textColor,font=("arial","15"))
        btnSupprVille = Button(self.mainFrame,text="   Supprimer une ville ",bg=color,fg=textColor,font=("arial","15"))
        #frame listFrame
        labelListe = Label(self.listFrame,bg=color,fg=textColor)
        #frame addVille
        btnAddHome = Button(self.addVilleFrame,text="Lieu de domicile",bg=color,fg=textColor)
        btnAddWork = Button(self.addVilleFrame,text="Lieu de travail",bg=color,fg=textColor)
        btnAddTonw = Button(self.addVilleFrame,text="Autre lieu",bg=color,fg=textColor)
        #frame supprville
        btnSupprHome = Button(self.supprVilleFrame,text="Lieu de domicile",bg=color,fg=textColor)
        btnSupprWork = Button(self.supprVilleFrame,text="Lieu de travail",bg=color,fg=textColor)
        btnSupprTonw = Button(self.supprVilleFrame,text="Autre lieu",bg=color,fg=textColor)
        #frame addFrame
        entryVille = Entry(self.addFrame,font=("arial","11"),borderwidth=2,relief="solid")
        btnAddValidate = Button(self.addFrame,text="Valider",bg=color,fg=textColor)
        #frame supprFrame
        menuVille = OptionMenu(self.supprFrame,varChoix,*listVille)
        btnSupprValidate = Button(self.supprFrame,text="Valider",bg=color,fg=textColor)
        #recuperartion valeur 
        centrageLargeur = self.mainFrame.winfo_reqwidth()
        #affichage
        labelTitre[0].place(x=((centrageLargeur-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnListMeteo.place(x=((centrageLargeur-btnListMeteo.winfo_reqwidth())//2),y=200)
        btnAddVille.place(x=((centrageLargeur-btnAddVille.winfo_reqwidth())//2),y=275)
        btnSupprVille.place(x=((centrageLargeur-btnSupprVille.winfo_reqwidth())//2),y=350)
        
    def view(self):
        self.mainFrame.pack(side="left")
        
    
        
        
        