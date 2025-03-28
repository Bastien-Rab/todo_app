import os

FILENAME = "tasks.txt"

def charger_taches():
    if not os.path.exists(FILENAME):
        return []

    with open(FILENAME, "r") as f:
        return [ligne.strip() for ligne in f.readlines()]

def sauvegarder_taches(taches):
    with open(FILENAME, "w") as f:
        for t in taches:
            f.write(t + "\n")

def afficher_taches(taches):
    if not taches:
        print("Aucune tâche enregistrée.")
        return

    print("\n📋 Tâches :")
    for i, t in enumerate(taches, 1):
        print(f"{i}. {t}")

def ajouter_tache(taches):
    tache = input("Entre une nouvelle tâche : ").strip()
    if tache:
        taches.append(tache)
        print("✅ Tâche ajoutée.")
    else:
        print("⛔ Tâche vide ignorée.")

def supprimer_tache(taches):
    afficher_taches(taches)
    index = input("Numéro de la tâche à supprimer : ")
    if index.isdigit():
        i = int(index) - 1
        if 0 <= i < len(taches):
            taches.pop(i)
            print("🗑️ Tâche supprimée.")
        else:
            print("⛔ Numéro invalide.")
    else:
        print("⛔ Entrée invalide.")

def menu():
    print("\n📝 Gestionnaire de tâches")
    print("1. Voir les tâches")
    print("2. Ajouter une tâche")
    print("3. Supprimer une tâche")
    print("4. Quitter")

def run():
    taches = charger_taches()

    while True:
        menu()
        choix = input("Choisis une option : ")

        if choix == "1":
            afficher_taches(taches)
        elif choix == "2":
            ajouter_tache(taches)
        elif choix == "3":
            supprimer_tache(taches)
        elif choix == "4":
            sauvegarder_taches(taches)
            print("👋 À bientôt !")
            break
        else:
            print("⛔ Choix invalide.")

if __name__ == "__main__":
    run()
