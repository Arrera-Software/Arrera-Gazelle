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

def activeWindows():
    arreraSetting.windows(screen)

def fncQuitter():
    screen.title("Test Setting")
    screen.maxsize(150,150)
    screen.minsize(150,150)
    mainBTN.pack()
    meteoBTN.pack()
    screen.update()

arreraSetting.passageFonctionQuitter(fncQuitter)

def unViewBTN():
    mainBTN.pack_forget()
    meteoBTN.pack_forget()

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
   

mainBTN.config(command=mainSetting)
meteoBTN.config(command=meteoSetting)
mainBTN.pack()
meteoBTN.pack()
screen.mainloop()