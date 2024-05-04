from operators.r6_operator import Operator
from gadgets.gadget import *
from weapons.assault_rifle import *
from weapons.handgun import *
from weapons.light_machine_gun import *
from weapons.machine_pistol import *
from weapons.marksman_rifle import *
from weapons.shield import *
from weapons.shotgun import *
from weapons.submachine_gun import *

class Defender(Operator):
    def __init__(self, name):
        super().__init__(name, side = Side.DEFEND)
        
class Pulse(Defender):
    def __init__(self):
        super().__init__("Pulse")
        self.add_weapon(M1014())
        self.add_weapon(UMP45())
        self.add_weapon(USG57(), False)
        self.add_weapon(M45_MEUSOC(), False)
        self.add_gadget(Deployable_Shield())
        self.add_gadget(Nitro_Cell())
        self.add_gadget(Observation_Blocker())

class Castle(Defender):
    def __init__(self):
        super().__init__("Castle")
        self.add_weapon(M1014())
        self.add_weapon(UMP45())
        self.add_weapon(USG57(), False)
        self.add_weapon(M45_MEUSOC(), False)
        self.add_weapon(SUPER_SHORTY(), False)
        self.add_gadget(Proximity_Alarm())
        self.add_gadget(Bulletproof_Camera())

class Smoke(Defender):
    def __init__(self):
        super().__init__("Smoke")
        self.add_weapon(M590A1())
        self.add_weapon(FMG_9())
        self.add_weapon(P226MK25(),False)
        self.add_weapon(SMG_11(), False)
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Proximity_Alarm())

class Mute(Defender):
    def __init__(self):
        super().__init__("Mute")
        self.add_weapon(M590A1())
        self.add_weapon(MP5K(1.0))
        self.add_weapon(P226MK25(),False)
        self.add_weapon(SMG_11(), False)
        self.add_gadget(Nitro_Cell())
        self.add_gadget(Bulletproof_Camera())

class Jager(Defender):
    def __init__(self):
        super().__init__("Jager")
        self.add_weapon(M870())
        self.add_weapon(AR_416_C_CARBINE())
        self.add_weapon(P12(), False)
        self.add_gadget(Bulletproof_Camera())
        self.add_gadget(Observation_Blocker())

class Bandit(Defender):
    def __init__(self):
        super().__init__("Bandit")
        self.add_weapon(MP7(1.0))
        self.add_weapon(M870())
        self.add_weapon(P12(), False)
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Nitro_Cell())

class Doc(Defender):
    def __init__(self):
        super().__init__("Doc")
        self.add_weapon(SG_CQB())
        self.add_weapon(MP5(1.5))
        self.add_weapon(P90())
        self.add_weapon(P9(), False)
        self.add_weapon(LFP586(), False)
        self.add_weapon(Bailiff_410(),False)
        self.add_gadget(Bulletproof_Camera())
        self.add_gadget(Barbed_Wire())

class Rook(Defender):
    def __init__(self):
        super().__init__("Rook")
        self.add_weapon(SG_CQB())
        self.add_weapon(MP5())
        self.add_weapon(P90())
        self.add_weapon(P9(), False)
        self.add_weapon(LFP586(), False)
        self.add_gadget(Impact_Grenade())
        self.add_gadget(Proximity_Alarm())
        self.add_gadget(Observation_Blocker())

class Kapkan(Defender):
    def __init__(self):
        super().__init__("Kapkan")
        self.add_weapon(SMG_9x19VSN(1.0))
        self.add_weapon(SASG_12())
        self.add_weapon(PMM(), False)
        self.add_weapon(GSH_18(), False)
        self.add_gadget(Nitro_Cell())
        self.add_gadget(Impact_Grenade())

class Tachanka(Defender):
    def __init__(self):
        super().__init__("Tachanka")
        self.add_weapon(SMG_9x19VSN())
        self.add_weapon(DP27())
        self.add_weapon(PMM(), False)
        self.add_weapon(GSH_18(), False)
        self.add_weapon(Bearing_9(), False)
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Deployable_Shield())
        self.add_gadget(Proximity_Alarm())

class Frost(Defender):
    def __init__(self):
        super().__init__("Frost")
        self.add_weapon(SUPER90())
        self.add_weapon(SMG_9mm_C1())
        self.add_weapon(ITA12S(), False)
        self.add_weapon(MK1_9mm(), False)
        self.add_gadget(Bulletproof_Camera())
        self.add_gadget(Deployable_Shield())

class Valkyrie(Defender):
    def __init__(self):
        super().__init__("Valkyrie")
        self.add_weapon(MPX(1.0))
        self.add_weapon(SPAS_12())
        self.add_weapon(D_50(), False)
        self.add_gadget(Impact_Grenade())
        self.add_gadget(Nitro_Cell())

class Caveira(Defender):
    def __init__(self):
        super().__init__("Caveira")
        self.add_weapon(M12())
        self.add_weapon(SPAS_15())
        self.add_weapon(LUISON(), False)
        self.add_gadget(Impact_Grenade())
        self.add_gadget(Proximity_Alarm())
        self.add_gadget(Observation_Blocker())

class Echo(Defender):
    def __init__(self):
        super().__init__("Echo")
        self.add_weapon(SUPERNOVA())
        self.add_weapon(MP5SD())
        self.add_weapon(P229(), False)
        self.add_weapon(Bearing_9(), False)
        self.add_gadget(Impact_Grenade())
        self.add_gadget(Deployable_Shield())

class Mira(Defender):
    def __init__(self):
        super().__init__("Mira")
        self.add_weapon(VECTOR_45_ACP(1.0))
        self.add_weapon(ITA12L())
        self.add_weapon(ITA12S(), False)
        self.add_weapon(USP40(), False)
        self.add_gadget(Nitro_Cell())
        self.add_gadget(Proximity_Alarm())

class Lesion(Defender):
    def __init__(self):
        super().__init__("Lesion")
        self.add_weapon(SIX12_SD())
        self.add_weapon(T_5_SMG())
        self.add_weapon(Q_929(), False)
        self.add_gadget(Impact_Grenade())
        self.add_gadget(Bulletproof_Camera())

class Ela(Defender):
    def __init__(self):
        super().__init__("Ela")
        self.add_weapon(SCORPION_EVO_3_A1())
        self.add_weapon(FO_12())
        self.add_weapon(RG15(), False)
        self.add_gadget(Deployable_Shield())
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Observation_Blocker())

class Vigil(Defender):
    def __init__(self):
        super().__init__("Vigil")
        self.add_weapon(K1A())
        self.add_weapon(BOSG_12_2())
        self.add_weapon(SMG_12(), False)
        self.add_weapon(C75_Auto(), False)
        self.add_gadget(Bulletproof_Camera())
        self.add_gadget(Impact_Grenade())

class Maestro(Defender):
    def __init__(self):
        super().__init__("Maestro")
        self.add_weapon(ALDA_5_56())
        self.add_weapon(ACS12())
        self.add_weapon(KERATOS_357(), False)
        self.add_weapon(Bailiff_410(), False)
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Impact_Grenade())
        self.add_gadget(Observation_Blocker())

class Alibi(Defender):
    def __init__(self):
        super().__init__("Alibi")
        self.add_weapon(Mx4_Storm())
        self.add_weapon(ACS12())
        self.add_weapon(KERATOS_357(), False)
        self.add_weapon(Bailiff_410(), False)
        self.add_gadget(Proximity_Alarm())
        self.add_gadget(Observation_Blocker())

class Clash(Defender):
    def __init__(self):
        super().__init__("Clash")
        self.add_weapon(CCE_Shield())
        self.add_weapon(SUPER_SHORTY(), False)
        self.add_weapon(SPSMG9(), False)
        self.add_weapon(P_10C(), False)
        self.add_gadget(Impact_Grenade())
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Deployable_Shield())

class Kaid(Defender):
    def __init__(self):
        super().__init__("Kaid")
        self.add_weapon(AUG_A3())
        self.add_weapon(TCSG12())
        self.add_weapon(H_44_Mag_Semi_Auto(), False)
        self.add_weapon(LFP586(), False)
        self.add_gadget(Nitro_Cell())
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Observation_Blocker())

class Mozzie(Defender):
    def __init__(self):
        super().__init__("Mozzie")
        self.add_weapon(COMMANDO_9())
        self.add_weapon(P10_RONI())
        self.add_weapon(SDP_9mm(), False)
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Nitro_Cell())

class Warden(Defender):
    def __init__(self):
        super().__init__("Warden")
        self.add_weapon(MPX())
        self.add_weapon(M590A1())
        self.add_weapon(SMG_12(), False)
        self.add_weapon(P_10C(), False)
        self.add_gadget(Nitro_Cell())
        self.add_gadget(Deployable_Shield())
        self.add_gadget(Observation_Blocker())

class Goyo(Defender):
    def __init__(self):
        super().__init__("Goyo")
        self.add_weapon(VECTOR_45_ACP())
        self.add_weapon(TCSG12())
        self.add_weapon(P229(), False)
        self.add_gadget(Bulletproof_Camera())
        self.add_gadget(Proximity_Alarm())
        self.add_gadget(Impact_Grenade())

class Wamai(Defender):
    def __init__(self):
        super().__init__("Wamai")
        self.add_weapon(AUG_A2(1.0))
        self.add_weapon(MP5K())
        self.add_weapon(KERATOS_357(), False)
        self.add_weapon(P12(), False)
        self.add_gadget(Impact_Grenade())
        self.add_gadget(Proximity_Alarm())

class Oryx(Defender):
    def __init__(self):
        super().__init__("Oryx")
        self.add_weapon(T_5_SMG())
        self.add_weapon(SPAS_12())
        self.add_weapon(Bailiff_410(),False)
        self.add_weapon(USP40(), False)
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Proximity_Alarm())

class Melusi(Defender):
    def __init__(self):
        super().__init__("Melusi")
        self.add_weapon(MP5(1.0))
        self.add_weapon(SUPER90())
        self.add_weapon(RG15(), False)
        self.add_gadget(Impact_Grenade())
        self.add_gadget(Bulletproof_Camera())

class Aruni(Defender):
    def __init__(self):
        super().__init__("Aruni")
        self.add_weapon(P10_RONI(1.0))
        self.add_weapon(Mk_14_EBR(1.5))
        self.add_weapon(PRB92(), False)
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Bulletproof_Camera())

class Thunderbird(Defender):
    def __init__(self):
        super().__init__("Thunderbird")
        self.add_weapon(SPEAR_308(1.0))
        self.add_weapon(SPAS_15())
        self.add_weapon(Bearing_9(), False)
        self.add_weapon(Q_929(), False)
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Bulletproof_Camera())

class Thorn(Defender):
    def __init__(self):
        super().__init__("Thorn")
        self.add_weapon(UZK50GI())
        self.add_weapon(M870())
        self.add_weapon(H_1911_TACOPS(), False)
        self.add_weapon(C75_Auto(), False)
        self.add_gadget(Deployable_Shield())
        self.add_gadget(Barbed_Wire())

class Azami(Defender):
    def __init__(self):
        super().__init__("Azami")
        self.add_weapon(SMG_9x19VSN(1.0))
        self.add_weapon(ACS12(1.5))
        self.add_weapon(D_50(), False)
        self.add_gadget(Impact_Grenade())
        self.add_gadget(Barbed_Wire())

class Solis(Defender):
    def __init__(self):
        super().__init__("Solis")
        self.add_weapon(P90(1.0))
        self.add_weapon(ITA12L())
        self.add_weapon(SMG_11(), False)
        self.add_gadget(Impact_Grenade())
        self.add_gadget(Bulletproof_Camera())

class Fenrir(Defender):
    def __init__(self):
        super().__init__("Fenrir")
        self.add_weapon(MP7(1.0))
        self.add_weapon(SASG_12())
        self.add_weapon(Bailiff_410(), False)
        self.add_weapon(USG57(), False)
        self.add_gadget(Barbed_Wire())
        self.add_gadget(Bulletproof_Camera())

# Add Tubarao
