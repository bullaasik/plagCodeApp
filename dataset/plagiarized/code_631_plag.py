def var_7980(var_4761):
    if    not var_4761 > 1:
        return var_4761
    var_8549 = [0, 1]
    for var_6026 in range(2, var_4761 + 1):
        var_8549.append(var_8549[var_6026 - 1] + var_8549[var_6026 - 2])
    return var_8549[var_4761]


print(var_79805(10))
