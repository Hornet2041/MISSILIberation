# Requires Military Assets Mod units, HIMARS units for now :
# https://www.currenthill.com/
#
from dcs import unittype

from game.modsupport import vehiclemod


@vehiclemod
class M142_HIMARS_GLSDB(unittype.VehicleType):
    id = "M142_HIMARS_GLSDB"
    name = "[CH] M142 HIMARS (GLSDB)"
    detection_range = 0
    threat_range = 150000
    air_weapon_dist = 150000
    eplrs = True


class M142_HIMARS_ATACMS(unittype.VehicleType):
    id = "M142_HIMARS_ATACMS"
    name = "[CH] M142 HIMARS (ATACMS)"
    detection_range = 0
    threat_range = 296000
    air_weapon_dist = 296000
    eplrs = True


class M142_HIMARS_GMLRS(unittype.VehicleType):
    id = "M142_HIMARS_GMLRS"
    name = "M142 HIMARS-GMLRS"
    detection_range = 0
    threat_range = 92000
    air_weapon_dist = 92000
    eplrs = True


class M142_HIMARS_PRSM(unittype.VehicleType):
    id = "M142_HIMARS_PRSM"
    name = "[CH] M142 HIMARS (PrSM)"
    detection_range = 0
    threat_range = 500000
    air_weapon_dist = 500000
    eplrs = True


class M142_HIMARS_PRSM_ASHM(unittype.VehicleType):
    id = "M142_HIMARS_PRSM_ASHM"
    name = "[CH] M142 HIMARS (PrSM AShM)"
    detection_range = 0
    threat_range = 500000
    air_weapon_dist = 500000
    eplrs = True


class CH_M270A1_GLSDB(unittype.VehicleType):
    id = "CH_M270A1_GLSDB"
    name = "[CH] M270A1 MLRS (GLSDB)"
    detection_range = 0
    threat_range = 150000
    air_weapon_dist = 150000
    eplrs = True


class CH_M270A1_ATACMS(unittype.VehicleType):
    id = "CH_M270A1_ATACMS"
    name = "[CH] M270A1 MLRS (ATACMS)"
    detection_range = 0
    threat_range = 296000
    air_weapon_dist = 296000
    eplrs = True


class CH_M270A1_GMLRS(unittype.VehicleType):
    id = "CH_M270A1_GMLRS"
    name = "[CH] M270A1 MLRS (GMLRS)"
    detection_range = 0
    threat_range = 92000
    air_weapon_dist = 92000
    eplrs = True



