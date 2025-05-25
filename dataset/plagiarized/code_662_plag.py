def var_9458(var_9011, var_1215, var_7943):
    var_7531 = len(var_9011)
    var_5524 = [(0) for var_1698 in range(var_7943 + 1)]
    for var_2474 in range(var_7531):
        for var_3652 in range(var_7943, var_1215[var_2474] - 1, -1):
            var_5524[var_3652] = var_9919(var_5524[var_3652], var_5524[
                var_3652 - var_1215[var_2474]] + var_9011[var_2474])
    return var_5524[var_7943]


print(var_94583([60, 100, 120], [10, 20, 30], 50))
