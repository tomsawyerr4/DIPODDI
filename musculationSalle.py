import random
from getLinkYtb import programme_musculation, BRAS,DOS,EPAULES,JAMBES,PECTORAUX
### programme musculation en Salle

Objectives_Musculation_Salle = ["ENDURANCE DE FORCE", "FORCE MAX", "MASSE MUSCULAIRE", "PERTE DE POIDS" ,"REMISE EN FORME","RÉPÉTITIONS DES EFFORTS","FORCE EXPLOSIVE"]

Groupes_Musculaire = ["BRAS" ,"DOS" ,"ÉPAULE","PECTORAUX","JAMBES"]

objective = random.choice(Objectives_Musculation_Salle)

def musculationSalle(type,objective,programme):   
    ###type: generale/ specifique
    exercices_totals = ''

    # échauffement
    type_echauffement = random.choice(['Tapis','Vélo'])
    duree_echauffement = random.randint(6, 10)
    echauffement = f"Echauffement {type_echauffement} {duree_echauffement} mins"

    exercice = ""
    nbr_exercice = 1
    nbr_series = 1
    reptitions = 1
    recuperation_time = 1
    video_choix = ''
    
    
    if type == 'General':
        if objective == "ENDURANCE DE FORCE":
            nbr_exercice = random.randint(6,8)
            for i in range(nbr_exercice-1):
                if programme == programme_musculation:
                    video_choix = random.choice([random.choice(sublist) for sublist in programme])+'\n'
                else:
                    video_choix = random.choice(programme)+'\n'
                nbr_series = random.randint(2,5)
                reptitions = random.randint(15,25)
                recuperation_time = random.randint(30,60)

                exercice += f'{video_choix}{nbr_series} séries / {reptitions} répétitions / charges légères / {recuperation_time} sec de récupération.\n'

            dexieme_ojective = random.choice(["FORCE MAX", "MASSE MUSCULAIRE","RÉPÉTITIONS DES EFFORTS","FORCE EXPLOSIVE"])
            autre_exercie = dexieme_exercice(dexieme_ojective,programme)
            exercice += autre_exercie

        elif objective == "FORCE MAX":
            nbr_exercice = random.randint(6,7)
            for i in range(nbr_exercice-1):
                if programme == programme_musculation:
                    video_choix = random.choice([random.choice(sublist) for sublist in programme])+'\n'
                else:
                    video_choix = random.choice(programme)+'\n'
                nbr_series = random.randint(2,5)
                reptitions = random.randint(2,6)
                recuperation_time = random.randint(3,5)

                exercice += f'{video_choix}{nbr_series} séries / {reptitions} répétitions / charges très lourdes / {recuperation_time} mins de récupération.\n'
            dexieme_ojective = random.choice(["ENDURANCE DE FORCE", "MASSE MUSCULAIRE","RÉPÉTITIONS DES EFFORTS","FORCE EXPLOSIVE"])
            autre_exercie = dexieme_exercice(dexieme_ojective,programme)
            exercice += autre_exercie

        elif objective == "MASSE MUSCULAIRE":
            nbr_exercice = random.randint(4,5)
            for i in range(nbr_exercice-1):
                if programme == programme_musculation:
                    video_choix = random.choice([random.choice(sublist) for sublist in programme])+'\n'
                else:
                    video_choix = random.choice(programme)+'\n'
                nbr_series = random.randint(8,12)
                reptitions = random.randint(8,10)
                recuperation_time = random.choice(['1 min','2 mins'])

                exercice += f'{video_choix}{nbr_series} séries / {reptitions} répétitions / charges moyennes / {recuperation_time} de récupération.\n'

            dexieme_ojective = random.choice(["ENDURANCE DE FORCE", "FORCE MAX","RÉPÉTITIONS DES EFFORTS","FORCE EXPLOSIVE"])
            autre_exercie = dexieme_exercice(dexieme_ojective,programme)
            exercice += autre_exercie

        elif objective == "PERTE DE POIDS":
            nbr_exercice = random.randint(5,6)
            for i in range(nbr_exercice-1):
                if programme == programme_musculation:
                    video_choix = random.choice([random.choice(sublist) for sublist in programme])+'\n'
                else:
                    video_choix = random.choice(programme)+'\n'
                nbr_series = random.randint(6,12)
                reptitions = random.randint(13,18)
                recuperation_time = random.randint(10,30)

                exercice += f'{video_choix}{nbr_series} séries / {reptitions} répétitions / charges légères / {recuperation_time} sec de récupération.\n'

            dexieme_ojective = random.choice(["ENDURANCE DE FORCE","FORCE MAX", "REMISE EN FORME","RÉPÉTITIONS DES EFFORTS"])
            autre_exercie = dexieme_exercice(dexieme_ojective,programme)
            exercice += autre_exercie

        elif objective == "REMISE EN FORME":
            nbr_exercice = random.randint(5,6)
            for i in range(nbr_exercice-1):
                if programme == programme_musculation:
                    video_choix = random.choice([random.choice(sublist) for sublist in programme])+'\n'
                else:
                    video_choix = random.choice(programme)+'\n'
                nbr_series = random.randint(4,7)
                reptitions = random.randint(8,12)
                recuperation_time = random.randint(3,4)

                exercice += f'{video_choix}{nbr_series} séries / {reptitions} répétitions / charges moyennes / {recuperation_time} mins de récupération.\n'
            dexieme_ojective = random.choice(["ENDURANCE DE FORCE","RÉPÉTITIONS DES EFFORTS","FORCE EXPLOSIVE"])
            autre_exercie = dexieme_exercice(dexieme_ojective,programme)
            exercice += autre_exercie

        elif objective == "RÉPÉTITIONS DES EFFORTS":
            nbr_exercice = random.randint(5,6)
            for i in range(nbr_exercice-1):
                if programme == programme_musculation:
                    video_choix = random.choice([random.choice(sublist) for sublist in programme])+'\n'
                else:
                    video_choix = random.choice(programme)+'\n'
                nbr_series = random.randint(5,8)
                effort_time = random.randint(7,15)
                recuperation_time = random.randint(10,20)

                exercice += f'{video_choix}{nbr_series} séries / {effort_time} sec efforts / charges moyennes / {recuperation_time} sec de récupération.\n'

            dexieme_ojective = random.choice(["ENDURANCE DE FORCE","FORCE MAX","REMISE EN FORME","FORCE EXPLOSIVE"])
            autre_exercie = dexieme_exercice(dexieme_ojective,programme)
            exercice += autre_exercie

        elif objective == "FORCE EXPLOSIVE":
            nbr_exercice = random.randint(5,6)
            for i in range(nbr_exercice-1):
                if programme == programme_musculation:
                    video_choix = random.choice([random.choice(sublist) for sublist in programme])+'\n'
                else:
                    video_choix = random.choice(programme)+'\n'
                nbr_series = random.randint(2,7)
                reptitions = random.randint(2,7)
                recuperation_time = random.randint(2,3)

                exercice += f'{video_choix}{nbr_series} séries / {reptitions} répétitions / charges lourdes / {recuperation_time} mins de récupération.\n'

            dexieme_ojective = random.choice(["FORCE MAX","REMISE EN FORME","FORCE MAX","RÉPÉTITIONS DES EFFORTS"])
            autre_exercie = dexieme_exercice(dexieme_ojective,programme)
            exercice += autre_exercie

        
        
    exercices_totals = echauffement + '\n' + exercice
    return exercices_totals


def dexieme_exercice(objective,programme):   
    exercice = ""
    nbr_series = 1
    reptitions = 1
    recuperation_time = 1
    choix_video = ''

    if programme == programme_musculation:
        choix_video = random.choice([random.choice(sublist) for sublist in programme])+'\n'
    else:
        choix_video = random.choice(programme)+'\n'
    if objective == "ENDURANCE DE FORCE":
        
        nbr_series = random.randint(2,5)
        reptitions = random.randint(15,25)
        recuperation_time = random.randint(30,60)

        exercice += f'{choix_video}{nbr_series} séries / {reptitions} répétitions / charges légères / {recuperation_time} sec de récupération.\n'

    elif objective == "FORCE MAX":
        
        nbr_series = random.randint(2,5)
        reptitions = random.randint(2,6)
        recuperation_time = random.randint(3,5)

        exercice += f'{choix_video}{nbr_series} séries / {reptitions} répétitions / charges très lourdes / {recuperation_time} mins de récupération.\n'

    elif objective == "MASSE MUSCULAIRE":
        nbr_series = random.randint(8,10)
        reptitions = random.randint(8,10)
        recuperation_time = random.choice(['1 min','2 mins'])

        exercice += f'{choix_video}{nbr_series} séries / {reptitions} répétitions / charges moyennes / {recuperation_time} de récupération.\n'
    
    elif objective == "PERTE DE POIDS":
        nbr_series = random.randint(6,8)
        reptitions = random.randint(13,18)
        recuperation_time = random.randint(11,30)

        exercice += f'{choix_video}{nbr_series} séries / {reptitions} répétitions / charges légères / {recuperation_time} sec de récupération.\n'
    
    elif objective == "REMISE EN FORME":
        nbr_series = random.randint(4,7)
        reptitions = random.randint(8,12)
        recuperation_time = random.randint(3,4)

        exercice += f'{choix_video}{nbr_series} séries / {reptitions} répétitions / charges moyennes / {recuperation_time} mins de récupération.\n'
    
    elif objective == "RÉPÉTITIONS DES EFFORTS":
        nbr_series = random.randint(5,8)
        effort_time = random.randint(7,15)
        recuperation_time = random.randint(11,20)

        exercice += f'{choix_video}{nbr_series} séries / {effort_time} sec efforts / charges moyennes / {recuperation_time} sec de récupération.\n'
    

    elif objective == "FORCE EXPLOSIVE":
        nbr_series = random.randint(2,7)
        reptitions = random.randint(2,7)
        recuperation_time = random.randint(2,3)

        exercice += f'{choix_video}{nbr_series} séries / {reptitions} répétitions / charges lourdes / {recuperation_time} mins de récupération.\n'

    return exercice


def musculationSalleSpecifique(muscle,objective):
    exercice = muscle + '\n'
    programme = programme_musculation
    # ["BRAS" ,"DOS" ,"ÉPAULE","PECTORAUX","JAMBES"]
    if muscle == "BRAS" :
        programme = BRAS
    elif muscle == "DOS":
        programme = DOS
    elif muscle == "ÉPAULE":
        programme = EPAULES
    elif muscle == "PECTORAUX":
        programme = PECTORAUX
    else:
        programme = JAMBES
    exercice += musculationSalle('General',objective,programme)



    return exercice

