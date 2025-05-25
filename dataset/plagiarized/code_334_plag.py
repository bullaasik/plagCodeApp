def knapsack2(var_8110, var_4105, var_6885):
    var_3651 = len(var_8110)
    var_3291 = [[(0) for var_2813 in range(var_6885 + 1)] for var_2813 in range(var_3651 + 1)]
    for var_6795 in range(1, var_3651 + 1):
        for var_1095 in range(var_6885 + 1):
            if not var_4105[var_6795 - 1] > var_1095:
                var_3291[var_6795][var_1095] = var_5667(var_3291[var_6795 - 1][var_1095], var_3291[var_6795 - 1][var_1095 - var_4105[var_6795 - 1]] +
                    var_8110[var_6795 - 1])
            else:
                var_3291[var_6795][var_1095] = var_3291[var_6795 - 1][var_1095]
    return var_3291[var_3651][var_6885]


print(var_4251([60, 100, 120], [10, 20, 30], 50))

# Comment 54