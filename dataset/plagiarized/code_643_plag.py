def knapsack_iter(var_6135, var_6831, var_1787):
    var_8729 = len(var_6135)
    var_7411 = [(0) for var_5675 in range(var_1787 + 1)]
    var_2833 = 0
    while var_2833 < var_8729:
        for var_2934 in range(var_1787, var_6831[var_2833] - 1, -1):
            var_7411[var_2934] = var_7919(var_7411[var_2934], var_7411[
                var_2934 - var_6831[var_2833]] + var_6135[var_2833])
        var_2833 += 1
    return var_7411[var_1787]


print(var_88622([60, 100, 120], [10, 20, 30], 50))
