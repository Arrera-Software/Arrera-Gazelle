# from setting_gui.CArreraGazelleUIRyleyCopilote import*
from gui.ArreraGazelleUISix import*
from test_gui_setting.test_setting import create_conf

user_conf = create_conf()

def quit(windows):
    windows.destroy()

def main():

    mode = int(input("1. Ryley/Copilote \n2. Six \n# "))
    match mode :
        case 1 :
            windows = aTk(theme_file="theme/theme_bleu_blanc.json")
            gui = CArreraGazelleUIRyleyCopilote(windows,
                                                "json_conf/configUser.json",
                                                "json_conf/configNeuron.json",
                                                "json_conf/sixConfig.json",
                                                "json_conf/configOldSetting.json")
            gui.passQUITFNC(lambda  : quit(windows))
            gui.passApropos(lambda  : print("Apropos"))
        case 2 :
            windows = aTk(theme_file="asset/theme/theme_bleu_blanc.json")
            gui = CArreraGazelleUISix(windows,user_conf)
            windows.maxsize(500,400)
            windows.minsize(500,400)
            gui.passFNCQuit(lambda  : quit(windows))
            gui.passFNCBTNIcon(lambda  : print("Icon"))
        case other :
            print("Invalid input")
            return

    gui.active()

    windows.mainloop()

if __name__ == "__main__":
    main()