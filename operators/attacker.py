from operators.Operator import Operator
from gadgets.Gadget import *
from weapons.AssaultRifle import *
from weapons.Handgun import *
from weapons.LightMachineGun import *
from weapons.MachinePistol import *
from weapons.MarksmanRifle import *
from weapons.Shield import *
from weapons.Shotgun import *
from weapons.SubmachineGun import *
from weapons.HandCannon import *

class Attacker(Operator):
    def __init__(self, name):
        super().__init__(name, side = "Attack")

class Ash(Attacker):
    def __init__(self):
        super().__init__("Ash")
        self.add_weapon(R4C())
        self.add_weapon(G36C())
        self.add_weapon(USG57(),False)
        self.add_weapon(M45_MEUSOC(),False)
        self.add_gadget(Claymore())
        self.add_gadget(Breach_Charge())

class Thermite(Attacker):
    def __init__(self):
        super().__init__("Thermite")
        self.add_weapon(AR_556XI())
        self.add_weapon(M1014())
        self.add_weapon(USG57(),False)
        self.add_weapon(M45_MEUSOC(),False)
        self.add_gadget(Stun_Grenade())
        self.add_gadget(Smoke_Grenade())

class Sledge(Attacker):
    def __init__(self):
        super().__init__("Sledge")
        self.add_weapon(L85A2(updated_mag=1.5))
        self.add_weapon(M590A1())
        self.add_weapon(P226MK25(),False)
        self.add_gadget(Frag_Grenade())
        self.add_gadget(Stun_Grenade())
        self.add_gadget(Impact_EMP_Grenade())

class Thatcher(Attacker):
    def __init__(self):
        super().__init__("Thatcher")
        self.add_weapon(L85A2())
        self.add_weapon(AR33())
        self.add_weapon(M590A1())
        self.add_weapon(P226MK25(), False)
        self.add_gadget(Breach_Charge())
        self.add_gadget(Claymore())

class IQ(Attacker):
    def __init__(self):
        super().__init__("IQ")
        self.add_weapon(AR_552_Commando(updated_mag=1.5))
        self.add_weapon(AUG_A2())
        self.add_weapon(G8A1(updated_mag=1.0))
        self.add_weapon(P12(), False)
        self.add_gadget(Breach_Charge())
        self.add_gadget(Claymore())

class Blitz(Attacker):
    def __init__(self):
        super().__init__("Blitz")
        self.add_weapon(G52_Tactical_Shield())
        self.add_weapon(P12(), False)
        self.add_gadget(Breach_Charge())
        self.add_gadget(Smoke_Grenade())

class Twitch(Attacker):
    def __init__(self):
        super().__init__("Twitch")
        self.add_weapon(F2())
        self.add_weapon(SG_CQB())
        self.add_weapon(M417())
        self.add_weapon(P9(), False)
        self.add_weapon(LFP586(), False)
        self.add_gadget(Smoke_Grenade())
        self.add_gadget(Claymore())

class Montagne(Attacker):
    def __init__(self):
        super().__init__("Montagne")
        self.add_weapon(LE_ROC_Shield())
        self.add_weapon(P9(), False)
        self.add_weapon(LFP586(), False)
        self.add_gadget(Hard_Breach_Charge())
        self.add_gadget(Smoke_Grenade())
        self.add_gadget(Impact_EMP_Grenade())

class Glaz(Attacker):
    def __init__(self):
        super().__init__("Glaz")
        self.add_weapon(OTs_03())
        self.add_weapon(PMM(), False)
        self.add_weapon(Gonne_6(), False)
        self.add_weapon(Bearing_9(), False)
        self.add_gadget(Smoke_Grenade())
        self.add_gadget(Frag_Grenade())
        
class Fuze(Attacker):
    def __init__(self):
        super().__init__("Fuze")
        self.add_weapon(AK_12())
        self.add_weapon(LMG_6P41())
        self.add_weapon(Ballistic_Shield())
        self.add_weapon(PMM(),False)
        self.add_weapon(GSH_18(),False)
        self.add_gadget(Breach_Charge())
        self.add_gadget(Hard_Breach_Charge())
        self.add_gadget(Smoke_Grenade())

class Buck(Attacker):
    def __init__(self):
        super().__init__("Buck")
        self.add_weapon(C8_SFW())
        self.add_weapon(CAMRS())
        self.add_weapon(MK1_9mm(), False)
        self.add_weapon(Gonne_6(), False)
        self.add_gadget(Stun_Grenade())
        self.add_gadget(Hard_Breach_Charge())

class Blackbeard(Attacker):
    def __init__(self):
        super().__init__("Blackbeard")
        self.add_weapon(MK17_CQB())
        self.add_weapon(SR_25())
        self.add_weapon(D_50(), False)
        self.add_gadget(Claymore())
        self.add_gadget(Stun_Grenade())
        self.add_gadget(Impact_EMP_Grenade())

class Capitao(Attacker):
    def __init__(self):
        super().__init__("Capitao")
        self.add_weapon(Para_308())
        self.add_weapon(M249())
        self.add_weapon(PRB92(), False)
        self.add_weapon(Gonne_6(), False)
        self.add_gadget(Claymore())
        self.add_gadget(Hard_Breach_Charge())

class Hibana(Attacker):
    def __init__(self):
        super().__init__("Hibana")
        self.add_weapon(Type_89())
        self.add_weapon(SUPERNOVA())
        self.add_weapon(P229(), False)
        self.add_weapon(Bearing_9(), False)
        self.add_gadget(Stun_Grenade())
        self.add_gadget(Breach_Charge())

class Jackal(Attacker):
    def __init__(self):
        super().__init__("Jackal")
        self.add_weapon(C7E())
        self.add_weapon(PDW9(1.5))
        self.add_weapon(ITA12L())
        self.add_weapon(USP40(), False)
        self.add_weapon(ITA12S(), False)
        self.add_gadget(Claymore())
        self.add_gadget(Smoke_Grenade())

class Ying(Attacker):
    def __init__(self):
        super().__init__("Ying")
        self.add_weapon(T_95_LSW())
        self.add_weapon(SIX12_SD())
        self.add_weapon(Q_929(), False)
        self.add_gadget(Hard_Breach_Charge())
        self.add_gadget(Smoke_Grenade())

class Zofia(Attacker):
    def __init__(self):
        super().__init__("Zofia")
        self.add_weapon(LMG_E())
        self.add_weapon(M762())
        self.add_weapon(RG15(), False)
        self.add_gadget(Breach_Charge())
        self.add_gadget(Claymore())

class Dokkaebi(Attacker):
    def __init__(self):
        super().__init__("Dokkaebi")
        self.add_weapon(Mk_14_EBR())
        self.add_weapon(BOSG_12_2())
        self.add_weapon(SMG_12(), False)
        self.add_weapon(C75_Auto(), False)
        self.add_gadget(Smoke_Grenade())
        self.add_gadget(Stun_Grenade())
        self.add_gadget(Impact_EMP_Grenade())

class Lion(Attacker):
    def __init__(self):
        super().__init__("Lion")
        self.add_weapon(V308())
        self.add_weapon(SG_CQB())
        self.add_weapon(M417())
        self.add_weapon(P9(), False)
        self.add_weapon(LFP586(), False)
        self.add_weapon(Gonne_6(), False)
        self.add_gadget(Stun_Grenade())
        self.add_gadget(Claymore())
        self.add_gadget(Impact_EMP_Grenade())

class Finka(Attacker):
    def __init__(self):
        super().__init__("Finka")
        self.add_weapon(SPEAR_308())
        self.add_weapon(SASG_12())
        self.add_weapon(LMG_6P41(2.0))
        self.add_weapon(Gonne_6(), False)
        self.add_weapon(PMM(),False)
        self.add_weapon(GSH_18(),False)
        self.add_gadget(Smoke_Grenade())
        self.add_gadget(Stun_Grenade())

class Maverick(Attacker):
    def __init__(self):
        super().__init__("Maverick")
        self.add_weapon(AR_15_50())
        self.add_weapon(M4())
        self.add_weapon(H_1911_TACOPS(), False)
        self.add_gadget(Stun_Grenade())
        self.add_gadget(Claymore())

class Nomad(Attacker):
    def __init__(self):
        super().__init__("Nomad")
        self.add_weapon(AK_74M())
        self.add_weapon(ARX200())
        self.add_weapon(PRB92(), False)
        self.add_weapon(H_44_Mag_Semi_Auto(), False)
        self.add_gadget(Stun_Grenade())
        self.add_gadget(Breach_Charge())

class Gridlock(Attacker):
    def __init__(self):
        super().__init__("Gridlock")
        self.add_weapon(F90())
        self.add_weapon(M249_SAW())
        self.add_weapon(SUPER_SHORTY(), False)
        self.add_weapon(SDP_9mm(), False)
        self.add_weapon(Gonne_6(), False)
        self.add_gadget(Smoke_Grenade())
        self.add_gadget(Breach_Charge())
        self.add_gadget(Impact_EMP_Grenade())

class Nokk(Attacker):
    def __init__(self):
        super().__init__("Nokk")
        self.add_weapon(FMG_9())
        self.add_weapon(SIX12_SD())
        self.add_weapon(USG57(), False)
        self.add_weapon(D_50(), False)
        self.add_gadget(Hard_Breach_Charge())
        self.add_gadget(Frag_Grenade())
        self.add_gadget(Impact_EMP_Grenade())

class Amaru(Attacker):
    def __init__(self):
        super().__init__("Amaru")
        self.add_weapon(G8A1())
        self.add_weapon(SUPERNOVA())
        self.add_weapon(SMG_11(), False)
        self.add_weapon(ITA12S(), False)
        self.add_weapon(Gonne_6(), False)
        self.add_gadget(Hard_Breach_Charge())
        self.add_gadget(Stun_Grenade())

class Kali(Attacker):
    def __init__(self):
        super().__init__("Kali")
        self.add_weapon(CSRX300())
        self.add_weapon(SPSMG9(), False)
        self.add_weapon(C75_Auto(), False)
        self.add_weapon(P226MK25(), False)
        self.add_gadget(Claymore())
        self.add_gadget(Breach_Charge())

class Iana(Attacker):
    def __init__(self):
        super().__init__("Iana")
        self.add_weapon(ARX200(1.0))
        self.add_weapon(G36C())
        self.add_weapon(MK1_9mm(), False)
        self.add_gadget(Frag_Grenade())
        self.add_gadget(Smoke_Grenade())

class Ace(Attacker):
    def __init__(self):
        super().__init__("Ace")
        self.add_weapon(AK_12(1.5))
        self.add_weapon(M1014())
        self.add_weapon(P9(), False)
        self.add_gadget(Breach_Charge())
        self.add_gadget(Claymore())

class Zero(Attacker):
    def __init__(self):
        super().__init__("Zero")
        self.add_weapon(SC3000K())
        self.add_weapon(MP7())
        self.add_weapon(USG57(), False)
        self.add_weapon(Gonne_6(), False)
        self.add_gadget(Hard_Breach_Charge())
        self.add_gadget(Claymore())

class Flores(Attacker):
    def __init__(self):
        super().__init__("Flores")
        self.add_weapon(AR33(2.0))
        self.add_weapon(SR_25())
        self.add_weapon(GSH_18(), False)
        self.add_gadget(Stun_Grenade())
        self.add_gadget(Claymore())

class Osa(Attacker):
    def __init__(self):
        super().__init__("Osa")
        self.add_weapon(PDW9(1.5))
        self.add_weapon(AR_556XI())
        self.add_weapon(PMM(), False)
        self.add_gadget(Impact_EMP_Grenade())
        self.add_gadget(Claymore())
        self.add_gadget(Smoke_Grenade())

class Sens(Attacker):
    def __init__(self):
        super().__init__("Sens")
        self.add_weapon(POF_9())
        self.add_weapon(M417())
        self.add_weapon(SDP_9mm(), False)
        self.add_weapon(Gonne_6(), False)
        self.add_gadget(Hard_Breach_Charge())
        self.add_gadget(Claymore())

class Grim(Attacker):
    def __init__(self):
        super().__init__("Grim")
        self.add_weapon(AR_552_Commando())
        self.add_weapon(SG_CQB())
        self.add_weapon(P229(), False)
        self.add_gadget(Breach_Charge())
        self.add_gadget(Claymore())

class Brava(Attacker):
    def __init__(self):
        super().__init__("Brava")
        self.add_weapon(Para_308(1.5))
        self.add_weapon(CAMRS())
        self.add_weapon(SUPER_SHORTY(), False)
        self.add_weapon(USP40(), False)
        self.add_gadget(Smoke_Grenade())
        self.add_gadget(Claymore())
