from src.setting_assistant import six_setting,ryley_copilote_setting

def main():

    mode = int(input("1. Ryley/Copilote \n2. Six \n# "))
    match mode :
        case 1 :
            ryley_copilote_setting()
        case 2 :
            six_setting()
        case other :
            print("Invalid input")
            return

if __name__ == "__main__":
    main()