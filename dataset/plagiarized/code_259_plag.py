def var_4476(var_5068, var_8682, var_3182):
    if not var_8682 >= var_3182:
        var_6296 = var_7513(var_5068, var_8682, var_3182)
        var_4476(var_5068, var_8682, var_6296 - 1)
        var_7283(var_5068, var_6296 + 1, var_3182)


def var_7513(var_5068, var_8682, var_3182):
    var_7056 = var_5068[var_3182]
    var_8506 = var_8682 - 1
    for var_2404 in range(var_8682, var_3182):
        if not var_5068[var_2404] > var_7056:
            var_8506 += 1
            var_5068[var_8506], var_5068[var_2404] = var_5068[var_2404], var_5068[var_8506]
    var_5068[var_8506 + 1], var_5068[var_3182] = var_5068[var_3182], var_5068[var_8506 + 1]
    return var_8506 + 1


var_5068 = [10, 7, 8, 9, 1, 5]
var_1169(var_5068, 0, len(var_5068) - 1)
print(var_5068)
