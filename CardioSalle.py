import random
from getLinkYtb import programme_cardio,VELO_ENDURANCE,VELO_PUISSANCE,TAPIS_ENDURANCE,TAPIS_PUISSANCE,TAPIS_RÉSISTANCE,SPRINT_EN_COTE,RAMEUR,MARCHE,MARCHE_EN_COTE,ELLIPTIQUE_INTENSE,ELLIPTIQUE_NORMAL,ABDOS,GAINAGES


def echauffement_cardio():
    #echauffement 
    duree_echauffement = random.randint(6,12)
    type_echauff = random.choice(['Tapis','Vélo'])
    echauffement = f"Echauffement {type_echauff} {duree_echauffement} mins\n"
    return echauffement

def terminer_par():
    duree_exercice_terminer = random.randint(4,7)
    exercice_terminer = random.choice(['Tapis','vélo','elliptique'])
    # exercice_terminer2 = random.choice(['Abdos','Gainage','Abdos et Gainage'])
    video_ex_ter = ''
    # video_ex_ter2 = ''

    if exercice_terminer == 'Tapis':
        video_ex_ter = random.choice([TAPIS_ENDURANCE[0],TAPIS_PUISSANCE[0],TAPIS_RÉSISTANCE[0]])
    elif exercice_terminer == 'vélo':
        video_ex_ter = random.choice([VELO_ENDURANCE[0],VELO_PUISSANCE[0]])
    else :
        video_ex_ter = random.choice([ELLIPTIQUE_INTENSE[0],ELLIPTIQUE_NORMAL[0]])
    
    
    dernier_exercice = f"Terminer par : {duree_exercice_terminer} mins de {exercice_terminer}\n{video_ex_ter}\n"

    return dernier_exercice

def puissanceTapis(lettre,inclure_terminer_par = True):

    exercices_totals = ''

    exercice = ""
    nbr_series = random.choice(['1 série','2 séries','3 séries'])
    effort_time = 0
    recuperation_time = 0
    allure = random.choice(['allure soutenue','bonne allure'])
    recuperation_active = random.choice(['1 min de récupération','2 mins de récupération','3 mins de récupération'])
    duree_exercice = random.choice([6,7,8])

    choix_video = ''
    #exerices de la seance
    if lettre == "A":
        duree_footing = random.randint(18,28)
        exercice = f"Footing {duree_footing} mins efforts / allure normale\n"
        exercice += puissanceTapis(random.choice(["B","C","D","E","F","G","H","I"]),False)
        pass
    else:
        choix_video = TAPIS_PUISSANCE[0]+'\n'
        if lettre =="B":
            effort_time = 5
            recuperation_time = 15
        elif lettre =="C":
            effort_time = 5
            recuperation_time = 25
        elif lettre =="D":
            effort_time = 10
            recuperation_time = 10
        elif lettre =="E":
            effort_time =  15
            recuperation_time = 15
        elif lettre =="F":
            effort_time = 20
            recuperation_time = 20
        elif lettre =="G":
            effort_time = 20
            recuperation_time = 10
        elif lettre =="H":
            effort_time = 30
            recuperation_time = 10
        elif lettre =="I":
            effort_time = 45
            recuperation_time = 15
    
        exercice =f"{choix_video}{nbr_series} / {effort_time} sec d'efforts {recuperation_time} sec de récupération \n {allure} / {recuperation_active} active / durée exercice {duree_exercice} mins"

    #terminer par
    dernier_exercice = ''
    if inclure_terminer_par:
        dernier_exercice = terminer_par()
        exercices_totals = exercice + "\n" + dernier_exercice
    else:
        exercices_totals = exercice
 
    return exercices_totals


def puissanceVelo(lettre,inclure_terminer_par=True):
    exercices_totals = ''


    exercice = ""
    nbr_series = random.choice(['1 série','2 séries','3 séries'])
    effort_time = 0
    recuperation_time = 0
    allure = random.choice(['allure soutenue','bonne allure'])
    recuperation_active = random.choice(['1 min de récupération','2 mins de récupération','3 mins de récupération'])
    duree_exercice = random.choice([6,7,8])
    

    if lettre == 'A':
        duree_footing = random.randint(18,28)
        choix_video = random.choice([VELO_PUISSANCE[0],VELO_ENDURANCE[0]])+'\n'
        exercice = f"{choix_video}Vélo {duree_footing} mins efforts / allure normale\n"
        exercice += puissanceVelo(random.choice(["B","C","D","E","F","G"]),False)
        pass

    else:
        choix_video = VELO_PUISSANCE[0]+'\n'
        if lettre =="B":
            effort_time = 15
            recuperation_time = 15
        elif lettre =="C":
            effort_time = 20
            recuperation_time = 10
        elif lettre =="D":
            effort_time = 25
            recuperation_time = 5
        elif lettre =="E":
            effort_time =  20
            recuperation_time = 20
        elif lettre =="F":
            effort_time = 30
            recuperation_time = 10
        elif lettre =="G":
            effort_time = 45
            recuperation_time = 15
        exercice =f"{choix_video}{nbr_series} / {effort_time} sec d'efforts {recuperation_time} sec de récupération \n {allure} / {recuperation_active} active / durée exercice {duree_exercice} mins"

    #terminer par

    dernier_exercice = ''
    if inclure_terminer_par:
        dernier_exercice = terminer_par()
        exercices_totals = exercice + "\n" + dernier_exercice
    else:
        exercices_totals = exercice

    return exercices_totals




def Endurance(lettre,inclure_terminer_par=True):
    exercices_totals = ''


    exercice = ""
    nbr_series = 1
    effort_time = 0
    recuperation_time = 0
    allure = random.choice(['allure soutenue','bonne allure'])
    recuperation_active = random.choice(['1 min de récupération','2 mins de récupération','3 mins de récupération'])
    duree_exercice = random.randint(12,15)
    choix_video = random.choice([random.choice(sublist) for sublist in programme_cardio])+'\n'
    if lettre == 'A':
        type_ex = random.choice(['Tapis','Vélo'])
        if type_ex == 'Tapis':
            choix_video = TAPIS_ENDURANCE[0]+'\n'
        else:
            choix_video = VELO_ENDURANCE[0]+'\n'
        
        duree_ex = random.randint(25,38)
        exercice = f"{choix_video}{type_ex} {duree_ex} mins efforts / allure normale\n"
        exercice += Endurance(random.choice(["B","C","D","E","F","G","H","I","J","K","L","M","N","O"]),False)
        pass

    elif lettre in ["B","C","D","E","F","G"]:
        if lettre == 'B':
            effort_time = 15
            recuperation_time = 15

        elif lettre == 'C':
            effort_time = 15
            recuperation_time = 15

        elif lettre == 'D':
            effort_time = 20
            recuperation_time = 20

        elif lettre == 'E':
            effort_time = 20
            recuperation_time = 10

        elif lettre == 'F':
            effort_time = 30
            recuperation_time = 10
            duree_exercice = random.randint(14,17)

        elif lettre == 'G':
            effort_time = 45
            recuperation_time = 15
            duree_exercice = random.randint(14,20)

        exercice =f"{choix_video} {nbr_series} série / {effort_time} sec d'efforts {recuperation_time} sec de récupération \n {allure} / {recuperation_active} active / durée exercice {duree_exercice} mins."
    
    elif lettre in ["H","I","J","K","L","M","N","O"]:
        nbr_series = random.randint(5,10)
        if lettre == 'H':
            effort_time = '40 sec'
            recuperation_active = '30 sec'

        elif lettre == 'I':
            effort_time = '40 sec'
            recuperation_active = '40 sec'

        elif lettre == 'J':
            effort_time = '1 min'
            recuperation_active = '15 sec'

        elif lettre == 'K':
            effort_time = '1 min'
            recuperation_active = '20 sec'

        elif lettre == 'L':
            effort_time ='1 min'
            recuperation_active ='30 sec'

        elif lettre == 'M':
            effort_time = '1 min'
            recuperation_active = '45 sec'

        elif lettre == 'N':
            effort_time = '1 min'
            recuperation_active = '1 min'

        elif lettre == 'O':
            effort_time = '2 mins'
            recuperation_active = '1 min'
        
        
        exercice = f"{choix_video}{nbr_series} séries / {effort_time} d'efforts {recuperation_active} de récupération active / bonne allure"
    #terminer par

    dernier_exercice = ''
    if inclure_terminer_par:
        dernier_exercice = terminer_par()
        exercices_totals = exercice + "\n" + dernier_exercice
    else:
        exercices_totals = exercice

    return exercices_totals



def Resistance(lettre,inclure_terminer_par=True):
    
    exercices_totals = ''

    exercice = ""
    nbr_series = random.choice([2,3])
    effort_time = 0
    allure = 'bonne allure'
    recuperation_active = random.choice(['1 min de récupération','2 mins de récupération','3 mins de récupération'])
    choix_video = TAPIS_RÉSISTANCE[0]+'\n'
    if lettre == 'A':
        type_ex = random.choice(['Tapis', 'Vélo'])
        if type_ex == 'Vélo':
            choix_video = random.choice([VELO_ENDURANCE[0],VELO_PUISSANCE[0]])+'\n'
        duree_ex = random.randint(20, 30)
        exercice = f"{choix_video}{type_ex} {duree_ex} mins efforts / allure normale\n"
        exercice += Resistance(random.choice(["B", "C", "D"]),False)
    else:
        if lettre == 'B':
            nbr_series = random.randint(8, 11)
            effort_time = random.randint(45, 90)
        elif lettre == 'C':
            nbr_series = random.randint(4, 7)
            effort_time = random.randint(90, 240)
        elif lettre == 'D':
            nbr_series = random.randint(2, 5)
            effort_time = random.randint(240, 300)

        # Convert effort_time to minutes and seconds if it exceeds 60
        if effort_time > 60:
            minutes = effort_time // 60
            seconds = effort_time % 60
            effort_time_str = f"{minutes} min {seconds} sec"
        else:
            effort_time_str = f"{effort_time} sec"

        exercice = f"{choix_video}{nbr_series} séries {effort_time_str} d'efforts / {allure} / {recuperation_active} active"


    dernier_exercice = ''
    if inclure_terminer_par:
        dernier_exercice = terminer_par()
        exercices_totals = exercice + "\n" + dernier_exercice
    else:
        exercices_totals = exercice

    return exercices_totals



def Sprint(lettre,inclure_terminer_par=True):
    
    exercices_totals = ''

    exercice = ""
    nbr_series = random.choice([ 2, 3])
    effort_time = 0
    allure = 'bonne allure'
    recuperation_time = 0
    choix_video = SPRINT_EN_COTE[0]+'\n'
    if lettre == 'A':
        duree_ex = random.randint(20, 30)
        choix_video = random.choice([TAPIS_ENDURANCE[0],TAPIS_PUISSANCE[0],TAPIS_RÉSISTANCE[0]])
        exercice = f"{choix_video} \nFooting {duree_ex} min efforts / allure normale\n"
        exercice += Sprint("B",False)  # On a eliminer exercice 'C'
    else:
        if lettre == 'B':
            nbr_series = random.randint(2, 4)
            effort_time = random.randint(7, 11)
            cote = random.randint(9,11)
            allure = 'allure vitesse max '
            recuperation_time = random.randint(45,80)

            # Convert effort_time to minutes and seconds if it exceeds 60
            if recuperation_time > 60:
                minutes = recuperation_time // 60
                seconds = recuperation_time % 60
                recuperation_time_str = f"{minutes} min {seconds} sec"
            else:
                recuperation_time_str = f"{recuperation_time} sec"

            exercice = f"{choix_video}Sur le tapis : {nbr_series} séries de 4 sprints entre {effort_time} sec d'efforts {cote} % de cote \n {allure} / {recuperation_time_str} de récupération"

        elif lettre == 'C':
            nbr_series = random.randint(4, 8)
            effort_time = random.randint(90, 240)
            sauts = random.randint(50,60)
            recuperation_time = random.randint(30,55)
            exercice = f'{choix_video} Corde a sautée {nbr_series} séries entre {sauts} sauts / bonne allure / {recuperation_time} sec de récupération passive'

    dernier_exercice = ''
    if inclure_terminer_par:
        dernier_exercice = terminer_par()
        exercices_totals = exercice + "\n" + dernier_exercice
    else:
        exercices_totals = exercice

    return exercices_totals



def pertePoids(lettre,inclure_terminer_par=True):
    
    exercices_totals = ''


    exercice = ""
    nbr_series = random.randint(5,10)
    effort_time = 1
    allure = 'bonne allure'
    recuperation_time = 1
    choix_video = random.choice([random.choice(sublist) for sublist in programme_cardio])+'\n'
    if lettre == 'A':
        type_ex = random.choice(['Tapis', 'Vélo'])
        if type_ex == 'Tapis':
            choix_video = random.choice([TAPIS_ENDURANCE[0],TAPIS_PUISSANCE[0],TAPIS_RÉSISTANCE[0]])+'\n'
        else:
            choix_video = random.choice([VELO_ENDURANCE[0],VELO_PUISSANCE[0]])+'\n'
        duree_ex = random.randint(25, 38)
        exercice = f"{choix_video}{type_ex} {duree_ex} min efforts / allure normale\n"
        exercice += Resistance(random.choice(["B", "C", "D"]),False)
    else:
        if lettre == 'B':
           
            effort_time = 1
            recuperation_time = 1
            exercice = f"{choix_video}{nbr_series} séries {effort_time} min d'efforts {recuperation_time} min de récupération active  / {allure}"

        elif lettre == 'C':
            effort_time = 2
            recuperation_time = 1
            exercice = f"{choix_video}{nbr_series} séries {effort_time} min d'efforts {recuperation_time} min de récupération active  / {allure}"

        elif lettre == 'D':
            nbr_series = random.randint(1,3)
            effort_time = 30
            recuperation_time = 30
            allure = random.choice(['bonne allure','allure soutenue'])
            recuperation_active = random.choice(['1 min de récupération','2 mins de récupération','3 mins de récupération'])
            duree_exo = random.randint(6,8)

            exercice = f"{choix_video}{nbr_series} séries / {effort_time} sec d'efforts {recuperation_time} sec de récupération \n {allure} / {recuperation_active} active / durée exercice {duree_exo} min"

    dernier_exercice = ''
    if inclure_terminer_par:
        dernier_exercice = terminer_par()
        exercices_totals = exercice + "\n" + dernier_exercice
    else:
        exercices_totals = exercice

    return exercices_totals

