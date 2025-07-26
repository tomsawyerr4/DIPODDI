import random 
from Kine import programme_kine
from CardioSalle import echauffement_cardio, puissanceTapis, puissanceVelo,Endurance,Resistance,Sprint,pertePoids
from musculationSalle import Objectives_Musculation_Salle,Groupes_Musculaire,musculationSalle,musculationSalleSpecifique
from MusculationSalleCardio import musculationSalleCardio
from programmeMaison import programmeMaison
from ProgrammeDehors import PerteDePoids,puissance,remiseEnForme,BoxTOBOX
from Bonus import ProgammeBonus
import re
from getLinkYtb import programme_musculation
# from spot1.translation import translate
from fpdf import FPDF

# from spot1.arabTrad import process_and_save_workout_program
# from spot1.translation import translate



def save_to_pdf(content, filename="exos.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    # pdf.image("image.png", x = 30, y = 0)
    pdf.set_font("Arial", size=12)

    # Regex pour détecter les liens
    link_pattern = r'(https?://\S+)'

    lines = content.split('\n')
    for line in lines:
        # Recherche des liens dans la ligne
        match = re.search(link_pattern, line)
        if match:
            # Extraire le lien
            url = match.group(0)
            # Remplacer le lien par "Video" cliquable
            text = "Video"
            pdf.set_font("Arial", style="", size=12)  # Style normal
            pdf.set_text_color(0, 0, 255)  # Bleu pour le lien

            # Centrer "Video"
            pdf.cell(0, 10, text, ln=True, align="C", link=url)
        else:
            if "Echauffement" in line:
                # Gestion du texte "Échauffement"
                pdf.set_font("Arial", style="", size=12)
                pdf.set_text_color(0, 0, 0)

                # Mesurer la largeur du texte
                text_width = pdf.get_string_width(line) + 2  # Marges

                # Calculer la position X pour centrer le texte souligné
                page_width = pdf.w - pdf.l_margin - pdf.r_margin
                x_position = (page_width - text_width) / 2 + pdf.l_margin

                # Ajouter le texte souligné
                pdf.set_x(x_position)
                pdf.cell(text_width, 10, line, border="B", ln=True, align="C")
            elif line.strip() and (line.isupper() or line.startswith("Jour") or line.startswith("PARTIE BONUS")):
                pdf.set_font("Arial", style="B", size=12)  # Gras
                pdf.set_text_color(0, 0, 0)  # Noir
                pdf.cell(0, 10, line, ln=True, align="C")
            else:
                pdf.set_font("Arial", style="", size=12)  # Normal
                pdf.set_text_color(0, 0, 0)  # Noir
                pdf.cell(0, 10, line, ln=True, align="C")

    pdf.output(filename)
    return f"Saved to {filename}"


Niveaux = ['Débutant',"Intermidiaire","Avancé"]




def programme_seance(choix,objective_kine,theme,niveau):

    echauffement = ''
    programme_seance = ''

    # programme_seance += f'Kine {objective_kine} \n'
    programme_seance += programme_kine(objective_kine)     ## Generale/Specifique


    ajout_Bonus = random.choice([0,1])

    if choix == 'MUSCULATION EN SALLE':
        programme_seance += musculationSalle('General',theme,programme_musculation)
    
    elif choix == 'MUSCULATION EN SALLE (Specifique)':
        obj = random.choice([
            "ENDURANCE DE FORCE", "FORCE MAX", 
            "PERTE DE POIDS", "REMISE EN FORME", "RÉPÉTITIONS DES EFFORTS", 
            "FORCE EXPLOSIVE"
        ])
        programme_seance += musculationSalleSpecifique(theme,obj)
    
    elif choix == 'CARDIO EN SALLE':
        echauffement = echauffement_cardio()
        programme_seance += echauffement
        ajout_Bonus = 1
        # programme_seance += theme + '\n'
        if theme == 'PUISSANCE':
            # lettre = random.choice(["A","B","C","D","E","F","G","H","I"])
            # if lettre in ['H','I']:
            #     programme_seance += puissanceTapis(lettre)
            # else:
            #     programme_seance += random.choice([puissanceTapis(lettre),puissanceVelo(lettre)])
            programme_seance += random.choice([puissanceTapis('A'),puissanceVelo('A')])

        elif theme == 'ENDURANCE':
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

        programme_seance += musculationSalleCardio(theme,'')
    
    elif choix == 'MUSCULATION EN SALLE + CARDIO(Specifique)':
        obj = random.choice([
            "ENDURANCE DE FORCE", "FORCE MAX", 
            "PERTE DE POIDS", "REMISE EN FORME", "RÉPÉTITIONS DES EFFORTS", 
            "FORCE EXPLOSIVE"
        ])
        programme_seance += musculationSalleCardio(obj,theme)
    
    elif choix == 'PROGRAMME MAISON':
        ajout_Bonus = 1
        programme_seance += programmeMaison(theme)
    
    elif choix == 'PROGRAMME DEHORS':
        ajout_Bonus = 1
        # programme_seance += echauffement_dehors()
        # programme_seance += theme + '\n'

        if theme == 'PERTE DE POIDS':
            lettre = random.choice(["A","B","C","D","E","F","G","H","I"])
            programme_seance += PerteDePoids(lettre)
        elif theme == 'PUISSANCE':
            lettre = random.choice(["A","B","C","D","E","F","G","H","I"])
            programme_seance += puissance(lettre)
        elif theme == 'REMISE EN FORME':
            lettre = random.choice(["A","B","C","D","E","F"])
            programme_seance+= remiseEnForme(lettre)
        elif theme == 'BOX TO BOX':
            lettre = random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N"])
            programme_seance += BoxTOBOX(lettre)
        
    else:
        programme_seance = 'choix invalide'


    ### partie Bonus


    if ajout_Bonus == 1:
        exercices_Bonus = ProgammeBonus(niveau)

        programme_seance += f'PARTIE BONUS: \n {exercices_Bonus}'
    else:
        pass
    return programme_seance

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
    if nbr_seances == 3:
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
        return "Nombre de séances invalide. Veuillez choisir entre 3 et 7 séances par semaine."

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


# def save_to_pdf_arabic(content, filename="document_ar.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Importation de la police prenant en charge l'arabe (exemple : Amiri-Regular.ttf)
    pdf.add_font("Amiri", fname='./dejavu-sans/DejaVuSans.ttf', uni=True)   
    pdf.set_font("Amiri", size=12)

    # Modèle pour détecter les liens
    link_pattern = r'(https?://\S+)'
    line_height = 5

    # Séparation des lignes
    lines = content.split('\n')
    for line in lines:
        # Recherche des liens dans la ligne
        match = re.search(link_pattern, line)
        if match:
            url = match.group(0)  # Extraire l'URL
            pdf.set_text_color(0, 0, 255)  # Couleur bleue pour les liens
            pdf.cell(0, line_height, "ﻮﻳﺪﻴﻔﻟﺍ ﻂﺑﺍﺭ ", ln=True, align="R", link=url)  # Ajout du lien
        else:
            pdf.set_text_color(0, 0, 0)  # Couleur noire
            if "ﺍﻹﺣﻤﺎﺀ" in line:  # Exemple pour des mots spécifiques
                pdf.set_font("Amiri", style="", size=12)
                pdf.cell(0, line_height, line, ln=True, align="R", border="B")  # Souligné
            elif line.strip() and (line.isupper() or line.startswith("ﻡﻮﻴﻟﺍ") or line.startswith("ﺓﺄﻓﺎﻜﻤﻟﺍ")):
                pdf.set_font("Amiri", style="", size=12)  # Gras
                pdf.cell(0, line_height, line, ln=True, align="R")
            else:
                pdf.set_font("Amiri", style="", size=12)  # Texte normal
                pdf.cell(0, line_height, line, ln=True, align="R")

    pdf.output(filename)
    return f"Saved to {filename}"




def translate_programme(language, programme):
    if not programme:
        raise ValueError("Programme content is empty or None. Please provide valid text.")
    
    lines = programme.split('\n')
    translated_lines = []
    
    # for line in lines:
        # translated_line = translate(language, line) or ""
        # translated_lines.append(translated_line)
    
    translated_programme = '\n'.join(translated_lines)
    
    
    return translated_programme



# def save_text_to_pdf_arabic(input_file, output_pdf):
    
    # Lire le contenu du fichier texte
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Appeler la fonction pour sauvegarder en PDF
    result = save_to_pdf_arabic(content, output_pdf)
    print(result)

# Appeler la fonction avec le nom du fichier texte
# save_text_to_pdf_arabic("arabic_programme.txt", "document_ar.pdf")

# exos = programme_seance('MUSCULATION EN SALLE (Specifique)','General','BRAS','Debutant')


# trans_exos = translate_programme('ar',programme=exos)
# print(trans_exos)

# save_to_pdf(exos)
# save_to_pdf_arabic('arabic_programme.txt', "arabic_programme.pdf")


