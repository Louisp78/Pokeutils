from math import *
from type import *
from talent import *
from pokemon import *
from attack import *
from capacity import *
import random


def pv_cal(niv, att, puiss, cm, defence):
    return ((((niv * 0.4 + 2) * att * puiss) // defence * 50) + 2) * cm

def cm_cal(stab, cap_type, critical):
    if critical:
        return round(random.uniform(0.85, 1.00), 2) * stab * cap_type * 2
    else:
        return round(random.uniform(0.85, 1.00), 2) * stab * cap_type

def critical_cal(niv, talent):
    critical_arr = []
    critical_arr.append(0) # Dont use this index
    critical_arr.append(0.0625)
    critical_arr.append(0.125)
    critical_arr.append(0.25)
    critical_arr.append(0.333)
    critical_arr.append(0.5)

    first = critical_arr[niv]
    if talent is Talent.SUPER_LUCK:
        return first * 2
    else:
        return first

def stab_cal(type_attack, type_poke):
    if type_attack == type_poke:
        return 1.50
    else:
        return 1

def mult_type(capacity, defendants):
    return type_matrix[capacity.type.value][defendants.type.value];

def critical_trial(prob):
    rand = round(random.uniform(0.0000, 1.0000),4)
    if rand <= prob:
        return True
    else:
        return False


def main(attacker, defendant, capacity):
    stab = stab_cal(attacker.type, defendant.type)
    cap_type = mult_type(capacity, defendant)
    prob_critical = critical_cal(capacity.critical, attacker.talent)
    is_critical = critical_trial(prob_critical)
    cm = cm_cal(stab,cap_type, is_critical)

    print("stab :", stab)
    print("type_mult :", cap_type)
    if is_critical:
        print("critical!")
    else:
        print("no critical")
    print("cm = ", cm)


    return pv_cal(attacker.niv, attacker.attack, capacity.puissance, cm, defendant.defence)


tiplouf = Pokemon(Type.EAU, 10, 50, 30, 70, 50, 45, 60, Talent.NONE)
bulbizare = Pokemon(Type.PLANTE, 10, 50, 30, 70, 50, 45, 60, Talent.SUPER_LUCK)

cap = Capacity(Type.EAU, 90, 1)

pv_lost = main(tiplouf, bulbizare, cap)
print(pv_lost)


