import os
import random
import time
from colorama import Fore, Style

class Chateau:
    def __init__(self):
        self.pv, self.bouclier, self.piege, self.double_attaque = 100, False, False, False

    def attaquer(self, autre_chateau):
        degats = 40 if self.double_attaque else 20
        degats /= 2 if autre_chateau.bouclier else 1
        autre_chateau.pv -= degats
        print(Fore.RED + 'BOOM!' + Style.RESET_ALL)
        self.pv -= 15 if autre_chateau.piege else 0; autre_chateau.piege = False
        self.double_attaque = False
        
    def renforcer(self): self.pv += 10; print(Fore.GREEN + 'Renforcement...' + Style.RESET_ALL); time.sleep(1)

    def activer_bouclier(self): self.bouclier = True; print(Fore.BLUE + 'Bouclier activé!' + Style.RESET_ALL); time.sleep(1)

    def poser_piege(self): self.piege = True; print(Fore.YELLOW + 'Piège posé!' + Style.RESET_ALL); time.sleep(1)

    def preparer_double_attaque(self): self.double_attaque = True; print(Fore.MAGENTA + 'Double attaque préparée!' + Style.RESET_ALL); time.sleep(1)

    est_detruit = lambda self: self.pv <= 0

def decision_bot(chateau_bot, chateau_joueur):
    random_factor = random.random()
    if chateau_bot.pv < 40: return "r" if random_factor < 0.8 else "a"
    elif chateau_joueur.pv < 40: return "a" if random_factor < 0.7 else "b"
    else: return "b" if random_factor < 0.4 else "a"


def affichage_ascii(chateau1, chateau2):
    trait = max(int(chateau1.pv) // 10, int(chateau2.pv) // 10)
    print("--------------------"+ "-" * trait)
    print("| Votre chateau : " + "♥" * (int(chateau1.pv) // 10) + " " * (trait - int(chateau1.pv) // 10))
    print("| Château Ennemi : " + "♥" * (int(chateau2.pv) // 10) + " " * (trait - int(chateau2.pv) // 10))
    print("--------------------"+ "-" * trait)

def jeu():
    chateau1, chateau2, tour = Chateau(), Chateau(), 1
    while not (chateau1.est_detruit() or chateau2.est_detruit()):
        print(f"\n\nTour {tour}\n")
        affichage_ascii(chateau1, chateau2)
        print("\nActions possibles : attaquer (a), renforcer (r), bouclier (b), piège (p), double attaque (d)\n")
        action = input("\033[32mChoisissez une action : \033[31m")
        print("\033[37m")
        if action == "a": chateau1.attaquer(chateau2)
        elif action == "r": chateau1.renforcer()
        elif action == "b": chateau1.activer_bouclier()
        elif action == "p": chateau1.poser_piege()
        elif action == "d": chateau1.preparer_double_attaque()


        os.system("clear")
        if chateau2.est_detruit(): print("Château 2 (Bot) est détruit! Joueur gagne!"); break
        action_bot = decision_bot(chateau2, chateau1)
        if action_bot == "a": print("\033[31mBot attaque!\033[37m"); chateau2.attaquer(chateau1)
        elif action_bot == "r": print("\033[31mBot renforce!\033[37m"); chateau2.renforcer()
        elif action_bot == "b": print("\033[31mBot active le bouclier!\033[37m"); chateau2.activer_bouclier()
        if chateau1.est_detruit(): os.system("clear"); print("Château 1 (Joueur) est détruit! Bot gagne!"); break
        tour += 1

if __name__ == "__main__":
    # Si le script est exécuté directement, on lance le jeu
    jeu()



