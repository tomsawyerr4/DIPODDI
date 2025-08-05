import random 
from Kine import programme_kine
from CardioSalle import echauffement_cardio, puissanceTapis, puissanceVelo,Endurance,Resistance,Sprint,pertePoids
from musculationSalle import Objectives_Musculation_Salle,Groupes_Musculaire,musculationSalle,musculationSalleSpecifique
from MusculationSalleCardio import musculationSalleCardio
from programmeMaison import programmeMaison
from ProgrammeDehors import PerteDePoids,puissance,remiseEnForme,BoxTOBOX
from Bonus import ProgammeBonus
import re
from getLinkYtb import programme_musculation, programme_musculation_haut, programme_musculation_bas

Niveaux = ['Débutant',"Intermidiaire","Avancé"]

def programme_seance(choix,objective_kine,theme,niveau):

    echauffement = ''
    programme_seance = ''

    mets_principal = 0
    mets_echauffement = 0
    mets_bonus = 0
    mets_total = 0

    # programme_seance += f'Kine {objective_kine} \n'
    programme_kin, mets_echauffement = programme_kine(objective_kine)
    programme_seance +=  programme_kin    ## Generale/Specifique


    ajout_Bonus = random.choice([0,1])

    if choix == 'MUSCULATION EN SALLE':
        pr = random.randint(0,1)
        if pr== 0:
            programme_musculation_choisi = programme_musculation_haut
        else :
            programme_musculation_choisi = programme_musculation_bas
        #programme_musculation_choisi = random.choice([programme_musculation_haut, programme_musculation_bas]) # Soit le haut soit le bas
        #print(programme_musculation)
        programme_princ, mets_principal = musculationSalle('General',theme,programme_musculation)
        programme_seance += programme_princ
    
    elif choix == 'MUSCULATION EN SALLE (Specifique)':
        obj = random.choice([
            "ENDURANCE DE FORCE", "FORCE MAX", 
            "PERTE DE POIDS", "REMISE EN FORME", "RÉPÉTITIONS DES EFFORTS", 
            "FORCE EXPLOSIVE"
        ])
        programme_seance += musculationSalleSpecifique(theme,obj)
    
    elif choix == 'CARDIO EN SALLE':



        if theme == 'PUISSANCE':
            mets_principal = 38 #16+5+10+7
        elif theme == 'ENDURANCE':
            mets_principal = 34.5 #12.5+5+10+7
        elif theme == 'RÉSISTANCE':
            mets_principal = 36 #14+5+10+7
        elif theme == 'SPRINT':
            mets_principal = 40 #18+5+10+7
        elif theme == 'PERTE DE POIDS':
            mets_principal = 36 #14+5+10+7

        echauffement = echauffement_cardio()
        programme_seance += echauffement
        ajout_Bonus = 1

        # programme_seance += theme + '\n'
        if theme == 'PUISSANCE':
            mets_principal = 21 #16+5
            # lettre = random.choice(["A","B","C","D","E","F","G","H","I"])
            # if lettre in ['H','I']:
            #     programme_seance += puissanceTapis(lettre)
            # else:
            #     programme_seance += random.choice([puissanceTapis(lettre),puissanceVelo(lettre)])
            programme_seance += random.choice([puissanceTapis('A'),puissanceVelo('A')])

        elif theme == 'ENDURANCE':
            mets_principal = 22.5 #12.5+10
            # lettre = random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"])

            programme_seance += Endurance("A")
        
        elif theme == 'RÉSISTANCE':
            # lettre = random.choice(["A","B","C","D"])

            programme_seance+= Resistance("A")
        
        elif theme == 'SPRINT':
            # lettre = random.choice(["A","B","C"])

            programme_seance += Sprint("A")
        
        elif theme == 'PERTE DE POIDS':
            # lettre = random.choice(["A","B","C","D"])
            programme_seance += pertePoids("A")

    elif choix == 'MUSCULATION EN SALLE + CARDIO(Generale)':
        prog, mets_principal = musculationSalleCardio(theme,'')
        programme_seance +=prog

        #programme_seance += musculationSalleCardio(theme,'')
    
    elif choix == 'MUSCULATION EN SALLE + CARDIO(Specifique)':
        obj = random.choice([
            "ENDURANCE DE FORCE", "FORCE MAX", 
            "PERTE DE POIDS", "REMISE EN FORME", "RÉPÉTITIONS DES EFFORTS", 
            "FORCE EXPLOSIVE"
        ])

        prog, mets_principal = musculationSalleCardio(obj,theme)
        programme_seance += prog
    
    elif choix == 'PROGRAMME MAISON':
        ajout_Bonus = 1
        prog, mets_principal = programmeMaison(theme)
        programme_seance += prog
        #programme_seance += programmeMaison(theme)
    
    elif choix == 'PROGRAMME DEHORS':
        ajout_Bonus = 1
        # programme_seance += echauffement_dehors()
        # programme_seance += theme + '\n'

        if theme == 'PERTE DE POIDS':
            lettre = random.choice(["A","B","C","D","E","F","G","H","I"])
            mets_principal = 38 #5+10+15+8
            programme_seance += PerteDePoids(lettre)
        elif theme == 'PUISSANCE':
            lettre = random.choice(["A","B","C","D","E","F","G","H","I"])
            programme_seance += puissance(lettre)
            mets_principal = 41 #7 + 10 + 16 + 8
        elif theme == 'REMISE EN FORME':
            lettre = random.choice(["A","B","C","D","E","F"])
            programme_seance+= remiseEnForme(lettre)
            mets_principal = 41 #7 + 10 + 16 + 8
        elif theme == 'BOX TO BOX':
            lettre = random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N"])
            programme_seance += BoxTOBOX(lettre)
            mets_principal = 39 #5+10+16+8
        
    else:
        programme_seance = 'choix invalide'


    ### partie Bonus


    if ajout_Bonus == 1:
        exercices_Bonus, mets_bonus = ProgammeBonus(niveau)

        programme_seance += f'PARTIE BONUS: \n {exercices_Bonus}'
    else:
        pass
    mets_total= mets_echauffement + mets_principal + mets_bonus

    return theme + '\n' + programme_seance + '\n Dépense énergétique de la seance: ' + str(mets_total) + 'METS'

def supprimer_doublons_terminer_par(programme):
    """
    Supprime les répétitions de la section "Terminer Par" et "Bonus supplémentaire" dans le texte du programme.
    """
    lignes = programme.split("\n")
    resultat = []
    terminer_par_buffer = set()  
    bonus_supplementaire_buffer = set() 
    skip_section = False

    for ligne in lignes:
        if "Terminer Par :" in ligne:
            if ligne in terminer_par_buffer:
                skip_section = True  # Ignorer cette section redondante
            else:
                terminer_par_buffer.add(ligne)
                resultat.append(ligne)
                skip_section = False

        # Détecter "Bonus supplémentaire"
        elif "--- Bonus supplémentaire ---" in ligne:
            if ligne in bonus_supplementaire_buffer:
                skip_section = True  # Ignorer cette section redondante
            else:
                bonus_supplementaire_buffer.add(ligne)
                resultat.append(ligne)
                skip_section = False

        # Ajouter les autres lignes (uniquement si non ignorées)
        elif not skip_section:
            resultat.append(ligne)
        else:
            skip_section = False  # Réinitialiser après avoir sauté une section

    return "\n".join(resultat)



def programme_semaine_utilisateur(choix, theme_principal, nbr_seances, niveau):
    """
    Génère un programme hebdomadaire basé sur le choix de l'utilisateur, 
    le thème principal, le nombre de séances, et le niveau.
    """
    # Liste des thèmes disponibles en fonction du choix de programme
    themes_possibles = {
        'MUSCULATION EN SALLE': [
            "ENDURANCE DE FORCE", "FORCE MAX", "MASSE MUSCULAIRE", 
            "PERTE DE POIDS", "REMISE EN FORME", "RÉPÉTITIONS DES EFFORTS", 
            "FORCE EXPLOSIVE"
        ],
        'MUSCULATION EN SALLE (Specifique)': ["BRAS" ,"DOS" ,"ÉPAULE","PECTORAUX","JAMBES"],
        'MUSCULATION EN SALLE + CARDIO(Generale)': [
                "ENDURANCE DE FORCE", "FORCE MAX", 
                "PERTE DE POIDS", "REMISE EN FORME", "RÉPÉTITIONS DES EFFORTS", 
                "FORCE EXPLOSIVE"
            ],
        'MUSCULATION EN SALLE + CARDIO(Specifique)' : ["BRAS" ,"DOS" ,"ÉPAULE","PECTORAUX","JAMBES"],
        'CARDIO EN SALLE': ["PUISSANCE", "ENDURANCE", "RÉSISTANCE", "SPRINT"],
        'PROGRAMME MAISON': ['Perte DE POIDS', "RENFORCEMENT", 'BRULER DES CALORIES'],
        'PROGRAMME DEHORS': ["PERTE DE POIDS", "PUISSANCE", "REMISE EN FORME", "BOX TO BOX"]
    }

    # Obtenir les thèmes alternatifs
    if choix not in themes_possibles:
        return "Choix invalide. Veuillez choisir un programme valide."
    
    themes = themes_possibles[choix]
    if theme_principal not in themes:
        return f"Thème invalide. Choisissez un thème parmi : {themes}"

    themes_alternatifs = [t for t in themes if t != theme_principal]
    
    # Déterminer la fréquence des thèmes principaux et alternatifs
    if nbr_seances == 2:
        nb_principal = 1
        nb_alternatif = 1
    elif nbr_seances == 3:
        nb_principal = 2
        nb_alternatif = 1
    elif nbr_seances == 4:
        nb_principal = 2
        nb_alternatif = 2
    elif nbr_seances == 5:
        nb_principal = 3
        nb_alternatif = 2
    elif nbr_seances == 6:
        nb_principal = random.choice([3, 4])
        nb_alternatif = nbr_seances - nb_principal
    elif nbr_seances == 7:
        nb_principal = random.choice([3, 4])
        nb_alternatif = nbr_seances - nb_principal
    else:
        return "Nombre de séances invalide. Veuillez choisir entre 2 et 7 séances par semaine."

    # Construire la liste des thèmes pour la semaine
    themes_semaine = [theme_principal] * nb_principal
    themes_semaine += random.choices(themes_alternatifs, k=nb_alternatif)
    random.shuffle(themes_semaine)

    # Générer le programme hebdomadaire
    programme_hebdomadaire = f"Programme hebdomadaire : {nbr_seances} séances\n"
    programme_hebdomadaire += "=" * 40 + "\n"

    for jour, theme in enumerate(themes_semaine, 1):
        objective_kine = random.choice(["General", "Spécifique"])  # Objectif aléatoire pour le kiné
        programme_journalier = programme_seance(choix, objective_kine, theme, niveau)
        choix2 = choix
        # Ajouter au programme hebdomadaire
        if choix in ['MUSCULATION EN SALLE + CARDIO(Generale)','MUSCULATION EN SALLE + CARDIO(Specifique)']:
            choix2 = 'MUSCULATION EN SALLE + CARDIO'
        elif choix == 'MUSCULATION EN SALLE (Specifique)':
            choix2 = 'MUSCULATION EN SALLE'

        programme_hebdomadaire += f"Jour {jour} : {choix2}\n\n"
        programme_hebdomadaire += f"{programme_journalier}\n"
        programme_hebdomadaire += "-" * 80 + '\n'
    
    programme_hebdomadaire_corrige = supprimer_doublons_terminer_par(programme_hebdomadaire)

    return programme_hebdomadaire_corrige

