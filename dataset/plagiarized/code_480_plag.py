def var_9700(var_5017, var_3301, var_1358):
    if not var_3301 >= var_1358:
        var_5774 = var_6918(var_5017, var_3301, var_1358)
        var_9700(var_5017, var_3301, var_5774 - 1)
        var_9700(var_5017, var_5774 + 1, var_1358)


def var_6918(var_5017, var_3301, var_1358):
    var_6371 = var_5017[var_1358]
    var_9955 = var_3301 - 1
    var_2114(var_5017, var_3301, var_1358)


def var_2114(var_5017, var_3301, var_1358):
    for var_5271 in range(var_3301, var_1358):
        if not var_5017[var_5271] > var_6371:
            var_9955 += 1
            var_5017[var_9955], var_5017[var_5271] = var_5017[var_5271
                ], var_5017[var_9955]
    var_5017[var_9955 + 1], var_5017[var_1358] = var_5017[var_1358], var_5017[
        var_9955 + 1]
    var_6143(var_5017, var_3301, var_1358)


def var_6143(var_5017, var_3301, var_1358):
    return var_9955 + 1


var_5017 = [10, 7, 8, 9, 1, 5]
var_9700(var_5017, 0, len(var_5017) - 1)
print(var_5017)
