import streamlit as st
import re
from programmeSport import programme_semaine_utilisateur, save_to_pdf, translate_programme
import numpy as np
from datetime import datetime, timedelta
import locale

# Configuration robuste de la locale
try:
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'fr_FR')
    except locale.Error:
        locale.setlocale(locale.LC_TIME, 'fr')
    finally:
        # Dictionnaire de traduction manuelle au cas où
        DAY_TRANSLATIONS = {
            'Monday': 'Lundi',
            'Tuesday': 'Mardi',
            'Wednesday': 'Mercredi',
            'Thursday': 'Jeudi',
            'Friday': 'Vendredi',
            'Saturday': 'Samedi',
            'Sunday': 'Dimanche'
        }

def get_specificite_weights(poste, profil, programme):
    weights = {
        "GARDIENS": {
            "PANTHERE (PUISSANT)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 35,
                    'FORCE MAX': 35,
                    'MASSE MUSCULAIRE': 30,
                    'RÉPÉTITIONS DES EFFORTS': 25,
                    'FORCE EXPLOSIVE': 40
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 40,
                    'FORCE MAX': 40,
                    'PERTE DE POIDS': 20,
                    'REMISE EN FORME': 30,
                    'RÉPÉTITIONS DES EFFORTS': 45,
                    'FORCE EXPLOSIVE': 50
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 30,
                    'DOS': 25,
                    'ÉPAULE': 20,
                    'PECTORAUX': 15,
                    'JAMBES': 40
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 25,
                    'DOS': 30,
                    'ÉPAULE': 20,
                    'PECTORAUX': 15,
                    'JAMBES': 40
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 40,
                    'ENDURANCE': 20,
                    'RÉSISTANCE': 20,
                    'SPRINT': 50,
                    'PERTE DE POIDS': 20
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 40,
                    'PUISSANCE': 50,
                    'REMISE EN FORME': 20,
                    'BOX TO BOX': 20
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "PIEUVRE (HABILE)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 40,
                    'FORCE MAX': 25,
                    'MASSE MUSCULAIRE': 30,
                    'RÉPÉTITIONS DES EFFORTS': 40,
                    'FORCE EXPLOSIVE': 25
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 50,
                    'FORCE MAX': 50,
                    'PERTE DE POIDS': 20,
                    'REMISE EN FORME': 20,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 30
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 35,
                    'DOS': 30,
                    'ÉPAULE': 25,
                    'PECTORAUX': 20,
                    'JAMBES': 35
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 30,
                    'DOS': 35,
                    'ÉPAULE': 25,
                    'PECTORAUX': 20,
                    'JAMBES': 35
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 50,
                    'ENDURANCE': 40,
                    'RÉSISTANCE': 60,
                    'SPRINT': 30,
                    'PERTE DE POIDS': 20
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 50,
                    'PUISSANCE': 50,
                    'REMISE EN FORME': 20,
                    'BOX TO BOX': 30
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "ARAIGNEE (MALIN)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 25,
                    'FORCE MAX': 20,
                    'MASSE MUSCULAIRE': 15,
                    'RÉPÉTITIONS DES EFFORTS': 40,
                    'FORCE EXPLOSIVE': 40
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 50,
                    'FORCE MAX': 30,
                    'PERTE DE POIDS': 20,
                    'REMISE EN FORME': 20,
                    'RÉPÉTITIONS DES EFFORTS': 60,
                    'FORCE EXPLOSIVE': 40
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 40,
                    'DOS': 25,
                    'ÉPAULE': 30,
                    'PECTORAUX': 15,
                    'JAMBES': 30
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 35,
                    'DOS': 30,
                    'ÉPAULE': 25,
                    'PECTORAUX': 20,
                    'JAMBES': 35
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 30,
                    'ENDURANCE': 40,
                    'RÉSISTANCE': 45,
                    'SPRINT': 50,
                    'PERTE DE POIDS': 20
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 30,
                    'PUISSANCE': 30,
                    'REMISE EN FORME': 20,
                    'BOX TO BOX': 40
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "CHAT (EXPLOSIF)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 45,
                    'FORCE MAX': 25,
                    'MASSE MUSCULAIRE': 20,
                    'RÉPÉTITIONS DES EFFORTS': 25,
                    'FORCE EXPLOSIVE': 35
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 40,
                    'FORCE MAX': 35,
                    'PERTE DE POIDS': 30,
                    'REMISE EN FORME': 30,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 50
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 25,
                    'DOS': 30,
                    'ÉPAULE': 20,
                    'PECTORAUX': 15,
                    'JAMBES': 45
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 20,
                    'DOS': 35,
                    'ÉPAULE': 25,
                    'PECTORAUX': 15,
                    'JAMBES': 40
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 40,
                    'ENDURANCE': 30,
                    'RÉSISTANCE': 50,
                    'SPRINT': 30,
                    'PERTE DE POIDS': 20
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 40,
                    'PUISSANCE': 50,
                    'REMISE EN FORME': 20,
                    'BOX TO BOX': 20
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            }
        },
        "DÉFENSEURS": {
            "CASSEUR (DURE)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 35,
                    'FORCE MAX': 45,
                    'MASSE MUSCULAIRE': 45,
                    'RÉPÉTITIONS DES EFFORTS': 35,
                    'FORCE EXPLOSIVE': 54
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 30,
                    'FORCE MAX': 50,
                    'PERTE DE POIDS': 20,
                    'REMISE EN FORME': 20,
                    'RÉPÉTITIONS DES EFFORTS': 40,
                    'FORCE EXPLOSIVE': 50
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 40,
                    'DOS': 50,
                    'ÉPAULE': 30,
                    'PECTORAUX': 25,
                    'JAMBES': 45
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 35,
                    'DOS': 45,
                    'ÉPAULE': 25,
                    'PECTORAUX': 20,
                    'JAMBES': 40
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 50,
                    'ENDURANCE': 45,
                    'RÉSISTANCE': 45,
                    'SPRINT': 40,
                    'PERTE DE POIDS': 20
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 45,
                    'PUISSANCE': 50,
                    'REMISE EN FORME': 20,
                    'BOX TO BOX': 50
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "CONTROLEUR (MAITRISE)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 35,
                    'FORCE MAX': 35,
                    'MASSE MUSCULAIRE': 25,
                    'RÉPÉTITIONS DES EFFORTS': 35,
                    'FORCE EXPLOSIVE': 35
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 50,
                    'FORCE MAX': 30,
                    'PERTE DE POIDS': 20,
                    'REMISE EN FORME': 20,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 30
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 35,
                    'DOS': 45,
                    'ÉPAULE': 30,
                    'PECTORAUX': 20,
                    'JAMBES': 40
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 30,
                    'DOS': 40,
                    'ÉPAULE': 25,
                    'PECTORAUX': 20,
                    'JAMBES': 35
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 50,
                    'ENDURANCE': 50,
                    'RÉSISTANCE': 50,
                    'SPRINT': 30,
                    'PERTE DE POIDS': 20
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 45,
                    'PUISSANCE': 45,
                    'REMISE EN FORME': 30,
                    'BOX TO BOX': 30
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "POLYVALENT (ADAPTATION)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 30,
                    'FORCE MAX': 30,
                    'MASSE MUSCULAIRE': 25,
                    'RÉPÉTITIONS DES EFFORTS': 30,
                    'FORCE EXPLOSIVE': 30
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 50,
                    'FORCE MAX': 50,
                    'PERTE DE POIDS': 20,
                    'REMISE EN FORME': 20,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 50
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 30,
                    'DOS': 40,
                    'ÉPAULE': 25,
                    'PECTORAUX': 20,
                    'JAMBES': 35
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 25,
                    'DOS': 35,
                    'ÉPAULE': 20,
                    'PECTORAUX': 15,
                    'JAMBES': 30
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 50,
                    'ENDURANCE': 50,
                    'RÉSISTANCE': 50,
                    'SPRINT': 40,
                    'PERTE DE POIDS': 30
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 50,
                    'PUISSANCE': 50,
                    'REMISE EN FORME': 30,
                    'BOX TO BOX': 50
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "RELANCEUR (PROPRE)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 40,
                    'FORCE MAX': 53,
                    'MASSE MUSCULAIRE': 35,
                    'RÉPÉTITIONS DES EFFORTS': 40,
                    'FORCE EXPLOSIVE': 40
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 40,
                    'FORCE MAX': 35,
                    'PERTE DE POIDS': 30,
                    'REMISE EN FORME': 50,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 35
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 45,
                    'DOS': 55,
                    'ÉPAULE': 35,
                    'PECTORAUX': 25,
                    'JAMBES': 50
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 40,
                    'DOS': 50,
                    'ÉPAULE': 30,
                    'PECTORAUX': 20,
                    'JAMBES': 45
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 50,
                    'ENDURANCE': 50,
                    'RÉSISTANCE': 50,
                    'SPRINT': 30,
                    'PERTE DE POIDS': 30
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 50,
                    'PUISSANCE': 35,
                    'REMISE EN FORME': 40,
                    'BOX TO BOX': 50
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            }
        }, #############################################################################################################################
        "MILIEUX": {
            "ARCHITECTE (CONSTRUCTION)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 30,
                    'FORCE MAX': 25,
                    'MASSE MUSCULAIRE': 20,
                    'RÉPÉTITIONS DES EFFORTS': 30,
                    'FORCE EXPLOSIVE': 35
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 50,
                    'FORCE MAX': 30,
                    'PERTE DE POIDS': 20,
                    'REMISE EN FORME': 50,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 35
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 30,
                    'DOS': 40,
                    'ÉPAULE': 25,
                    'PECTORAUX': 20,
                    'JAMBES': 35
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 25,
                    'DOS': 35,
                    'ÉPAULE': 20,
                    'PECTORAUX': 15,
                    'JAMBES': 30
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 35,
                    'ENDURANCE': 50,
                    'RÉSISTANCE': 50,
                    'SPRINT': 30,
                    'PERTE DE POIDS': 20
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 50,
                    'PUISSANCE': 30,
                    'REMISE EN FORME': 30,
                    'BOX TO BOX': 50
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "GAZELLE (CARDIO)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 45,
                    'FORCE MAX': 30,
                    'MASSE MUSCULAIRE': 30,
                    'RÉPÉTITIONS DES EFFORTS': 45,
                    'FORCE EXPLOSIVE': 45
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 50,
                    'FORCE MAX': 30,
                    'PERTE DE POIDS': 20,
                    'REMISE EN FORME': 50,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 20
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 35,
                    'DOS': 45,
                    'ÉPAULE': 30,
                    'PECTORAUX': 20,
                    'JAMBES': 40
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 30,
                    'DOS': 40,
                    'ÉPAULE': 25,
                    'PECTORAUX': 15,
                    'JAMBES': 35
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 50,
                    'ENDURANCE': 50,
                    'RÉSISTANCE': 50,
                    'SPRINT': 30,
                    'PERTE DE POIDS': 30
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 50,
                    'PUISSANCE': 50,
                    'REMISE EN FORME': 30,
                    'BOX TO BOX': 50
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "PITBULL (AGRESSIF)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 30,
                    'FORCE MAX': 55,
                    'MASSE MUSCULAIRE': 52,
                    'RÉPÉTITIONS DES EFFORTS': 40,
                    'FORCE EXPLOSIVE': 55
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 30,
                    'FORCE MAX': 40,
                    'PERTE DE POIDS': 30,
                    'REMISE EN FORME': 30,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 50
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 45,
                    'DOS': 50,
                    'ÉPAULE': 35,
                    'PECTORAUX': 30,
                    'JAMBES': 50
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 40,
                    'DOS': 45,
                    'ÉPAULE': 30,
                    'PECTORAUX': 25,
                    'JAMBES': 45
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 50,
                    'ENDURANCE': 40,
                    'RÉSISTANCE': 30,
                    'SPRINT': 50,
                    'PERTE DE POIDS': 20
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 50,
                    'PUISSANCE': 50,
                    'REMISE EN FORME': 20,
                    'BOX TO BOX': 50
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "ROCK (UNE MACHINE)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 30,
                    'FORCE MAX': 55,
                    'MASSE MUSCULAIRE': 55,
                    'RÉPÉTITIONS DES EFFORTS': 35,
                    'FORCE EXPLOSIVE': 55
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 50,
                    'FORCE MAX': 50,
                    'PERTE DE POIDS': 30,
                    'REMISE EN FORME': 30,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 40
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 50,
                    'DOS': 55,
                    'ÉPAULE': 40,
                    'PECTORAUX': 35,
                    'JAMBES': 55
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 45,
                    'DOS': 50,
                    'ÉPAULE': 35,
                    'PECTORAUX': 30,
                    'JAMBES': 50
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 50,
                    'ENDURANCE': 50,
                    'RÉSISTANCE': 50,
                    'SPRINT': 40,
                    'PERTE DE POIDS': 30
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 50,
                    'PUISSANCE': 50,
                    'REMISE EN FORME': 30,
                    'BOX TO BOX': 40
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            }
        },
        "ATTAQUANTS": {
            "MAGICIEN (TALENTUEUX)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 35,
                    'FORCE MAX': 35,
                    'MASSE MUSCULAIRE': 35,
                    'RÉPÉTITIONS DES EFFORTS': 35,
                    'FORCE EXPLOSIVE': 35
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 55,
                    'FORCE MAX': 40,
                    'PERTE DE POIDS': 20,
                    'REMISE EN FORME': 40,
                    'RÉPÉTITIONS DES EFFORTS': 40,
                    'FORCE EXPLOSIVE': 40
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 35,
                    'DOS': 40,
                    'ÉPAULE': 30,
                    'PECTORAUX': 25,
                    'JAMBES': 40
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 30,
                    'DOS': 35,
                    'ÉPAULE': 25,
                    'PECTORAUX': 20,
                    'JAMBES': 35
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 50,
                    'ENDURANCE': 50,
                    'RÉSISTANCE': 40,
                    'SPRINT': 40,
                    'PERTE DE POIDS': 20
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 50,
                    'PUISSANCE': 40,
                    'REMISE EN FORME': 30,
                    'BOX TO BOX': 50
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "RENARD (FINSSEUR)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 50,
                    'FORCE MAX': 30,
                    'MASSE MUSCULAIRE': 25,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 50
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 50,
                    'FORCE MAX': 20,
                    'PERTE DE POIDS': 20,
                    'REMISE EN FORME': 20,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 55
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 40,
                    'DOS': 45,
                    'ÉPAULE': 35,
                    'PECTORAUX': 25,
                    'JAMBES': 45
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 35,
                    'DOS': 40,
                    'ÉPAULE': 30,
                    'PECTORAUX': 20,
                    'JAMBES': 40
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 50,
                    'ENDURANCE': 50,
                    'RÉSISTANCE': 40,
                    'SPRINT': 55,
                    'PERTE DE POIDS': 20
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 60,
                    'PUISSANCE': 50,
                    'REMISE EN FORME': 30,
                    'BOX TO BOX': 60
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "SNIPER (PRECISION)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 50,
                    'FORCE MAX': 30,
                    'MASSE MUSCULAIRE': 25,
                    'RÉPÉTITIONS DES EFFORTS': 40,
                    'FORCE EXPLOSIVE': 35
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 50,
                    'FORCE MAX': 40,
                    'PERTE DE POIDS': 30,
                    'REMISE EN FORME': 30,
                    'RÉPÉTITIONS DES EFFORTS': 40,
                    'FORCE EXPLOSIVE': 50
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 45,
                    'DOS': 50,
                    'ÉPAULE': 35,
                    'PECTORAUX': 25,
                    'JAMBES': 40
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 40,
                    'DOS': 45,
                    'ÉPAULE': 30,
                    'PECTORAUX': 20,
                    'JAMBES': 35
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 50,
                    'ENDURANCE': 40,
                    'RÉSISTANCE': 30,
                    'SPRINT': 60,
                    'PERTE DE POIDS': 30
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 60,
                    'PUISSANCE': 40,
                    'REMISE EN FORME': 30,
                    'BOX TO BOX': 50
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            },
            "TANK (PUISSANT)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 35,
                    'FORCE MAX': 50,
                    'MASSE MUSCULAIRE': 35,
                    'RÉPÉTITIONS DES EFFORTS': 40,
                    'FORCE EXPLOSIVE': 50
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 40,
                    'FORCE MAX': 60,
                    'PERTE DE POIDS': 30,
                    'REMISE EN FORME': 30,
                    'RÉPÉTITIONS DES EFFORTS': 50,
                    'FORCE EXPLOSIVE': 60
                },
                'MUSCULATION EN SALLE (Specifique)': {
                    'BRAS': 50,
                    'DOS': 55,
                    'ÉPAULE': 40,
                    'PECTORAUX': 35,
                    'JAMBES': 55
                },
                'MUSCULATION EN SALLE + CARDIO(Specifique)': {
                    'BRAS': 45,
                    'DOS': 50,
                    'ÉPAULE': 35,
                    'PECTORAUX': 30,
                    'JAMBES': 50
                },
                'CARDIO EN SALLE': {
                    'PUISSANCE': 65,
                    'ENDURANCE': 25,
                    'RÉSISTANCE': 25,
                    'SPRINT': 50,
                    'PERTE DE POIDS': 18
                },
                'PROGRAMME DEHORS': {
                    'PERTE DE POIDS': 30,
                    'PUISSANCE': 65,
                    'REMISE EN FORME': 30,
                    'BOX TO BOX': 50
                },
                'PROGRAMME MAISON': {
                    'Perte DE POIDS': 50,
                    'RENFORCEMENT': 50,
                    'BRULER DES CALORIES': 50
                }
            }
        }
    }  
    return (weights.get(poste, {}).get(profil, {}).get(programme, {}))

def choose_specificite(weights, current_specificite):
    if not weights:
        return current_specificite
    
    # Retire la spécificité actuelle pour éviter les répétitions
    filtered_weights = {k: v for k, v in weights.items() if k != current_specificite}
    
    if not filtered_weights:
        return current_specificite
    
    # Normalise les poids
    total = sum(filtered_weights.values())
    normalized = {k: v/total for k, v in filtered_weights.items()}
    
    # Choisit une spécificité aléatoire selon les poids
    choices = list(normalized.keys())
    probabilities = list(normalized.values())
    return np.random.choice(choices, p=probabilities)
    
def display_program(content):
    # Séparer le contenu en lignes
    lines = content.split('\n')
    
    # Traiter chaque ligne
    for line in lines:
        # Détecter les liens
        match = re.search(r'(https?://\S+)', line)
        
        if match:
            # Ligne avec lien - afficher "Vidéo" centré et cliquable
            url = match.group(0)
            st.markdown(
                f'<div style="text-align: center; margin: 10px 0;">'
                f'<a href="{url}" style="color: blue; text-decoration: none;">Vidéo</a>'
                f'</div>',
                unsafe_allow_html=True
            )
        elif "Echauffement" in line:
            # Échauffement - texte centré avec soulignement
            st.markdown(
                f'<div style="text-align: center; margin: 10px 0; border-bottom: 1px solid black; '
                f'padding-bottom: 5px;">{line}</div>',
                unsafe_allow_html=True
            )
        elif line.strip() and (line.isupper() or line.startswith("Jour") or line.startswith("PARTIE BONUS")):
            # Titres en gras et centrés
            st.markdown(
                f'<div style="text-align: center; margin: 10px 0; font-weight: bold;">{line}</div>',
                unsafe_allow_html=True
            )
        else:
            # Texte normal centré
            st.markdown(
                f'<div style="text-align: center; margin: 5px 0;">{line}</div>',
                unsafe_allow_html=True
            )
            
def mettre_a_jour_specificite(programme):
    if programme == 'MUSCULATION EN SALLE':
        return ["ENDURANCE DE FORCE", "FORCE MAX", "MASSE MUSCULAIRE", 
                "PERTE DE POIDS", "REMISE EN FORME", "RÉPÉTITIONS DES EFFORTS", 
                "FORCE EXPLOSIVE"]
    elif programme == 'MUSCULATION EN SALLE (Specifique)':
        return ["BRAS", "DOS", "ÉPAULE", "PECTORAUX", "JAMBES"]
    elif programme == 'MUSCULATION EN SALLE + CARDIO(Generale)':
        return ["ENDURANCE DE FORCE", "FORCE MAX", 
                "PERTE DE POIDS", "REMISE EN FORME", "RÉPÉTITIONS DES EFFORTS", 
                "FORCE EXPLOSIVE"]
    elif programme == 'MUSCULATION EN SALLE + CARDIO(Specifique)':
        return ["BRAS", "DOS", "ÉPAULE", "PECTORAUX", "JAMBES"]
    elif programme == 'CARDIO EN SALLE':
        return ["PUISSANCE", "ENDURANCE", "RÉSISTANCE", "SPRINT"]
    elif programme == 'PROGRAMME MAISON':
        return ["Perte DE POIDS", "RENFORCEMENT", "BRULER DES CALORIES"]
    elif programme == 'PROGRAMME DEHORS':
        return ["PERTE DE POIDS", "PUISSANCE", "REMISE EN FORME", "BOX TO BOX"]
    return []

def main():
    st.title("Générateur de Programme Sportif Personnalisé DIPODDI")

    prenom = st.text_input("Prénom :", value="user")

    discipline = st.selectbox("Quel est votre discipline ?", ["FOOTBALL", "FUTSAL"])
    poste = st.selectbox("Quel est votre poste ?", ["GARDIENS", "DÉFENSEURS", "MILIEUX", "ATTAQUANTS"])

    profils = {
        "GARDIENS": ["PANTHERE (PUISSANT)", "PIEUVRE (HABILE)", "ARAIGNEE (MALIN)", "CHAT (EXPLOSIF)"],
        "DÉFENSEURS": ["CASSEUR (DURE)", "CONTROLEUR (MAITRISE)", "POLYVALENT (ADAPTATION)", "RELANCEUR (PROPRE)"],
        "MILIEUX": ["ARCHITECTE (CONSTRUCTION)", "GAZELLE (CARDIO)", "PITBULL (AGRESSIF)", "ROCK (UNE MACHINE)"],
        "ATTAQUANTS": ["MAGICIEN (TALENTUEUX)", "RENARD (FINISSEUR)", "SNIPER (PRECISION)", "TANK (PUISSANT)"]
    }

    profil = st.selectbox("Quel est votre profil ?", profils[poste])
    blessure = st.radio("Avez-vous une blessure ou douleur actuelle ?", ["NON", "OUI"])
    
    localisation = ""
    if blessure == "OUI":
        localisation = st.selectbox("Où se situe la blessure ?", [
            "CHEVILLES", "GENOUX", "HANCHES", "PIEDS", "ADDUCTEURS", "FESSIERS",
            "ISCHIOS JAMBIERS", "MOLLETS", "MOYEN FESSIERS", "PSOAS FLECHISSEURS", "QUADRICEPS"
        ])

    niveau = st.selectbox("Votre niveau :", ['Debutant', 'Intermidiaire', 'Avance'])
    programme = st.selectbox("Choisissez un programme :", [
        'MUSCULATION EN SALLE',
        'MUSCULATION EN SALLE (Specifique)',
        'MUSCULATION EN SALLE + CARDIO(Generale)',
        'MUSCULATION EN SALLE + CARDIO(Specifique)',
        'CARDIO EN SALLE',
        'PROGRAMME MAISON',
        'PROGRAMME DEHORS'
    ])

    specificites = mettre_a_jour_specificite(programme)
    specificite = st.selectbox("Spécificité :", specificites)
    #nbr_seances = st.slider("Nombre de séances par semaine :", min_value=3, max_value=7, value=4)
    est_dans_club = st.radio("Êtes-vous dans un club ?", ["OUI", "NON"])
    
    jours_match = []
    if est_dans_club == "OUI":
        jours_match = st.multiselect(
            "Quels jours avez-vous match ?",
            ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"],
            default=[]
        )
    
    jours_disponibles = st.multiselect(
        "Quels jours voulez-vous effectuer votre programme DIPODDI ? (3 jours min)",
        ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"],
        default=["LUNDI", "MERCREDI", "VENDREDI"]
    )
    nbr_seances = len(jours_disponibles)
    if len(jours_disponibles) < 3:
        st.warning("Veuillez sélectionner au moins 3 jours.")
        if st.button("Générer le programme du mois"):
        st.success(f"Programme généré pour {prenom}")
        if len(jours_disponibles) >= 3:
            weights = get_specificite_weights(poste, profil, programme)
            
            # Définir la date de début (aujourd'hui ou lundi prochain)
            today = datetime.now()
            start_date = today + timedelta(days=(0 - today.weekday()))  # Lundi de cette semaine
            
            for semaine in range(1, 5):
                current_specificite = specificite if semaine == 1 else choose_specificite(weights, specificite)
                st.markdown(f"### Semaine {semaine} - {current_specificite}")
                
                resultat = programme_semaine_utilisateur(
                    choix=programme,
                    theme_principal=current_specificite,
                    nbr_seances=nbr_seances,
                    niveau=niveau
                )
                
                # Traitement des jours avec dates
                lines = resultat.split('\n')
                processed_lines = []
                
                for line in lines:
                    for i, jour in enumerate(jours_disponibles):
                        if f"Jour {i+1}" in line:
                            # Calcul de la date
                            jours_semaine = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"]
                            date_index = jours_semaine.index(jour)
                            current_date = start_date + timedelta(days=date_index + (semaine-1)*7)
                            
                            # Formatage de la date
                            try:
                                date_str = current_date.strftime("%A %d/%m/%Y").capitalize()
                            except:
                                # Fallback si la locale ne fonctionne pas
                                english_day = current_date.strftime("%A")
                                date_str = DAY_TRANSLATIONS.get(english_day, english_day) + current_date.strftime(" %d/%m/%Y")
                            
                            match_str = " (jour de match)" if jour in jours_match else ""
                            line = line.replace(f"Jour {i+1}", f"{date_str}{match_str}")
                            break
                    
                    processed_lines.append(line)
                
                display_program('\n'.join(processed_lines))
if __name__ == "__main__":
    main()
