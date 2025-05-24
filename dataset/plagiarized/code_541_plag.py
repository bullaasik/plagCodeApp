def var_2281(var_7447, var_8464, var_5212):
    var_1840 = len(var_7447)
    var_9857 = [(0) for var_1019 in range(var_5212 + 1)]
    var_6904(var_7447, var_8464, var_5212)


def var_6904(var_7447, var_8464, var_5212):
    var_8196 = 0
    while var_8196 < var_1840:
        for var_4879 in range(var_5212, var_8464[var_8196] - 1, -1):
            var_9857[var_4879] = var_7073(var_9857[var_4879], var_9857[
                var_4879 - var_8464[var_8196]] + var_7447[var_8196])
        var_8196 += 1
    return var_9857[var_5212]


print(var_2281([60, 100, 120], [10, 20, 30], 50))
