from gui.ArreraGazelleUIOld import*
from gui.ArreraGazelleUI import*



def quit(windows):
    windows.destroy()

def main():
    windows = Tk()
    mode = int(input("1. Old\n2.New\n# "))
    match mode :
        case 1 :
            gui = CArreraGazelleUIOld(windows,"FileJSON/configUser.json",
                                    "FileJSON/configNeuron.json",
                                    "FileJSON/sixConfig.json",
                                    "FileJSON/configOldSetting.json")
            gui.passQuitFnc(quit)
        case 2 :
            gui = CArreraGazelleUI(windows,"FileJSON/configUser.json",
                                    "FileJSON/configNeuron.json",
                                    "FileJSON/sixConfig.json",
                                    "FileJSON/configNewSetting.json")
            windows.maxsize(500,400)
            windows.minsize(500,400)
        case other :
            print("Invalid input")
            return

    mode = int(input("1 : Dark \n2 : Light \n# "))

    match mode :
        case 1 :
            gui.active(True)
        case 2 :
            gui.active(False)

    windows.mainloop()

if __name__ == "__main__":
    main()