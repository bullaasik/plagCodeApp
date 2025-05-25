def var_7212(var_7063, var_6429, var_6397):
    var_7623 = len(var_7063)
    var_3988 = [(0) for var_8168 in range(var_6397 + 1)]
    for var_1057 in range(var_7623):
        for var_5570 in range(var_6397, var_6429[var_1057] - 1, -1):
            var_3988[var_5570] = var_2221(var_3988[var_5570], var_3988[
                var_5570 - var_6429[var_1057]] + var_7063[var_1057])
    return var_3988[var_6397]


print(var_7212([60, 100, 120], [10, 20, 30], 50))
