from CardioSalle import echauffement_cardio,puissanceTapis,puissanceVelo,Endurance,Resistance,Sprint
from musculationSalle import musculationSalleSpecifique
import random
def musculationSalleCardio(objective,muscle):

    total_exercice = ''
    exo1 = ''
    exo2 = ''
    type_exos2 = ''
    lettre = ''

    if objective == 'ENDURANCE DE FORCE':
        exo1 = musculationSalleSpecifique(muscle,"ENDURANCE DE FORCE")
        type_exos2 = random.choice(['ENDURANCE','RÉSISTANCE'])
        if type_exos2 == 'ENDURANCE':
            # lettre = random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"])
            exo2 = Endurance("A",False)
        else:
            # lettre = random.choice(["A","B","C","D"])
            exo2 = Resistance("A",False)
        
    if objective == 'FORCE MAX':
        exo1 = musculationSalleSpecifique(muscle,"FORCE MAX")
        type_exos2 = 'PUISSANCE'
        lettre = random.choice(["A","H","I"]) #"B","C","D","E","F","G"
        
        if lettre in ['H','I']:
            exo2 = puissanceTapis(lettre,False)
        else:
            exo2 = random.choice([puissanceTapis(lettre,False),puissanceVelo(lettre,False)])
        
    if objective == 'PERTE DE POIDS':
        exo1 = musculationSalleSpecifique(muscle,"PERTE DE POIDS")
        type_exos2 = random.choice(['ENDURANCE','RÉSISTANCE'])
        
        if type_exos2 == 'ENDURANCE':
            # lettre = random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"])
            exo2 = Endurance("A",False)
        else:
            # lettre = random.choice(["A","B","C","D"])
            exo2 = Resistance("A",False)
        
    if objective == 'REMISE EN FORME':
        exo1 = musculationSalleSpecifique(muscle,"REMISE EN FORME")
        type_exos2 = random.choice(['ENDURANCE','RÉSISTANCE'])
        
        if type_exos2 == 'ENDURANCE':
            # lettre = random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"])
            exo2 = Endurance("A",False)
        else:
            # lettre = random.choice(["A","B","C","D"])
            exo2 = Resistance("A",False)
    
    if objective == 'RÉPÉTITIONS DES EFFORTS':
        exo1 = musculationSalleSpecifique(muscle,"RÉPÉTITIONS DES EFFORTS")
        type_exos2 = random.choice(['PUISSANCE','RÉSISTANCE','SPRINT'])
        
        if type_exos2 == 'PUISSANCE':
            lettre = random.choice(["A","H","I"]) #"B","C","D","E","F","G",
        
            if lettre in ['H','I']:
                exo2 = puissanceTapis(lettre,False)
            else:
                exo2 = random.choice([puissanceTapis(lettre,False),puissanceVelo(lettre,False)])
               
        elif type_exos2 == 'RÉSISTANCE':
            # lettre = random.choice(["A","B","C","D"])
            exo2 = Resistance("A",False)

        else: 
            # lettre = random.choice(["A","B", "C"])
            exo2 = Sprint("A",False)

    if objective == 'FORCE EXPLOSIVE':
        exo1 = musculationSalleSpecifique(muscle,'FORCE EXPLOSIVE')
        type_exos2 = random.choice(['PUISSANCE','SPRINT'])
        
        if type_exos2 == 'PUISSANCE':
            lettre = random.choice(["A","H","I"]) #"B","C","D","E","F","G"
        
            if lettre in ['H','I']:
                exo2 = puissanceTapis(lettre,False)
            else:
                exo2 = random.choice([puissanceTapis(lettre,False),puissanceVelo(lettre,False)])

        else: 
            # lettre = random.choice(["A","B", "C"])
            exo2 = Sprint("A",False)
    
    
    # exos = random.choice([exo1+exo2,exo2+exo1])
    total_exercice = f'{exo1}{exo2}\n'
    

    return total_exercice


