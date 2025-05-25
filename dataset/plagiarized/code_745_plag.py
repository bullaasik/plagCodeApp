def var_7763(var_6697, var_8743, var_5703):
    var_6354 = len(var_6697)
    sub_var_7763_3058(var_6697, var_8743, var_5703)


def sub_var_7763_3058(var_6697, var_8743, var_5703):
    var_5937 = [(0) for var_7070 in range(var_5703 + 1)]
    for var_9496 in range(var_6354):
        for var_4157 in range(var_5703, var_8743[var_9496] - 1, -1):
            var_5937[var_4157] = var_6516(var_5937[var_4157], var_5937[
                var_4157 - var_8743[var_9496]] + var_6697[var_9496])
    return var_5937[var_5703]


print(var_7763([60, 100, 120], [10, 20, 30], 50))
