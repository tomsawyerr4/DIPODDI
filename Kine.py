# programme kine a mettre au debut de la salle
import random
from getLinkYtb import kine_list_general,chevilles,genoux,hanche,Pieds,Adducteurs,Chevilles,Fessiers,Ishios_Jambiers,Mollets,Moyen_Fessiers,Psoas_Flechisseurs_Hanches,Quadriceps
def programme_kine(objectif):
    
    #kiné
    kine = random.choice(['MOBILITÉ','RENFORCEMENT'])
    total_exos = 'Echauffement\n'
    nbr_exercices_kine = random.randint(3,4)
    nbr_series_exercice_kine =5
    duree_mouvement = 30
    duree_recuperation = 20
    video_choix = ''
    mets = 0
    if kine == 'MOBILITÉ' :
        mets = 3
    else:
        mets = 4

    if objectif == 'General':
        for i in range(nbr_exercices_kine):
            video_choix += random.choice([random.choice(sublist) for sublist in kine_list_general]) + '\n'

        exercice = f'{video_choix} Effectuer {nbr_series_exercice_kine} séries de {duree_mouvement} sec du mouvement ({duree_recuperation} sec de récupération).\n'
        total_exos += exercice 

    elif objectif == 'Spécifique':  
        for i in range(nbr_exercices_kine):
            if kine == 'MOBILITÉ':
                type_kine = random.choice(["CHEVILLES", "GENOUX","HANCHES","PIEDS"])
                
                if type_kine == "CHEVILLES":
                    video_choix += random.choice(chevilles)+'\n'
                elif type_kine == "GENOUX":
                    video_choix += random.choice(genoux)+'\n'
                elif type_kine == "HANCHES":
                    video_choix += random.choice(hanche)+'\n'
                elif type_kine == "PIEDS":
                    video_choix += random.choice(Pieds)+'\n'
            else:
                type_kine = random.choice(["ADDUCTEURS","CHEVILLES","FESSIERS" ,"ISCHIOS JAMBIERS","MOLLETS" ,"MOYEN FESSIERS","PSOAS FLÉCHISSEURS HANCHES","QUADRICEPS"])

                if type_kine == "ADDUCTEURS":
                    video_choix += random.choice(Adducteurs)+'\n'
                elif type_kine == "CHEVILLES":
                    video_choix += random.choice(Chevilles)+'\n'
                elif type_kine == "FESSIERS":
                    video_choix += random.choice(Fessiers)+'\n'
                elif type_kine == "ISCHIOS JAMBIERS":
                    video_choix += random.choice(Ishios_Jambiers)+'\n'
                elif type_kine == "MOLLETS":
                    video_choix += random.choice(Mollets)+'\n'
                elif type_kine == "MOYEN FESSIERS":
                    video_choix += random.choice(Moyen_Fessiers)+'\n'
                elif type_kine == "PSOAS FLÉCHISSEURS HANCHES":
                    video_choix += random.choice(Psoas_Flechisseurs_Hanches)+'\n'
                elif type_kine == "QUADRICEPS":
                    video_choix += random.choice(Quadriceps)+'\n'

        exercice = f'{video_choix} Effectuer {nbr_series_exercice_kine} séries de {duree_mouvement} sec du mouvement ({duree_recuperation} sec de récupération).\n'
        total_exos += exercice
    else: 
        return 'Choix Invalide'
    return (total_exos, mets)


# print(programme_kine('Spécifique'))