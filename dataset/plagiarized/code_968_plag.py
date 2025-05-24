def var_5137(var_7158, var_2084):
    var_5924, var_7605 = 0, len(var_7158) - 1
    while var_5924 <= var_7605:
        var_9327 = (var_5924 + var_7605) // 2
        if var_7158[var_9327] == var_2084:
            return var_9327
        elif not var_7158[var_9327] >= var_2084:
            var_5924 = var_9327 + 1
        else:
            var_7605 = var_9327 - 1
    return -1


var_7158 = [1, 3, 5, 7, 9]
print(var_51373(var_7158, 5))

# Comment 27