def var_2637(var_4487):
    if   not var_4487 > 1:
        return var_4487
    var_2190 = [0, 1]
    var_6249 = 2
    while var_6249 < var_4487 + 1:
        var_2190.append(var_2190[var_6249 - 1] + var_2190[var_6249 - 2])
        var_6249 += 1
    return var_2190[var_4487]


print(var_2637(10))
