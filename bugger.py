notes = []
historique = []

while True:
    print("\n=== MENU ===")
    print("1. Ajouter une note")
    print("2. Voir la moyenne")
    print("3. Voir l'historique d'exécution")
    print("4. Quitter")
    
    choix = input("Ton choix (1-4) : ")
    
    if choix == "1":
        note = int(input("saisie une note: "))
        
        # 1. On ajoute le NOMBRE dans la liste des notes
        notes.append(note)
        
        # 2. On ajoute l'ACTION (texte) dans l'historique
        historique.append(f"Ajout de la note : {note}")
        
        if note >= 15:
            print("u did well go play go play")
        else:
            print("better luck next feetie, you a playahh")
            
        print(f"nouvelle note saisie est : {note}")
        
    elif choix == "2":
        # On vérifie qu'il y a au moins une note enregistrée
        if len(notes) > 0:
            # Somme de toutes les notes divisée par le nombre de notes
            moy = sum(notes) / len(notes)
            
            if moy >= 15:
                print("u getting into harvarddddd")
            else:
                print("more studying keep the funk away, better luck next time?")
                
            print(f"la moyenne est : {moy}")
            
            # On enregistre le calcul dans l'historique
            historique.append(f"Consultation de la moyenne : {moy}")
        else:
            print("Aucune note enregistrée pour l'instant !")
            
    elif choix == "3":
        print("\n--- HISTORIQUE DES EXÉCUTIONS ---")
        if len(historique) == 0:
            print("L'historique est vide.")
        else:
            # On affiche CHAQUE entrée de l'historique une par une
            for entree in historique:
                print(f"- {entree}")
                
    elif choix == "4":
        print("Bye twin ! 👋")
        break