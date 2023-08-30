import os
import random


class Chateau:
    # Initialisation de la classe Chateau
    def __init__(self):
        self.pv = 100  # Points de vie du château
        self.bouclier = False  # Indicateur si le bouclier est actif
        self.piege = False  # Indicateur si un piège est posé
        self.double_attaque = False  # Indicateur si une double attaque est préparée

    # Méthode pour attaquer un autre château
    def attaquer(self, autre_chateau):
        degats = 40 if self.double_attaque else 20  # Dégâts de l'attaque
        if autre_chateau.bouclier:  # Si le château attaqué a un bouclier, les dégâts sont réduits de moitié
            degats /= 2
        autre_chateau.pv -= degats  # Soustraction des dégâts aux points de vie du château attaqué
        if autre_chateau.piege:  # Si le château attaqué a un piège, le château attaquant perd 15 points de vie
            self.pv -= 15
            autre_chateau.piege = False  # Le piège est désactivé après utilisation
        self.double_attaque = False  # La double attaque est désactivée après utilisation

    # Méthode pour renforcer le château (augmente les points de vie)
    def renforcer(self):
        self.pv += 10

    # Méthode pour activer le bouclier
    def activer_bouclier(self):
        self.bouclier = True

    # Méthode pour poser un piège
    def poser_piege(self):
        self.piege = True

    # Méthode pour préparer une double attaque
    def preparer_double_attaque(self):
        self.double_attaque = True

    # Méthode pour vérifier si le château est détruit (points de vie <= 0)
    def est_detruit(self):
        return self.pv <= 0

def decision_bot(chateau_bot, chateau_joueur):
    random_factor = random.random()  # Génère un nombre aléatoire entre 0 et 1
    
    if chateau_bot.pv < 40:
        if random_factor < 0.8:  # 80% de chance de renforcer si les points de vie sont bas
            return "r"
        else:
            return "a"
    elif chateau_joueur.pv < 40:
        if random_factor < 0.7:  # 70% de chance d'attaquer si les points de vie du joueur sont bas
            return "a"
        else:
            return "b"
    else:
        if random_factor < 0.4:  # 40% de chance d'activer le bouclier si les points de vie sont suffisants
            return "b"
        else:
            return "a"


def affichage_ascii(chateau1, chateau2):
    # Affichage de l'état des châteaux en utilisant des coeurs pour représenter les points de vie
    if (int(chateau1.pv) // 10) > (int(chateau2.pv) // 10):
        trait = (int(chateau1.pv) // 10)
    else :
        trait = (int(chateau2.pv) // 10)
    print("--------------------"+ "-" * trait)
    print("| Votre chateau : " + "♥" * (int(chateau1.pv) // 10))
    print("| Château Ennemi : " + "♥" * (int(chateau2.pv) // 10))
    print("--------------------"+ "-" * trait)

def jeu():
    # Initialisation du jeu
    chateau1 = Chateau()  # Création du château du joueur
    chateau2 = Chateau()  # Création du château du bot
    tour = 1  # Initialisation du compteur de tours

    # Boucle de jeu qui continue tant qu'aucun château n'est détruit
    while not (chateau1.est_detruit() or chateau2.est_detruit()):
        print(f"Tour {tour}")  # Affichage du numéro du tour
        affichage_ascii(chateau1, chateau2)  # Affichage de l'état des châteaux

        # Le joueur choisit son action
        action = input("\033[32mChoisissez une action - attaquer (a), renforcer (r), bouclier (b), piège (p), double attaque (d) : \033[31m")
        print("\033[37m")
        if action == "a":  # Si le joueur choisit d'attaquer
            chateau1.attaquer(chateau2)
        elif action == "r":  # Si le joueur choisit de renforcer
            chateau1.renforcer()
        elif action == "b":  # Si le joueur choisit d'activer le bouclier
            chateau1.activer_bouclier()
        elif action == "p":  # Si le joueur choisit de poser un piège
            chateau1.poser_piege()
        elif action == "d":  # Si le joueur choisit de préparer une double attaque
            chateau1.preparer_double_attaque()


        os.system("clear")
        # Si le château du bot est détruit, le joueur gagne
        if chateau2.est_detruit():
            print("Château 2 (Bot) est détruit! Joueur gagne!")
            break

        # Le bot choisit son action
        action_bot = decision_bot(chateau2, chateau1)
        if action_bot == "a":  # Si le bot choisit d'attaquer
            print("\033[31mBot attaque!\033[37m")
            chateau2.attaquer(chateau1)
        elif action_bot == "r":  # Si le bot choisit de renforcer
            print("\033[31mBot renforce!\033[37m")
            chateau2.renforcer()
        elif action_bot == "b":  # Si le bot choisit d'activer le bouclier
            print("\033[31mBot active le bouclier!\033[37m")
            chateau2.activer_bouclier()

        # Si le château du joueur est détruit, le bot gagne
        if chateau1.est_detruit():
            os.system("clear")
            print("Château 1 (Joueur) est détruit! Bot gagne!")
            
            break

        tour += 1  # Incrémentation du compteur de tours

if __name__ == "__main__":
    # Si le script est exécuté directement, on lance le jeu
    jeu()


