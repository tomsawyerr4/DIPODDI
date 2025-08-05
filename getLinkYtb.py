from fpdf import FPDF
import random

# KINE RENFORCEMENT

# Quadriceps
Quadriceps = [
    'https://youtube.com/shorts/05HR5YAvGDc?si=qUpGdv1_GX-7roVd',
    'https://youtube.com/shorts/IKmo4cBFEk4?si=xyuXIFAWx8MuXBaD',
    'https://youtube.com/shorts/bziCwpR4n8w?si=JjOiz1oLiVwtG1AG',
    'https://youtube.com/shorts/GzrMAtMgvFQ?si=mWjwHcJT0tB4d2TP',
    'https://youtube.com/shorts/zdrJ4GKFQ6c?si=fUecFqoCyN__IFYq',
    'https://youtube.com/shorts/TCdMMQmJOK8?si=gY1UmIqNXqbbbDDo'
]

# Psoas Fléchisseurs Hanches
Psoas_Flechisseurs_Hanches = [
    'https://youtube.com/shorts/kdokuhYUhvI?si=phE1j4BrXoEdjvrO',
    'https://youtube.com/shorts/5vlR3j5ULog?si=sU8YbO7_17djAGRQ',
    'https://youtube.com/shorts/uvgma7UsCKM?si=_3DOD4Sl2mghSPTx',
    'https://youtube.com/shorts/RmMbh-yXGUQ?si=HR5Y5HxFFpgkxcNe',
    'https://youtube.com/shorts/nznd4lI3KEA?si=8Kn7ZwCENvytEp7B',
    'https://youtube.com/shorts/KrKj07QJbx0?si=3LB0YL4KyV5JmS-X'
]

# Pieds
Pieds = [
    'https://youtube.com/shorts/kQjdeoz7fSY?si=Pvvc5XHnQbYzgaTG',
    'https://youtube.com/shorts/zIm7uiXVcdo?si=6ltw6L1JhJHB6qhn',
    'https://youtube.com/shorts/SY--0iWYaC8?si=ITDyUzkQeUroJ0ps',
    'https://youtube.com/shorts/_onHMkRo5kc?si=2ixd4llddddkgZmR',
    'https://youtube.com/shorts/lY1YjXsd5s4?si=c4fAEwVghKzGOllS',
    'https://youtube.com/shorts/rgu8MNT89ME?si=SmmuZPR_PfGEX3PY'
]

# Moyen Fessiers
Moyen_Fessiers = [
    'https://youtube.com/shorts/z_tqjn-LV24?si=6Dn8ZiFVZcEiK3As',
    'https://youtube.com/shorts/z_tqjn-LV24?si=hgNY64IrSibEtSqQ',
    'https://youtube.com/shorts/WWp79ePdI4g?si=R3HArwJKs1SfhBMG',
    'https://youtube.com/shorts/Ecwp7jL_8u4?si=gTSSGCkQpgr5Wag1',
    'https://youtube.com/shorts/_8JfY3ofVnE?si=K-UmRwFO0BVjAx7c'
]

# Mollets
Mollets = [
    'https://youtube.com/shorts/3EB7ZAB5AWo?si=bQwB2rFmyLNhedIA',
    'https://youtube.com/shorts/L0_QOx5h7CY?si=GBw67rUYMh-5vcpg',
    'https://youtube.com/shorts/JRd9zoOL_dY?si=iFoZ3-tLrTn_IIwy',
    'https://youtube.com/shorts/h3csfW9JrdA?si=7JtXoOusaMtIpzVg',
    'https://youtube.com/shorts/ZM6c015fDl0?si=Yixah63kr4-iqPFO'
]

# Ishios Jambiers
Ishios_Jambiers = [
    'https://youtube.com/shorts/ydpzy7IIFOM?si=22wthTIPWdCUwhzy',
    'https://youtube.com/shorts/Pdy2NVmSfko?si=AGNdfKfcaZcffczg',
    'https://youtube.com/shorts/AVluREI0nkU?si=4af1ajbjjyzvb-XX',
    'https://youtube.com/shorts/yWUxQQP_UVI?si=xRGLDyCsyLdpZa15',
    'https://youtube.com/shorts/Hg9bUiEmnUc?si=PLyixXaOrMC8xgHj'
]

# Fessiers
Fessiers = [
    'https://youtube.com/shorts/SdZKcrOCiJ4?si=0Og5vOUcWycuPudU',
    'https://youtube.com/shorts/_YutftKthMc?si=8IALrSOE0raI7WCs',
    'https://youtube.com/shorts/eprrreviA-Y?si=47coyzdLcFJ95p9t',
    'https://youtube.com/shorts/wGrw4sHYzqo?si=1v2ytFKXyQa5-1u1',
    'https://youtube.com/shorts/VxSiapVUcvQ?si=pu9uXihHne4sc_OW',
    'https://youtube.com/shorts/3nzCdHztpqM?si=lbuQSX_ZOgE2yhqJ',
    'https://youtube.com/shorts/ejXv68SlgJ0?si=RaNT5eZCIJ1vtWEd'
]

# Chevilles
Chevilles = [
    'https://youtube.com/shorts/mma9QnLC0kc?si=onXdPvGf9cyAUqmN',
    'https://youtube.com/shorts/_ONChb1TqNE?si=hPlgmHDkqvh2Q5N5',
    'https://youtube.com/shorts/taAgzIx25pA?si=yLzCoQGugLEZlQls',
    'https://youtube.com/shorts/tPFFfJ093ns?si=DXjehanIZ2Hh4ZA3',
    'https://youtube.com/shorts/vaTGg6ByiPg?si=bCfedubbTwTVdWvH'
]

# Adducteurs
Adducteurs = [
    'https://youtube.com/shorts/JUlDFRTNA6w?si=p0M_4LqKKPDmlUyX',
    'https://youtube.com/shorts/HuS1WuH7M7s?si=ASOkotzT5aHG2mSi',
    'https://youtube.com/shorts/0Y1d_xR0HKY?si=BiT5U8RZCsqV4rkm',
    'https://youtube.com/shorts/8JuNUeqNg7w?si=szgaMuqcYqPOTW8p',
    'https://youtube.com/shorts/pHusO6546sc?si=y-duF5B-kC33_Zir'
]


#KINE MOBILITÉ

# Pied Voute Plantaire
pied_voute_plantaire = [
    "https://youtube.com/shorts/2xsX7cNsMyk?si=Fg-BLBsR9k9bWoly",
    "https://youtube.com/shorts/MFgpE3FBsuo?si=iBG0WY6PtEpPN2ls",
    "https://youtube.com/shorts/ALnYLAPsD1w?si=6CEAcOMuz2k3FuXh",
    "https://youtube.com/shorts/kMO8D8eb7Xo?si=eRjlCSpNx8FEDkem"
]

# Hanche
hanche = [
    "https://youtube.com/shorts/Hem1BU0Hxiw?si=tWM1ZucLrHcHJLlx",
    "https://youtube.com/shorts/LrKRE0t6uuo?si=v0PmL5FYdRmvJZRi",
    "https://youtube.com/shorts/lzgAXKHsT-A?si=j8HksjG9BjI0mCf6",
    "https://youtube.com/shorts/p6Em-gZgvuU?si=9vYRqLpYMNA_dPrQ"
]

# Genoux
genoux = [
    "https://youtube.com/shorts/dAOZ1DIwS_k?si=cdJzITl3IBdS_SnJ",
    "https://youtube.com/shorts/Z9fhJGCC5yo?si=rc_vKxAlqyHMLZQ3",
    "https://youtube.com/shorts/P9q9s73dhcY?si=5HDjmzl-bvyq2aNB"
]

# Chevilles
chevilles = [
    "https://youtube.com/shorts/avXpC0-grZ8?si=4zt1Z7NjeDuf60zU",
    "https://youtube.com/shorts/vvIH4O4BltY?si=FaFzB-jaDDEBg_Dh",
    "https://youtube.com/shorts/kGDXD0mt6RU?si=QwLMJaCGTFkJep_E",
    "https://youtube.com/shorts/AXj80wM2dnY?si=3ad3H97_IdP509uB",
    "https://youtube.com/shorts/IbxH9o3TqUA?si=_sGfxKJCqtg6pUBC"
]


#PROGRAMME GRATUIT MAISON

cardio = [
    "https://youtube.com/shorts/0agTTLqEBDo?si=T85-f6-0nUFrmmsf",
    "https://youtube.com/shorts/1-_dvwTVd6g?si=JO91dax3i6ncCiAU",
    "https://youtube.com/shorts/8ige7jhJuOc?si=VcShB6rnuq2ELsS6",
    "https://youtube.com/shorts/94lMAmmpuFM?si=xqHlI7d1XcOaB3A1",
    "https://youtube.com/shorts/9P2h17GJqlg?si=wb--UzYuaDVeaI0v",
    "https://youtube.com/shorts/A-zAPau66ac?si=PoEISGE7-xt13b8I",
    "https://youtube.com/shorts/D231oAExvbo?si=9Fq-qRW3FcejXMgP",
    "https://youtube.com/shorts/DAj3ReIVqj4?si=aOQiqDs9-yr32Ecg",
    "https://youtube.com/shorts/H2oDhb5h6FY?si=mfJC98p_Pr1flg5D",
    "https://youtube.com/shorts/HyNQX-mZOgM?si=DNp1WqgLhsg9g1SL",
    "https://youtube.com/shorts/Hz4QAamSytE?si=IeprP10MSe_9CLDh",
    "https://youtube.com/shorts/I_mpQjwhm10?si=B0p3hFL3Nz8fiokm",
    "https://youtube.com/shorts/In16LZOKH64?si=EM80Q1CWO8tEjTbj",
    "https://youtube.com/shorts/K86XtCL2DsI?si=8IIDc94E7iIejHIR",
    "https://youtube.com/shorts/KxcOh0eDv4Y?si=5fk094YTmbuv0Ogq",
    "https://youtube.com/shorts/LWi75HPvz3Y?si=QI-cDa9MZ5xXYs8x",
    "https://youtube.com/shorts/LWyOnYcY-b4?si=L0BVZmhMN7vo22g7",
    "https://youtube.com/shorts/ObkAeR5jviY?si=n8q_kwuqglTsJeJA",
    "https://youtube.com/shorts/Q0gHHIOF5qs?si=3GXJxM7wrL_QGgC2",
    "https://youtube.com/shorts/QvWDu-caqZ0?si=PHIwhbNqfmh1HFhP",
    "https://youtube.com/shorts/S4CkPRvMuSQ?si=CCKExNFnNqLeq5WX",
    "https://youtube.com/shorts/TY1jbTBewpw?si=6ZmVhHyDfSfA5e8r",
    "https://youtube.com/shorts/VGUQouIknj4?si=VWjvarSN48UmNHoU",
    "https://youtube.com/shorts/XX94L3sMPfc?si=Jy9eqRdVQpUySFxd",
    "https://youtube.com/shorts/YWpOhfveyOA?si=N4MD4my0BKAnP9Zv",
    "https://youtube.com/shorts/_iPXls5g968?si=_ckfooDC4UnE8vsH",
    "https://youtube.com/shorts/a4m2ly2z0AM?si=XXsaQ3s7QU-TWNmM",
    "https://youtube.com/shorts/aqqGoG8AQ6U?si=pMqZPtDvU6WfO2rI",
    "https://youtube.com/shorts/bRMBSum63Cg?si=XPQhI0aVK_C1MMaZ",
    "https://youtube.com/shorts/cvdLWUv2TAU?si=mCDlbh2aN5NGipKl",
    "https://youtube.com/shorts/efcAyXO_ruE?si=oA22650AVvz7Hqwk",
    "https://youtube.com/shorts/hckp15sC3fo?si=GJD4dZ7DZIElcDhI",
    "https://youtube.com/shorts/ibiPv340Bc8?si=yjTcEFKP3JZUsbsu",
    "https://youtube.com/shorts/j-XaHL3MZp4?si=lXk7tNyw745Vq_ob",
    "https://youtube.com/shorts/j90R2w2S_Ic?si=XsrxvEwhOg4cK4s3",
    "https://youtube.com/shorts/jyYi_SzP868?si=vFbEEUwM_fCUZzTU",
    "https://youtube.com/shorts/m1-yQOy87Dg?si=88C9K5w4OU-IsWvE",
    "https://youtube.com/shorts/mTbuFt8JUf4?si=o57O3TMkaX33VOnd",
    "https://youtube.com/shorts/moCoaOAnXm8?si=MqqYq6PLqYABT9ef",
    "https://youtube.com/shorts/pFhk9fCburg?si=iIX3owhwJ5XQZLyF",
    "https://youtube.com/shorts/pVdimwL-Q-E?si=6Ea9S-y2aykZtijR",
    "https://youtube.com/shorts/q4OaYt9paYE?si=faeM7FfivzYKVCpj",
    "https://youtube.com/shorts/rL6YSzeJLpA?si=CgEgiy669otI9SoM",
    "https://youtube.com/shorts/r_E7F2CxskI?si=MXR9NvL8KyZ1idXn",
    "https://youtube.com/shorts/sRdUS6P0Xq8?si=kR_UMNes6ER2n7XF",
    "https://youtube.com/shorts/syUylhYZ3Ow?si=bOr0KL3Ogo7UQSOJ",
    "https://youtube.com/shorts/ts64BaBgL18?si=oo1mx79JEoUTM1QL",
    "https://youtube.com/shorts/wgb_eFMivR0?si=gzEKlRRBj0y2aht5",
    "https://youtube.com/shorts/xmiJbgFUFX0?si=Wa6hEJ_v4m3YmoO6",
    "https://youtube.com/shorts/yfYFlqHZ1i8?si=c9Tyhm2EwZ0O6-Xb",
    "https://youtube.com/shorts/1bOtpKjmYFA?si=FWmid5yTN4n2o1_x",
    "https://youtube.com/shorts/AQffsv8l0fw?si=tChlXOBh9S1zmXiT",
    "https://youtube.com/shorts/Doa0MuXwz1Y?si=EQcLa1ImLX1YyyJl",
    "https://youtube.com/shorts/HNwUQUMTtCI?si=6WzNVWRHLlSUMVNK",
    "https://youtube.com/shorts/MRFEC7P72yc?si=s8PWUilMeEdsxT-g",
    "https://youtube.com/shorts/NEc2KFrEons?si=YIPAsK97SFG1zFU_",
    "https://youtube.com/shorts/YWZ48FX5pbY?si=NxhVfGAxKOFl7l8a",
    "https://youtube.com/shorts/g-scz7j6qeQ?si=qBE1LUgmc9oqA1LF",
    "https://youtube.com/shorts/j8Q1FytUvaM?si=Mc7Euu60703oj2k_"
]

renforcement = [
    "https://youtube.com/shorts/4mZiR6juYvQ?si=MGO-CE2OAElk1F3H",
    "https://youtube.com/shorts/7iOwd-vcM1Y?si=X28H5MAiemABMgpr",
    "https://youtube.com/shorts/9lD41hGN33U?si=HZr_6g20UjIIC2Xa",
    "https://youtube.com/shorts/A2QgyQccmkc?si=WKNoW_8Fv_ZCUJEZ",
    "https://youtube.com/shorts/EXJhlEGDOtM?si=GFeC481FGlmcwQWR",
    "https://youtube.com/shorts/FQunMsCY2S4?si=SI3TNlMwZaXPQfOt",
    "https://youtube.com/shorts/Lt9IM1Btxs8?si=s15B8-5ZdlXD_jYv",
    "https://youtube.com/shorts/VTCVcS0ZYPU?si=p-CoR6XMp78D6Mg7",
    "https://youtube.com/shorts/Wz_XlGy2r8I?si=FV9nXDf2GLHRXYbq",
    "https://youtube.com/shorts/jPH87b3jEH4?si=ujz8mJs_feOLMLb8",
    "https://youtube.com/shorts/kEIZymTabJo?si=HoTkWUs08T1-Rr7O",
    "https://youtube.com/shorts/sAYigNyptcE?si=dmPPN8vWGDPKAx4B",
    "https://youtube.com/shorts/xfmRurcAx-s?si=owEgGMDmy4mmwU3u",
    "https://youtube.com/shorts/y9q5Lg-Tsvw?si=GpixBHPdsI87N2EG",
    "https://youtube.com/shorts/GULC7LkCYN0?si=i3Zgqa0M7-Tq3R1h",
    "https://youtube.com/shorts/IfUVcGOb4yg?si=mZHTPjnFgqPlDROA",
    "https://youtube.com/shorts/SKJy-sRZzZw?si=xS9VFS4-rwGTBLDk",
    "https://youtube.com/shorts/XwppXLYfLTo?si=56rRntJw0hw4aky7",
    "https://youtube.com/shorts/dL5L6TOA6Z8?si=ZbpPmgoNZOoV5763",
    "https://youtube.com/shorts/esHt_ozPaes?si=Kdwr5uL-wIM2dvS7",
    "https://youtube.com/shorts/jQsuxabTsSg?si=k2paOo5UgqutmwJV",
    "https://youtube.com/shorts/oSQ-SzXXXJw?si=CWDtx9fu36gIkoP-",
    "https://youtube.com/shorts/HWHVw1jKPQA?si=uzmZ92Pmf0D12K05",
    "https://youtube.com/shorts/Mjj8g1pqmwY?si=SFyU6P4y63-hjx-C",
    "https://youtube.com/shorts/3AtNuJcOtgA?si=H7PNzvMDERbqFShQ",
    "https://youtube.com/shorts/3LBmCMbReps?si=jLYygPI43127JozO",
    "https://youtube.com/shorts/5ANwnOhZNXU?si=NGitEEOUZWFLSVkI",
    "https://youtube.com/shorts/DHmtBGQKUEI?si=l-B_bMwruyeBP5PX",
    "https://youtube.com/shorts/Y09Q93d0Ddk?si=BPmDOVyeXGY1EWw4",
    "https://youtube.com/shorts/cZxg5ii2tPI?si=bbEKiYS5WdoPrOre",
    "https://youtube.com/shorts/hUwO4QDv7tY?si=1_SsSi3eIkdqbAG7",
    "https://youtube.com/shorts/kw3uUWC1aaU?si=w7IcX_ovXxSvIc7x",
    "https://youtube.com/shorts/onRM9ys0FHI?si=VF9p6FVyb9Yb46Ki",
    "https://youtube.com/shorts/u3R0fmHQkvs?si=pW6_nCgbWiE6CaSI",
    "https://youtube.com/shorts/u5B6ntasNtk?si=qq1qddk3bH9WeYqI",
    "https://youtube.com/shorts/4b73iXRSr8s?si=zy7p94FAjXoQZZEf",
    "https://youtube.com/shorts/dFriMN_O7ns?si=2jOA9nLlExAC_mv7",
    "https://youtube.com/shorts/-2OVfN5SWI0?si=n6GoDPKXesMUZn-M",
    "https://youtube.com/shorts/2PeZgd-dDQA?si=lr-c73iMOb-09tRC",
    "https://youtube.com/shorts/7jhoYRjW4W8?si=4-hjpetqzflpaoyV",
    "https://youtube.com/shorts/9dPReYSPDEo?si=PfKjpmti2uz4Thay",
    "https://youtube.com/shorts/FhNhP56iF_s?si=zxXNtWTB4JMXF7mk",
    "https://youtube.com/shorts/MoD4WPEUmLQ?si=1NfXeTEbD8VlqPcJ",
    "https://youtube.com/shorts/NCII6SGPMQo?si=H0DF5bUA5GkVtoFb",
    "https://youtube.com/shorts/RxBivpr678U?si=eW5AmdDBTorEkXkq",
    "https://youtube.com/shorts/T3MSRFltTfk?si=kMQZPRkslEhrkxKJ",
    "https://youtube.com/shorts/UOIPYVxh-XU?si=Eu5LeUfDBcLYalDM",
    "https://youtube.com/shorts/V24bj9s2iFE?si=yJ50nnGjwswF3_FM",
    "https://youtube.com/shorts/X1CY9w4ZhR0?si=Q15omAIW_7KuSAkr",
    "https://youtube.com/shorts/_Vcrq4FuS18?si=tRrUymSWnYb6-A_K",
    "https://youtube.com/shorts/jdkxTgOreTw?si=SsXV8QdBlaGw5Zht",
    "https://youtube.com/shorts/psNY9JBuGA8?si=YmyKYaEVeqhYg7vs",
    "https://youtube.com/shorts/rfstIp6U0EQ?si=-guGlWjYEyGChzNX",
    "https://youtube.com/shorts/vnoFLq_Kr_c?si=J9UjS4QtqT5y6VUS",
    "https://youtube.com/shorts/2PVXepKrot4?si=R0hl4Qd4WnOXymwc",
    "https://youtube.com/shorts/BY6L8Au4jXk?si=TMwVL08x1JWOjWHa",
    "https://youtube.com/shorts/C0zVzX_vDFM?si=3Kg4Cz3vZVY_z3xB",
    "https://youtube.com/shorts/KCkIY7y8RKQ?si=dXdoUP736_PtF4JE",
    "https://youtube.com/shorts/R888LJ_r1ck?si=-YfnBXGyWBrbRyB8",
    "https://youtube.com/shorts/UINRkR9L_Go?si=KYYE4XphbXflBQrX",
    "https://youtube.com/shorts/inlGW14Y2vI?si=JQV0qwFbLvq0bCwq",
    "https://youtube.com/shorts/zjAWS7dJjA0?si=VE_iOU5e2M2iPRaU"
]

##PROGRAMME GRATUIT BONUS

ABDOS = [
    "https://youtube.com/shorts/FHjjTqxcB8w?si=ho-kzZxZJkkvKA_E",
    "https://youtube.com/shorts/-C79TR7Rvdc?si=x0mvP1oLXY4IG48C",
    "https://youtube.com/shorts/0pSJ6mfzHJE?si=HQMQFSk5rkiyXAk8",
    "https://youtube.com/shorts/1mrDGRnlwmE?si=pgjVWF22U8ZzttST",
    "https://youtube.com/shorts/55D_CHEx7oI?si=vPs1bbObAOBzr_sp",
    "https://youtube.com/shorts/5Rl3YZ3Vm-8?si=_GTNVXpMt-NhOe5s",
    "https://youtube.com/shorts/8YCCNcJQrjw?si=cC_BLnsyGnQ4JtuJ",
    "https://youtube.com/shorts/8vdQ2WGokxs?si=b9E6a-skAext3sX5",
    "https://youtube.com/shorts/A4u79ge-bDI?si=GA0yCrDlyGudY7l1",
    "https://youtube.com/shorts/AeymKJ5KNa0?si=MJk5RTPPyG44cZkV",
    "https://youtube.com/shorts/BCnRS8YIG5s?si=m_rtDchq-wfJICmC",
    "https://youtube.com/shorts/DmWpsSJRoUg?si=JlyI3zxsFLFIBDp2",
    "https://youtube.com/shorts/EzXEg8vsXF0?si=ciUlpcu3XEoQ2Cut",
    "https://youtube.com/shorts/Kn0xgs_xKeQ?si=IuKmzsqcCQpJW0yk",
    "https://youtube.com/shorts/M1WaAJMNGRo?si=jIP9suAjYMtrUI0A",
    "https://youtube.com/shorts/MhzCOvdFk6k?si=uddmlurCKtqqVMfU",
    "https://youtube.com/shorts/Ms2-saauSB8?si=nqpHds8QrqSN4f6v",
    "https://youtube.com/shorts/OgLG8TYScwo?si=mKOrODUtEibprMm4",
    "https://youtube.com/shorts/Qa8_jvhjdco?si=IedVP0O3MivMNyD1",
    "https://youtube.com/shorts/RtNJaY1jhus?si=JOSNl6JSJOZLfXO5",
    "https://youtube.com/shorts/VEflbldS2W8?si=SzEFBa8FGzC-719L",
    "https://youtube.com/shorts/WFBanM956Q8?si=s7i_daRn4gz3SlZ4",
    "https://youtube.com/shorts/aDW4jV--tlU?si=HNuB6tLa78QGGHhk",
    "https://youtube.com/shorts/aHS_y-7DBSQ?si=iIke3UFpJGx81NGI",
    "https://youtube.com/shorts/apWeP7KQzss?si=NquEIxQsdpmVv7Lh",
    "https://youtube.com/shorts/cD13kQFwamQ?si=G5-ro2UB-PRYaSxs",
    "https://youtube.com/shorts/c_1TrVgeIoo?si=RdFefvpvlnnLrWYZ",
    "https://youtube.com/shorts/dIx_9-1S9OM?si=MZSXH5PK7vsbzEs8",
    "https://youtube.com/shorts/dxjoSvJIt9c?si=vuMkgcIa88D_D1p1",
    "https://youtube.com/shorts/e3vL9NTBOD8?si=8kLiKCuUE4jJ2Slp",
    "https://youtube.com/shorts/eKT4xJt_luw?si=1-H3A8GDn55Sp7KE",
    "https://youtube.com/shorts/fby-Kv5V-cs?si=Ni2N4y9mlu7m_p6F",
    "https://youtube.com/shorts/jCxkLJ7dQQs?si=XfZDOsIL2jAbwZzj",
    "https://youtube.com/shorts/lBaXb6G3qdY?si=l_c5BgqwGm4TQRul",
    "https://youtube.com/shorts/lmptWZg6rQE?si=LPqFexUDGwb7qW3V",
    "https://youtube.com/shorts/n_zj6m61Rtw?si=ijOgeog2SO8K3MkA",
    "https://youtube.com/shorts/nwQ4b2gqMBE?si=Ua-pLo79rj_rpqMA",
    "https://youtube.com/shorts/oAAtI1FPRNU?si=hUVwDc_o2_iFxoOm",
    "https://youtube.com/shorts/oHgV-9U9CbY?si=siWNu0tdA0bBuQhM",
    "https://youtube.com/shorts/oO8e3NJ34DA?si=FensVwKBLaIlAtLa",
    "https://youtube.com/shorts/oRBiCQG2Cb8?si=fnt5iGZcpBkc90f3",
    "https://youtube.com/shorts/qYzVKdWulns?si=5EkaN0GPcZp_Gfy1",
    "https://youtube.com/shorts/sO2fm7K2LFY?si=USGOHvf9S10DghoW",
    "https://youtube.com/shorts/tyvCo_zhxuo?si=4ysBE-y4Vo5ZpFpr",
    "https://youtube.com/shorts/ugV6LCh96bY?si=pEQgSTWBgZDX-kbG",
    "https://youtube.com/shorts/uoa3D_F9Gek?si=Q3lUfb6ogBhSfmjD",
    "https://youtube.com/shorts/xfY8f_DZBFE?si=v77kM53vr4Z1MmtR",
    "https://youtube.com/shorts/yx0sg34-2qY?si=wTckcYSv1rtFfndq",
    "https://youtube.com/shorts/0uoMY7xJRxg?si=COZla940lavTuNYq",
    "https://youtube.com/shorts/2_j0jNDsybE?si=Qx0DmjEm94yTCRT_",
    "https://youtube.com/shorts/AQ9-CsvQCNI?si=e4KJqTyUmlo5rcG2",
    "https://youtube.com/shorts/BKIkR5OTrT8?si=pwxpE0ga7mXnGMre",
    "https://youtube.com/shorts/FnhGMHMiUF4?si=7swGQ4ZI5uZv_YXG",
    "https://youtube.com/shorts/KE48i0UnNuU?si=d2vskNGI-GB4owAk",
    "https://youtube.com/shorts/MDM0ZBNDGRM?si=gjb2eLq3ep78z7ql",
    "https://youtube.com/shorts/O0vrS2TMXKM?si=HI5mKthBxI7M6onC",
    "https://youtube.com/shorts/OeRyyZPi0f0?si=B9XyGoE_ndcTtHQF",
    "https://youtube.com/shorts/OmPOUsIgAAI?si=yPrqr5Z4l9J7_cn9",
    "https://youtube.com/shorts/ShC9vHtQ1VE?si=6Ril-Vhcjp_1Kmhz",
    "https://youtube.com/shorts/Tm4QIjr0W4w?si=iL4apvMqHKeXszt8",
    "https://youtube.com/shorts/Vqc9S60EMjo?si=RRAlnvfYeys-Gje1",
    "https://youtube.com/shorts/aVjJJut9n4g?si=AY33rIOhlvy96p5S",
    "https://youtube.com/shorts/dUurkUxIu_k?si=FJDrP3ClEqw-Yxrw",
    "https://youtube.com/shorts/eeR0xBPcIA4?si=s9Xrgua0-UYE1sKp",
    "https://youtube.com/shorts/eph63VK4UIk?si=tBtB7xdCdpuN0qYR",
    "https://youtube.com/shorts/kyUvs-A8BC4?si=PRpHyy7SP2jaxYBK",
    "https://youtube.com/shorts/oQc-zksDnAQ?si=rEn4IlW2OQVClsHt",
    "https://youtube.com/shorts/oyE9EAWJyOc?si=e1lzdg-5DZ5AtXOd",
    "https://youtube.com/shorts/pbFwUVX3-lU?si=E4VQhY4oY8OCmhin",
    "https://youtube.com/shorts/qyONW6UbHjU?si=w1Q9VrVlfmaBBKon",
    "https://youtube.com/shorts/tpsdzlN5GZs?si=3TEP4kqlQGr3Zrpg",
    "https://youtube.com/shorts/uuZj_7KleGc?si=l34y5sZD3LhTCivw"
]

POMPES = [
    "https://youtube.com/shorts/dtPHZ0Zd-jE?si=PPrk73x9fTFXU834",
    "https://youtube.com/shorts/egyQnsDcVUU?si=iGbDziTxvBcd-_5A",
    "https://youtube.com/shorts/lUg2kVNNrig?si=ushyJhxx-s4pg3NW",
    "https://youtube.com/shorts/oaWppeQ8xRQ?si=zbLWEX_DGBVI3I9s",
    "https://youtube.com/shorts/pO1RcFF0LJ0?si=YueUk5WEpj0QVRF5",
    "https://youtube.com/shorts/s5Q_6GcVV0U?si=ZgvgEbhu4meMMNIt",
    "https://youtube.com/shorts/tckP3mUPnag?si=8xtw-gyFKJC9uwmY",
    "https://youtube.com/shorts/vfkz3PKAPPE?si=ag3xt0htO4GATGIg",
    "https://youtube.com/shorts/wSmLXqmTgbQ?si=TFouvbyovUrszjWa",
    "https://youtube.com/shorts/CAr_ugYl40U?si=NplKfEwfCHHROVpx",
    "https://youtube.com/shorts/F8J5wpXtQgM?si=txruNj1U6pbxEnwu",
    "https://youtube.com/shorts/MRpkhhSwto8?si=UrSUoz0nm-9vw44N",
    "https://youtube.com/shorts/OZV5x6EdOec?si=DCo0AQmfXUHsfYOP",
    "https://youtube.com/shorts/UHPyledUqzA?si=bWULqwqzL9aK9SPj",
    "https://youtube.com/shorts/VJdyNIk3fxs?si=8rgKJMFrQ38UXQ9s",
    "https://youtube.com/shorts/WkHojcyM0Ks?si=tG75HSYQrP8QuR3J",
    "https://youtube.com/shorts/X6EsXzkbuGk?si=ffMZmajxh7_gK4od",
    "https://youtube.com/shorts/YaiqzdRurO8?si=Z6YUDuNPVDmjhRi0",
    "https://youtube.com/shorts/1UXYPbKSvG4?si=YcNL4zkJr4CUtMXN",
    "https://youtube.com/shorts/B1cysxnPvo8?si=YNLNlivZf0_I5zS9",
    "https://youtube.com/shorts/XvbqpamfnrQ?si=c834IJLnHOFTHMiC",
    "https://youtube.com/shorts/ZRjQbKkrlvI?si=Nnm2SRq5FsETdePw",
    "https://youtube.com/shorts/ZiuSABKUTTc?si=Y0y-dSDnGiVHJsmQ",
    "https://youtube.com/shorts/_YLAj1Tylak?si=HatYySgvqWwweYhx",
    "https://youtube.com/shorts/bq9TRYyk-bw?si=9sM9KzoS4Hj4y0ax",
    "https://youtube.com/shorts/c2kpt2hWsi0?si=cB_cY0hZ2gUqviw4"
]

GAINAGES = [
    "https://youtube.com/shorts/pMZFuFkykmA?si=omypoRLFfAUuHPg1",
    "https://youtube.com/shorts/0knDxost67c?si=-jCE6y2XuHf2zpyM",
    "https://youtube.com/shorts/0oXYdSIgzCg?si=9UKQw5L5unSAIPkN",
    "https://youtube.com/shorts/2Hscb3ZaJCA?si=LSVNeTld3FU3z9Tj",
    "https://youtube.com/shorts/7J6ekvM5ic0?si=_9wu14MTAZM0cDkw",
    "https://youtube.com/shorts/7Zo2wnNBZD0?si=f2b7loqI9cDBQLS-",
    "https://youtube.com/shorts/9KfQAGQWB-0?si=Emm7OXNYkK_kRKtt",
    "https://youtube.com/shorts/Cx9DJ4-FPIg?si=NmUXQ9a-SzGvtQy8",
    "https://youtube.com/shorts/DMKlmNtCXOg?si=6gmncBFQBLnsN5im",
    "https://youtube.com/shorts/FNzuRYM-NVA?si=3--jx1_SEgeKBrTM",
    "https://youtube.com/shorts/HTRA7P4yTls?si=iOgdOTNc2MaPsS5Z",
    "https://youtube.com/shorts/IULIkw7tlWo?si=LNzc6Rz-VW03n3SK",
    "https://youtube.com/shorts/JZnLjft0DfI?si=7V8G_cnkKzqXN6bS",
    "https://youtube.com/shorts/PwOFsR8pVE0?si=YZHCfbqWg_lL5CwF",
    "https://youtube.com/shorts/V_16CKCoXi8?si=7Sd3zCAn4KyoPuBi",
    "https://youtube.com/shorts/X1aqllvkXYs?si=JllOknPgU0Q0xEvQ",
    "https://youtube.com/shorts/YS38MiAFOLs?si=EBD22dtV6fGEao2I",
    "https://youtube.com/shorts/bBq2AZcvSQQ?si=Iv1kgiBS4THlJ4gq",
    "https://youtube.com/shorts/bXtaueKw5pw?si=pqPQOuwLcUL78dPz",
    "https://youtube.com/shorts/cT8FDM5s_ys?si=aExYRk93feYrUbXV",
    "https://youtube.com/shorts/ff0PdTxT9q4?si=QXpc4qr5sOMTN8Zp",
    "https://youtube.com/shorts/kiP-mKbvuFQ?si=qObyb9VM1ieVQMfk",
    "https://youtube.com/shorts/l3zgH4Jf5Xc?si=Sbd7Xm-Kb6OFDRNz",
    "https://youtube.com/shorts/m_27_EBCALw?si=8kgXY8VI_mk2c5d8",
    "https://youtube.com/shorts/pFDCTzfUK_Q?si=hixBDDmASfYoVsQz",
    "https://youtube.com/shorts/qRa5Edo9Z-U?si=mwJBVPeofA5xKe5C",
    "https://youtube.com/shorts/rqmY4Kkh-9U?si=ihWgwHel64ny8BwU",
    "https://youtube.com/shorts/sBCyP_iGJG4?si=dTFKx9WVBhf0z6pV",
    "https://youtube.com/shorts/txJ3T9Sj0Ck?si=-P6j0_sEY1NSAas8",
    "https://youtube.com/shorts/v9keA20vANA?si=36FJwwbyXIQXu4pe",
    "https://youtube.com/shorts/v9pQzSq_QA8?si=ac5LGSeldNeRSJ4_",
    "https://youtube.com/shorts/w42JqLa-ZDQ?si=1le8cgXGWU7lbF-k",
    "https://youtube.com/shorts/wZ85ALFy7kU?si=o5sskF_KqgJg8ldE",
    "https://youtube.com/shorts/xZlGJc_nxmU?si=r9pIpN19UPYqQntS",
    "https://youtube.com/shorts/zEI7gHU_Sg8?si=4gI9EhvKMjOJ_p-m",
    "https://youtube.com/shorts/zHFwLnFmxmU?si=mJxNeXj2I_LXI1TV"
]

##TUTO CARDIO

VELO_ENDURANCE = [
    "https://youtube.com/shorts/IL2fF-2G1SA?si=qbo96dxP9mnaue2l"
]

VELO_PUISSANCE = [
    "https://youtube.com/shorts/0G6vdBt6uys?si=gopLv8wkx1yxMkPo"
]

TAPIS_RÉSISTANCE = [
    "https://youtube.com/shorts/KxiO7DfDuO4?si=eHkyxQJtrW_ufMgc"
]

TAPIS_PUISSANCE = [
    "https://youtube.com/shorts/1VFwn0chdOM?si=eT83mW-rSSwXjXvy"
]

TAPIS_ENDURANCE = [
    "https://youtube.com/shorts/yQuD5T7MSIY?si=_q8MkPirWqn9khC_"
]

SPRINT_EN_COTE = [
    "https://youtube.com/shorts/xW0n7BhD80A?si=StHKpUnCY-Sobhhu"
]

RAMEUR = [
    "https://youtube.com/shorts/PqkRs9SLU8U?si=ZImTMweVlCawyPML"
]

MARCHE = [
    "https://youtube.com/shorts/OEnjPm4zPvE?si=e_Trv67A0TsmSNV6"
]

MARCHE_EN_COTE = [
    "https://youtube.com/shorts/d1fzhB1glsc?si=BPAJKjXbEFhPxr4N"
]

ELLIPTIQUE_NORMAL = [
    "https://youtube.com/shorts/HwZQ9Cz2Igo?si=AjyYtfiimU-7udg1"
]

ELLIPTIQUE_INTENSE = [
    "https://youtube.com/shorts/60ktrN58nhg?si=W1pe7Fz3NY4AnLrO"
]

##TUTO MUSCULATION

BRAS = [
    "https://youtube.com/shorts/bwKQtIsbDlc?si=KQIvG9trqVT1vseE",
    "https://youtube.com/shorts/3ORL_3I_yO8?si=t1nakbIGbHw_TGe2",
    "https://youtube.com/shorts/4W1Vxinj7Cc?si=5VnMU3DKbOkJQHBj",
    "https://youtube.com/shorts/KpACz0Quf2Y?si=9QF9hienzxyVgt63",
    "https://youtube.com/shorts/5PMPmzX-pj0?si=iPzgleRrYVwpGcf-",
    "https://youtube.com/shorts/FYAxHurQMc8?si=Mk3k82e9hejLVSwA",
    "https://youtube.com/shorts/k52Y6HiUMnw?si=XvqE3-sg9paMmBC8",
    "https://youtube.com/shorts/a-hQ4YvwO3c?si=taC0tgD6wnjeVVWU",
    "https://youtube.com/shorts/Qx3RyJ8Ffeg?si=O4tPljNV60xR6ClR",
    "https://youtube.com/shorts/1OryNw0bGPA?si=8iUrt_deF-nl3oyp",
    "https://youtube.com/shorts/3TkYPAT6YiU?si=t33S-lp-qkRd2YM2",
    "https://youtube.com/shorts/IV4TqOD7TSg?si=PFf0NB2DnxmtX0jT",
    "https://youtube.com/shorts/RLmjB3G6G-A?si=c2NnhwX1ImCw5yGO",
    "https://youtube.com/shorts/EqgF5tl4lsU?si=lJ3jDCZQr-USmpDr",
    "https://youtube.com/shorts/Q_Ek61tAKZs?si=G2TurvnYFzzf8cwr",
    "https://youtube.com/shorts/HvA7CaJwh4w?si=qeewIr2tPmTSh5AK",
    "https://youtube.com/shorts/C4i700_0vCQ?si=zc4MwCv419QpyYNi",
    "https://youtube.com/shorts/S-ctXxcCbqY?si=Bd_hcgyH4yjK9qgC",
    "https://youtube.com/shorts/tqXI1di-Scs?si=CbRODSGJtrTxj427",
    "https://youtube.com/shorts/2aozd3ce3ew?si=uSsgrj29VtWR9wbH",
    "https://youtube.com/shorts/NT8lw0rbm0g?si=EcgfCwNKIizq4SwD",
    "https://youtube.com/shorts/qra5gCFCebA?si=XP3o0C_UCXpcnyHv",
    "https://youtube.com/shorts/shPqDLH1QPM?si=ps5yMtm9kJHtyXgP",
    "https://youtube.com/shorts/ohR_uESI6YY?si=88fO7Q8VigKVZiCN",
    "https://youtube.com/shorts/uwEsWGuyJ8c?si=4NXbGHKg2U30PcLh",
    "https://youtube.com/shorts/9QUpKxQgGUI?si=DpKWakFp7tRftaWr",
    "https://youtube.com/shorts/AL_RrGhqo8M?si=fp0zbc6c5p7ByoEM"
]

DOS = [
    "https://youtube.com/shorts/kgtw5d42998?si=yEozIFunhLvc7lw6",
    "https://youtube.com/shorts/HrkT2FNWrrg?si=MqNf57hwkb8F2fUD",
    "https://youtube.com/shorts/sUGBt0fY77s?si=f6SyzXO5avMU8sO3",
    "https://youtube.com/shorts/1-YFlMEmDEs?si=r7nr63gEjMAzGigA",
    "https://youtube.com/shorts/QaWpgYmByTM?si=HZNcZNnbABLS6vKv",
    "https://youtube.com/shorts/KpzFeoMhPto?si=7YJ3mQwABbwQYv_M",
    "https://youtube.com/shorts/_eMGcaQ5rzs?si=HcLynWmsomXhPySe",
    "https://youtube.com/shorts/lmasox6N8VA?si=O28YiKP5G6eaY2ls",
    "https://youtube.com/shorts/MvueY8B2q4o?si=8y3VfHqaSqPm0zbQ",
    "https://youtube.com/shorts/THoeE7EVLLM?si=L0H-Ry6y4cGYn45B",
    "https://youtube.com/shorts/fsBMsR0lrfk?si=0WbgQSaN5qee52JC",
    "https://youtube.com/shorts/JRVZ06ZqofU?si=4NJyjR7lhuaE1eV4",
    "https://youtube.com/shorts/xJCJVw8rP1A?si=yGOU5Vj9cQF4c7Nd",
    "https://youtube.com/shorts/4Sv7HB0ZzIY?si=4q8fiR6Sdjldu9kq",
    "https://youtube.com/shorts/IG3rs3XoYvY?si=0PZ1JH08j0vUHD0F",
    "https://youtube.com/shorts/EfacqHYrKOs?si=JZd-uLDY82WWIdHf",
    "https://youtube.com/shorts/L_a8GC45PHY?si=Cqh2n61EWfqC6Gma",
    "https://youtube.com/shorts/LqbtL9DpJmU?si=B7-fRQfN-1A-j1Gg"
]

EPAULES = [
    "https://youtube.com/shorts/JSbZ3CkeAQg?si=j_CLdEn6r_IO2DZB",
    "https://youtube.com/shorts/YsNHINdI2s4?si=AL_OceXXo2LXOUs-",
    "https://youtube.com/shorts/HJZ7A0VQs6o?si=n0QsQhJKVUDCnXGj",
    "https://youtube.com/shorts/xgIQYtq4Tio?si=fnYwf_Ss6nm-3obj",
    "https://youtube.com/shorts/gJdp6Ri_dp8?si=obdM19KxOIQpr6zk",
    "https://youtube.com/shorts/DFNKfMe6dcA?si=k73jNYRlKt_bEF-6",
    "https://youtube.com/shorts/fHCc5uO07lA?si=M53H6_CXGOlb1rbE",
    "https://youtube.com/shorts/ebwsDi4DuCM?si=COgZoIjcGpGX_Kfb",
    "https://youtube.com/shorts/n5FPulqnuzE?si=tttKVO1ZpGOGEkK4",
    "https://youtube.com/shorts/f9Pkth7EP6g?si=u0Qt3DAC6YZP1Ru4",
    "https://youtube.com/shorts/au_SOwOCWg4?si=ShUvywxojR2_4ENS",
    "https://youtube.com/shorts/WX7Z7fZ4094?si=nwheHiZaoq0ABYuH",
    "https://youtube.com/shorts/erBXdVu6ONo?si=IYxt0jJBvJC891s7",
    "https://youtube.com/shorts/lgnUP3dz1P0?si=mQEszp2oEtNqcLpG",
    "https://youtube.com/shorts/w7QO6pOHrbk?si=j5-vLV4u-K6YWC2L",
    "https://youtube.com/shorts/gZouEVOnZcg?si=Pu2_tgEE-TX3utBT",
    "https://youtube.com/shorts/uzun1E5bu8M?si=uKlA4pkZjA_hYCwd",
    "https://youtube.com/shorts/KqchQZJHdhA?si=Ka7UJskCGI3F6d7f",
    "https://youtube.com/shorts/3xux5bpIY5o?si=E2YOltaO7vj8RWV6",
    "https://youtube.com/shorts/RQCuI8n9c34?si=yke6qvsE_1Dy2Os2",
    "https://youtube.com/shorts/r1VuoHW2bpI?si=nzp417QB7lmESe80",
    "https://youtube.com/shorts/1MxqyqJcN2Y?si=MX9FGsKudnzwq4no",
    "https://youtube.com/shorts/68nhsTdg_Fg?si=3TkYUB9q6TgZWo5x",
    "https://youtube.com/shorts/PQUIzw2Taxs?si=IXpcLLuKOHswKFVQ",
    "https://youtube.com/shorts/Ke1etRLIUNw?si=x-gFyMkGlDYAI9Yh",
    "https://youtube.com/shorts/guXsPqtxG8A?si=hyBedN1oT5uUa9ro"
]

JAMBES = [
    "https://youtube.com/shorts/7TopI0LAcOc?si=C9IRL5YFwMZKLSv-",
    "https://youtube.com/shorts/f198IoNb6pU?si=otHeQTO2cFaGECKK",
    "https://youtube.com/shorts/V5zGzu5SFG0?si=V6KR2qr3YRGwD6US",
    "https://youtube.com/shorts/Z4o9rnutvdA?si=NhOgbxpOPs_FW0ll",
    "https://youtube.com/shorts/CASNofbIq5o?si=tZdgpovzS2wD54bu",
    "https://youtube.com/shorts/SXpvJG8dz2o?si=eRFlVg03Q-KbyNLH",
    "https://youtube.com/shorts/udV65CGZFzA?si=cZvwrSqYPyR2Bwwb",
    "https://youtube.com/shorts/LdoaQhFjnus?si=18NSZabHaGE92KEM",
    "https://youtube.com/shorts/WWU_MVyg1Xs?si=qE34GC5Luyd4eTuq",
    "https://youtube.com/shorts/sCUaH2SAspQ?si=q5uC9fxxBfhDGZ1t",
    "https://youtube.com/shorts/FUs8XyVFQKY?si=_fIaoegiZbac3wm7",
    "https://youtube.com/shorts/sqvrPCMDvHM?si=bg7277UfK6fWEouY",
    "https://youtube.com/shorts/0oQ98CvcAko?si=YgQl-YxGMW63tRQL",
    "https://youtube.com/shorts/hCafqJ2lJA8?si=88Ml1lluZOFQ7tKC",
    "https://youtube.com/shorts/O4odcNAMYVE?si=01pPT_dqoYyBn4Kz",
    "https://youtube.com/shorts/qWqtUctNBQ4?si=veDQnrI2BUvzjL_c",
    "https://youtube.com/shorts/HojeFBRoA4U?si=q-sTeYEy9Z1nauON"
]

PECTORAUX = [
    "https://youtube.com/shorts/xoXojBVTN_8?si=NbGiin3dXBwWBuMG",
    "https://youtube.com/shorts/H_2XGGh-n8s?si=qc9KdSDGumSCmm7D",
    "https://youtube.com/shorts/Ze81cO6uzDM?si=Yhk-VcxzJOCwI-r0",
    "https://youtube.com/shorts/kvx-XkAp2QM?si=m1CpXBxVRNlsUt0U",
    "https://youtube.com/shorts/17c7vOMesd4?si=31hrf8vmsCPGEFtv",
    "https://youtube.com/shorts/p5AufLpj53c?si=4GCPD9DHFvpSW4yF",
    "https://youtube.com/shorts/k4MpQYpo2b4?si=W2neTHWaP8OoTvIr",
    "https://youtube.com/shorts/tRA7T9nVHLE?si=FO0jBWrtfCiZNmkU",
    "https://youtube.com/shorts/uJD0cFKLg8g?si=a2uz78hSLv296Xdx",
    "https://youtube.com/shorts/vEzVopa4-kE?si=t1fw-foQLhiISvKL",
    "https://youtube.com/shorts/3iyM4LpgkOY?si=IFuCWVwW5Xjbd1-J",
    "https://youtube.com/shorts/u3-lb2YLVD4?si=C4a2oc9DLoB5jrlv",
    "https://youtube.com/shorts/LUZRKX-Pw_w?si=KZR8FH91mqJWYMap",
    "https://youtube.com/shorts/xnb6ug1Br2k?si=jpUe-TXZP4Sr8K_m",
    "https://youtube.com/shorts/vsEIWPRnFkw?si=4V9uXiuxpovg02Mu",
    "https://youtube.com/shorts/DYWP4yR9iR8?si=aa6erjWSQwxaPC_c",
    "https://youtube.com/shorts/wLDF0HaiIF8?si=wfkWDj9XBy3XSjWC",
    "https://youtube.com/shorts/Sty3Vee4yek?si=p1vdSfXeOfpyoxx2",
    "https://youtube.com/shorts/b7S7hVrDUu0?si=ILwbaAacF8mp7n0p",
    "https://youtube.com/shorts/N0qMQIR4W6E?si=J6u0dDJ4_ArNxTtO",
    "https://youtube.com/shorts/Raq9icmnwn8?si=Iq68_4cJcIBaSz5l",
    "https://youtube.com/shorts/ryB1eLke_e8?si=lFG7rIPfdH44pVbW",
    "https://youtube.com/shorts/efg0MlRq3Ig?si=huspMoAmq95qfYYg",
    "https://youtube.com/shorts/mUbY2tVEmt0?si=YKYfxzUNxcMzQpro",
    "https://youtube.com/shorts/tHompI9e5-c?si=SuuRjwLiJkg1pSDa",
    "https://youtube.com/shorts/0N6WU8-Ko4E?si=cipItlxymwcdYL3x"
]

kine_list_general = [Quadriceps,Psoas_Flechisseurs_Hanches,Pieds,Moyen_Fessiers,Mollets,Ishios_Jambiers,Fessiers,chevilles,Adducteurs]

# kine_list_renforcement = [pied_voute_plantaire,hanche,genoux,chevilles]

# programme_maison = [cardio,renforcement]

programme_bonus = [ABDOS,POMPES,GAINAGES]

programme_cardio = [VELO_ENDURANCE,VELO_PUISSANCE,TAPIS_ENDURANCE,TAPIS_RÉSISTANCE,TAPIS_PUISSANCE,SPRINT_EN_COTE,RAMEUR,MARCHE,MARCHE_EN_COTE,ELLIPTIQUE_INTENSE,ELLIPTIQUE_NORMAL]

programme_musculation = [BRAS,DOS,EPAULES,JAMBES,PECTORAUX]
programme_musculation_haut = [BRAS,DOS,EPAULES,PECTORAUX]
programme_musculation_bas = [JAMBES]

