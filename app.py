import os
import random
import time
from colorama import Fore, Style, init


init(autoreset=True)

def printf(input_string, delay=0.01):
    for char in input_string:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class Chateau:
    def __init__(self, nom):
        self.nom = nom
        self.pv, self.bouclier, self.piege, self.double_attaque, self.pv_precedent = 100, False, False, False, 100

    def attaquer(self, autre_chateau):
        degats = 40 if self.double_attaque else 20
        degats /= 2 if autre_chateau.bouclier == False else 1
        autre_chateau.pv -= degats
        self.pv -= 15 if autre_chateau.piege else 0
        autre_chateau.piege = False
        if self.double_attaque:
            print(f"{self.nom} a lancé une double attaque!")
        self.double_attaque = False
        self.pv_precedent = self.pv
        autre_chateau.bouclier = False  # Remise à zéro du bouclier après l'attaque
        
        
    def renforcer(self):
        self.pv += 10
        self.pv_precedent = self.pv

    def activer_bouclier(self):
        self.bouclier = True

    def poser_piege(self):
        self.piege = True

    def preparer_double_attaque(self):
        self.double_attaque = True
        print(f"{self.nom} se prépare pour une double attaque!")

    est_detruit = lambda self: self.pv <= 0

    def afficher_pv_change(self):
        if self.pv > self.pv_precedent:
            print(f"{self.nom} a "+Fore.GREEN + f"gagné {self.pv - self.pv_precedent} points de vie.")
        elif self.pv < self.pv_precedent:
            print(f"{self.nom} a "+Fore.RED+ f"perdu {self.pv_precedent - self.pv} points de vie.")
        self.pv_precedent = self.pv

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
    print(Fore.MAGENTA + "| " + chateau1.nom + " : " + "♥" * (int(chateau1.pv) // 10) + " " * (trait - int(chateau1.pv) // 10))
    print(Fore.RED + "| " + chateau2.nom + " : " + "♥" * (int(chateau2.pv) // 10) + " " * (trait - int(chateau2.pv) // 10))
    print(Fore.GREEN + "--------------------" + "-" * trait + Style.RESET_ALL)


def jeu():
    chateau1, chateau2, tour = Chateau("Votre chateau"), Chateau("Château Ennemi"), 1
    while not (chateau1.est_detruit() or chateau2.est_detruit()):
        affichage_ascii(chateau1, chateau2)
        chateau1.afficher_pv_change()
        chateau2.afficher_pv_change()
        printf("\nActions possibles : attaquer ⚔️ (a), renforcer 🍎 (r), bouclier 🛡️ (b), piège 🪤 (p), double attaque 🔫 (d)")
        action = input("Choisissez une action : ")
        os.system("clear")

        if action == "a":
            printf("Vous Attaquez ⚔️")
            chateau1.attaquer(chateau2)
        elif action == "r":
            printf("Vous Renforcez 🍎")
            chateau1.renforcer()
        elif action == "b":
            printf("Vous utilisez Bouclier 🛡️")
            chateau1.activer_bouclier()
        elif action == "p":
            printf("Vous posez un piege 🪤")
            chateau1.poser_piege()
        elif action == "d":
            printf("Vous Double attaquez 🔫")
            chateau1.preparer_double_attaque()

        if chateau2.est_detruit():
            printf("Château 2 (Bot) est détruit! Joueur gagne!")
            break
        time.sleep(0.5)

        action_bot = decision_bot(chateau2, chateau1)
        if action_bot == "a":
            printf("Bot utilise Attaque ⚔️")
            chateau2.attaquer(chateau1)
        elif action_bot == "r":
            printf("Bot utilise Renforcement 🍎")
            chateau2.renforcer()
        elif action_bot == "b":
            printf("Bot utilise Bouclier 🛡️")
            chateau2.activer_bouclier()

        chateau1.bouclier = False  # Remise à zéro du bouclier du joueur à la fin du tour
        chateau2.bouclier = False  # Remise à zéro du bouclier du bot à la fin du tour

        time.sleep(0.5)
        if chateau1.est_detruit():
            printf("Château 1 (Joueur) est détruit! Bot gagne!")
            break

        tour += 1

if __name__ == "__main__":
    os.system("clear")  # Effacer l'écran au début du jeu
    printf("Bienvenue dans le jeu Château Bataille!")
    printf("Vous devez Buter le chateaux enemie !")
    printf("...",1)
    os.system("clear")
    print(Fore.GREEN +"Début de la game")
    jeu()