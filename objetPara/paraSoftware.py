from tkinter import*
from Librairy.dectectionOS import*
from travailJSON import*
from tkinter import messagebox

class SettingSoftware :
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,textColor:str,color:str):
        #varriable
        self.config = config
        #declaration cadre
        self.mainFrame = cadre
        self.acceuilFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.addFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.supprFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        #objet detction 
        dectOS = OS()
        #widget
        labelTitre = [
            Label(self.acceuilFrame,text="Gestion logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addFrame,text="Ajouter un logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addFrame,text="Supprimer un logiciel",bg=color,fg=textColor,font=("arial","20"))]
        btnRetour = [
            Button(self.addFrame,text="Supprimer",bg=color,fg=textColor,font=("arial","15")),
            Button(self.supprFrame,text="Supprimer",bg=color,fg=textColor,font=("arial","15"))
        ]
        #acceuilFrame
        btnAjout=Button(self.acceuilFrame,text="Ajouter un logiciel",bg=color,fg=textColor,font=("arial","15")) 
        btnSuppr=Button(self.acceuilFrame,text="Supprimer un logiciel",bg=color,fg=textColor,font=("arial","15"))
        #supprFrame
        btnValiderSuppr = Button(self.supprFrame,text="Supprimer",bg=color,fg=textColor,font=("arial","15")) 
        #addFrame
        entryNameSoft = Entry(self.addFrame,font=("arial","15"),borderwidth=2,relief="solid")
        btnValiderAdd = Button(self.addFrame,text="Ajouter",bg=color,fg=textColor,font=("arial","15")) 
        """
        if (dectOS.osWindows() == True) :
            
        else :
        """
        #calcule affichage
        largeurFrame=self.acceuilFrame.winfo_reqwidth()
        hauteurFrame=self.acceuilFrame.winfo_reqheight()
        #Affichage
        labelTitre[0].place(x=((largeurFrame-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnAjout.place(x=((largeurFrame-btnAjout.winfo_reqwidth())//2),y=200)
        btnSuppr.place(x=((largeurFrame-btnSuppr.winfo_reqwidth())//2),y=275)
    
    def view(self)->bool:
        self.mainFrame.pack(side="left")
        self.acceuilFrame.place(x=0,y=0)
        return True
        
        