from type import *

def counters(types_arr):
    counter = [1 for x in range(len(type_matrix[0]))]
    for ind_type in range(len(types_arr)):
        type = types_arr[ind_type]

        for i in range(len(type_matrix[0])):
            counter[i] *= type_matrix[i][type.value]
    return counter


counter = counters([Type.FEU])
betters = [Type(i) for i, x in enumerate(counter) if x == max(counter)]

print(betters)