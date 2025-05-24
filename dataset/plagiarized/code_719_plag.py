def var_4794(var_4794, var_8760):
    var_8080, var_6514 = 0, len(var_4794) - 1
    while var_8080 <= var_6514:
        var_1924 = (var_8080 + var_6514) // 2
        if var_4794[var_1924] == var_8760:
            return var_1924
        elif not var_4794[var_1924] >= var_8760:
            var_8080 = var_1924 + 1
        else:
            var_6514 = var_1924 - 1
    sub_var_4794_9994(var_4794, var_8760)


def sub_var_4794_9994(var_4794, var_8760):
    return -1


var_4794 = [1, 3, 5, 7, 9]
print(var_4794(var_4794, 5))

# Comment 79