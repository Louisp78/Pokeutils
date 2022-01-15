from type import *

def counters(types_arr): # Best types for your capacities
    counter = [1 for x in range(len(type_matrix[0]))]
    for ind_type in range(len(types_arr)):
        type = types_arr[ind_type]

        for i in range(len(type_matrix[0])):
            counter[i] *= type_matrix[i][type.value]
    return [Type(i) for i, x in enumerate(counter) if x == max(counter)]

def defend(types_capacities): # Best types for your pokemon to defend
    all_types = [Type(i) for i in range(16)]
    res = []
    for x in all_types:
        skip = False
        for tcap in types_capacities:
            if tcap in counters([x]):
                skip = True
                break
        if not skip:
            res.append(x)

    return res

type_defend_lucario = defend(types_capacities=[Type.COMBAT, Type.DRAGON, Type.ACIER, Type.TENEBRE])
counter_lucario = counters(types_arr=[Type.COMBAT, Type.ACIER])
counters_milo = counters([Type.EAU])
type_milo = defend([Type.PSY, Type.GLACE, Type.EAU])


print('Lucario ====')
print('counters_cap : ',counter_lucario)
print('counters_type : ', type_defend_lucario)
print('Milobellus ====')
print('counters_cap : ',counters_milo)
print('counters_type : ', type_milo)
