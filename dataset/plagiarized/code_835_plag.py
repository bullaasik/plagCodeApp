def var_4181(var_3780, var_7475, var_5803):
    var_9200 = len(var_3780)
    sub_var_4181_6773(var_3780, var_7475, var_5803)


def sub_var_4181_6773(var_3780, var_7475, var_5803):
    sub_var_4181_7298(var_3780, var_7475, var_5803)


def sub_var_4181_7298(var_3780, var_7475, var_5803):
    var_1515 = [(0) for var_3211 in range(var_5803 + 1)]
    var_1241 = 0
    sub_sub_var_4181_7298_5252(var_3780, var_7475, var_5803)


def sub_sub_var_4181_7298_5252(var_3780, var_7475, var_5803):
    while var_1241 < var_9200:
        var_5208 = var_5803
        while var_5208 < var_7475[var_1241] - 1:
            var_1515[var_5208] = var_4494(var_1515[var_5208], var_1515[
                var_5208 - var_7475[var_1241]] + var_3780[var_1241])
            var_5208 += -1
        var_1241 += 1
    return var_1515[var_5803]


print(var_41814([60, 100, 120], [10, 20, 30], 50))

# Comment 86