import os
import random
import time
from colorama import Fore, Style, init

init(autoreset=True)
class Chateau:
    def __init__(self):
        self.pv, self.bouclier, self.piege, self.double_attaque = 100, False, False, False

    def attaquer(self, autre_chateau):
        degats = 40 if self.double_attaque else 20
        degats /= 2 if autre_chateau.bouclier else 1
        autre_chateau.pv -= degats
        self.pv -= 15 if autre_chateau.piege else 0
        autre_chateau.piege = False
        self.double_attaque = False
        
    def renforcer(self):
        self.pv += 10

    def activer_bouclier(self):
        self.bouclier = True

    def poser_piege(self):
        self.piege = True

    def preparer_double_attaque(self):
        self.double_attaque = True

    est_detruit = lambda self: self.pv <= 0

def decision_bot(chateau_bot, chateau_joueur):
    random_factor = random.random()
    if chateau_bot.pv < 40:
        return "r" if random_factor < 0.8 else "a"
    elif chateau_joueur.pv < 40:
        return "a" if random_factor < 0.7 else "b"
    else:
        return "b" if random_factor < 0.4 else "a"

def affichage_ascii(chateau1, chateau2):
    trait = max(int(chateau1.pv) // 10, int(chateau2.pv) // 10)
    print(Fore.GREEN + "--------------------" + "-" * trait)
    print(Fore.MAGENTA + "| Votre chateau : " + "♥" * (int(chateau1.pv) // 10) + " " * (trait - int(chateau1.pv) // 10))
    print(Fore.RED + "| Château Ennemi : " + "♥" * (int(chateau2.pv) // 10) + " " * (trait - int(chateau2.pv) // 10))
    print(Fore.GREEN + "--------------------" + "-" * trait + Style.RESET_ALL)


def jeu():
    chateau1, chateau2, tour = Chateau(), Chateau(), 1
    while not (chateau1.est_detruit() or chateau2.est_detruit()):
        affichage_ascii(chateau1, chateau2)
        action = input("Actions possibles : attaquer ⚔️ (a), renforcer 🍎 (r), bouclier 🛡️ (b), piège 🪤 (p), double attaque 🔫 (d)\nChoisissez une action : ")
        os.system("clear")

        if action == "a":
            print("Vous Attaquez ⚔️")
            chateau1.attaquer(chateau2)
        elif action == "r":
            print("Vous Renforcez 🍎")
            chateau1.renforcer()
        elif action == "b":
            print("Vous utilisez Bouclier 🛡️")
            chateau1.activer_bouclier()
        elif action == "p":
            print("Vous posez un piege 🪤")
            chateau1.poser_piege()
        elif action == "d":
            print("Vous Double attaquez 🔫")
            chateau1.preparer_double_attaque()

        if chateau2.est_detruit():
            print("Château 2 (Bot) est détruit! Joueur gagne!")
            break
        
        action_bot = decision_bot(chateau2, chateau1)
        if action_bot == "a":
            print("Bot utilise Attaque ⚔️")
            chateau2.attaquer(chateau1)
        elif action_bot == "r":
            print("Bot utilise Renforcement 🍎")
            chateau2.renforcer()
        elif action_bot == "b":
            print("Bot utilise Bouclier 🛡️")
            chateau2.activer_bouclier()
            
        if chateau1.est_detruit():
            print("Château 1 (Joueur) est détruit! Bot gagne!")
            break
        tour += 1

if __name__ == "__main__":
    os.system("clear")  # Effacer l'écran au début du jeu
    print("Bienvenue dans le jeu Château Bataille!")
    print("Vous êtes prêt à combattre!")
    time.sleep(2)
    os.system("clear")
    jeu()