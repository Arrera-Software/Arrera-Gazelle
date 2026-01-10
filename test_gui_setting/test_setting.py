from Arrera_neuron.gestionnaire.gestion import gestionnaire
from Arrera_neuron.config.confNeuron import confNeuron

def create_conf():
    conf = confNeuron(name="Opale",
                      lang="fr",
                      icon="setting_asset/icon.png",
                      asset="setting_asset/",
                      assistant_color="white",
                      assistant_texte_color="black",
                      bute="developper un algo de ChatBot qui sera inclut dans SIX et Ryley",
                      createur="Pauchet Baptiste",
                      listFonction=["ouvrir une application", "aider sur les recherches de internet", "donner la meteo",
                                    "faire un résumer des actualités"],
                      moteurderecherche="google",
                      etatService=1,
                      etatTime=1,
                      etatOpen=1,
                      etatSearch=1,
                      etatChatbot=1,
                      etatApi=1,
                      etatCodehelp=1,
                      etatWork=1,
                      etatSocket=1,
                      lienDoc="www.google.com",
                      fichierLangue="language/vouvoiment/",
                      fichierKeyword="keyword/",
                      voiceAssistant=True)
    gest = gestionnaire(conf)
    return gest.getUserConf()