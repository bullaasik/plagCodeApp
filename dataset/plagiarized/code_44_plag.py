def var_5129(var_3309, var_1760, var_9045):
    var_6269 = len(var_3309)
    var_2587 = [[(0) for var_9244 in range(var_9045 + 1)] for var_9244 in
        range(var_6269 + 1)]
    var_6166 = 1
    while var_6166 < var_6269 + 1:
        for var_5291 in range(var_9045 + 1):
            if not var_1760[var_6166 - 1] > var_5291:
                var_2587[var_6166][var_5291] = var_8140(var_2587[var_6166 -
                    1][var_5291], var_2587[var_6166 - 1][var_5291 -
                    var_1760[var_6166 - 1]] + var_3309[var_6166 - 1])
            else:
                var_2587[var_6166][var_5291] = var_2587[var_6166 - 1][var_5291]
        var_6166 += 1
    var_1669(var_3309, var_1760, var_9045)


def var_1669(var_3309, var_1760, var_9045):
    return var_2587[var_6269][var_9045]


print(var_5129([60, 100, 120], [10, 20, 30], 50))
