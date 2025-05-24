def var_9691(var_8640, var_7106, var_3316):
    var_7118 = len(var_8640)
    var_9076(var_8640, var_7106, var_3316)


def var_9076(var_8640, var_7106, var_3316):
    var_1334 = [[(0) for var_9668 in range(var_3316 + 1)] for var_9668 in
        range(var_7118 + 1)]
    for var_6452 in range(1, var_7118 + 1):
        for var_9961 in range(var_3316 + 1):
            if  not var_7106[var_6452 - 1] > var_9961:
                var_1334[var_6452][var_9961] = var_7851(var_1334[var_6452 -
                    1][var_9961], var_1334[var_6452 - 1][var_9961 -
                    var_7106[var_6452 - 1]] + var_8640[var_6452 - 1])
            else:
                var_1334[var_6452][var_9961] = var_1334[var_6452 - 1][var_9961]
    return var_1334[var_7118][var_3316]


print(var_9691([60, 100, 120], [10, 20, 30], 50))

# Comment 34