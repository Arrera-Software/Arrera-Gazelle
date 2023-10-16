from arreraAssistantSetting import*

screen = Tk()
arreraSetting = ArreraSettingAssistant("configSetting.json",
                                       "FichierConfigAssistant/configNeuron.json",
                                       "FichierConfigAssistant/sixConfig.json"
                                       ,"FileUser/configUser.json")
screen.title("Test Setting")
screen.maxsize(150,150)
screen.minsize(150,150)
screen.config(bg="red")
mainBTN = Button(screen,text="Acceuil")
meteoBTN = Button(screen,text="Meteo")
gpsBTN = Button(screen,text="GPS")

def activeWindows():
    arreraSetting.windows(screen)

def fncQuitter():
    screen.title("Test Setting")
    screen.maxsize(150,150)
    screen.minsize(150,150)
    mainBTN.pack()
    meteoBTN.pack()
    gpsBTN.pack()
    screen.update()

arreraSetting.passageFonctionQuitter(fncQuitter)

def unViewBTN():
    mainBTN.pack_forget()
    meteoBTN.pack_forget()
    gpsBTN.pack_forget()

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
   

mainBTN.config(command=mainSetting)
meteoBTN.config(command=meteoSetting)
gpsBTN.config(command=gpsView)
mainBTN.pack()
meteoBTN.pack()
gpsBTN.pack()
screen.mainloop()