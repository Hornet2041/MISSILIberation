# Requires Military Assets Mod units, HIMARS units for now :
# https://www.currenthill.com/
#
from dcs import unittype

from game.modsupport import vehiclemod


@vehiclemod
class M142_HIMARS_GLSDB(unittype.VehicleType):
    id = "M142_HIMARS_GLSDB"
    name = "M142 HIMARS (GLSDB)"
    detection_range = 0
    threat_range = 150000
    air_weapon_dist = 150000
    eplrs = True

@vehiclemod
class M142_HIMARS_ATACMS(unittype.VehicleType):
    id = "M142_HIMARS_ATACMS"
    name = "M142 HIMARS (ATACMS)"
    detection_range = 0
    threat_range = 296000
    air_weapon_dist = 296000
    eplrs = True

@vehiclemod
class M142_HIMARS_GMLRS(unittype.VehicleType):
    id = "M142_HIMARS_GMLRS"
    name = "M142 HIMARS-GMLRS"
    detection_range = 0
    threat_range = 92000
    air_weapon_dist = 92000
    eplrs = True

@vehiclemod
class M142_HIMARS_PRSM(unittype.VehicleType):
    id = "M142_HIMARS_PRSM"
    name = "M142 HIMARS (PrSM)"
    detection_range = 0
    threat_range = 500000
    air_weapon_dist = 500000
    eplrs = True

@vehiclemod
class M142_HIMARS_PRSM_ASHM(unittype.VehicleType):
    id = "M142_HIMARS_PRSM_ASHM"
    name = "M142 HIMARS (PrSM AShM)"
    detection_range = 0
    threat_range = 500000
    air_weapon_dist = 500000
    eplrs = True

@vehiclemod
class CH_M270A1_GLSDB(unittype.VehicleType):
    id = "CH_M270A1_GLSDB"
    name = "M270A1 MLRS (GLSDB)"
    detection_range = 0
    threat_range = 150000
    air_weapon_dist = 150000
    eplrs = True

@vehiclemod
class CH_M270A1_ATACMS(unittype.VehicleType):
    id = "CH_M270A1_ATACMS"
    name = "M270A1 MLRS (ATACMS)"
    detection_range = 0
    threat_range = 296000
    air_weapon_dist = 296000
    eplrs = True

@vehiclemod
class CH_M270A1_GMLRS(unittype.VehicleType):
    id = "CH_M270A1_GMLRS"
    name = "M270A1 MLRS (GMLRS)"
    detection_range = 0
    threat_range = 92000
    air_weapon_dist = 92000
    eplrs = True

@vehiclemod
class CH_CJ10(unittype.VehicleType):
    id = "CH_CJ10"
    name = "CJ-10 GLCM"
    detection_range = 2000000
    threat_range = 2000000
    air_weapon_dist = 2000000
    eplrs = True

@vehiclemod
class CH_IskanderM(unittype.VehicleType):
    id = "CH_IskanderM"
    name = "Iskander-M SRBM"
    detection_range = 500000
    threat_range = 500000
    air_weapon_dist = 500000
    eplrs = True

@vehiclemod
class CH_IskanderK(unittype.VehicleType):
    id = "CH_IskanderK"
    name = "Iskander-K GLCM"
    detection_range = 1500000
    threat_range = 1500000
    air_weapon_dist = 1500000
    eplrs = True

@vehiclemod
class K300P(unittype.VehicleType):
    id = "K300P"
    name = "AShM K-300P Bastion-P TEL"
    detection_range = 400000
    threat_range = 400000
    air_weapon_dist = 400000
    eplrs = True

@vehiclemod
class MonolitB(unittype.VehicleType):
    id = "MonolitB"
    name = "AShM Monolit-B Radar"
    detection_range = 800000
    threat_range = 0
    air_weapon_dist = 0

@vehiclemod
class CH_PZH2000(unittype.VehicleType):
    id = "CH_PZH2000"
    name = "[CH] PzH 2000 SPG"
    detection_range = 0
    threat_range = 50000
    air_weapon_dist = 50000
    eplrs = True

@vehiclemod
class CH_Shahed136(unittype.VehicleType):
    id = "CH_Shahed136"
    name = "[CH] Shahed 136 LM"
    detection_range = 0
    threat_range = 360000
    air_weapon_dist = 360000
    eplrs = True

@vehiclemod
class CH_Alligator_Sniper(unittype.VehicleType):
    id = "CH_Alligator_Sniper"
    name = "[CH] Alligator Sniper AMR"
    detection_range = 5000
    threat_range = 3000
    air_weapon_dist = 3000
    eplrs = True

@vehiclemod
class CH_DSHK_HMG_RUS(unittype.VehicleType):
    id = "CH_DSHK_HMG_RUS"
    name = "[CH] DShK HMG"
    detection_range = 5000
    threat_range = 1800
    air_weapon_dist = 1800
    eplrs = True

@vehiclemod
class CH_DSHK_HMG_UKR(unittype.VehicleType):
    id = "CH_DSHK_HMG_UKR"
    name = "[CH] DShK HMG"
    detection_range = 5000
    threat_range = 1800
    air_weapon_dist = 1800
    eplrs = True

@vehiclemod
class CH_Stugna_P(unittype.VehicleType):
    id = "CH_Stugna_P"
    name = "[CH] Stugna-P ATGM"
    detection_range = 5500
    threat_range = 5500
    air_weapon_dist = 5500
    eplrs = True

@vehiclemod
class X_2S38(unittype.VehicleType):
    id = "2S38"
    name = "SPAAG 2S38"
    detection_range = 12000
    threat_range = 8000
    air_weapon_dist = 8000
    eplrs = True

@vehiclemod
class CH_S350_50P6_9M96D(unittype.VehicleType):
    id = "CH_S350_50P6_9M96D"
    name = "[CH] S-350 50P6 9M96D LN"
    detection_range = 0
    threat_range = 150000
    air_weapon_dist = 150000
    eplrs = True

@vehiclemod
class CH_S350_50P6_9M100(unittype.VehicleType):
    id = "CH_S350_50P6_9M100"
    name = "[CH] S-350 50P6 9M100 LN"
    detection_range = 0
    threat_range = 15000
    air_weapon_dist = 15000
    eplrs = True

@vehiclemod
class CH_S350_50N6(unittype.VehicleType):
    id = "CH_S350_50N6"
    name = "[CH] S-350 50N6 STR"
    detection_range = 200000
    threat_range = 0
    air_weapon_dist = 0
    eplrs = True

@vehiclemod
class CH_S350_50K6(unittype.VehicleType):
    id = "CH_S350_50K6"
    name = "[CH] S-350 50K6 CP"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0
    eplrs = True

@vehiclemod
class CH_S350_96L6(unittype.VehicleType):
    id = "CH_S350_96L6"
    name = "[CH] S-350 96L6 SR"
    detection_range = 300000
    threat_range = 0
    air_weapon_dist = 0

@vehiclemod
class CH_Centurion_C_RAM(unittype.VehicleType):
    id = "CH_Centurion_C_RAM"
    name = "[CH] Centurion C-RAM"
    detection_range = 20000
    threat_range = 2000
    air_weapon_dist = 2000
    eplrs = True

@vehiclemod
class MIM104_M903_PAC2(unittype.VehicleType):
    id = "MIM104_M903_PAC2"
    name = "[CH] SAM MIM-104 M903 PAC-2 GEM/T LN"
    detection_range = 0
    threat_range = 150000
    air_weapon_dist = 150000
    eplrs = True

@vehiclemod
class MIM104_M903_PAC3(unittype.VehicleType):
    id = "MIM104_M903_PAC3"
    name = "[CH] SAM MIM-104 M903 PAC-3 MSE LN"
    detection_range = 0
    threat_range = 120000
    air_weapon_dist = 120000
    eplrs = True

@vehiclemod
class MIM104_ECS(unittype.VehicleType):
    id = "MIM104_ECS"
    name = "[CH] SAM MIM-104 ECS"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0
    eplrs = True

@vehiclemod
class MIM104_ANMPQ65(unittype.VehicleType):
    id = "MIM104_ANMPQ65"
    name = "[CH] SAM MIM-104 AN/MPQ-65 STR"
    detection_range = 200000
    threat_range = 0
    air_weapon_dist = 0
    eplrs = True

@vehiclemod
class MIM104_ANMPQ65A(unittype.VehicleType):
    id = "MIM104_ANMPQ65A"
    name = "[CH] SAM MIM-104 AN/MPQ-65A STR"
    detection_range = 260000
    threat_range = 0
    air_weapon_dist = 0
    eplrs = True

@vehiclemod
class MIM104_EPP(unittype.VehicleType):
    id = "MIM104_EPP"
    name = "[CH] SAM MIM-104 EPP"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0
    eplrs = True

@vehiclemod
class CH_NASAMS3_LN_AMRAAM_ER(unittype.VehicleType):
    id = "CH_NASAMS3_LN_AMRAAM_ER"
    name = "[CH] NASAMS 3 LCHR LN (AMRAAM-ER)"
    detection_range = 0
    threat_range = 50000
    air_weapon_dist = 50000
    eplrs = True

@vehiclemod
class CH_NASAMS3_LN_AIM9X2(unittype.VehicleType):
    id = "CH_NASAMS3_LN_AIM9X2"
    name = "[CH] NASAMS 3 LCHR LN (AIM-9X-2)"
    detection_range = 0
    threat_range = 20000
    air_weapon_dist = 20000
    eplrs = True

@vehiclemod
class CH_NASAMS3_SR(unittype.VehicleType):
    id = "CH_NASAMS3_SR"
    name = "[CH] NASAMS 3 SR"
    detection_range = 120000
    threat_range = 0
    air_weapon_dist = 0
    eplrs = True

@vehiclemod
class CH_NASAMS3_CP(unittype.VehicleType):
    id = "CH_NASAMS3_CP"
    name = "[CH] NASAMS 3 CP"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0
    eplrs = True

@vehiclemod
class PGL_625(unittype.VehicleType):
    id = "PGL_625"
    name = "SPAAGM PGL-625"
    detection_range = 20000
    threat_range = 10000
    air_weapon_dist = 10000
    eplrs = True

@vehiclemod
class PantsirS1(unittype.VehicleType):
    id = "PantsirS1"
    name = "SPAAGM Pantsir-S1"
    detection_range = 36000
    threat_range = 20000
    air_weapon_dist = 20000
    eplrs = True

@vehiclemod
class PantsirS2(unittype.VehicleType):
    id = "PantsirS2"
    name = "SPAAGM Pantsir-S2"
    detection_range = 40000
    threat_range = 30000
    air_weapon_dist = 30000
    eplrs = True

@vehiclemod
class ZBD04A(unittype.VehicleType):
    id = "ZBD04A"
    name = "ZBD-04A"
    detection_range = 0
    threat_range = 4800
    air_weapon_dist = 0
    eplrs = True

@vehiclemod
class CH_T90M(unittype.VehicleType):
    id = "CH_T90M"
    name = "[CH] T-90M MBT"
    detection_range = 8000
    threat_range = 5000
    air_weapon_dist = 5000
    eplrs = True


