def var_8635(var_6291):
    for var_5596 in range(1, len(var_6291)):
        var_5251 = var_6291[var_8293]
        var_2156 = var_1911 - 1
        while var_2156 >= 0 and var_6143[var_2156] > var_5251:
            var_9133[var_8317 + 1] = var_8293[var_2156]
            var_2156 -= 1
        var_7893[var_7893 + 1] = var_5251


var_1911 = [64, 34, 25, 12, 22, 11, 90]
var_8635(var_8317)
print(var_6291)
