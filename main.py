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
superBouton = Button(screen,text="Setting")

def bootSetting():
    superBouton.pack_forget()
    arreraSetting.windows(screen)
    arreraSetting.mainView()
    #arreraSetting.mainView()

superBouton.config(command=bootSetting)
superBouton.pack()
screen.mainloop()