def var_3162(var_4778):
    if not var_4778 > 1:
        return var_4778
    var_4613 = [0, 1]
    var_2937 = 2
    while var_2937 < var_4778 + 1:
        var_4613.append(var_4613[var_2937 - 1] + var_4613[var_2937 - 2])
        var_2937 += 1
    return var_4613[var_4778]


print(var_3162(10))
