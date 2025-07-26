import random


# def echauffement_dehors():
#     duree_echauffement = random.randint(8,12)
#     echauffement = f"Echauffement Footing {duree_echauffement} min\n"
    
#     return echauffement

def PerteDePoids(lettre):

    exercice = ""
    nbr_series = random.choice(['1 série','2 séries' ,'3 séries'])
    effort_time = 1
    recuperation_time = 1
    allure = 'grosse allure'
    duree_exercice = 1

    #exerices de la seance
    if lettre == "A":
        duree_footing = random.randint(22,37)
        exercice = f"Footing {duree_footing} min efforts / allure normale\n"
        exercice += PerteDePoids(random.choice(["B","C","D","E","F","G","H","I"]))
        pass
    else:
        if lettre =="B":
            effort_time = '30 sec'
            recuperation_time = '30 sec'
            duree_exercice = random.randint(5,8)
        elif lettre =="C":
            effort_time = '45 sec'
            recuperation_time = '15 sec'
            duree_exercice = random.randint(8,12)
        elif lettre =="D":
            effort_time = '55 sec'
            recuperation_time = '2 min'
            duree_exercice = random.randint(6,14)
        elif lettre =="E":
            effort_time =  random.choice(['1 min','2 min'])
            recuperation_time = '2 min'
            duree_exercice = random.randint(6,14)

        elif lettre =="F":
            effort_time = random.choice(['1 min','2 min','3 min'])
            recuperation_time = '2 min'
            duree_exercice = random.randint(12,24)
        elif lettre =="G":
            nbr_series = '1 série'
            effort_time = random.choice(['2 min','3 min'])
            recuperation_time = '3 min'
            duree_exercice = random.randint(12,24)
        elif lettre =="H":
            nbr_series = '1 série'
            effort_time = random.choice(['2 min','3 min','4 min'])
            recuperation_time = '2 min'
            duree_exercice = random.randint(14,35)
        elif lettre =="I":
            nbr_series = '1 série'
            effort_time = random.choice(['2 min','3 min','4 min'])
            recuperation_time = '3 min'
            duree_exercice = random.randint(14,35)
    
        exercice =f"{nbr_series} / {effort_time} d'efforts {recuperation_time} récupérations / {duree_exercice} min d'efforts  / {allure}\n"

    FootingTime = random.randint(9,22)
    exercice += f'terminer par {FootingTime} min de Footing.\n'

    return exercice


def puissance(lettre):
   
    exercice = ""
    nbr_series = random.choice(['1 série','2 séries','3 séries'])
    effort_time = 0
    recuperation_time = 0
    allure = 'grosse allure'
    effort = 1

    if lettre == 'A':
        duree_footing = random.randint(12,25)
        exercice = f"Footing {duree_footing} min efforts / allure normale\n"
        exercice += puissance(random.choice(["B","C","D","E","F","G","H","I"]))

    else:
        if lettre =="B":
            effort_time = 5
            recuperation_time = 5
            effort = random.randint(4,7)
        elif lettre =="C":
            effort_time = 10
            recuperation_time = 5
            effort = random.randint(4,7) 
        elif lettre =="D":
            effort_time = 10
            recuperation_time = 10
            effort = random.randint(4,7)
        elif lettre =="E":
            effort_time =  15
            recuperation_time =15
            effort = random.randint(5,7)
        elif lettre =="F":
            effort_time = 20
            recuperation_time = 10
            effort = random.randint(5,7)
        elif lettre =="G":
            effort_time = 20
            recuperation_time = 20  
            effort = random.randint(5,7)
        elif lettre =="H":
            effort_time = 30
            recuperation_time = 10 
            effort = random.randint(5,8)
        elif lettre =="I":
            effort_time = 30
            recuperation_time = 20  
            effort = random.randint(5,8)
        exercice =f"{nbr_series} / {effort_time} sec d'efforts {recuperation_time} sec récupérations / {effort} min d'efforts / {allure}\n"

        FootingTime = random.randint(9,22)
        exercice += f'terminer par {FootingTime} min de Footing.\n'
    
    return exercice


def remiseEnForme(lettre):
    exercice = ""
    nbr_series = random.choice(['1 série','2 séries','3 séries'])
    effort_time = 0
    recuperation_time = 0
    allure = 'grosse allure'
    effort = 1

    if lettre == "A":
        duree_footing = random.randint(22,35)
        exercice = f"Footing {duree_footing} min efforts / allure normale\n"
        exercice += puissance(random.choice(["B","C","D","E","F"]))
    else:
        if lettre =="B":
            effort_time = '20 sec'
            recuperation_time = '20 sec'
            effort = random.randint(5,7)
        elif lettre =="C":
            effort_time = '30 sec'
            recuperation_time = '30 sec'
            effort = random.randint(5,8) 
        elif lettre =="D":
            effort_time = random.choice(['1 min','2 min'])
            recuperation_time = '2 min'
            effort = random.randint(6,16)
        elif lettre =="E":
            effort_time = random.choice(['1 min','2 min','3 min'])
            recuperation_time ='3 min'
            effort = random.randint(12,24)
        elif lettre =="F":
            effort_time = random.choice(['2 min','3 min'])
            recuperation_time = '3 min'
            effort = random.randint(12,24)
        
        exercice =f"{nbr_series} / {effort_time} d'efforts {recuperation_time} récupérations / {effort} min d'efforts / {allure}\n"

        FootingTime = random.randint(9,22)
        exercice += f'terminer par {FootingTime} min de Footing.\n'
    return exercice


def BoxTOBOX(lettre):
    exercice = ""
    nbr_series = random.choice(['1 série','2 séries','3 séries'])
    effort_time = 0
    recuperation_time = 0
    allure = 'grosse allure'
    effort = 1

    if lettre == 'A':
        duree_footing = random.randint(20,40)
        exercice = f"Footing {duree_footing} min efforts / allure normale\n"
        exercice += BoxTOBOX(random.choice(["B","C","D","E","F","G","H","I","J","K","L","M","N"]))

    else:
        if lettre =="B":
            effort_time = '10 sec'
            recuperation_time = '10 sec'
            effort = random.randint(4,7)
        elif lettre =="C":
            effort_time = '15 sec'
            recuperation_time = '15 sec'
            effort = random.randint(5,7) 
        elif lettre =="D":
            effort_time = '20 sec'
            recuperation_time = '10 sec'
            effort = random.randint(5,7)
        elif lettre =="E":
            effort_time = '20 sec'
            recuperation_time ='20 sec'
            effort = random.randint(5,7)
        elif lettre =="F":
            effort_time = '30 sec'
            recuperation_time = '20 sec'
            effort = random.randint(5,8)
        
        elif lettre =="G":
            effort_time = '30 sec'
            recuperation_time = '30 sec'
            effort = random.randint(5,8)
        
        elif lettre =="H":
            effort_time = '45 sec'
            recuperation_time = '15 sec'
            effort = random.randint(8,12)

        elif lettre =="I":
            effort_time = random.choice(['55 sec','1 min','2 min'])
            recuperation_time = '45 sec'
            effort = random.randint(6,16)
        
        elif lettre =="J":
            effort_time = random.choice(['1 min','2 min'])
            recuperation_time = '2 min'
            effort = random.randint(6,16)
        
        elif lettre =="K":
            effort_time = random.choice(['3 min','1 min','2 min'])
            recuperation_time = '2 min'
            effort = random.randint(12,24)
        
        elif lettre =="L":
            effort_time = random.choice(['1 min','2 min','3 min'])
            recuperation_time = '3 min'
            effort = random.randint(12,24)
        
        elif lettre =="M":
            effort_time = random.choice(['2 min','3 min','4 min'])
            recuperation_time = '2 min'
            effort = random.randint(14,35)
        
        elif lettre =="N":
            effort_time = random.choice(['2 min','3 min','4 min'])
            recuperation_time = '3 min'
            effort = random.randint(14,35)

       
        exercice =f"{nbr_series} / {effort_time} d'efforts {recuperation_time} récupérations / {effort} min d'efforts / {allure}\n"

        FootingTime = random.randint(9,22)
        exercice += f'terminer par {FootingTime} min de Footing.\n'
    return exercice



# exos1 = echauffement_dehors()+BoxTOBOX("B")

# # exos2 = puissanceVelo("A")

# print(exos1)
