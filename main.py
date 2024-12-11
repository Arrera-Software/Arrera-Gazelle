from gui.CArreraGazelleUIRyleyCopilote import*
from gui.ArreraGazelleUISix import*

def quit(windows):
    windows.destroy()

def main():
    arrtk = CArreraTK()
    windows = arrtk.aTK()
    mode = int(input("1. Ryley/Copilote \n2. Six \n# "))
    match mode :
        case 1 :
            gui = CArreraGazelleUIRyleyCopilote(arrtk,windows,
                                                "FileJSON/configUser.json",
                                                "FileJSON/configNeuron.json",
                                                "FileJSON/sixConfig.json",
                                                "FileJSON/configOldSetting.json")
            gui.passQuitFnc(lambda : quit(windows))
        case 2 :
            gui = CArreraGazelleUISix(windows, "FileJSON/configUser.json",
                                    "FileJSON/configNeuron.json",
                                    "FileJSON/sixConfig.json",
                                    "FileJSON/configNewSetting.json")
            windows.maxsize(500,400)
            windows.minsize(500,400)
        case other :
            print("Invalid input")
            return

    gui.active()

    windows.mainloop()

if __name__ == "__main__":
    main()