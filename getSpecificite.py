import numpy as np
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
    
    
    # Normalise les poids
    total = sum(weights.values())
    normalized = {k: v/total for k, v in weights.items()}
    
    # Choisit une spécificité aléatoire selon les poids
    choices = list(normalized.keys())
    probabilities = list(normalized.values())
    return np.random.choice(choices, p=probabilities)
