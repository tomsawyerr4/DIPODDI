import random
from getLinkYtb import ABDOS,GAINAGES,POMPES

def ProgammeBonus(niveau):
    
    nbr_series = 0
    nbr_repititions = 0
    recuperation = 0
    type_exercice = random.choice(['ABDOS','POMPES','GAINAGE'])
    video_choice = ''

    mets = 0


    if niveau == 'Debutant':
        mets = 4
    elif niveau == 'Intermidiaire':
        mets = 4
    elif niveau == 'Avance':  
        mets =  6 
    
    if niveau == 'Debutant':
        if type_exercice == 'ABDOS':
            nbr_series = random.choice([2,3])
            nbr_repititions = str(random.randint(10,15)) + ' répétitions'
            recuperation = random.randint(20,30)
            
        elif type_exercice == 'POMPES':
            nbr_series = random.choice([2,3])
            nbr_repititions = str(random.randint(5,8))+ ' répétitions'
            recuperation = random.randint(30,55)
        else:
            nbr_series = random.choice([4,5])
            nbr_repititions = str(random.choice([10,15])) + ' sec statiques'
            recuperation = random.randint(20,55)
        
    elif niveau == 'Intermidiaire':
        if type_exercice == 'ABDOS':
            nbr_series = random.randint(3,5)
            nbr_repititions = str(random.randint(15,25)) + ' répétitions'
            recuperation = random.randint(15,25)
        
        elif type_exercice == 'POMPES':
            nbr_series = random.randint(3,5)
            nbr_repititions = str(random.randint(12,16)) + ' répétitions'
            recuperation = random.randint(30,45)

        else:
            nbr_series = random.randint(3,5)
            nbr_repititions = str(random.choice([20,25,30,35])) + ' sec statiques'
            recuperation = random.randint(15,25)
        
    elif niveau == 'Avance':
        if type_exercice == 'ABDOS':
            nbr_series = random.randint(3,5)
            nbr_repititions = str(random.randint(25,32)) + ' répétitions'
            recuperation = random.randint(12,22)
        
        elif type_exercice == 'POMPES':
            nbr_series = random.randint(3,5)
            nbr_repititions = str(random.randint(15,25)) + ' répétitions'
            recuperation = random.randint(40,55)

        else:
            nbr_series = random.randint(4,5)
            nbr_repititions = random.choice(['55 sec','1 min','1 min 30 sec']) + ' statiques'
            recuperation = random.randint(10,23)
    

    for i in range(nbr_series):
        if type_exercice == 'ABDOS':
            video_choice += random.choice(ABDOS)+'\n' + f'{nbr_series} séries / {nbr_repititions} / {recuperation} sec de récupération \n'
        elif type_exercice == 'POMPES':
            video_choice += random.choice(POMPES)+'\n' + f'{nbr_series} séries / {nbr_repititions} / {recuperation} sec de récupération \n'
        else:
            video_choice += random.choice(GAINAGES)+'\n' + f'\n{nbr_series} séries / {nbr_repititions} / {recuperation} sec de récupération \n'
        
        
    
    exercice = f'{type_exercice} \n{video_choice}'

    # deuxieme_bonus = random.choice([0, 1])
    # if deuxieme_bonus == 1:
    #     exercice += "\n--- Bonus supplémentaire ---\n"
    #     exercice += ProgammeBonus(niveau,0)
    # else:
    #     pass
    return exercice, mets

