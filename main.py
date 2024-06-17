from gui.ArreraGazelleUIOld import*

windows = Tk()
oldGui = CArreraGazelleUI(windows,"FileJSON/configUser.json",
                          "FileJSON/configNeuron.json",
                          "FileJSON/sixConfig.json",
                          "FileJSON/configSetting.json")
def quit():
    windows.destroy()
    
oldGui.passQuitFnc(quit)
mode = int

mode = int(input("1 : Dark \n2 : Light \n#"))

match mode :
    case 1 : 
        oldGui.active(True)
    case 2 :
        oldGui.active(False)

windows.mainloop()

#"FileJSON/configUser.json","FileJSON/configNeuron.json","FileJSON/sixConfif.json"