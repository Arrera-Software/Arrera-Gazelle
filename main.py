from gui.ArreraGazelleUIOld import*

windows = Tk()
oldGui = CArreraGazelleUI(windows,"FileJSON/configUser.json",
                          "FileJSON/configNeuron.json",
                          "FileJSON/sixConfif.json",
                          "FileJSON/configSetting.json")
oldGui.active(True)
windows.mainloop()

#"FileJSON/configUser.json","FileJSON/configNeuron.json","FileJSON/sixConfif.json"