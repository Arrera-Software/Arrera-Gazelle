from arreraAssistantSetting import*

screen = Tk()
arreraSetting = ArreraSettingAssistant("configSetting.json",
                                       "FichierConfigAssistant/configNeuron.json",
                                       "FichierConfigAssistant/sixConfig.json"
                                       ,"FileUser/configUser.json")
screen.title("Test Setting")

screen.minsize(150,150)
screen.config(bg="red")
mainBTN = Button(screen,text="Acceuil")
meteoBTN = Button(screen,text="Meteo")
gpsBTN = Button(screen,text="GPS")
rechercheBTN = Button(screen,text="Recherche")
softwareBTN = Button(screen,text="Software")
internetBTN = Button(screen,text="Internet")

def activeWindows():
    arreraSetting.windows(screen,"dark")

def fncQuitter():
    screen.title("Test Setting")
    screen.minsize(150,150)
    mainBTN.pack()
    meteoBTN.pack()
    gpsBTN.pack()
    rechercheBTN.pack()
    softwareBTN.pack()
    internetBTN.pack()
    screen.update()

arreraSetting.passageFonctionQuitter(fncQuitter)

def unViewBTN():
    mainBTN.pack_forget()
    meteoBTN.pack_forget()
    gpsBTN.pack_forget()
    rechercheBTN.pack_forget()
    softwareBTN.pack_forget()
    internetBTN.pack_forget()

def mainSetting():
    unViewBTN()
    activeWindows()
    arreraSetting.mainView()
    screen.update()

def meteoSetting():
    unViewBTN()
    activeWindows()
    arreraSetting.meteoView()
    screen.update()
    
def gpsView():
    unViewBTN()
    activeWindows()
    arreraSetting.gpsView()
    screen.update()
    
def rechercheView():
    unViewBTN()
    activeWindows()
    arreraSetting.rechercheView()
    screen.update()
    
def softwareView():
    unViewBTN()
    activeWindows()
    arreraSetting.softwareView()
    screen.update()
    
def internetView():
    unViewBTN()
    activeWindows()
    arreraSetting.internetView()
    screen.update()

mainBTN.config(command=mainSetting)
meteoBTN.config(command=meteoSetting)
gpsBTN.config(command=gpsView)
rechercheBTN.config(command=rechercheView)
softwareBTN.config(command=softwareView)
internetBTN.config(command=internetView)
mainBTN.pack()
meteoBTN.pack()
gpsBTN.pack()
rechercheBTN.pack()
softwareBTN.pack()
internetBTN.pack()
screen.mainloop()