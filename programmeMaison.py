import random

from getLinkYtb import cardio,renforcement
def programmeMaison(objective):

    exercice = ''
    nbr_exercice = 5
    duree_exercice = 1
    nbr_tours= 1
    recuperation_time = 1

    choix_video = ''
    if objective == 'Perte DE POIDS':
        for i in range(nbr_exercice):
            duree_exercice = random.choice([20,30])
            nbr_tours = random.choice([5,8])
            recuperation_time = random.choice([10,15,20])

            choix_video += random.choice(cardio)+'\n'

        exercice += f'{choix_video}Chaque exercice dure {duree_exercice} sec, 5 videos équivaux 1 tour\n(Effectuer {nbr_tours} tours, récupération si vous fatiguez {recuperation_time} sec ).\n'

    elif objective == 'RENFORCEMENT':
        for i in range(nbr_exercice):
            duree_exercice = random.choice([20,30])
            nbr_tours = random.choice([5,8])
            recuperation_time = random.choice([10,15,20])
            choix_video += random.choice(renforcement) +'\n'

        exercice += f'{choix_video} Chaque exercice dure {duree_exercice} sec, 5 videos équivaux 1 tour\n(Effectuer {nbr_tours} tours, récupération si vous fatiguez {recuperation_time} sec ).\n'
    
    elif objective == 'BRULER DES CALORIES':
        # exercice += 'CARDIO \n'
        exos_cardio = random.choice([2,3])
        for i in range(exos_cardio):
            duree_exercice = random.choice([20,30])
            nbr_tours = random.choice([5,8])
            recuperation_time = random.choice([10,15,20])

            choix_video += random.choice(cardio) + '\n'

        for i in range(5-exos_cardio):
            choix_video += random.choice(renforcement)+'\n'
            duree_exercice = random.choice([20,30])
            nbr_tours = random.choice([5,8])
            recuperation_time = random.choice([10,15,20])


        exercice += f'{choix_video} Chaque exercice dure {duree_exercice} sec, 5 videos équivaux 1 tour\n( Effectuer {nbr_tours} tours, récupération si vous fatiguez {recuperation_time} sec ).\n'
    
    return exercice



# print(programmeMaison('BRULER DES CALORIES'))

